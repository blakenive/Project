from random import*
from turtle import*
a = randint(1,100)
write("я загадала число 1-100. \n угадай его", font = ("Arial",20,"normal"))
b = int(input("какое число я загадала?:"))
while b != a:
    if b > a:
        clear()
        write("меньше", font = ("Arial",20,"normal"))
        b = int(input("какое число я загадала?:"))
    elif b < a:
        clear()
        write("больше", font = ("Arial",20,"normal"))
        b = int(input("какое число я загадала?:"))
clear()
write("Молодец возми с полки огурец", font = ("Arial",20,"normal"))
