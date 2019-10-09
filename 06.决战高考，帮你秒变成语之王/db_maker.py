# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/6 22.使用Python学习打军体拳:23
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : db_maker.py


import sqlite3
from DBUtils.PooledDB import PooledDB


class DB_Maker:
    def __init__(self):
        self.POOL = PooledDB(
            check_same_thread=False,
            creator=sqlite3,  # 使用链接数据库的模块
            maxconnections=10,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping SQlite服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            database='database.db',
        )
        self.check_db()

    def check_db(self):
        sql = "SELECT name FROM sqlite_master where name=?"
        if not self.fetch_one(sql, ('idiom',)):
            self.create_table()

    def create_table(self):
        print("create table ...")
        sql = """create table idiom (
                        [id]            integer PRIMARY KEY autoincrement,
                        [name]         varchar (10),
                        [speak]      varchar (30),
                        [meaning]      varchar (100),
                        [source]      varchar (100),
                        [example]      varchar (100),
                        [hot]      int(10)
                    )"""
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
        conn, cursor = self.db_conn
        if not args:
            cursor.execute(sql)
        else:
            cursor.execute(sql, args)
        record = cursor.fetchone()
        self.db_close(conn, cursor)
        return record

    def fetch_all(self, sql, args):
        conn, cursor = self.db_conn
        cursor.execute(sql, args)
        record_list = cursor.fetchall()
        self.db_close(conn, cursor)
        return record_list

    def insert(self, sql, args):
        conn, cursor = self.db_conn
        row = cursor.execute(sql, args)
        conn.commit()
        self.db_close(conn, cursor)
