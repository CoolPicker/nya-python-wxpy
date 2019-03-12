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

t0 = bot.friends(update=False)

for each in bot.friends():
    name = each.name
    nick_name = each.nick_name
    province = each.province
    remark_name = each.remark_name
    sex = each.sex
    gender = "男"
    if sex == 2:
        gender = "女"
    signature = each.signature
    print 'friend - name : ' + name + " nick_name : " + nick_name + " province : " + province + " remark_name : " + remark_name + " gender : " + gender + " signature : " + signature

print '我的好友数 : ' + str(len(t0)-1)



