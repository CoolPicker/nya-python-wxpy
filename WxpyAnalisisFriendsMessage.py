#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

from wxpy import *

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

bot = Bot(cache_path="/home/han/python-test/wxpy.pkl")

my_friends = bot.friends(update=False)

print my_friends.stats_text(total=True,sex=True,top_provinces=15,top_cities=20)