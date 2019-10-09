# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/23 23:08
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : NationalFlag.py


import os
import argparse
from PIL import Image

BasePath = os.path.dirname(os.path.realpath(__file__))


class NationalFlag:
    def __init__(self):
        self.border = 30
        self.user_picture_size=None
        self.picture, self.picture_size = self.sharpe_image(args.picture.replace('\\', '/'), 'user_picture')
        self.icon, self.icon_size = self.sharpe_image(os.path.join(BasePath, 'icon.png'))

    def sharpe_image(self, picture_path, img_type=None):
        image = Image.open(picture_path).convert("RGBA")
        size = min(image.size)
        if not img_type:
            size = 240
        image = image.resize((size, size), Image.ANTIALIAS)
        reset_picture = self.blank_image(size, img_type)
        if not img_type:
            pimage = image.load()  # 像素的访问对象
            preset_picture = reset_picture.load()
            r = float(size / 2)  # 圆心横坐标
            r3 = int(size // 2)
            for i in range(size):
                for j in range(size):
                    lx = abs(i - r)  # 到圆心距离的横坐标
                    ly = abs(j - r)  # 到圆心距离的纵坐标
                    l = (pow(lx, 2) + pow(ly, 2)) ** 0.5  # 三角函数 半径
                    if l < r3:
                        preset_picture[i - (r - r3), j - (r - r3)] = pimage[i, j]
        else:
            reset_picture.paste(image, (self.border, self.border))

        return reset_picture, size

    def blank_image(self, size, img_type=None):

        if img_type:
            new_size = size + self.border * 2
            color_type = (255, 255, 255)
            return Image.new('RGBA', (new_size, new_size), color_type)
        else:
            color_type = (255, 255, 255, 0)
            return Image.new('RGBA', (size, size), color_type)

    def final_paste(self):
        r, g, b, a = self.icon.split()
        locate = self.picture_size+ self.border//2 -self.icon_size
        self.picture.paste(self.icon, (locate, locate), mask=a)
        self.picture.save('result.png')


def run():
    main = NationalFlag()
    main.final_paste()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--picture", required=True,
                        help="请填写所需制作的图片全路径")
    args = parser.parse_args()
    run()
