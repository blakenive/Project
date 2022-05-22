#переменные
from pygame import*
from random import*
from time import time as timer
#звуки
mixer.init()
mixer.music.set_volume(1)
mixer.music.load("main.ogg")
mixer.music.play(-1)
kicklose = mixer.Sound("lose.ogg")
kickrestart = mixer.Sound("restart.ogg")
kickkill = mixer.Sound("kill.ogg")
kickwin = mixer.Sound("win.ogg")
#?фонт
font.init()
font1 = font.SysFont("Comic Sans MS",30)
font2 = font.SysFont("Comic Sans MS",70)
#! переменные
clock = time.Clock()
FPS = 60
#* переменные игры
game = True
finish = False
#* экран
window = display.set_mode((1280, 720))
display.set_caption("Шутер:Бой против алкоголизма")
background = transform.scale(image.load("background.jpg"),(1280,720))
#* счёты
score = 0
lost = 0
#* перезарядка
num_fire = 0
rel_time = False
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
#* игрок
class Player(GameSprite):
    def update(self):
        self.key = key.get_pressed()
        if self.key[K_a] and self.rect.x >= 5:
            self.rect.x -= self.speed
        if self.key[K_d] and self.rect.x <= 1215:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("rocket.png", 15, self.rect.centerx, self.rect.top , 25, 50)
        bullets.add(bullet)
#* противник(шампусик)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 700:
            self.rect.y = 0
            self.rect.x = randint(10,1250)
            self.speed = randint(2,3)
            lost = lost + 1
#* метеор(моргенштерн)
class Enemy2(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 700:
            self.rect.y = 0
            self.rect.x = randint(10,1250)
            self.speed = randint(2,3)
#* пули
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y == 0:
            self.kill()
#! группы
bullets = sprite.Group()
enemys = sprite.Group()
enemySUS = sprite.Group()
#?персонажи
player = Player("player.png", 10, 600, 600, 74, 100)
for i in range(6):
    enemy = Enemy("bot.png", randint(2,3), randint(10,1250),0, 50, 100)
    enemys.add(enemy)
for i in range(2):
    enemy2 = Enemy2("enemy2.png", randint(1,2), randint(10,1250),0, 90, 100)
    enemySUS.add(enemy2)
#! игра
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == MOUSEBUTTONDOWN:
            if num_fire < 5 and rel_time == False:
                num_fire += 1
                player.fire()
            if num_fire >= 5 and rel_time == False:
                rel_time = True
                a = timer()
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                num_fire = 0
                rel_time = False
                finish = False
                kicklose.stop()
                kickwin.stop()
                mixer.music.play()
                lost = 0
                score = 0
                for j in enemys:
                    j.kill()
                for f in enemySUS:
                    f.kill()
                for i in range(6):
                    enemy = Enemy("bot.png", randint(2,3), randint(10,1250),0, 50, 100)
                    enemys.add(enemy)
                for i in range(2):
                    enemy2 = Enemy2("enemy2.png", randint(1,2), randint(10,1250),0, 90, 100)
                    enemySUS.add(enemy2)
#! проигрышь победа и т.д.
    if not finish:
        window.blit(background, (0,0))
        player.reset()
        player.update()
        enemys.draw(window)
        enemys.update()
        enemySUS.draw(window)
        enemySUS.update()
        bullets.update()
        bullets.draw(window)
        text = font1.render("Пролетели:" + str(lost),1,(255,255,255))
        text2 = font1.render("Убиты:" + str(score),1,(255,255,255))
        window.blit(text,(10,50))
        window.blit(text2,(10,10))  
        if lost >= 20 or sprite.spritecollide(player, enemys, False) or sprite.spritecollide(player, enemySUS, False):
            finish = True
            mixer.music.stop()
            lost = 0
            text3 = font2.render("Проигрышь!!", 1,(255,255,255))
            window.blit(text3,(400,300))
            kicklose.play()
        sprite_list = sprite.groupcollide(enemys, bullets, True, True)
        for c in sprite_list:
            score += 1
            kickkill.play()
            enemy = Enemy("bot.png", randint(2,3), randint(10,1250),0, 50, 100)
            enemys.add(enemy)
        if score >= 15:
            finish = True
            kickwin.play()
            mixer.music.stop()
            text4 = font2.render("Победа!!", 1,(255,255,255))
            window.blit(text4,(400,300))
        if rel_time == True:
            b = timer()
            if b-a <= 2:
                text5 = font1.render("Reload", 1,(255,255,255))
                window.blit(text5,(600,650))
            else:
                num_fire = 0
                rel_time = False
#! работа экрана
    display.update()
    clock.tick(FPS)