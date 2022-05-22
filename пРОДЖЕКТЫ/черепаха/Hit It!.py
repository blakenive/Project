from turtle import*
penup()
goto(100, 250)
pendown()
class sprite(Turtle):
    def __init__(self, x, y, step=10, shape="circle", color="black"):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = step
    def setright(self):
        self.goto(self.xcor() + 10, self.ycor())
    def setleft(self):
        self.goto(self.xcor() - 10, self.ycor())
    def setup(self):
        self.goto(self.xcor(), self.ycor() + 10)
    def setdown(self):
        self.goto(self.xcor(), self.ycor() - 10)
    def set_move(self, x_start, y_start, x_end, y_end):
       self.x_start = x_start
       self.y_start = y_start       
       self.x_end = x_end
       self.y_end = y_end
       self.goto(x_start, y_start)
       self.setheading(self.towards(x_end, y_end)) #направление
  
    def make_step(self):
       self.forward(self.step) #направление уже есть

       if self.distance(self.x_end, self.y_end) < self.step: #если расстояние меньше полушага
           self.set_move(self.x_end, self.y_end, self.x_start, self.y_start) #меняем направление
    def is_collide(self,sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
player = sprite(0, -100, 10, "classic", "blue")
enemy1 = sprite(-250, 50, 10, "square" , "red")
enemy1.set_move(-250, 50, 250, 50)
enemy2 = sprite(250, -50, 10, "square" , "red")
enemy2.set_move(250, -50, -250, -50)
enemy3 = sprite(250, 150, 0, "square" , "red")
enemy3.set_move(250, 150, -250, 150)
finish = sprite(0, 250, 0, "circle" , "yellow")
scr = player.getscreen()

scr.listen()
scr.onkey(player.setright,"Right")
scr.onkey(player.setleft,"Left")
scr.onkey(player.setup,"Up")
scr.onkey(player.setdown,"Down")

total = 0
while total < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(finish):
        player.hideturtle()
        finish.hideturtle()
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        write("Выигрышь")
        break
    if player.is_collide(enemy1) or player.is_collide(enemy3) or player.is_collide(enemy2):
        total += 1
        clear()
        write(str(total))
        player.goto(0, -100)
player.hideturtle()
finish.hideturtle()
enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()
write("Проигрышь")
                
