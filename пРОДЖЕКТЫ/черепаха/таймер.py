from time import*
from turtle import*
write("я черепуха таймер \n запуск 1 стоп 0")

number = int(input("1 - старт, 0 - стоп:"))
while number != 0:
    if number == 1:
        start = time()
    else:
        write("ERROR 0000x1")
        sleep(10)
        clear()
    number = int(input("1 - старт, 0 - стоп:"))
clear()
end = time()
times = (end - start)
write("общее время:" + str(round(times,2)))







































































































#пашалка
