#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "NYA"

# import sched
# import time
# from datetime import datetime
#
# '''
# 每个 10 秒打印当前时间。
# '''
# def timedTask():
#     # 初始化 sched 模块的 scheduler 类
#     scheduler = sched.scheduler(time.time, time.sleep)
#     # 增加调度任务
#     scheduler.enter(10, 1, task , '')
#     # 运行任务
#     scheduler.run()
#
# # 定时任务
# def task():
#     print datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
# if __name__ == '__main__':
#     timedTask()

import schedule
import time
from datetime import datetime

def job():
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
