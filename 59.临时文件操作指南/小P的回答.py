# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/6/4 22:30
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 小P的回答.py

import os


def three_func(file_object=None):
    data = file_object.read()
    final_data = data.decode() if isinstance(data, bytes) else data
    print(f'read file info:{final_data}')


def make_temp_file():
    _base_dir = os.path.dirname(os.path.realpath(__file__))
    _tmp_file = os.path.join(_base_dir, 'tmp_file.txt')
    print(_tmp_file)
    with open(_tmp_file, 'w+') as f:
        f.write("something")
        f.seek(0)
        # call three_func
        three_func(f)
    os.remove(_tmp_file)


make_temp_file()
