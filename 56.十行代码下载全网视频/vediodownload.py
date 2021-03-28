# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/12/20 22:55
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : vediodownload.py


import sys, os
import you_get


def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


if __name__ == '__main__':
    print('begin to download...')
    url = input('please input url:')
    path = os.getcwd()
    download(url, path)
    print('download success!')
