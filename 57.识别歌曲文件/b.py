# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/3/14 0:48
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : b.py


import re

with open('a.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

for line in lines:
    line = line.strip()
    matchObj = re.match(r"（.?）", line, re.M | re.I)
    # matchObj = re.match(r"（[\D\d]?）", line, re.M | re.I)
    if matchObj:
        print(matchObj.group())

