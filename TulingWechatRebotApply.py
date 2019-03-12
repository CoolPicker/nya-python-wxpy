#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

from wxpy import *
import time

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/lab/wxpy/wxpy.pkl")

tuling = Tuling(api_key='1f62dcd7b2374f08a76253c6eb661711')

print "图灵机器人已启动..."

friend_name = unicode('王永哲', errors='replace')

my_friend = bot.friends().search(friend_name)[0]

# @bot.register(my_friend)
# def reply_my_friend(msg):
#     print "recieve : " + str(msg)
#     tuling.do_reply(msg)

@bot.register(chats= [Friend])
def reply_my_friend(msg):
    print "recieve : " + str(msg)
    time.sleep(2)
    tuling.do_reply(msg)

embed()