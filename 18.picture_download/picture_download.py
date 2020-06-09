# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/25 23:55.记一次python配置文件的大坑
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : picture_download.py

import os
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, urljoin, urlsplit
import threading


class PictureDownload:
    BaseUrl = "https://pixabay.com/zh/images/search/"
    DefaultPages = 5
    Path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        # cookie大家在使用的时候，记得替换...
        self.headers = {
            "cache-control":"Cache-control: private, max-age=0, no-cache",
            "cf-ray":"4fc0bf640b4e20be-LAX",
            "set-cookie":"lang=zh; expires=Sun, 22.使用Python学习打军体拳-Jul-2029 20:05:15 GMT; Max-Age=315360000; Path=/",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "cookie": "__cfduid=db4c7fedc0b42d0ba4df71f0a6bb61b001564084956; lang=zh; _ga=GA1.2.314030298.1564084752; _gid=GA1.2.2023032267.1564084752; is_human=1; client_width=1903; cf_clearance=65c758669b4c70b8d7300c06185fc16df3861533-1564085107-1800-250; _gat_UA-20223345-1=1"
        }
        self.url, self.download_path = self.set_basic()

    def set_basic(self):
        _url = urljoin(self.BaseUrl, quote(keyword))
        _download_Path = os.path.join(self.Path, keyword)
        if not os.path.exists(_download_Path):
            os.mkdir(_download_Path)
        return _url, _download_Path

    def get_url(self):
        for page in range(self.DefaultPages + 1):
            parameter = {'pagi': page}
            r = requests.get(self.url, params=parameter, headers=self.headers, timeout=10)
            soup = BeautifulSoup(r.text, 'lxml')

            items = soup.find("div", {"class": "search_results"}).find_all("div", {"class": "item"})
            for item in items:
                _img = item.a.img.attrs
                link = _img.get("data-lazy-srcset") or _img.get("srcset")
                alt = _img.get('alt')
                t = threading.Thread(target=self.save_picture, args=(link, alt))
                t.start()
                time.sleep(0.2)

    def save_picture(self, link, alt):

        _url = link.split(' 1x')[0].replace('__340', '_960_720')
        _file_name = os.path.join(self.download_path, alt + _url.split('/')[-1])
        r = requests.get(_url, headers=self.headers, timeout=5)
        try:
            with open(_file_name, 'wb') as f:
                f.write(r.content)
            print("{}下载完成".format(_file_name))
        except:
            print("{}下载失败".format(_file_name))


if __name__ == '__main__':
    keyword = str(input("请输入所需下载图片的关键字："))
    main = PictureDownload()
    main.get_url()
