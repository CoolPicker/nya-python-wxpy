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

for each in bot.friends():
    print each.alias

# friend_name = unicode('王永哲', errors='replace')
# friend_test = bot.friends().search(friend_name)[0]

# # 发送文本
# friend_test.send('Hello,Wechat!')
# # 发送图片
# friend_test.send_image('/home/lab/javacv/i3.jpg')
# print friend_test.alias


# 发送视频
#friend_test.send_video('/home/lab/javacv/t1.mp4')
# 发送文件
#friend_test.send_file('/home/lab/javacv/base64.txt')
