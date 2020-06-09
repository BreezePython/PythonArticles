# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/5 22:26
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : icon.py

import base64

with open('清风Python.gif','rb') as f:
    data = f.read()
img = base64.b64encode(data)
print(img)

