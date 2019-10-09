# # -*- coding: utf-8 -*-
# # @Author   : 王翔
# # @JianShu  : 清风Python
# # @Date     : 2019/8/19 23:49
# # @Software : PyCharm
# # @version  ：Python 3.7.3
# # @File     : LearnDecorator.py
#
# # 函数的定义与赋值
# def hello(name='BreezePython'):
#     return "say hello to {}".format(name)
#
#
# hello()
# # 'say hello to BreezePython'
#
# hi = hello
#
# hi('tommorow')
#
#
# # 'say hello to tommorow'
#
# # 函数嵌套
# def hello():
#     print('is hello function...')
#
#     def hi():
#         return 'hi ,nice to meet you!'
#
#     def bye():
#         return 'bye,stranger...'
#
#     print(hi())
#     print(bye())
#
#
# # 函数中返回函数
#
# def hello(name=None):
#     print('is hello function...')
#
#     def hi():
#         return 'hi ,nice to meet you!'
#
#     def bye():
#         return 'bye,stranger...'
#
#     if name == 'BreezePython':
#         return hi
#     else:
#         return bye
#
#
# # 函数作为参数传递
# def child():
#     return 'is child function...'
#
#
# def main(func):
#     print('is main function...')
#     print(func())
#
#
# main(child)

# from functools import wraps
#
#
# # first Decorator
# def main(func):
#     print('is main function...')
#
#     @wraps(func)
#     def child():
#         print('it print before exec func...')
#         func()
#         print('it print after exec func...')
#
#     return child
#
#
# @main
# def alone():
#     print("I'm  alone function ...")
#     print(alone.__name__)
#
# alone()

# import time
# from functools import wraps
#
#
# def log_level(level='DEBUG'):
#     def log_format(func):
#         @wraps(func)
#         def format(*args, **kwargs):
#             logtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
#             print("[{}]{}: ".format(level, logtime), end='')
#             return func(*args, **kwargs)
#
#         return format
#
#     return log_format
#
#
# @log_level()
# def log1():
#     print("Hello,Welcome to 清风Python...")
#
#
# @log_level('ERROR')
# def log2():
#     print("清风Python 是我的公众号...")
#
#
# log1()
# time.sleep(1)
# log2()

import time
from functools import wraps


class Logger:
    def __init__(self,level='DEBUG'):
        self.level = level

    def __call__(self, func):
        @wraps(func)
        def log_format(*args, **kwargs):
            log_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            print("[{}]{}: ".format(self.level, log_time), end='')
            return func(*args, **kwargs)
        return log_format


@Logger()
def log1():
    print("Hello,Welcome to 清风Python...")


@Logger('Error')
def log2():
    print("清风Python 是我的公众号...")


log1()
time.sleep(1)
log2()
