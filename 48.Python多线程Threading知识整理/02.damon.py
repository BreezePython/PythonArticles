# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/21 21:24
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 02.damon.py

import threading
import time
from atexit import register


def install():
    print('启动漫长的程序安装...')
    time.sleep(5)
    print('程序安装完成.')


def until():
    while True:
        time.sleep(1)
        print("the python project is running ...")


@register
def _atexit():
    print('All Done.')


main = threading.Thread(target=install)
main.start()
time.sleep(0.1)
note = threading.Thread(target=until, daemon=True)
note.start()
