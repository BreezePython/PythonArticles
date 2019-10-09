# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/29 23:36
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : NetworkNovels.py


from requests_html import HTMLSession
from urllib.parse import quote, urljoin
import time
import os


class NetworkNovels:
    # 笔趣阁免费小说网
    URL = 'http://www.biquge.cm'

    def __init__(self, novels_name):
        self.name = novels_name
        self.quote_name = quote(self.name, encoding='gbk')
        self.headers = {"User-Agent": ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                                       "(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
                        }
        self.session = HTMLSession()

    def get_method(self, url):
        return self.session.get(url, headers=self.headers)

    def post_method(self, url):
        return self.session.post(url, headers=self.headers)

    def find_novel(self):
        paras = "searchkey={}&ct=2097152&si=biquge.cm&sts=biquge.cm".format(self.quote_name)
        post_url = "{}/modules/article/sou.php?{}".format(self.URL, paras)
        response = self.post_method(post_url)
        novel_data = response.html.find('#list a')
        if not novel_data:
            return None
        print("找到您搜索的小说：《{}》,共{}章".format(self.name, len(novel_data)))
        # 打印小说近10章内容，为避免新书，添加异常处理...
        try:
            print('以下为近十章内容：')
            for data in novel_data[-10:]:
                print(data.text)
        except IndexError:
            pass
        return novel_data

    def download_novel(self, datas, choice):
        if choice > 0:
            chapters = datas[:choice+1]
        else:
            chapters = datas[choice:]
        path = os.path.dirname(os.path.realpath(__file__))
        filename = '%s_%s.txt' % (self.name, time.strftime('%Y-%m-%d.%H.%M.%S', time.localtime()))
        download_file = os.path.join(path,filename)
        with open(download_file, 'w+', encoding='utf-8') as f:
            for chapter in chapters:
                chapter_name = chapter.text
                print("开始下载章节:%s" % chapter_name)
                f.write(chapter_name + '\n')
                chapter_url = urljoin(self.URL, chapter.attrs['href'])
                try:
                    response = self.get_method(chapter_url)
                    content = response.html.find('#content', first=True).text
                    f.write(content + '\n')
                except:
                    print('获取%s章节内容失败...' % chapter_name)


class PrepareWork:
    def get_novel(self):
        note = ("*******************华丽的分割线*******************\n"
                "***欢迎使用清风Python小说下载器,工具仅供娱乐使用**\n"
                "********欢迎关注我的微信公众号[清风Python]********\n"
                "*********带你学习的同时收获更多好玩的知识*********\n"
                "*******************华丽的分割线*******************\n"
                "请输入您想要搜索的小说名: ")
        novel_name = str(input(note))
        if novel_name:
            print("开始检索小说：《%s》" % novel_name)
            self.search_novel(novel_name)
        else:
            print("输入为空，请重新输入")
            self.get_novel()

    def search_novel(self, name):
        main_func = NetworkNovels(name)
        novel_data = main_func.find_novel()
        if not novel_data:
            print("未找到您搜索的小说内容，请确认名称正确或者换个小说看看？")
            self.get_novel()
        else:
            choice = self.get_user_choice(len(novel_data))
            main_func.download_novel(novel_data, choice)
            print("小说下载完成,起飞吧骚年！")

    def get_user_choice(self, limit_number):
        notice = ("\n请选择系统下载方式：(如您选择的章节数过多,下载期间请耐心等待...)\n"
                  "下载小说前x章,请输入章数,eg:前10章 10\n"
                  "下载小说后x章,请输入'-章数',eg:最后10章 -10\n"
                  "全书下载,请输入 0 \n"
                  "请根据要求输入:")
        try:
            user_choice = int(input(notice))
            if abs(user_choice) > limit_number:
                print("您输入的章节数大于总章节数,请重新输入...")
                self.get_user_choice(limit_number)
            return user_choice
        except ValueError:
            print("您的输入有误，请根据要求重新输入...")
            self.get_user_choice(limit_number)


if __name__ == '__main__':
    Main = PrepareWork()
    Main.get_novel()
