#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

from wxpy import *

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/han/python-test/wxpy.pkl")

str = unicode('弟', errors='replace')

my_friend = bot.friends().search(str)[0]
bot.file_helper.send("test  test  test")
friends = bot.friends()
for fri in friends:
    print fri
print my_friend
my_friend.send('test from python second')
#my_friend.send_image('/home/han/100901.jpg')
#my_friend.send_file('/home/han/niuya/11.txt')

# my_friend.send_video('/data/rosetta/test.mp4')