# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/6 01:18
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : ChangeImage.py


from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import *
import base64
from PIL import Image, ImageFilter, ImageOps
import os

img_bs64 = b'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'


def dodge(a, b, alpha):
    return min(int(a * 255 / (256 - b * alpha)), 255)


def draw(dir_info, blur=25, alpha=1.0):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_file_name = os.path.join(base_dir, 'final.png')
    img = Image.open(dir_info)
    img1 = img.convert('L')  # 图片转换灰色
    img2 = img1.copy()
    img2 = ImageOps.invert(img2)
    for i in range(blur):
        img2 = img2.filter(ImageFilter.BLUR)
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))
            b = img2.getpixel((x, y))
        img1.putpixel((x, y), dodge(a, b, alpha))
    img1.save(save_file_name)
    img1.show()


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (420, 240))
        self.page = Frame(self.root)
        self.Dir = StringVar()
        self.Port = StringVar()
        self.path = StringVar()
        self.dir_info = StringVar()
        self.create_page()

    def create_page(self):
        self.page.grid()
        with open('tmp.gif', 'wb+') as f:
            f.write(base64.b64decode(img_bs64))
        self.photo = PhotoImage(file='tmp.gif')
        os.remove('tmp.gif')
        Label(self.page, text='''
        公众号: 清风Python
        作者  : 王翔 
        时间  ：2019-08-06
        工具  ：Python 3.7.3 Tkinter        
        详情  : 将图片转化为素描画''', justify=LEFT).grid(row=0, column=0, columnspan=2, rowspan=1, stick=NW)
        Label(self.page, text="图片路径").grid(row=3, column=0, sticky=W, pady=5)
        self.dir_info = Entry(self.page, textvariable=self.path)
        self.dir_info.grid(row=3, column=1, columnspan=1, padx=20)
        Button(self.root, text="选择路径", command=lambda: self.select_path()).grid(row=0, column=0, sticky=S, padx=20,
                                                                                pady=5)
        Label(self.page, image=self.photo).grid(row=0, column=2)
        Button(self.page, text='转换', command=self.login_check, width=10).grid(row=3, column=2, padx=10, pady=5)

    def select_path(self):
        path_ = askopenfilename(filetypes=[("file", "*.*")])
        self.path.set(path_)

    def login_check(self):
        img_dir = self.dir_info.get()
        if img_dir == "":
            showinfo(title='错误', massage='路径错误')
        else:
            draw(img_dir)


root = Tk()
root.title('素描画转化工具')
LoginPage(root)
root.mainloop()
