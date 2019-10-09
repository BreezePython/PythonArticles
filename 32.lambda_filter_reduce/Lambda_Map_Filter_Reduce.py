# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/22 1:02
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Lambda_Map_Filter_Reduce.py


# x = lambda x, y, z: x + y + z
#
# x(2, 3, 4)
#
# y = (lambda a='hello', b='world': a + b)
#
# y(b='清风')

# l = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]
#
# for f in l:
#     print(f(2))
# print(l[0](3))

# def f1(x):
#     return x ** 2
#
#
# def f2(x):
#     return x ** 3
#
#
# def f3(x):
#     return x ** 4
#
#
# l = [f1, f2, f3]
#
# for f in l:
#     print(f(2))
# print(l[0](3))

# counters = [1, 2, 3, 4]
#
# # 方式1
# new_counters = []
# for i in counters:
#     new_counters.append(i + 10)
#
# print(new_counters)
#
#
# # 方式2
# def adds(x):
#     return x + 10
#
# print(list(map(adds, counters)))
#
# # 更优雅的方式3：
# print(list(map(lambda x: x + 10, counters)))

# counters = [1, -2, 3, -4, 5, -6]
# print(list(map(abs, counters)))

# print(list(filter(lambda x: x % 2 == 0, range(10))))

from functools import reduce

list_show = [1, 2, 3, 4]
print(reduce(lambda x, y: x + y, list_show))
print(reduce(lambda x, y: x * y, list_show))