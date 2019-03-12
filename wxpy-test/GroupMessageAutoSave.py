#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

# 导入模块
import os

from wxpy import *

from datetime import datetime

# 初始化机器人,扫码登录
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
"""
Bot : 机器人对象,用于登陆和操作微信账号
    cache_path : 设置当前会话的缓存路径,并开启缓存功能;默认不开启
        开启缓存后可短时间内避免重复扫码,缓存失效将要求重新登陆
"""
bot = Bot(cache_path="/home/lab/wxpy/wxpy.pkl")

# 启动聊天对象的 puid (wxpy 特有的聊天对象/ 用户ID )
# 注: 微信好友包含puid , 微信群无该属性
bot.enable_puid('wxpy_puid.pkl')

# 消除手机端新消息小红点提醒 默认 False
bot.auto_mark_as_read = True

rowList = [] # 保存输入的文本信息
"""
Bot.groups() - 获取所有群聊对象
一些不活跃的群可能无法被获取到，可通过在群内发言，或修改群名称的方式来激活
update - 是否更新
contact_only - 是否限于保存为联系人的群聊
"""
group = bot.groups(update=False,contact_only=False).search(unicode('group', errors='replace'))[0]

print '** ** ** ** ** ** ** ** ** ** ** '
print '群名: ' + group.name
print '群主名: ' + group.owner.name
members = group.members
for fri in members:
    name = str(fri.name)
    nick_name = str(fri.nick_name)
    print 'member : ' + name + " nick_name : " + nick_name

"""
    公共方法
"""
# 读取图片
def file_extension(path):  # 定义一个取文件扩展名的函数
    return os.path.splitext(path)[1]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 读取文件
def get_file_content(file_Path):
    with open(file_Path, 'rb') as fp:
        return fp.read()

"""
自动回复 - 通过 预先注册(将 Bot.register() - 作为函数的装饰器,即可完成注册) 的方式,实现消息的自动处理
Bot.register(chats=None,
             msg_types=None,
             except_self=True,
             run_async=True,
             enabled=True)
    装饰器: 用于注册消息配置
    chats - 消息所在的聊天对象:单个或列表形式的多个聊天对象或聊天类型,为空时匹配所有聊天对象
    msg_types - 消息的类型: 单个或列表形式的多个消息类型,为空时匹配所有消息类型(SYSTEM类消息除外)
    except_self - 排除由自己发送的消息
    run_async - 是否异步执行所配置的函数
    enabled - 当前配置的默认开启状态,可事后动态开启或关闭
"""
@bot.register(group,except_self=False)
def reply_group(msg):
    print 'receive : ' + str(msg)
    rowList.append(str(msg))
    if len(rowList) >= 100:
        nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fileName = 'test' + '-' + nowTime + '.log'
        file = open('/home/lab/wxpy/nya/' + fileName, 'wb')
        for num in range(0, len(rowList)):
            file.write(rowList.pop())
        file.close()

    if msg.type != 'Text':
        now_type = msg.type
        print now_type
        if now_type == 'Picture':
            now_type = 'picture'
            # 另存图片
            now_time = datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
            file_name = '/home/lab/wxpy/nya/image/group' + '-' + now_time + file_extension(msg.file_name)
            msg.get_file(file_name)
            size = os.path.getsize(file_name) # 获取下载到本地的图片大小

            if size > 0:
                print 'image saved'
                ret = 'image saved ... '
            else:
                print 'image err'
                ret = 'please import image not gif'

        elif now_type == 'Recording':
            now_type = 'recording'
            # 语音识别
            recording_time = datetime.now().strftime("%Y-%m-%d--%H:%M:%S")
            record_name = '/home/lab/wxpy/nya/record/group' + '-' + recording_time + file_extension(msg.file_name)
            msg.get_file(record_name)

            size = os.path.getsize(record_name)  # 获取语音大小

            if size > 0:
                print 'record saved'
                ret = 'record saved ... '
            else:
                print 'record err'
                ret = 'record saved err '
        else:
            now_type = now_type
            ret = 'now type = ' + now_type
        print now_type
    else:
        ret = 'Text test'
    # 直接 return 等同调用 msg.reply('...')
    return ret
    # # 如果是群聊,但没有被 @ , 则不回复
    # if isinstance(msg.chat,Group) and not msg.is_at:
    #     return
    # else:
    #     if msg.type != 'Text':
    #         ret = 'what is this .. please input text'
    #     elif is_number(msg):
    #         ret = 'number'
    #     else:
    #         ret = 'not number'
    #     print 'send : ' + str(ret)
    #     # 直接 return 等同调用 msg.reply('...')
    #     return ret


# 进入 Python 命令行、让程序保持运行
embed()



# # 定义定时任务
# def job():
#     nowTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print nowTime
#     # fileName = 'test' + '-' + nowTime + '.log'
#     # file = open('/home/lab/wxpy/nya/' + fileName, 'wb')
#     # for num in range(0,len(rowList)):
#     #     file.write(rowList.pop())
#     # file.close()
#
# # 每隔60s保存一次聊天记录
# schedule.every(1).seconds.do(job)
#
# while True:
#     schedule.run_pending()



