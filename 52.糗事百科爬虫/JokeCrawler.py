# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/15 1:21
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : JokeCrawler.py

import requests
from bs4 import BeautifulSoup
import re
import time


class JokeCrawler:
    def __init__(self):
        self.host = "https://www.qiushibaike.com"
        self.headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                                       '(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')}
        _time = time.strftime('%y%m%d.%H.%M.%S', time.localtime())
        self.file = open('糗事百科{}.txt'.format(_time),
                         'w+', encoding='utf-8')

    def get_request(self, url):
        r = requests.get(url, headers=self.headers)
        return BeautifulSoup(r.text, 'lxml')

    def crawler(self, url):
        jokes = self.get_request(url).findAll('div', {'id': re.compile("qiushi_tag_[0-9]+")})
        for number, joke in enumerate(jokes, start=1):
            if joke.find('span', {'class': "contentForAll"}):
                _href = joke.find('a', {"class": "contentHerf"})['href']
                content = self.get_request(self.host + _href).find('div', {"class": "content"}).text.strip()
            else:
                content = joke.find('div', {"class": "content"}).text.strip()
            self.file.write("{}.{}\n".format(number, content))

    def run(self):
        for page in range(1, 11):
            _url = "{}/text/page/{}".format(self.host, page)
            self.file.write("第{}页\n\n".format(page))
            self.crawler(_url)

    def __exit__(self):
        self.file.close()


if __name__ == '__main__':
    main = JokeCrawler()
    main.run()