from turtle import*
from time import*
shape("turtle")
write("Привет", font=("Times new roman",20,"italic"))
sleep(3)
clear()
write("Я умею считать", font=("Times new roman",20,"italic"))
sleep(3)
clear()
write("Введи два числа", font=("Times new roman",20,"italic"))
a = int(input("Первое число:"))
b = int(input("Второе число:"))
clear()
penup()
goto(-200,0)
pendown()
write("Выберите операцию(+,-,*,/,**(это возвести в степень))", font=("Times new roman",20,"italic"))
c = input('Введи операцию:')
clear()
if c == "+":
    write(str(a+b), font=("Times new roman",20,"italic"))
if c == "-":
    write(str(a-b), font=("Times new roman",20,"italic"))
if c == "*":
    write(str(a*b), font=("Times new roman",20,"italic"))
if c == "**":
    write(str(a**b), font=("Times new roman",20,"italic"))
if c == "/":
    if b == 0:
        write("На ноль делить нельзя", font=("Times new roman",20,"italic"))
    else:
        write(str(a/b), font=("Times new roman",20,"italic"))
