# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/1 23:53
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : JunTiQuan.py

import os
import requests
from bs4 import BeautifulSoup
from PIL import Image


class JunTiQuan:
    def __init__(self):
        self.headers = {
            "Referer": url,
            'Connection': 'keep-alive',
            'user-agent': ('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
                           '(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36')
        }
        self.path = self.image_path()
        self.images_list = list()

    @staticmethod
    def image_path():
        """
        获取代码执行目录，并在目录下创建Music文件夹
        :return 图片下载文件夹
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        _path = os.path.join(base_dir, "Images")
        if not os.path.exists(_path):
            os.mkdir(_path)
        return _path

    def get_request(self, url):
        """
        封装requests.get方法
        如果为网页请求，返回网页内容
        否则，解析图片地址，并返回图片二进制内容
        :param url: 请求url（分网页、图片两类）
        :return: 网页内容 & 图片二进制文件
        """
        r = requests.get(url, headers=self.headers, timeout=5)
        if url.endswith('html'):
            return r.text
        else:
            return r.content

    def download_images(self, html):
        """
        解析军体拳图片
        :param html: 网页内容
        """
        soup = BeautifulSoup(html, 'lxml')
        # 根据关键字onclick查找每个下载地址
        for num, img in enumerate(soup.findAll('img', attrs={'fcksavedurl': True}), start=1):
            img_bytes = self.get_request(img['src'])
            image_name = '{}.png'.format(num)
            _full_name = os.path.join(self.path, image_name)
            self.images_list.append(_full_name)
            with open(_full_name, 'wb') as f:
                f.write(img_bytes)
            print("已下载 {}".format(image_name))

    def composite_gif(self):
        _images = []
        # 创建初始图片
        base_im = Image.open(self.images_list[0])
        # 获取图片尺寸
        _picture_size = base_im.size
        for file in self.images_list[1:]:
            im = Image.open(file)
            if im.size != _picture_size:
                # 调整尺寸
                im = im.resize(_picture_size)
            _images.append(im)
        gif = os.path.join(self.path, "juntiquan.gif")
        base_im.save(gif, save_all=True, loop=True, append_images=_images, duration=300)

    def run(self):
        html = self.get_request(url)
        self.download_images(html)
        self.composite_gif()


if __name__ == '__main__':
    url = 'http://www.360doc.com/content/16/0601/13/33121396_564170382.shtml'
    main = JunTiQuan()
    main.run()
