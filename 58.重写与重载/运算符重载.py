# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/4/11 19:36
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 运算符重载.py


class NewList:
    def __init__(self, *args):
        self._list = []
        for i in args:
            self._list.append(i)

    def __add__(self, other):
        self._list = [i + other for i in self._list]

    def call(self):
        print(self._list)


N = NewList(1, 2, 3, 4, 5)
N + 10
N.call()
