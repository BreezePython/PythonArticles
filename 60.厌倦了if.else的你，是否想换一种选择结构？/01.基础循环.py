# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/6/9 23:32
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 01.基础循环.py

# 传统方式
def show_price_list(user_choice):
    if user_choice.lower() == 'single':
        print(150)
    elif user_choice.lower() == 'business':
        print(300)
    elif user_choice.lower() == 'couple':
        print(500)
    else:
        print("未找到你所需要的房间类型")


# show_price_list('couple')

# 更加简洁的方式
PRICES = {'single': 150, 'business': 300, 'couple': 500}


def show_price_list(user_choice):
    print(PRICES.get(user_choice.lower(), "未找到你所需要的房间类型"))


# show_price_list('couple')
# show_price_list('special')


