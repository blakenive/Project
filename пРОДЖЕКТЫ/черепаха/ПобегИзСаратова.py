from random import*
from turtle import*
from time import*
#Setting1
t1 = Turtle()
t1.color("red")
t1.shape("circle")

#Setting2
t2 = Turtle()
t2.color("blue")
t2.shape("circle")
t2.left(120)

#Setting3
t3 = Turtle()
t3.color("green")
t3.shape("circle")
t3.right(120)

#screen size
x = 200
y = 200

def catch1(x,y):
    t1.penup()
    t1.goto(randint(-100,100),randint(-100,100))
    t1.pendown()
    t1.left(randint(0,180))
t1.onclick(catch1)

def catch2(x,y):
    t2.penup()
    t2.goto(randint(-100,100),randint(-100,100))
    t2.pendown()
    t2.left(randint(0,180))
t2.onclick(catch2)

def catch3(x,y):
    t3.penup()
    t3.goto(randint(-100,100),randint(-100,100))
    t3.pendown()
    t3.left(randint(0,180))
t3.onclick(catch3)

def game_finish(t1,t2,t3):
    t1_outside = abs(t1.xcor()) > x or abs(t1.ycor()) > y
    t2_outside = abs(t2.xcor()) > x or abs(t2.ycor()) > y
    t3_outside = abs(t3.xcor()) > x or abs(t3.ycor()) > y
    isOutside = t1_outside or t2_outside or t3_outside
    return isOutside

while game_finish(t1,t2,t3)!= True:
    t1.forward(4)
    t2.forward(4)
    t3.forward(4)
    sleep(0.1)
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t1.clear()
t2.clear()
t3.clear()
t1.write("Облом!")
t2.write("Облом!")
t3.write("Облом!")
