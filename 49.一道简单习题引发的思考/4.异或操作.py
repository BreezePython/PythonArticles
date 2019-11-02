# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/24 0:38
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 4.异或操作.py


from functools import reduce

# 错误的示范！
def func():
    case_list = map(int, input("请输入用例列表：").strip().split(','))
    print(reduce(lambda x, y: x ^ y, case_list))


if __name__ == '__main__':
    func()
