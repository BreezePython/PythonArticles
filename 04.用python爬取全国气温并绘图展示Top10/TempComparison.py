# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 一梦七年诗
# @Date     : 2019/5/25 11:45
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : TempComparison.py

import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line
import time


class TempComparison:
    def __init__(self):
        self.cityInfoList = []

    def get_request(self):
        areas_list = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
        headers = {
            'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/70.0.3538.67 Safari/537.36',
            'Referer': 'http://www.weather.com.cn/textFC/xn.shtml'
        }
        for area in areas_list:
            req = requests.get("http://www.weather.com.cn/textFC/%s.shtml" % area,
                               headers=headers)
            content = req.content.decode('utf-8')
            soup = BeautifulSoup(content, 'lxml')
            for line in soup.find('div', {'class': 'conMidtab'}).findAll('div', {'class': 'conMidtab2'}):
                td_list = line.findAll('tr')[2].findAll('td')[1:8:3]
                self.cityInfoList.append(list(map(lambda x: x.text.strip(), td_list)))

    def filter_result(self):
        top_city_info = sorted(self.cityInfoList, key=lambda x: x[1], reverse=True)[:10]
        city, high_temp, low_temp = list(zip(*top_city_info))
        charts_bar = (
            Line()
                .set_global_opts(
                title_opts={"text": "全国省会城市温度Top10 %s " % time.strftime("%Y-%m-%d", time.localtime()),
                            "subtext": "author:一梦七年诗"})
                .add_xaxis(city)
                .add_yaxis("高温", high_temp, color='#C3322D')  # is_symbol_show=True, is_smooth=True,
                .add_yaxis("低温", low_temp, color='#399EFF')
        )
        charts_bar.render('Python.html')


if __name__ == '__main__':
    main = TempComparison()
    main.get_request()
    main.filter_result()
