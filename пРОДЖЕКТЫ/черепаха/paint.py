from turtle import*
#настройки
t = Turtle()
i = 5
t.width(i)
t.speed(50)
scr = t.getscreen()
#реакция
def draw(x,y):
    t.goto(x,y)
t.ondrag(draw)

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
scr.onscreenclick(move)

#клавиатура
scr.listen()
def sneg():
    for i in range(6):
        t.fd(20)
        t.right(60)
        for i in range(3):
            t.fd(20)
            t.backward(20)
            t.left(60)
        t.right(120)
        t.back(40)
        t.left(60)
def scrclear():
    t.clear()
def setright():
    t.goto(t.xcor() + 5, t.ycor())
def setleft():
    t.goto(t.xcor() - 5, t.ycor())
def setup():
    t.goto(t.xcor(), t.ycor() + 5)
def setdown():
    t.goto(t.xcor(), t.ycor() - 5)
def BeginFill():
    t.begin_fill()
def EndFill():
    t.end_fill()
def setgreen():
    t.color("green")
def setred():
    t.color("red")
def setblue():
    t.color("blue")
def setblack():
    t.color("black")
def setwhite():
    t.color("white")
scr.onkey(setgreen,"g")
scr.onkey(setred,"r")
scr.onkey(setblue,"b")
scr.onkey(setblack,"h")
scr.onkey(setwhite,"w")
scr.onkey(BeginFill,"f")
scr.onkey(EndFill,"e")
scr.onkeypress(setright,"Right")
scr.onkeypress(setleft,"Left")
scr.onkeypress(setup,"Up")
scr.onkeypress(setdown,"Down")
scr.onkey(scrclear,"c")
scr.onkey(sneg,"p")
