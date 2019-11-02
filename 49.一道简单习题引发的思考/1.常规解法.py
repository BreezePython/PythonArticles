# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/24 0:01
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 1.常规解法.py


def func():
    case_list = input("请输入用例列表：").strip().split(',')
    case_set = set(case_list)
    for num in case_set:
        if case_list.count(num) % 2:
            print("找到符合要求的数字: {}".format(num))
            break
    else:
        print("未找到符合要求的数字")


if __name__ == '__main__':
    func()
