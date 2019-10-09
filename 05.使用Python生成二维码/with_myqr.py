# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 0:20
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : with_myqr.py

from MyQR import myqr

myqr.run(
    words='https://u.wechat.com/MBRIKvkCaVjbuxRSdYeaG70',
    level='Q',
    version=6,
    picture='微信.jpg',
    colorized=True,
    contrast=1.0,
    save_name='1.gif'
)
