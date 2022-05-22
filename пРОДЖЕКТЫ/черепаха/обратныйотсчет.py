from time import*
from turtle import*
color("red")
write("Я умею плентить бомбу \n введи число", font = ("Arial",20,"normal"))
a = int(input("введи число:"))
write("Bomb has been planted", font =('Arial',20,'normal'))
clear()
while a > 0:
    write(a, font =('Arial',20,'normal'))
    sleep(1)
    clear()
    a -= 1
write("BOOM", font = ("Arial",20,'normal'))
hideturtle()
