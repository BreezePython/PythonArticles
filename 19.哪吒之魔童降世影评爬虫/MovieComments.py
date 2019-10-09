# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/30 2:44.NationalFlag
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : MovieComments.py


import requests
from bs4 import BeautifulSoup


class MovieComments:
    def __init__(self):
        self.pages = 1

    def make_urls(self):
        for page in range(self.pages):
            r = requests.get("https://movie.douban.com/subject/26794435/comments?start={}".format(page * 20))
            with open('comments.html', 'w', encoding='utf-8') as f:
                f.write(r.text)
            # soup = BeautifulSoup(r.text, 'lxml')
            # print(soup.h1)


if __name__ == '__main__':
    main = MovieComments()
    main.make_urls()
