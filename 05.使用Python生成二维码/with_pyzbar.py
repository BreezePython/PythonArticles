# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 1:14
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : with_pyzbar.py

from pyzbar import pyzbar
from PIL import Image

image = Image.open('清风python.jpg')
txt_list = pyzbar.decode(image)
for txt in txt_list:
    barcodeData = txt.data.decode("utf-8")
    print(barcodeData)
