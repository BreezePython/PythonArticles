# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/31 23:25
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : DouYinMusic.py

import os
import requests
from bs4 import BeautifulSoup
import threading
import time


class DouYinMusic:
    def __init__(self):
        self.music_list = []
        self.path = self.download_path()

    @staticmethod
    def download_path():
        """
        获取代码执行目录，并在目录下创建Music文件夹
        :return Music文件夹全路径
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        _path = os.path.join(base_dir, "Music")
        if not os.path.exists(_path):
            os.mkdir(_path)
        return _path

    def get_request(self, url):
        """
        封装requests.get方法
        如果为网页请求，返回网页内容
        否则，解析音乐地址，并返回音乐二进制文件
        :param url: 请求url（分网页、音乐两类）
        :return: 网页内容 & 音乐二进制文件
        """
        r = requests.get(url, timeout=5)
        if url.endswith('html'):
            return r.text
        else:
            return r.content

    def analysis_html(self, html):
        """
        根据获取的网页内容，解析音乐名称、下载地址
        调用音乐下载方法
        :param html: 网页内容
        """
        soup = BeautifulSoup(html, 'lxml')
        # 根据关键字onclick查找每个下载地址
        for tag_a in soup.findAll('a', attrs={'onclick': True}):
            # 下载格式'("name","link","")',通过eval将str转化为tuple类型
            link_list = eval(tag_a['onclick'][5:])
            music_name, music_link = link_list[:2]
            # 因为存在部分重复音乐，故设置判断下载过的音乐跳过
            if music_name in self.music_list:
                continue
            self.music_list.append(music_name)
            t = threading.Thread(target=self.download_music, args=(music_name, music_link))
            time.sleep(0.5)
            t.start()

    def download_music(self, music_name, music_link):
        """
        解析音乐文件,完成音乐下载
        :param music_name: 音乐名称
        :param music_link: 下载地址
        """
        _full_name = os.path.join(self.path, music_name)
        with open(_full_name + '.mp3', 'wb') as f:
            f.write(self.get_request(music_link))
        print("抖音音乐： {} 下载完成".format(music_name))

    def run(self):
        """
        主方法，用于批量生成url
        """
        for page in range(1,55):
            url = "http://douyin.bm8.com.cn/t_{}.html".format(page)
            html = self.get_request(url)
            self.analysis_html(html)


if __name__ == '__main__':
    main = DouYinMusic()
    main.run()
