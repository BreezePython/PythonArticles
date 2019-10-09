# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 22.使用Python学习打军体拳:23
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : db_maker.py


import sqlite3
from DBUtils.PooledDB import PooledDB


class DbMaker:
    def __init__(self):
        self.POOL = PooledDB(
            check_same_thread=False,
            creator=sqlite3,
            maxconnections=10,
            mincached=2,
            maxcached=5,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            database='Car.db',
        )
        self.create_table()

    def create_table(self):
        print("create table if not exists car_logo ...")
        sql = ("create table if not exists car_logo ("
               "ID INTEGER PRIMARY KEY AUTOINCREMENT,"
               "Name varchar (30) not null,"
               "image BLOB not null,"
               "founded varchar (10),"
               "models varchar (50),"
               "website varchar (50) )")
        self.fetch_one(sql)

    def db_conn(self):
        conn = self.POOL.connection()
        cursor = conn.cursor()
        return conn, cursor

    @staticmethod
    def db_close(conn, cursor):
        cursor.close()
        conn.close()

    def fetch_one(self, sql, args=None):
        conn, cursor = self.db_conn()
        if not args:
            cursor.execute(sql)
        else:
            cursor.execute(sql, args)
        record = cursor.fetchone()
        self.db_close(conn, cursor)
        return record

    def fetch_all(self, sql, args):
        conn, cursor = self.db_conn()
        cursor.execute(sql, args)
        record_list = cursor.fetchall()
        self.db_close(conn, cursor)
        return record_list

    def insert(self, sql, args):
        conn, cursor = self.db_conn()
        cursor.execute(sql, args)
        conn.commit()
        self.db_close(conn, cursor)
