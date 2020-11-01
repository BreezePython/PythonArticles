# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/08/09 22:01:22
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : remove_readonly_file.py

import os
import stat

# os.remove('demo.txt')

p = os.stat('demo.txt')
print(oct(p.st_mode))
# os.chmod('demo.txt', stat.S_IWRITE)
os.chmod('demo.txt', stat.S_IWOTH)
p = os.stat('demo.txt')
print(oct(p.st_mode))

import os
import stat


def judge_mode(path, file):
    abs_file = os.path.join(path, file)
    if not os.access(abs_file, os.W_OK):
        os.chmod(abs_file, stat.S_IWOTH)


for root, dirs, files in os.walk('D:\\software_temp', topdown=False):
    for file in files:
        judge_mode(root, file)
        os.remove(os.path.join(root, file))
    for doc in dirs:
        judge_mode(root, doc)
        os.rmdir(os.path.join(root, doc))
