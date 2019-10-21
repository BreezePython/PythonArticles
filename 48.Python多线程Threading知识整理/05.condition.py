# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/22 0:41
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 05.condition.py

import threading
import time


def seeker(cond, name):
    time.sleep(2)
    cond.acquire()
    print('%s :我已经把眼睛蒙上了！' % name)
    cond.notify()
    cond.wait()
    for i in range(2):
        print('%s is finding!!!' % name)
        time.sleep(1)
    cond.notify()
    cond.release()
    print('%s :哈哈，我赢了！' % name)


def hider(cond, name):
    cond.acquire()
    cond.wait()
    for i in range(2):
        print('%s is hiding!!!' % name)
        time.sleep(1)
    print('%s :我已经藏好了，你快来找我吧！' % name)
    cond.notify()
    cond.wait()
    cond.release()
    print('%s :被你找到了，唉~^~!' % name)


cond = threading.Condition()
seeker = threading.Thread(target=seeker, args=(cond, 'seeker'))
hider = threading.Thread(target=hider, args=(cond, 'hider'))
seeker.start()
hider.start()
