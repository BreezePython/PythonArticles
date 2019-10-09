# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 22.使用Python学习打军体拳:52
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : IdiomCrawler.py

import requests
from bs4 import BeautifulSoup
import re
import threading
import time
from string import ascii_uppercase
from db_maker import DB_Maker


class IdiomCrawler:
    def __init__(self):
        self.url = "http://chengyu.haoshiwen.org"
        self.headers = {
            'Host': "chengyu.haoshiwen.org",
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
        }
        self.db=DB_Maker()

    def get_response(self, url, params=None):
        r = requests.get(url, headers=self.headers, params=params)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        return soup

    def traverse_character(self):
        # page style: http://chengyu.haoshiwen.org/list.php?t=A&page=1
        url = self.url + '/list.php'
        for char in ascii_uppercase:
            for page_num in range(1, 100):
                params = {"t": char, "page": page_num}
                soup = self.get_response(url, params)
                links = soup.findAll("a", {"href": re.compile("/view.php\?id=\d")})
                if not links:
                    continue
                for link in links:
                    t = threading.Thread(target=self.idiom_index, args=(self.url + link["href"],))
                    t.start()
                    time.sleep(0.1)

    def idiom_index(self, url):
        sem.acquire()
        try:
            soup = self.get_response(url)
            tr = soup.find("table").findAll("tr")[:6]
            info = {td.findAll('td')[0].text: td.findAll('td')[1].text for td in tr}
            info['人气'] = int(info['人气'][:-1])
            sql = "insert into idiom (name,speak,meaning,source,example,hot) values " \
                  "(?,?,?,?,?,?)"

            self.db.insert(sql,list(info.values()))
        except Exception as error_info:
            print(error_info)
        finally:
            sem.release()


if __name__ == '__main__':
    sem = threading.Semaphore(5)  # 设置线程阀值
    Crawler = IdiomCrawler()
    Crawler.traverse_character()
    while threading.active_count() != 1:
        pass  # print threading.active_count()
    else:
        print('### Selenium Jobs is over!!!###')
