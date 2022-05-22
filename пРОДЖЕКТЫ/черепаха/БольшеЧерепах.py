from turtle import*
t1 = Turtle()
t2 = Turtle()
t34 = Turtle()
t4 = Turtle()
#color
t1.color("green")
t2.color("red")
t34.color("yellow")
t4.color("blue")
#shape
t2.shape("square")
t34.shape("turtle")
t4.shape("circle")
#speed
t1.speed(1000)
t2.speed(1000)
t34.speed(1000)
t4.speed(1000)
#penup
t1.penup()
t2.penup()
t34.penup()
t4.penup()
#goto
t1.goto(50,50)
t2.goto(-50,50)
t34.goto(50,-50)
t4.goto(-50,-50)
#pendown
t1.pendown()
t2.pendown()
t34.pendown()
t4.pendown()
#uzor
def kvadrat():
    for i in range(500):
        t1.forward(i)
        t1.left(120)
        t2.forward(i)
        t2.left(120)
        t34.forward(i)
        t34.left(120)
        t4.forward(i)
        t4.left(120)
kvadrat()
