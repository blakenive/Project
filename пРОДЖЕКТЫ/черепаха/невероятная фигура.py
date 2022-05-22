#Оптимизируй код прошлого разработчика

from turtle import *
pensize(3)
speed(100)
k = 0
while k != 23:
    left(15)
    color('black')
    s = 0
    while s != 5:
        forward(75)
        left(72)
        s += 1
    begin_fill()
    color('silver')
    circle(50)
    end_fill()
    color('gold')
    begin_fill()
    l = 0
    while l != 4:
        forward(50)
        left(90)
        l += 1
    end_fill()
   
    k += 1

