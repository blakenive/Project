from pygame import*
#Peremenie
GREEN =(0,255,0)
win_width = 700
win_height = 500

x1 = 100
y1 = 300

x2 = 300
y2 = 100
#Class
class Card(sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        super().__init__()
        self.rect=Rect(x,y,width,height)
        self.fill_color = color
    def draw(self):
        draw.rect(window, self.fill_color,self.rect)
player1 = Card(80,80,100,150,GREEN)

class Pic(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect=self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
player2 = transform.scale(image.load("Печенька.png"),(106,100))
player3 = transform.scale(image.load("D class.png"),(34,100))
#Экран
window = display.set_mode((700, 500))
display.set_caption("Scp:Догонялки")
background = transform.scale(image.load("background.jpg"),(700,500))
#Clock
clock = time.Clock()
FPS = 60
#Game cicle
game = True
while game:
    window.blit(background, (0,0))
    window.blit(player2,(x1,y1))
    window.blit(player3,(x2,y2))

    for e in event.get():
        if e.type == QUIT:
            game = False
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and y1 > 5:
            y1 -= 10
        if keys_pressed[K_DOWN] and y1 > 695:
            y1 += 10
        if keys_pressed[K_LEFT] and x1 > 5:
            x1 -= 10
        if keys_pressed[K_RIGHT] and x1 > 495:
            x1 += 10
        if keys_pressed[K_w]:
            y2 -= 10
        if keys_pressed[K_s]:
            y2 += 10
        if keys_pressed[K_a]:
            x2 -= 10
        if keys_pressed[K_d]:
            x2 += 10
    #other
    display.update()
    clock.tick(FPS)
    
