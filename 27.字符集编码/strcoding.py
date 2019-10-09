# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/14 2:09
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : str_coding.py


# https://www.hao123.com/

# import requests
# import chardet
#
# urls = ['https://www.jb51.net', 'https://www.baidu.com/']
# for url in urls:
#     r = requests.get(url)
#     print(url, chardet.detect(r.content))


# from chardet.universaldetector import UniversalDetector
# detector = UniversalDetector()

# for line in open('strcoding.py','rb'):
#     print(line.decode())

# import chardet
# import time
#
# t0 = time.process_time()
# with open("伏天氏.txt",'rb') as f:
#     print(chardet.detect(f.read()))
# t1 = time.process_time()
# print(t1-t0)


# import time
# from chardet.universaldetector import UniversalDetector
#
# detector = UniversalDetector()
#
# t0 = time.process_time()
# for line in open("伏天氏.txt", 'rb'):
#     detector.feed(line)
#     if detector.done:
#         break
# detector.close()
# print(detector.result)
# t1 = time.process_time()
# print(t1 - t0)
