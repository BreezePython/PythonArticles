# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/27 1:28
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : yeji_college.py

from requests_html import HTMLSession
import json


class YejiCollege:
    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent": ("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                                       "(KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
                        }

    def get_response(self):
        session = HTMLSession()
        return session.get(self.url, headers=self.headers)

    def filter_info(self):
        html_data = self.get_response()
        # 从第三个P标签开始，获取野鸡大学数据
        return html_data.html.find('div#data249708 p')[2:]

    @staticmethod
    def get_json(data):
        info = {}
        city = None
        for line in data:
            # 每个城市会显示为 <p><strong>北京：151所</strong></p>
            if 'strong' in line.html:
                # 拆分城市与野鸡大学数量
                city, total_college = line.text.split('：')
                # 构造字典
                info[city] = dict(total=total_college, data=[])
                continue
            info[city]['data'].append(line.text)
        with open('colleges.json', 'w+', encoding='utf-8') as f:
            # ensure_ascii默认为True,json.dump后会被转码...
            f.write(json.dumps(info, ensure_ascii=False))


def run():
    url = 'http://www.gaosan.com/gaokao/249708.html'
    main = YejiCollege(url)
    data = main.filter_info()
    main.get_json(data)


if __name__ == '__main__':
    run()
