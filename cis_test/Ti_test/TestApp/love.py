# -*- coding: utf-8 -*-
# @Time    : 2022/11/11 10:39
# @Author  : PengJiong
# @Email   : 18390050274@qq.com
# @File    : love.py
# coding: utf-8
import turtle
import time


def LittleHeart():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)
love=input('请输入表白语句，然后回车，(例如: 小美\\n，I Love You):\n')
me=input('请输入署名:\n')
if love=='':
    love='I Love you'
if me=='':
    me='I Love you'
turtle.setup(width=900,height=600)
turtle.color('red','pink')
turtle.pensize(15)
turtle.speed(1200)

turtle.up()

turtle.hideturtle()
turtle.goto(0,-180)
turtle.showturtle()
turtle.down()
turtle.speed(500)
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
LittleHeart()
turtle.left(120)
LittleHeart()
turtle.forward(224)
turtle.end_fill()
turtle.pensize(12)
turtle.up()
turtle.hideturtle()
turtle.goto(0,-20)
turtle.showturtle()
turtle.color('#CD5C5C','pink')
turtle.write(love,font=('gungsuh',50,),align="center")
turtle.up()
turtle.hideturtle()
if me !='':
    turtle.color('black', 'pink')
    time.sleep(1)
turtle.goto(180,-180)
turtle.showturtle()
turtle.write(me, font=(20,25), align="center", move=True)
window=turtle.Screen()
window.exitonclick()

