# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/26 22:54
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : InputPassword.py


import msvcrt
import os

print("Please input your password:")
chars = []
while True:
    newChar = msvcrt.getch().decode(encoding="utf-8")
    if newChar in os.linesep:  # 如果是换行，则输入结束
        break
    elif newChar == '\b':
        if chars:
            del chars[-1]
            msvcrt.putch('\b'.encode(encoding='utf-8'))
            msvcrt.putch(' '.encode(encoding='utf-8'))
            msvcrt.putch('\b'.encode(encoding='utf-8'))
    else:
        chars.append(newChar)
        msvcrt.putch('*'.encode(encoding='utf-8'))  # 显示为星号


pwd = (''.join(chars))
print("\nyour password is:{0}".format(pwd))

