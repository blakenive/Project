from pygame import*
mixer.init()
mixer.music.set_volume(0.5)
mixer.music.load("background.ogg")
mixer.music.play(-1)
kick1 = mixer.Sound("finish.ogg")
kick2 = mixer.Sound("lose.ogg")

class GameSprite(sprite.Sprite):
    def __init__(self,plimage,speed,x,y,x1,x2):
        super().__init__()
        self.image = transform.scale(image.load(plimage),(65,65))
        self.speed = speed 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.x1 = x1
        self.x2 = x2
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        self.key = key.get_pressed()
        if self.key[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if self.key[K_s] and self.rect.y <= 640:
            self.rect.y += self.speed
        if self.key[K_a] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if self.key[K_d] and self.rect.x <= 1215:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direc = "Left"
    def update(self):
        if self.direc == "Left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        if self.rect.x <= self.x1 :
            self.direc = "Right"
        if self.rect.x >= self.x2:
            self.direc = "Left"

class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((1280, 720))
display.set_caption("Лабиринт:Смешанный")
background = transform.scale(image.load("background.png"),(1280,720))

dclass = Player("D class.png", 5,50,75,0,0)
scp049 = Enemy("SCP-049.png", 15,1100,400,1000,1200)
scp0492 = Enemy("SCP-049.png", 10,50,300,5,200)
finish = GameSprite("Finish.png", 0,1100,600,0,0)
wall1 = Wall(255,170,70,265,0,20,630)
wall2 = Wall(255,170,70,960,100,20,630)
wall3 = Wall(255,170,70,265,610,600,20)
wall4 = Wall(255,170,70,410,100,550,20)
wall5 = Wall(255,170,70,845,220,20,400)
wall6 = Wall(255,170,70,730,100,20,420)
wall7 = Wall(255,170,70,610,220,20,400)
wall8 = Wall(255,170,70,510,100,20,420)
wall9 = Wall(255,170,70,410,220,20,400)

clock = time.Clock()
FPS = 60

Finish=False
game = True

font.init()
font1 = font.Font(None,70)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not Finish:
        window.blit(background, (0,0))
        dclass.reset()
        scp049.reset()
        scp0492.reset()
        finish.reset()
        dclass.update()
        scp049.update()
        scp0492.update()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        if sprite.collide_rect(dclass, finish):
            Finish = True
            text = font1.render("You win!!", 1,(0,0,0))
            window.blit(text,(500,300))
            kick1.play()
            mixer.music.stop()
        if sprite.collide_rect(dclass, scp049) or sprite.collide_rect(dclass, scp0492) or sprite.collide_rect(dclass, wall1) or sprite.collide_rect(dclass, wall2) or sprite.collide_rect(dclass, wall3) or sprite.collide_rect(dclass, wall4) or sprite.collide_rect(dclass, wall5) or sprite.collide_rect(dclass, wall6) or sprite.collide_rect(dclass, wall7) or sprite.collide_rect(dclass, wall8) or sprite.collide_rect(dclass, wall9):
            Finish = True
            text = font1.render("Ты облажался!! space - restart", 1,(255,0,0))
            window.blit(text,(300,300))
            kick2.play()
            mixer.music.stop()

    restart = key.get_pressed()
    if restart[K_SPACE]:
        Finish = False
        kick1.stop()
        kick2.stop()
        mixer.music.play(-1)
        dclass.rect.x = 50
        dclass.rect.y = 75

    speedup = key.get_pressed()
    if speedup[K_LSHIFT]:
        dclass.speed = 12
    else:
        dclass.speed = 5
        
    display.update()
    clock.tick(FPS)