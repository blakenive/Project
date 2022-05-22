from turtle import*
from time import*
from random import*

speed(100)
#небо
penup()
goto(-500,0)
pendown()
color("cyan")
begin_fill()
for i in range(4):
    forward(1000)
    left(90)
end_fill()
#трава
penup()
goto(-500,-1000)
pendown()
color("green")
begin_fill()
for i in range(4):
    forward(1000)
    left(90)
end_fill()
#слонце
def sun():
    color("gold","yellow")
    begin_fill()
    for i in range(18):
        forward(100)
        left(100)
    end_fill()
#звезда
def zvezda():
    color("gold","yellow")
    begin_fill()
    for i in range(5):
        forward(20)
        left(144)
    end_fill()
#дом
def home():
    color("black","burlywood")
    begin_fill()
    for i in range(4):
        forward(100)
        left(90)
    end_fill()
    left(90)
    forward(100)
    right(90)
    color("black","chocolate4")
    begin_fill()
    for i in range(3):
        forward(100)
        left(120)
    end_fill()
#дерево
def derevo():

    color("black","lime")
    begin_fill()
    for i in range(3):
        forward(60)
        left(120)
    forward(25)
    right(120)
    for i in range(3):
        forward(100)
        left(120)
    end_fill()
    penup()
    left(30)
    forward(65)
    pendown()
    color('brown4')
    width(12)
    forward(50)
#рисунок
def zwe():    
    for i in range(3):
        x = randint (-300,300)
        y = randint (10,400)
        penup()
        goto(x,y)
        pendown()
        zvezda()
zwe()
def drevi():    
    for i in range(30):
        
        a = randint (-300,300)
        b = randint (0,600)*-1
        penup()
        goto(a,0)
        pendown()
        derevo()
        left(90)
        width(1)
drevi()



