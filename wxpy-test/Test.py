#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

# 导入模块
from wxpy import *

# 初始化机器人,扫码登录
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
"""
Bot : 机器人对象,用于登陆和操作微信账号
    cache_path : 设置当前会话的缓存路径,并开启缓存功能;默认不开启
        开启缓存后可短时间内避免重复扫码,缓存失效将要求重新登陆
"""
bot = Bot()

# 启动聊天对象的 puid (wxpy 特有的聊天对象/ 用户ID )
# 注: 微信好友包含puid , 微信群无该属性
bot.enable_puid('wxpy_puid.pkl')

# 消除手机端新消息小红点提醒 默认 False
# bot.auto_mark_as_read = True

# 在 Web 微信中把自己加为好友
# bot.self.add()
# bot.self.accept()

# # 发送消息给 文件传输助手
# bot.file_helper.send('222')
# bot.file_helper.send_image('/home/lab/11.jpeg')
# # bot.file_helper.send_video('/home/lab/liveness-examples/02.mp4')
# bot.file_helper.send_file('/home/lab/liveness-examples/VideoVerifyService.java')
#
# group = bot.groups(update=False,contact_only=False).search(unicode('group-test', errors='replace'))[0]
#
# group.send('text : ')
# group.send('222')
# group.send('image : ')
# group.send_image('/home/lab/11.jpeg')
# # bot.file_helper.send_video('/home/lab/liveness-examples/02.mp4')
# group.send('file : ')
# group.send_file('/home/lab/liveness-examples/VideoVerifyService.java')

@bot.register(except_self=False)
def print_msg(msg):
    print msg
embed()