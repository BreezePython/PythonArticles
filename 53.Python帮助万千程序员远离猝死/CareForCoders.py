# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/11/28 23:23
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : CareForCoders.py

from tkinter import *
from tkinter.messagebox import showwarning, showinfo
import time
from ctypes import *
import threading


# tkinter GUI工具居中展示
def center_window(master, width, height):
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
    master.geometry(size)


# 锁定屏幕
def close_windows():
    user32 = windll.LoadLibrary('user32.dll')
    user32.LockWorkStation()


class CareForCoders:
    def user_setting(self):
        note = LabelFrame(root, text="说明", padx=10, pady=10,
                          fg="red", font=("黑体", '11'))
        note.grid(padx=10, pady=2, sticky=NSEW)
        index = Label(note, text='程序猿/媛们,久坐伤身请务必定时休息！')
        index.grid()
        lb = LabelFrame(root, text="定时设置(支持小数)", padx=10,
                        pady=10, fg="red", font=("黑体", '11'))
        lb.grid(padx=10, pady=2, sticky=NSEW)
        self.time_entry = Entry(lb)
        self.time_entry.grid(row=1, column=0)
        unit = Label(lb, text="(单位：分)")
        unit.grid(row=1, column=1, padx=5)

        self.countdown_lb = Label(text="休息倒计时:", justify=LEFT,
                                  font=("黑体", '11'))
        self.countdown_lb.grid(row=2)
        self.submit = Button(root, text="启动", width=8,
                             command=lambda: self.get_countdown(self.time_entry.get())
                             )
        self.submit.grid(row=3, column=0, pady=10)

    def get_countdown(self, countdown):
        try:
            _float_countdown = float(countdown)
            if _float_countdown <= 0:
                showwarning("提示：", message="倒计时必须为正数！")
            else:
                self.countdown_show(_float_countdown * 60)
        except ValueError:
            showwarning("提示：", message="请填写正确的倒计时！")

    def countdown_show(self, countdown_sec):
        self.time_entry.config(state=DISABLED)
        self.submit.config(state=DISABLED)
        time.sleep(1)
        self.countdown_lb.config(text="休息倒计时: %02d:%02d" %
                                      (countdown_sec // 60, countdown_sec % 60))
        root.update()
        # 为了避免突如其来的锁屏，倒计时30秒给出提示...
        if countdown_sec == 10:
            t = threading.Thread(target=self.notice)
            t.start()

        if countdown_sec < 1:
            # 启动锁屏操作
            close_windows()
            self.time_entry.config(state=NORMAL)
            self.submit.config(state=NORMAL)
            self.countdown_lb.config(text="欢迎主人回来...")
            root.update()
            return
        countdown_sec -= 1
        self.countdown_lb.after(1000, self.countdown_show(countdown_sec))

    @staticmethod
    def notice():
        message = Toplevel(root)
        message.title('提示')
        Label(message, text='主人，工作这么久了，准备休息下吧！'
              , justify=CENTER, font=("黑体", '11')).grid()
        time.sleep(3)
        message.destroy()


if __name__ == '__main__':
    root = Tk()
    center_window(root, 260, 200)
    root.resizable(width=False, height=False)
    root.title('久坐提醒 by:清风Python')
    Main = CareForCoders()
    Main.user_setting()
    root.mainloop()
