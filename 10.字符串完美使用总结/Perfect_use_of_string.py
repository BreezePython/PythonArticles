# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/24 23:19
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Perfect_use_of_string.py
#
# a = '12345'
# b = 'abcdf'
# c = 'abc123'


# print(a.isdigit())
# print(b.isalpha())
# print(c.isalnum())

# d = '①②③④⑤'
# e = '一壹'
# print(e.isupper())
# print(e.isdecimal())
# print(e.isnumeric())

# print('123'.isdecimal())
# q = '123.12'
# print(q.isdecimal())
# print(q.isdigit())
# print(q.isnumeric())

# a='123'
#
# print(isinstance(a, (str, int)))

long_string = "To live is to learn，to learn is to better live"
long_string.startswith('To')
long_string.startswith('li', 3, 5)
long_string.endswith('live')
long_string.endswith('live', 0, 7)

long_string.replace('li')