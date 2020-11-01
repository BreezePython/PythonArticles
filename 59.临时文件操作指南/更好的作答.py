# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/6/4 22:39
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 更好的作答.py

import tempfile
import os


def three_func(file_object=None):
    data = file_object.read()
    final_data = data.decode() if isinstance(data, bytes) else data
    print(f'read file info:{final_data}')


def make_temp_file():
    _tmp_file = tempfile.TemporaryFile()
    try:
        print(_tmp_file.name)
        _tmp_file.write(b"something")
        _tmp_file.seek(0)
        # call three_func
        three_func(_tmp_file)
    finally:
        _tmp_file.close()


make_temp_file()
