# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 0:20
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : with_myqr.py

from MyQR import myqr

myqr.run(
    words='https://alltodata.cowtransfer.com/s/5b483c08987243',
    level='H',
    version=30,
    picture='收缩原图.jpg',
    colorized=True,
    contrast=1.0,
    save_name='github1.png'
)
