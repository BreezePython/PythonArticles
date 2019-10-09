# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/30 3:32
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : LearnBeautifulsoup.py

from bs4 import BeautifulSoup

with open('comments.html', encoding='utf-8') as f:
    html = f.read()

# 通过标签直接定位
soup = BeautifulSoup(html, 'lxml')
# print(soup.h1)
# print(soup.html.body.h1)
# print(soup.findAll(('h1','title')))
#
# print(soup.findAll("div", {"class":"mod-bd"}))

# print(soup.find(id="comments"))
import re
print(soup.findAll("div", {"class":re.compile("comment-.*?")}))


#
