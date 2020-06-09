# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/2/6 0:21
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : a.py


import mutagen

inf = mutagen.File('00000040.mp3')
print(inf)
# artwork = inf.tags['APIC:'].data  # 获取歌曲图片
title = inf.tags["TIT2"].text[0]  # 获取歌曲名
print(title.encode('LATIN1').decode('gbk'))
#
# author = inf.tags["TPE1"].text[0]  # 获取歌曲作者
# print(author)
# album = inf.tags["TALB"].text[0]  # 获取歌曲信息
# print(album)


#
# # 将图片保存为和歌曲同名，jpg格式的图片
# with open(title + '.jpg', 'wb') as img:
#     img.write(artwork)
