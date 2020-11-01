# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/11/12 22:54.神探程序员，带你千里捉小三
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : CareForCoders.py


from Enneagram_GUI import *
from tkinter import *


def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(size)


root = Tk()

center_window(root, 750, 700)

root.resizable(width=False, height=False)
root.title('九型人格测试 | 公众号: 清风Python')
ExamPage(root)
root.mainloop()
