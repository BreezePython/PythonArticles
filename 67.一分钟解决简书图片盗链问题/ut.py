# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/12/20 23:32:01
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : ut.py
# import os
#
# expect_dict = {"dirs": ['.git', '.idea', 'static'],
#                "files": ["README.md", "_sidebar.md", ".nojekyll"]}
#
# for root, dirs, files in os.walk(r'D:\blog'):
#     if '.git' in dirs:
#         dirs.remove('.git')
#     print(root)
# # if os.path.split(root)[-1] in expect_dict.get('dirs'):
# #     continue
#     for file in files:
#         if file in expect_dict.get('files'):
#             continue
#         print(os.path.join(root, file))

import time


def fun1(a, b):
    print('fun1')
    print(a, b)
    time.sleep(1)


def fun2():
    print('fun2')
    time.sleep(1)


def fun3():
    print('fun3')
    time.sleep(2)


def fun4():
    print('fun4')
    time.sleep(1)


def fun5():
    print('fun5')
    time.sleep(1)
    fun4()


fun1('foo', 'bar')
fun2()
fun3()
fun5()
