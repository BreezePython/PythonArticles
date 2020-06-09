# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 0:20
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : with_myqr.py

from MyQR import myqr

myqr.run(
    words='https://github.com/BreezePython',
    level='Q',
    version=5,
    picture='icon.png',
    colorized=True,
    contrast=1.1,
    save_name='github.png'
)
