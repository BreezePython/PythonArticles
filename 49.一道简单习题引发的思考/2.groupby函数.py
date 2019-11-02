# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/24 0:10
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 2.groupby函数.py

from itertools import groupby

def func():
    case_list = input("请输入用例列表：").strip().split(',')
    list_group = groupby(case_list)
    for k, v in list_group:
        if len(list(v)) % 2:
            print("找到符合要求的数字: {}".format(k))
            break

if __name__ == '__main__':
    func()