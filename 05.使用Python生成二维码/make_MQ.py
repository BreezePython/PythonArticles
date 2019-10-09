# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 0:20
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : make_MQ.py
import os
from MyQR import myqr


def make_QR(filename,words):
    if not os.path.exists(filename):
        print('未找到背景文件，请检查文件名称')
    else:

        myqr.run(
            words=words.encode('utf-8'),
            picture='panda.gif',
            colorized=True,
            save_name='qingfeng.gif'
        )


filename = input("请将所需设置的背景图放置在exe同级目录,并填写用户名\n:")
words = input(str("请输入二维码中的内容\n:"))

make_QR(filename,words)


