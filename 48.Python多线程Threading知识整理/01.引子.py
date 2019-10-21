# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/21 21:38
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 01.引子.py


import threading
import random
import time


def exercising():
    for i in range(4):
        time.sleep(2)
        print("{}开始跑步了，我跑了{}公里".format(threading.current_thread().name, i))


def entertaining():
    for i in range(5):
        time.sleep(1)
        print("{}躺在床上,他又刷到一个好看的妹子".format(threading.current_thread().name))


def learning():
    print("{}开始学习了".format(threading.current_thread().name))
    time.sleep(10)
    print("{}学习结束了了".format(threading.current_thread().name))


def run():
    # 这些都是我的分身
    boys = ['怪蜀黍', '小逗比', '透明人']
    things = [exercising, entertaining, learning]
    random.shuffle(boys)
    for num, boy in enumerate(boys):
        t = threading.Thread(target=things[num], name=boy)
        t.start()
        time.sleep(0.1)
    while True:
        time.sleep(1)
        print(123)

run()
