# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/21 23:53
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 04.event.py


import threading
import time


def do(event, name):
    print('{}号车主就位'.format(name))
    event.wait()  # 所有线程执行都这里都在等待


event_obj = threading.Event()
for i in range(1, 5):
    t = threading.Thread(target=do, args=(event_obj, i))
    t.start()
    time.sleep(0.1)

print("倒计时")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

event_obj.set()
print('出发')
