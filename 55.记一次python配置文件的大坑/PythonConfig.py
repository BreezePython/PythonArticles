# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/12/12 21:54
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : PythonConfig.py

import configparser


class NewConfig(configparser.ConfigParser):
    def optionxform(self, option_str):
        return option_str


def get_items(file):
    conf = NewConfig()
    conf.read(file, encoding='utf-8')
    return dict(map(lambda x: x, conf.items('Info')))


print(get_items('config.ini'))
