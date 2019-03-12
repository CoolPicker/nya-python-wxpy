#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

# 导入模块
from wxpy import *

# 初始化机器人,扫码登录
if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/lab/wxpy/wxpy.pkl")

group = bot.groups()

for each in group:
    print ''
    print '*'
    print '**'
    print '***'
    print '****'
    print '*****'
    print '**************************************************'
    print '群名: ' + each.name
    print '群主名: ' + each.owner.name
    members = each.members
    print '成员总数: ' + str(len(members))
    print '群成员: -----'
    for fri in members:
        name = str(fri.name)
        nick_name = str(fri.nick_name)
        print 'member : ' + name + " nick_name : " + nick_name
    print '----- :群成员'

group = group.search(unicode('test', errors='replace'))[0]

print '** ** ** ** ** ** ** ** ** ** ** '

members = group.members
for fri in members:
    name = str(fri.name)
    nick_name = str(fri.nick_name)
    print 'member : ' + name + " nick_name : " + nick_name

# group.send('调试代码呢,测试微信群自动回复机器人')

@bot.register(group)
def reply_group(msg):
    print 'receive : ' + str(msg)
    if msg.type != 'Text':
        ret = 'what is this .. 尴尬的一匹  听不见 看不懂'
    elif '1' in str(msg):
        ret = 'desktop wechat ...'
    else:
        ret = '哈哈哈'
    print 'send : ' + str(ret)
    return ret
embed()