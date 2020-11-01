# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/6/10 0:08
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : play_choice.py

from play_list import work, play, drink

choices = {'work': work, 'play': play, 'drink': drink}


def to_do(user_choice):
    try:
        choices.get(user_choice)()
    except TypeError:
        print("你玩的太溜,我的字典里没有...")


to_do('dance')
to_do('drink')
