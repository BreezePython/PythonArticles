# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/7/24 2:23
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : DearestGirl.py
import jieba
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import numpy as np
from PIL import Image


class DearestGirl:
    ROLES = "秦问天 倾城 青儿"

    def __init__(self):
        self.result = dict()

    def add_key_word(self):
        for user in self.ROLES.split():
            jieba.add_word(user)

    def cut_word(self):
        data = open("太古神王全本.txt", encoding='utf-8').read()
        jieba_cut = jieba.cut(data)
        for word in jieba_cut:
            if word not in self.ROLES.split():
                continue
            else:
                self.result[word] = self.result.get(word, 0) + 1

    def sort_words(self):
        print(sorted(self.result.items(), key=lambda x: x[1], reverse=True))

    def word_cloud(self):
        mask = np.array(Image.open('1.png'))
        wc = WordCloud(
            font_path='C:/Windows/Fonts/simhei.ttf',  # 设置字体格式
            mask=mask,
            max_words=200,
            max_font_size=100
        )
        wc.generate_from_frequencies(self.result)
        image_colors = ImageColorGenerator(mask)
        wc.recolor(color_func=image_colors)
        wc.to_file('result.jpg')


if __name__ == '__main__':
    main = DearestGirl()
    main.add_key_word()
    main.cut_word()
    main.sort_words()
