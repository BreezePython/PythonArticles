# -*- coding: utf-8 -*-
# @Author   : 王翔
# @JianShu  : 清风Python
# @Date     : 2019/6/7 23:19
# @Software : PyCharm
# @version  ：Python 3.6.8
# @File     : fristblood.py
import turtle


def goto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def zhengfang():
    turtle.begin_fill()
    goto(200, -200)
    for _ in range(4):
        turtle.left(90)
        turtle.forward(400)
    turtle.end_fill()


def huabian():
    for _ in range(4):
        turtle.begin_fill()
        for _ in range(5):
            turtle.circle(40, 180)
            turtle.right(180)
        turtle.right(90)
        turtle.forward(400)
        turtle.end_fill()
        turtle.left(180)
        turtle.forward(400)


def neitu():
    turtle.color('#D1C185', "#D1C185")
    goto(0, -25)
    for _ in range(12):
        turtle.begin_fill()
        turtle.circle(150, 60)
        turtle.left(90)
        turtle.circle(150, 60)
        turtle.end_fill()

def wirte():

    goto(-40,10)
    turtle.color("red")
    turtle.write("端午快乐", font=("Time", 18, "bold"))


if __name__ == '__main__':
    turtle.speed(10)
    turtle.color('#D1C185', "#839F26")
    zhengfang()
    huabian()
    neitu()
    wirte()

turtle.done()