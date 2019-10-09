# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @Date     : 2019/9/22 22:11
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : 43.FunnyPicture.py

import argparse
from PIL import Image
import os
import copy
import random

BasePath = os.path.dirname(os.path.realpath(__file__))


class FunnyPicture:
    def __init__(self):

        self.img_mode = None
        self.img_size = None
        self.blank_image = None
        self.git_list = list()
        # 获取图片名称(去除后缀名)
        self.picture_name = os.path.splitext(os.path.split(args.picture)[1])[0]
        self.save_path = os.path.join(BasePath, self.picture_name)
        if not os.path.exists(self.save_path):
            os.mkdir(self.save_path)
        # 格式化图片路径
        self.picture = self.resize_picture()

    def resize_picture(self):
        img = Image.open(args.picture.replace('\\', '/'))
        self.img_mode = img.mode
        _width, _height = img.size
        self.img_size = _width if _width > _height else _height
        self.blank_image = Image.new(self.img_mode, (self.img_size, self.img_size), color='white')
        self.blank_image.save(os.path.join(self.save_path, '{}_blank.jpg'.format(self.picture_name)))
        _image = copy.copy(self.blank_image)
        if _width > _height:
            _image.paste(img, (0, int((self.img_size - _height) / 2)))
        else:
            _image.paste(img, (int((self.img_size - _width) / 2), 0))
        return _image

    def split_picture(self):
        size = int(args.split_number ** 0.5)
        side_len = int(self.img_size / size)
        _index = 1
        random_list = []
        blank_image = copy.copy(self.blank_image)
        for i in random.sample(range(0, size), size):
            for j in random.sample(range(0, size), size):
                random_list.append((i,j))
        random.shuffle(random_list)
        for i, j in random_list:
            if args.type != "join":
                blank_image = copy.copy(self.blank_image)
            per_size = (j * side_len, i * side_len, (j + 1) * side_len, (i + 1) * side_len)
            per_img = self.picture.crop(per_size)
            blank_image.paste(per_img, (j * side_len, i * side_len))
            self.git_list.append(copy.copy(blank_image))
            # 希望保留部分图片内容的可以取消注释
            # 中途的每一块局部图
            # per_img.save(os.path.join(self.save_path, '{}_per{}.jpg'.format(self.picture_name, _index)))
            # 动图的每一帧图片
            # blank_image.save(os.path.join(self.save_path, '{}_per_gif{}.jpg'.format(self.picture_name, _index)))
            _index += 1

    def composite_gif(self):
        images = []
        im = Image.open(os.path.join(self.save_path, '{}_blank.jpg'.format(self.picture_name)))
        # random.shuffle(self.git_list)
        for per_gif in self.git_list:
            images.append(per_gif)
        for i in range(10):
            images.append(self.picture)
        gif_name = "{}_result.gif".format(os.path.join(self.save_path, self.picture_name))
        im.save(gif_name, save_all=True, loop=True, append_images=images, duration=200)
        self.composite_mp4(gif_name)

    @staticmethod
    def composite_mp4(filename):
        import moviepy.editor as mp
        clip = mp.VideoFileClip(filename)
        clip.write_videofile(os.path.splitext(filename)[0] + '.mp4')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--picture", required=True,
                        help="请填写所需制作的图片全路径")
    parser.add_argument('-t', '--type', default='join',
                        choices=['join', 'alone'],
                        help="join为分块加载,alone为轮播闪现")
    parser.add_argument("-n", "--split_number", type=int, default=9,
                        choices=[9, 16, 25, 36, 49, 64, 81, 100],
                        help="选择拆分的图片数量")
    args = parser.parse_args()
    main = FunnyPicture()
    main.split_picture()
    main.composite_gif()
