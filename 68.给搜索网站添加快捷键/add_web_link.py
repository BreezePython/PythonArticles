# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2021/01/24 22:38:53
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : add_web_link.py
import sqlite3
import csv
import os


class AddChromeLink:
    def __init__(self):
        self.db_file = os.path.join(os.environ['LOCALAPPDATA'], r'Google\Chrome\User Data\Default\Web Data')
        self.conn = self.db_conn()

    def check_db_file(self):
        if not os.path.exists(self.db_file):
            input("奇怪了，洗洗睡吧。怎么找不到你的chrome浏览器数据库!")
            exit(1)

    def db_conn(self):
        conn = sqlite3.connect(self.db_file, timeout=3)
        return conn

    def get_start_id(self):
        cursor = self.conn.cursor()
        try:
            cursor.execute('select max(id) from keywords')
            record = cursor.fetchone()
            return record[0] + 1
        except sqlite3.OperationalError:
            input("数据库已锁，请先关闭chrome浏览器，在进行数据插入操作.")
            exit(1)
        finally:
            cursor.close()

    def insert_web_link(self):
        web_links = csv.DictReader(open('website.csv'), delimiter='\t')
        start_id = self.get_start_id()
        cursor = self.conn.cursor()
        try:
            for id, line in enumerate(web_links, start=start_id):
                sql = "insert into keywords (id,favicon_url,short_name,keyword,url) values (?,?,?,?,?)"
                cursor.execute(sql, (id, '', *line.values()))
                print("数据 %s 已插入." % list(line.values()))
            self.conn.commit()
        except sqlite3.OperationalError:
            input("数据库已锁，请先关闭chrome浏览器，在进行数据插入操作.")
        finally:
            cursor.close()
            self.conn.close()


if __name__ == '__main__':
    ChromeLink = AddChromeLink()
    ChromeLink.check_db_file()
    ChromeLink.db_conn()
    ChromeLink.insert_web_link()
    input()
