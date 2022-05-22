from turtle import*
from time import*
from random import*
a = randint(1,5)
penup()
goto(-200,0)
pendown()
write("Привет! \n Я черепеха предсказываю будущее", font=('Times new roman',25,'bold'))
sleep(4)
clear()
write("Хочешь раскажу твоё будущее ?", font=('Times new roman',25,'bold'))
clear()
b = input("Предсказать?(да/нет)")
if b == "да":
    penup()
    goto(0,0)
    pendown()
    if a == 1:
        bgpic("1.gif")
        color("blue")
        write("в зимней куртке ты найдешь сотку", font=('Times new roman',20,'normal'))
    elif a == 2:
        bgpic("2.gif")
        color("red")
        write("Ты упадешь в лужу", font=('Times new roman',20,'normal'))
    elif a == 3:
        bgcolor("black")
        color("white")
        write("У тебя дома выключат свет", font=('Times new roman',20,'normal'))
    elif a == 4:
        bgpic("3.gif")
        color("green")
        write("Тебе подарят шоколадку", font=('Times new roman',20,'normal'))
    elif a == 5:
        bgpic("4.gif")
        color("gray")
        write("Скучный день \n скушай мусс", font=('Times new roman',20,'normal'))
else:
    penup()
    goto(-100,0)
    pendown()
    bgpic("нет.gif")
    color("red")
    write("Держи Рик рол", font=('Times new roman',20,'normal'))
