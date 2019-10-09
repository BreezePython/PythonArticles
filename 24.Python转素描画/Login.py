# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/5 22:18
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : Login.py


from tkinter import *
from tkinter.messagebox import *
import base64
from icon import img
from tkinter.filedialog import *
from PIL import Image, ImageFilter, ImageOps
import os


def dodge(a, b, alpha):
    return min(int(a * 255 / (256 - b * alpha)), 255)


def draw(dir_info, blur=25, alpha=1.0):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    save_file_name = os.path.join(base_dir, 'final.png')
    print(save_file_name)
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
        self.Dir = StringVar()
        self.Port = StringVar()
        self.path = StringVar()
        self.dir_info = StringVar()
        self.createpage()

    def createpage(self):
        self.page = Frame(self.root)
        self.page.grid()
        self.tmp = open('tmp.gif', 'wb+')
        self.tmp.write(base64.b64decode(img))
        self.tmp.close()
        self.photo = PhotoImage(file='tmp.gif')
        os.remove('tmp.gif')
        Label(self.page, text='''
    公众号: 清风Python
    作者  : 王翔 
    时间  ：2019-08-06
    工具  ：Python 3.7.3 Tkinter
    详情  : 将图片转化为素描画
    ''', justify=LEFT).grid(row=0, column=0, columnspan=2, rowspan=1, stick=W, pady=5)
        Label(self.page, text="图片路径").grid(row=3, column=0, sticky=W, pady=5)
        self.dir_info = Entry(self.page, textvariable=self.path)
        self.dir_info.grid(row=3, column=1, columnspan=1, padx=20)
        Button(self.root, text="选择路径", command=lambda: self.selectPath()).grid(row=0, column=0, sticky=S, padx=20,
                                                                               pady=5)
        Label(self.page, image=self.photo).grid(row=0, column=2)
        Button(self.page, text='转换', command=self.LoginCheck, width=10).grid(row=3, column=2, padx=10, pady=5)

    def selectPath(self):
        self.path_ = askopenfilename(filetypes=[("file", "*.*")])
        self.path.set(self.path_)

    def LoginCheck(self):
        self.dir = self.dir_info.get()
        if self.dir_info == "":
            showinfo(title='错误', massage='路径错误')
        else:
            draw(self.dir)


root = Tk()
root.title('素描画转化工具')
LoginPage(root)
root.mainloop()
