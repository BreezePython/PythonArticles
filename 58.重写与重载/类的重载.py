# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/4/11 19:11
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 类的重载.py


class Person:
    def __init__(self, age, sex):
        self._age = age
        self._sex = sex

    def say(self):
        print("欢迎关注 [清风Python] 公众号")

    def call(self):
        print("This Person age {_age},sex {_sex}".format(**self.__dict__))


class WangPangZi(Person):
    def __init__(self, name, age, sex):
        super().__init__(age, sex)
        self._name = name

    def call(self):
        print("This Person name {_name},age {_age},sex {_sex}".format(**self.__dict__))


P = Person(18, '女')
P.call()

W = WangPangZi('王胖子', 30, '男')
W.call()
W.say()

