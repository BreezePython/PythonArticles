# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/12/28 23:53:52
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : download_images.py
import os
import re
import uuid
import requests


class DownloadImages:
    def __init__(self, file_path, git_image_path, url_prefix, expects):
        self.file_path = file_path
        self.remote_path = git_image_path
        self.url_prefix = url_prefix
        self.expect_dict = expects

    def read_file(self):
        for root, dirs, files in os.walk(self.file_path):
            if os.path.split(root)[-1] in self.expect_dict.get('dirs'):
                continue
            for file in files:
                if file in self.expect_dict.get('files'):
                    continue
                self.analysis_url(os.path.join(root, file))

    def analysis_url(self, file):
        file_info_list = list()
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
        for line in data:
            markdown_pattern = re.compile('\s*!\[.*\]\(https://.*(png|jpg|gif)')
            if markdown_pattern.match(line):
                url_pattern = re.compile('https://.*(png|jpg|gif)')
                url = url_pattern.search(line)[0]
                git_url = self.download(url)
                file_info_list.append(re.sub('https://.*(png|jpg|gif).*', git_url + ')', line))
            else:
                file_info_list.append(line)
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(file_info_list)

    def download(self, url):
        print(url)
        image_type = url.split('.')[-1]
        image_name = '%s.%s' % (uuid.uuid1().hex, image_type)
        image_path = os.path.join(self.remote_path, image_name)
        response = requests.get(url)
        img = response.content
        with open(image_path, 'wb') as f:
            f.write(img)
        return '%s/%s' % (self.url_prefix, image_name)


if __name__ == '__main__':
    markdown_path = r'E:\Codes_Repository\Python\PythonArticles\67.一分钟解决简书图片盗链问题'
    remote_path = r'D:\blogimages\images'
    expect_dict = {"dirs": ['.git', '.idea', 'static'],
                   "files": ["README.md", "_sidebar.md"]}
    git_url_prefix = 'https://gitee.com/BreezePython/blogimages/raw/master/images/'
    main = DownloadImages(markdown_path, remote_path, git_url_prefix, expect_dict)
    main.read_file()
