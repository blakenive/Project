#подключение
from pygame import*
#звуки
mixer.init()
mixer.music.set_volume(1)
mixer.music.load("Captain_Nutcase_22_restricted_edit_tiktok.ogg")
mixer.music.play(-1)
#?фонт
font.init()
font1 = font.SysFont("Comic Sans MS",70)
font2 = font.SysFont("Comic Sans MS",30)
#! переменные
clock = time.Clock()
FPS = 60
#* переменные игры
game = True
finish = False
speed_x = 5
speed_y = 5
score = 0
score1 = 0
#* экран
window = display.set_mode((1280, 720))
display.set_caption("Пим Пам Понг")
background = transform.scale(image.load("background.jpg"),(1280,720))
#! классы
class GameSprite(sprite.Sprite):
    def __init__(self,plimage,speed,x,y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(plimage),(size_x,size_y))
        self.speed = speed 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
    def colliderect(self,rect):
        return self.rect.colliderect(rect)
#* игрок
class Player(GameSprite):
    def update(self):
        self.key = key.get_pressed()
        if self.key[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if self.key[K_s] and self.rect.y <= 555:
            self.rect.y += self.speed
    def update1(self):
        self.key = key.get_pressed()
        if self.key[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if self.key[K_DOWN] and self.rect.y <= 555:
            self.rect.y += self.speed

# игроки
player1 = Player("player 1.png", 10, 20, 310, 30, 150)
player2 = Player("player 2.png", 10, 1230, 310, 30, 150)
ball = GameSprite("ball.png", 5,620,350,50,50)
#! игра
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background, (0,0))
        player1.reset()
        player1.update()
        player2.reset()
        player2.update1()
        ball.reset()
        text = font2.render("Игрок 1:" + str(score),1,(255,255,255))
        text2 = font2.render("Игрок 2:" + str(score1),1,(255,255,255))
        window.blit(text,(10,10))
        window.blit(text2,(1120,10))
    ball.rect.x += speed_y
    ball.rect.y += speed_x

    if ball.colliderect(player1.rect):
        speed_y *= -1
    if ball.colliderect(player2.rect):
        speed_y *= -1
    if ball.rect.y < 0:
        speed_x *= -1
    if ball.rect.y > 660:
        speed_x *= -1

    if ball.rect.x >= 1230:
        score += 1
        speed_y *= -1
    if ball.rect.x <= 0:
        score1 += 1
        speed_y *= -1
    if score == 15:
        text3 = font1.render("Игрок 1 Выигрышь!",1,(255,255,255))
        window.blit(text3,(300,310))
        mixer.music.stop()
        finish = True
    if score1 == 15:
        text4 = font1.render("Игрок 2 Выигрышь!",1,(255,255,255))
        window.blit(text4,(300,310))
        finish = True
        mixer.music.stop()

#! работа экрана
    display.update()
    clock.tick(FPS)