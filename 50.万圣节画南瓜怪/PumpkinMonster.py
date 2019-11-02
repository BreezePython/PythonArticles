# -*- coding: utf-8 -*-
# @Author   : 王翔
# @WeChat   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2019/10/29 22:30
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : PumpkinMonster.py


import turtle as t


def init():
    # 初始化
    t.bgpic('dark_night.png')
    t.screensize(500, 500, bg='white')
    t.speed(10)
    t.hideturtle()
    t.bgcolor('black')
    t.bgpic('dark_night.png')


def outline():
    #  绘制南瓜轮廓
    t.color('#CF5E1A', '#CF5E1A')
    t.penup()
    t.goto(250, 30)
    t.pendown()
    t.seth(90)
    t.begin_fill()
    for j in range(25):
        t.fd(j)
        t.left(3.6)
    for j in range(25, 0, -1):
        t.fd(j)
        t.left(3.6)
    t.seth(-90)
    t.circle(254, 180)
    t.end_fill()


def tail():
    # 绘制南瓜枝
    t.penup()
    t.goto(0, 180)
    t.pendown()
    t.color('#2E3C01')
    t.seth(100)
    t.pensize(25)
    t.circle(60, 100)


def eyes(args):
    # 眼睛
    for items in args:
        position, angle, direction = items
        t.pensize(6)
        t.penup()
        t.goto(position, 0)
        t.pendown()
        t.color('#4C180D', '#4C180D')
        t.begin_fill()
        t.seth(angle)
        for j in range(55):
            t.fd(3)
            if direction:
                t.left(3)  # 左转3度
            else:
                t.right(3)  # 左转3度
        t.goto(position, 0)
        t.end_fill()


def nose():
    # 鼻子
    t.penup()
    t.goto(0, 0)
    t.seth(180)
    t.pendown()
    t.begin_fill()
    t.circle(50, steps=3)
    t.end_fill()


def mouth():
    # 嘴巴
    t.color('#F9D503', '#F9D503')
    t.pensize(6)
    t.penup()
    t.penup()
    t.goto(-150, -100)
    t.pendown()
    t.begin_fill()
    t.seth(-30)
    t.fd(100)
    t.left(90)
    t.fd(30)
    t.right(90)
    t.fd(60)
    t.left(60)
    t.fd(60)
    t.right(90)
    t.fd(30)
    t.left(90)
    t.fd(100)
    t.end_fill()
    t.done()


if __name__ == '__main__':
    init()
    outline()
    tail()
    eyes_items = [(-60, 230, 0), (60, -50, 1)]
    eyes(eyes_items)
    nose()
    mouth()
    t.done()
