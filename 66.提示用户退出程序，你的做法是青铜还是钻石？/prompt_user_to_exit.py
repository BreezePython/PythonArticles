# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/12/06 22:50:23
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : prompt_user_to_exit.py

# # 青铜
# import sys
#
# user_input = input("输入q,退出程序")
# if user_input == 'q':
#     sys.exit()

# # 白银
# import msvcrt
#
# user_input = msvcrt.getche()
# if user_input.decode() == 'q':
#     exit()

# 王者
import msvcrt

quit_command = 'quit'
listening_str = ''
while True:
    user_input = msvcrt.getche()
    if isinstance(user_input, bytes):
        user_input = user_input.decode()
    if user_input == '\b':
        listening_str = listening_str[:-1]
    elif user_input in ['\n', '\r']:
        listening_str = ''
    else:
        listening_str += user_input
    print('listening_str now is: %s' % listening_str)
    if listening_str == quit_command:
        exit()
