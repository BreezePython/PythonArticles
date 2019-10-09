# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/16 01:14
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : EnglishWordsTest.py

import os
import random
import re


class EnglishWordsTest:
    def __init__(self):
        self.root_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(self.root_path, 'basic', 'cet4.txt'), encoding='utf-8') as f:
            _all_words = f.readlines()
        self.html = ""
        self.clean_data(random.sample(_all_words, text_num))

    def clean_data(self, data):
        exam_data = list(map(lambda x: re.sub("\s", '', x).split('/'), data))
        for num, line in enumerate(exam_data, start=1):
            self.html += """
            <tr>
                <td>{0}</td>
                <td>{3}</td>
                <td>{2}</td>
                <td><div class='word line{0}'>{1}</div></td>
                <td><button class='show'line='line{0}'>查看</button></td>
            </tr>
             """.format(num, *line)
        with open(os.path.join(self.root_path, 'basic', 'root.html'), encoding='utf-8') as f:
            data = f.read()
        with open(os.path.join(self.root_path, 'exam.html'), 'w+', encoding='utf-8') as f:
            f.write(data.replace('{content}', self.html))


if __name__ == '__main__':
    print("请输入所需测试的单词数量(范围:1-100)：")
    while True:
        try:
            text_num = int(input())
            if 1 < text_num < 100:
                break
        except ValueError:
            pass
        print("请仔细阅读输入范围！")

    EnglishWordsTest()
