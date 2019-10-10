# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/10 23:19
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : WordsToPinyin.py


from tkinter import *
from pypinyin import pinyin


class WordsToPinyin:
    def __init__(self, master=None):
        self.root = master
        self.user_input = None
        self.translation = None

    def create_frame(self, text_info):
        frame = LabelFrame(self.root, text=text_info, font=('黑体', '11'), fg='red')
        frame.grid(padx=10, pady=10, sticky=NSEW)
        return frame

    def notice(self):
        frame = self.create_frame('说明')
        info = "欢迎使用【清风Python】汉语注音工具\n请将待注音的汉字或句子，填写在下方的文本框内"
        note = Label(frame, text=info, justify=LEFT, font=('黑体', '11'))
        note.grid(sticky=EW)

    def user_words(self):
        frame = self.create_frame('待注音汉字')
        self.user_input = Text(frame, width=80, height=10, borderwidth=2, font=('黑体', '11'))
        self.user_input.grid(padx=10, pady=5)

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

    def translate(self):
        self.translation.delete(0.0, END)
        total_info = ''
        info = self.user_input.get(1.0, END).split('\n')
        for line in info:
            if not line:
                continue
            a = self.split_words(line)
            total_info += ''.join(map(lambda x: x[0].ljust(6), pinyin(line))) + '\n'
            total_info += a + '\n'

        self.translation.insert(1.0, total_info)

    def start_translate(self):
        b = Button(self.root, text='开始注音', width=15, command=self.translate)
        b.grid()

    def result_info(self):
        frame = self.create_frame('执行结果')
        self.translation = Text(frame, width=80, height=20, borderwidth=2, font=('黑体', '11'))
        self.translation.grid(padx=10, pady=5)


if __name__ == '__main__':
    def center_window(width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)


    root = Tk()
    center_window(700, 700)
    root.resizable(width=False, height=False)
    root.title('清风Python--汉字注音工具')
    Main = WordsToPinyin(root)
    Main.notice()
    Main.user_words()
    Main.start_translate()
    Main.result_info()
    root.mainloop()
