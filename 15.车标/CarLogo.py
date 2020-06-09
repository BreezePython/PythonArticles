# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/22.使用Python学习打军体拳 23:08
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : CarLogo.py

import os
from db_maker import DbMaker as DB
from string import ascii_uppercase as au
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from sqlite3 import Binary
import threading
import time


class CarLogo:
    DATABASE = 'car.db'

    def __init__(self):
        self.db = DB()
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.images_path = os.path.join(self.path, 'images_path')
        self.host = "http://www.chebiaow.com"
        self.headers = {
            'Connection': 'keep-alive',
            'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
        }

    def check_dir(self):
        if not os.path.exists(self.images_path):
            os.mkdir(self.images_path)

    def get_response(self, url, params=None):
        try:
            r = requests.get(url, headers=self.headers, params=params, timeout=15)
        except:
            pass
        soup = BeautifulSoup(r.text, "lxml")
        return soup

    def create_url(self):
        _url_format = "http://www.chebiaow.com/logo/{}.html"
        for uppercase in au:
            try:
                soup = self.get_response(_url_format.format(uppercase))
                _cars = soup.find("ul", {"class": "cb-list"}).findAll('li')
                for car in _cars:
                    # self.car_info()
                    t = threading.Thread(target=self.car_info, args=(urljoin(self.host, car.div.a['href']),))
                    time.sleep(0.1)
                    t.start()
            except:
                pass

    def car_info(self, url):
        sm.acquire()
        try:
            soup = self.get_response(url)
            left_index = soup.find("div", {"class": "xq-left"}).findAll('p')
            name = left_index[0].text
            image_byte = requests.get(left_index[1].img['src'], headers=self.headers).content
            right_index = soup.find("ul", {"class": "xq-right"}).findAll('li')
            founded = right_index[3].span.text
            models = right_index[5].span.text
            website = right_index[7].span.text
            print("Insert Car Logo {}".format(name))
            _sql = "insert into car_logo(name,image,founded,models,website) values (?,?,?,?,?)"
            self.db.insert(_sql, (name, Binary(image_byte), founded, models, website))
        except Exception as error:
            print(error)
        sm.release()


if __name__ == '__main__':
    sm = threading.Semaphore(5)
    m = CarLogo()
    m.create_url()
