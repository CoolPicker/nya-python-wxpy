#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

from wxpy import *

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/han/python-test/wxpy.pkl")

friend_name = unicode('唐光聪', errors='replace')

my_friend = bot.friends().search(friend_name)[0]
print my_friend
my_friend.send('hello')

@bot.register(my_friend)
def my_friend_message(msg):
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

