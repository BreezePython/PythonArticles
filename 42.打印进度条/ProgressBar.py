# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/16 22:09
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : ProgressBar.py
# import time
#
#
#
# def progress_bar(total):
#     if total <= 0:
#         raise ValueError("Wrong total number ...")
#
#     for i in range(0, total):
#         time.sleep(0.05)
#         step = int(100 / total * (i + 1))
#         str1 = '\r[%3d%%] %s' % (step, '>' * step)
#         print(str1, end='', flush=True)
#
#
# progress_bar(20)
# print()
# progress_bar(110)

from tqdm import tqdm
import string
import time

for char in tqdm(string.ascii_uppercase):
    time.sleep(0.1)


for i in tqdm(range(50)):
    time.sleep(0.05)

# import sys,time
# for i in range(100):
#     sys.stdout.write('>')
#     sys.stdout.flush()
#     time.sleep(0.1)
# import sys,time
# for i in range(100):
#     sys.stdout.write('\r%s%%'%(i+1))
#     sys.stdout.flush()
#     time.sleep(0.1)

# import sys,time
# for i in range(100):
#     k = i + 1
#     str = '>'*i+' '*(100-k)
#     sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
#     sys.stdout.flush()
#     time.sleep(0.1)

# import sys,time
# for i in range(100):
#     k = i + 1
#     str = '>'*(i//2)+' '*((100-k)//2)
#     sys.stdout.write('\r'+str+'[%s%%]'%(i+1))
#     sys.stdout.flush()
#     time.sleep(0.1)


# import time
# for i in range(0, 101, 2):
#     time.sleep(0.1)
#     char_num = i // 2  # 打印多少个'*'
#     per_str = '\r%s%% : %s' % (i, '*' * char_num)
#     print(per_str, end='', flush=True)


# from colorama import init, Fore, Back, Style
#
# if __name__ == "__main__":
#     init(autoreset=True)  # 初始化，并且设置颜色设置自动恢复
#     print(Fore.RED + 'some red text')
#     print(Back.CYAN + 'and with a green background')
#     print(Style.DIM + 'and in dim text')
#     # 如果未设置autoreset=True，需要使用如下代码重置终端颜色为初始设置
#     # print(Fore.RESET + Back.RESET + Style.RESET_ALL)  autoreset=True
#     print('back to normal now')

# def with_color(string, fg, bg=49):
#     print("\33[0m\33[%d;%dm%s\33[0m" % (fg, bg, string))
#     return 0
#
#
# def B(string):
#     print("\33[1m%s\33[22m" % string)
#     return 0
#
#
# # front color
# Red = 1
# Green = 2
# Yellow = 3
# Blue = 4
# Magenta = 5
# Cyan = 6
# White = 7
#
#
# def fr(string):
#     return with_color(string, Red + 30)  # Red
#
#
# def fg(string):
#     return with_color(string, Green + 30)  # Green
#
#
# def fy(string):
#     return with_color(string, Yellow + 30)  # Yellow
#
#
# def fb(string):
#     return with_color(string, Blue + 30)  # Blue
#
#
# def fm(string):
#     return with_color(string, Magenta + 30)  # Magenta
#
#
# def fc(string):
#     return with_color(string, Cyan + 30)  # Cyan
#
#
# def fw(string):
#     return with_color(string, White + 30)  # White
#
#
# fr("red")
# fy("yellow")
# fm("magenta")
# fg("green")
# fc("cyan")
