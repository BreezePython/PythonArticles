# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/4/11 19:55
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Python实现Java的重载.py


# def eg1(name, hobby='Python'):
#     print("{}的是{}开发".format(name, hobby))
#
#
# eg1('老王')
# eg1('老张', 'Java')

# from functools import singledispatch
#
#
# @singledispatch
# def shop(price):
#     pass
#
# @shop.register(int)
# def int_price(price):
#     print('获取整数单价%s' % price)
#
# @shop.register(float)xzccxzcxz
# def float_price(price):
#     print('获取小数单价%s' % price)
#
# if __name__ == '__main__':
#     shop(100)
#     shop(99.8)
class a:
    def __init__(self):
        pass

    def b(self):
        self.q=123

    def c(self):
        print(self.q)

A= a()
A.b()
A.c()