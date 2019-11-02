# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/24 0:58
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 3.Counter函数.py

from collections import Counter


def func():
    case_list = input("请输入用例列表：").strip().split(',')
    for k, v in Counter(case_list).items():
        if v % 2:
            print("找到符合要求的数字: {}".format(k))
            break


if __name__ == '__main__':
    func()
