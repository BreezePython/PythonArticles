# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/21 23:35
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 03.join.py

import threading
import time
from atexit import register


def study(name, hours):
    print("{}今晚学习{}小时".format(name, hours))
    time.sleep(hours)
    print("{}学完了...".format(name))


def watch_tv():
    print("终于能打开电视了...")
    time.sleep(2)


@register
def _atexit():
    print('看完睡觉,关灯...')


print('c今天不学习...')
print('电视是a买的，a没学完习，你们都不能看')
a = threading.Thread(target=study, args=('a', 5,))
a.start()

b = threading.Thread(target=study, args=('b', 3))
b.start()
# 关注此处join点
a.join()


c = threading.Thread(target=watch_tv)
c.start()
print('啤酒炸鸡走起来！')
