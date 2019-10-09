# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/25 0:41
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : NationalFlag.py


import requests

r = requests.get('http://img.chebiaow.com/thumb/cb/allimg/1303/1-1303061Z600520,c_fill,h_138,w_160.jpg')
print(r.content)

print(open('a.png', 'rb').read())