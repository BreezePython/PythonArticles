# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2020/6/18 23:56
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : csdn_crawler.py


import tkinter as tk
import requests
import openpyxl
from bs4 import BeautifulSoup

class BlogCrawler:
    def __init__(self, url, sheet_name, show):
        self.sheet = sheet_name
        self.show = show
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                                      "(KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
                        }
        self.url = f"{url.rstrip('/')}/article/list"
        self.url_parser()

    def url_parser(self):
        for page_num in range(1, 100):
            self.show.config(text="正在获取第%s页数据" % page_num)
            root.update()
            response = requests.get(f'{self.url}/{page_num}', headers=self.headers)
            response.encoding = response.apparent_encoding
            response.raise_for_status()
            content = response.content
            soup = BeautifulSoup(content, 'html.parser')
            article_table = soup.find('div', class_='article-list')
            if article_table is None:
                self.show.config(text="数据获取结束.")
                return
            for article in article_table.find_all('div', class_='article-item-box'):
                article_type = article.a.span.text
                article_url = article.a["href"]
                article_span = article.a.find_all('span')
                for i in article_span:
                    i.clear()
                article_name = article.a.get_text().strip()
                create_date = article.find('div', class_='info-box').find('span', class_='date').text.strip()
                read_num, comment_num = article.find('div', class_='info-box').find_all('span', class_='read-num')
                print(article_type, article_name, article_url, create_date, read_num.text, comment_num.text)
                self.sheet.append(
                    [article_type, article_name, article_url, create_date, read_num.text, comment_num.text])


def start_crawler(url, show_info):
    wb = openpyxl.Workbook()
    try:
        st = wb.create_sheet(index=0)
        st.append(["类型", "标题", "链接", "创建时间", "阅读量", "评论数"])
        BlogCrawler(url, st, show_info)
    finally:
        wb.save("清风Python数据爬虫.xlsx")


def center_window(master, width, height):
    # tkinter GUI工具居中展示
    screenwidth = master.winfo_screenwidth()
    screenheight = master.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2,
                            (screenheight - height) / 2)
    master.geometry(size)


def user_input(root):
    note = tk.LabelFrame(root, text="软件说明", padx=10, pady=10, fg="red", font=("黑体", '11'))
    note.grid(padx=10, pady=3, sticky=tk.NSEW)
    index = tk.Label(note, text='欢迎使用CSDN文章数据统计工具,输入用户首页 URL ,'
                                '即可统计他的所有文章数据').grid()
    lb = tk.LabelFrame(root, text="输入用户主页的URL ", padx=10,
                       pady=10, fg="red", font=("黑体", '11'))
    lb.grid(padx=10, pady=3, sticky=tk.NSEW)
    unit = tk.Label(lb, text="URL: ")
    unit.grid(row=1, column=0, padx=5)
    url = tk.Entry(lb)
    url.grid(row=1, column=1, columnspan=2, padx=5, ipadx=130, pady=2)
    show_info = tk.Label(root, text='')
    show_info.grid(row=3, column=0, padx=10, pady=2, sticky=tk.W)
    submit = tk.Button(root, text="启动", width=8,
                       command=lambda: start_crawler(url.get(), show_info)
                       )
    submit.grid(row=2, column=0, pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    center_window(root, 500, 300)
    root.resizable(width=False, height=False)
    root.title('CSDN爬虫 By：清风Python')
    user_input(root)
    root.mainloop()
