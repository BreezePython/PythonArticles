# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/8/15 21:39
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : TempComparison.py

import requests
from bs4 import BeautifulSoup
from pyecharts.charts import Line
import datetime


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
            for line in soup.findAll('div', {'class': 'conMidtab'})[1].findAll('div', {'class': 'conMidtab2'}):
                td_list = line.findAll('tr')[2].findAll('td')[1:8:3]
                self.cityInfoList.append(list(map(lambda x: x.text.strip(), td_list)))
        print(self.cityInfoList)

    def filter_result(self):
        top_city_info = sorted(self.cityInfoList, key=lambda x: x[1], reverse=True)[:10]
        city, high_temp, low_temp = list(zip(*top_city_info))
        now = datetime.datetime.now()
        tommorrow = (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        charts_bar = (
            Line()
                .set_global_opts(
                title_opts={"text": "省会城市温度Top10 清风Python",
                            "subtext": tommorrow})
                .add_xaxis(city)
                .add_yaxis("高温", high_temp, color='#C3322D')  # is_symbol_show=True, is_smooth=True,
                .add_yaxis("低温", low_temp, color='#399EFF')
        )
        charts_bar.render('TempComparison.html')


if __name__ == '__main__':
    main = TempComparison()
    main.get_request()
    main.filter_result()
