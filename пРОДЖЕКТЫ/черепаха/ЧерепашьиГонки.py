#подключения
from turtle import*
from random import*
#финишь
finish = 200
penup()
goto(200,150)
right(90)
pendown()
forward(300)
hideturtle()
#черепахи
t1=Turtle()
t2=Turtle()
t3=Turtle()
#цвет
t1.color("gold")
t2.color("silver")
t3.color("brown")
#форма
t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")
#расположение
t1.penup()
t2.penup()
t3.penup()
t1.goto(-200,90)
t2.goto(-200,0)
t3.goto(-200,-90)
#dance
def dance(t):
    t.goto(0,0)
    t.pendown()
    t.speed(100)
    for i in range(274):
        t.forward(i)
        t.left(91)
#гонка
while t1.xcor() <= finish and t2.xcor() <= finish and t3.xcor() <= finish:
    t1.forward(randint(1,7))
    t2.forward(randint(1,7))
    t3.forward(randint(1,7))
#победа победа вместо обеда
result = max(t1.xcor(),t2.xcor(),t3.xcor())
if t1.xcor() == result:
    dance(t1)
elif t2.xcor() == result:
    dance(t2)
else:
    dance(t3)
