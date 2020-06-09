# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/14 22.使用Python学习打军体拳:23
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : BossCrawler.py

import requests
from bs4 import BeautifulSoup
import csv
import random
import time
import argparse
from pyecharts.charts import Line
import pandas as pd


class BossCrawler:
    def __init__(self, query):

        self.query = query
        self.filename = 'boss_info_%s.csv' % self.query
        self.city_code_list = self.get_city()
        self.boss_info_list = []
        self.csv_header = ["city", "profession", "salary", "company"]

    @staticmethod
    def getheaders():
        user_list = [
            "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
            "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
            "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
            "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
            "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
            "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
            "Opera/12.0(Windows NT 5.2;U;en)Presto/22.使用Python学习打军体拳.9.168 Version/12.00",
            "Opera/12.0(Windows NT 5.1;U;en)Presto/22.使用Python学习打军体拳.9.168 Version/12.00",
            "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
            "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
            "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52.糗事百科爬虫",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52.糗事百科爬虫",
            "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
            "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50.万圣节画南瓜怪",
            "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50.万圣节画南瓜怪",
            "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
            "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
            "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
            "Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
            "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
            "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
            "Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
            "Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01",
            "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01",
            "Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
            "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
            "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00",
            "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00"
        ]
        user_agent = random.choice(user_list)
        headers = {'User-Agent': user_agent}
        return headers

    def get_city(self):
        headers = self.getheaders()
        r = requests.get("http://www.zhipin.com/wapi/zpCommon/data/city.json", headers=headers)
        data = r.json()
        return [city['code'] for city in data['zpData']['hotCityList'][1:]]

    def get_response(self, url, params=None):
        headers = self.getheaders()
        r = requests.get(url, headers=headers, params=params)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, "lxml")
        return soup

    def get_url(self):
        for city_code in self.city_code_list:
            url = "https://www.zhipin.com/c%s/" % city_code
            self.per_page_info(url)
            time.sleep(10)

    def per_page_info(self, url):
        for page_num in range(1, 11):
            params = {"query": self.query, "page": page_num}
            soup = self.get_response(url, params)
            lines = soup.find('div', class_='job-list').select('ul > li')
            if not lines:
                # 代表没有数据了，换下一个城市
                return
            for line in lines:
                info_primary = line.find('div', class_="info-primary")
                city = info_primary.find('p').text.split(' ')[0]
                job = info_primary.find('div', class_="job-title").text
                # 过滤答非所谓的招聘信息
                if self.query.lower() not in job.lower():
                    continue
                salary = info_primary.find('span', class_="red").text.split('-')[0].replace('K', '')
                company = line.find('div', class_="info-company").find('a').text.lower()
                result = dict(zip(self.csv_header, [city, job, salary, company]))
                print(result)
                self.boss_info_list.append(result)

    def write_result(self):
        with open(self.filename, "w+", encoding='utf-8', newline='') as f:
            f_csv = csv.DictWriter(f, self.csv_header)
            f_csv.writeheader()
            f_csv.writerows(self.boss_info_list)

    def read_csv(self):
        data = pd.read_csv(self.filename, sep=",", header=0)
        data.groupby('city').mean()['salary'].to_frame('salary').reset_index().sort_values('salary', ascending=False)
        result = data.groupby('city').apply(lambda x: x.mean()).round(1)['salary'].to_frame(
            'salary').reset_index().sort_values('salary', ascending=False)
        print(result)
        charts_bar = (
            Line()
                .set_global_opts(
                title_opts={"text": "全国%s薪酬榜" % self.query})
                .add_xaxis(result.city.values.tolist())
                .add_yaxis("salary", result.salary.values.tolist())
        )
        charts_bar.render('%s.html' % self.query)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--keyword", help="请填写所需查询的关键字")
    args = parser.parse_args()
    if not args.keyword:
        print(parser.print_help())
    else:
        main = BossCrawler(args.keyword)
        main.get_url()
        main.write_result()
        main.read_csv()
