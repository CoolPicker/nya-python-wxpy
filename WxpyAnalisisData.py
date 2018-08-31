#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

from wxpy import *

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/han/python-test/wxpy.pkl")

# test = unicode('我的好友数 : ', errors='replace')

t0 = bot.friends(update=False)

print '我的好友数 : ' + str(len(t0)-1)

t1 = bot.groups(update=False)

print '群聊数 : ' + str(len(t1))

t2 = bot.mps(update=False)

print '关注的微信公众号数 : ' + str(len(t2))

fri = unicode('唐光聪', errors='replace')

my_friend = bot.friends().search(fri)[0]

print my_friend

#print 'the count of my friends ' + str(len(t0) - 1)