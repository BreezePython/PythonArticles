# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/14 0:47
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : SumAdd.py


# 系统输入两个数字M、N，M为1-9的数字，N为系数。
# eg:
# 输入 2 5，则需计算 2 22 222 2222 22222 的总和，即 24690
# 输入 1 3，则需计算 1 11 111 的总和，即 123

#  常规解法
# 初看这道题，第一个想法就是简单的数字循环叠加求和，无非考虑下10进制的乘数而已。解题如下

# def func()
#     M, N = map(int, input().split())
#     sum_number = number = 0
#     for i in range(N):
#         number += M * 10 ** i
#         sum_number += number
#
#     print(sum_number)

def func():
    M, N = input().split()
    print(sum([int(M * i) for i in range(1, int(N) + 1)]))


if __name__ == '__main__':
    func()
