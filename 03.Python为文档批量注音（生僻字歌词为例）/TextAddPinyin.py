# -*- coding: utf-8 -*-
# @Author  : 王翔
# @JianShu : 一梦七年诗
# @Date    : 2019/5/23 22.使用Python学习打军体拳:52
# Software : PyCharm
# version  ：Python 3.6.8
# @File    : TextAddPinyin.py

from pypinyin import pinyin
import re


class ChangePinyin:
    def __init__(self, filename):
        self.file = filename
        self.lyric = self.read_file()
        self.pinyin = []

    def read_file(self):
        with open(self.file, encoding='utf-8') as f:
            return f.readlines()

    def write_file(self):
        with open('New_%s' % self.file, 'w', encoding='utf-8') as f:
            print(self.lyric)
            for line in self.lyric:
                # print(line)
                if line.strip() == '':
                    continue
                _new_line = re.sub(r'\s', '', line)
                # 行内容转拼音
                _pinyin = ''.join(map(lambda x: x[0].ljust(6), pinyin(_new_line)))
                # 根据中英文,将行内容进行字符与汉字的拆分
                _lyric = self.split_words(_new_line)
                f.write('%s\n%s\n' % (_pinyin, _lyric))

    @staticmethod
    def split_words(words):
        word_list = ""
        tmp = ""
        for string in words:
            if len(bytes(string, 'utf-8')) == 3 and len(string) == 1:
                if tmp != '':
                    word_list += tmp.ljust(6)
                    tmp = ""
                word_list += string.ljust(5)
            else:
                tmp += string
        return word_list


if __name__ == '__main__':
    Main = ChangePinyin('lyric.txt')
    Main.write_file()
