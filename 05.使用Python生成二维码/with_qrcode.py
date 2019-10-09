# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/5 23:58
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : with_qrcode.py

import qrcode

txt = '安达市多'
img = qrcode.make(txt)
img.save('qingfeng.png')
