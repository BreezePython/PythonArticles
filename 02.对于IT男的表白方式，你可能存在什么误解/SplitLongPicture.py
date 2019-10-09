# -*- coding: utf-8 -*-
# @Author  : 王翔
# @JianShu : 一梦七年诗
# @Date    : 2019/5/23 22.使用Python学习打军体拳:44.NationalFlag
# Software : PyCharm
# version  ：Python 3.6.8
# @File    : SplitLongPicture.py


import argparse
from PIL import Image
import os


class SplitLongPicture:
    def __init__(self):
        self.dirName = os.path.split(os.path.abspath(__file__))[0]
        self.ImagePath = args.ImagePath
        self.SplitTimes = args.SplitTimes
        self.SwitchingTime = args.SwitchingTime
        self.Path, self.File = os.path.split(self.ImagePath)
        self.Image = self.check_image_file()
        self.pictureList = []

    def check_image_file(self):
        _imageType = ['.jpg', '.png', '.bmp']
        if not os.path.isfile(self.ImagePath):
            raise IOError("请检查图片路径", self.ImagePath)
        elif os.path.splitext(self.File)[1].lower() not in _imageType:
            raise TypeError("请选择系统适配的图片类型", _imageType)
        else:
            return Image.open(self.ImagePath)

    def split_image(self):
        os.chdir(self.Path)
        try:
            os.makedirs('pictures')
        except FileExistsError:
            pass
        width, height = self.Image.size
        _unitHeight = height / self.SplitTimes
        for pictureNumber in range(self.SplitTimes):
            _cropBox = (0, _unitHeight * pictureNumber, width * 0.8, _unitHeight * (pictureNumber + 1))
            _unitPicture = self.Image.crop(_cropBox)
            _pictureName = os.path.join(self.Path, 'pictures', "%d.png" % pictureNumber)
            self.pictureList.append(_pictureName)
            _unitPicture.save(_pictureName)

    def composite_gif(self):
        images = []
        im = Image.open(self.pictureList[0])
        for file in self.pictureList[1:]:
            images.append(Image.open(file))
        gifName = os.path.join(self.Path, "result.gif")
        im.save(gifName, save_all=True, loop=True, append_images=images, duration=self.SwitchingTime * 1000)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--ImagePath', help="所需分隔的图片途径")
    parser.add_argument('-t', '--SplitTimes', type=int, help="图片分隔次数")
    parser.add_argument('-s', '--SwitchingTime', type=float, help="GIF图片切换时常长(单位：秒),支持小数")
    args = parser.parse_args()
    if None in args.__dict__.values():
        parser.print_help()
    else:
        Main = SplitLongPicture()
        Main.split_image()
        Main.composite_gif()
