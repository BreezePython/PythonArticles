# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2020/5/20 01:56
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : LovePictures.py
import os
import random
from PIL import Image

SideLength = 9
ImagesTypes = ['.jpg', '.png', '.jpeg']


def get_image_path():
    """
    用户输入图片路径，并判断
    :return: 图片路径
    """
    image_path = 'images'
    if not os.path.exists(image_path):
        raise FileNotFoundError("图片路径有误，请检查...")
    return image_path


def images_side_calc(row, col):
    if row == 0 and col in [1, 2, 6, 7]:
        return True
    elif row == 1 and col not in [3, 4, 5]:
        return True
    elif row == 2 and col != 4:
        return True
    elif row in [3, 4]:
        return True
    elif row >= 5 and (row - 5) < col < (13 - row):
        return True


class LovePictures:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.image_list = list()
        self.image_path = get_image_path()

    def composite_data(self):
        dir_info = os.listdir(self.image_path)
        for file in dir_info:
            if os.path.splitext(file)[1] in ImagesTypes:
                self.image_list.append(os.path.join(self.image_path, file))
        self.image_list = random.sample(self.image_list * (SideLength * SideLength // len(dir_info) + 1),
                                        SideLength * SideLength)
        if not self.image_list:
            raise IOError("未找到符合条件的图片内容...")

    def mark_pictures(self):
        heart_image = Image.new('RGB', (128 * SideLength, 128 * SideLength))
        row = col = 0
        for side in range(SideLength * SideLength):
            if images_side_calc(col, row):
                img = Image.open(self.image_list.pop())
                img = img.resize((128, 128), Image.ANTIALIAS)
            else:
                img = Image.new("RGB", (128, 128), (0, 0, 0))
            heart_image.paste(img, (row * 128, col * 128))
            col += 1
            if col == SideLength:
                col = 0
                row += 1
            if row == col == SideLength:
                break
        heart_image.save("heart_image.jpg")


if __name__ == '__main__':
    Main = LovePictures()
    Main.composite_data()
    Main.mark_pictures()
