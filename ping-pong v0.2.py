from pygame import *
from random import randint
from time import time as timer



ing_back = '1382.htm'
ing_hero = '8zvh2rnn1osmmvqj8riv9cyae5arq6af.jpg'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):

        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
    def update_l(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.x += self.speed


class Roscet(Player):
    def update(self):

        keys = key.get_pressed()

        if keys[K_W] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_S] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
class Mach():
    def update(self):
        self.rect.x += self.speed
        global lost
        if self.rect.x > win_height:
            self.rect.y += self.speed
            if self.rect.y > win_height:
                self.rect.x += self.speed
                



back = ((200, 255, 255))
win_width = 600
win_height = 500
display.set_caption("Пинг-Понг кирпичём")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(ing_back), (win_width, win_height))
window.fill(back)


game = True
finish = True
clock = time.Clock()
FPS = 60
Player1 = Roscet1('8zvh2rnn1osmmvqj8riv9cyae5arq6af.jpg', 200, 200, 4, 50, 150)
Player2 = Roscet2('8zvh2rnn1osmmvqj8riv9cyae5arq6af.jpg', 520, 200, 4, 50, 150)
Mach = GameSprite('9bc5086af344731ef7a660a136c8c600.webp', 200, 200, 4, 500, 500)


font.init()
font = font.Font(None, 35)
lose1 = font.render('PLYEAR 1 LOSE!', True, (180, 0, 0))
lose2 = font.render('PLYEAR 2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3
#if rel_time == True:
#            now_time = timer()




while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
 
    
    if finish != True:
        window.fiil(back)
        Roscet1.update_r()
        Roscet2.update_l()
        Mach.rect.x += speed_x
        ball.rect.y = speed_y

        if sprite.collide_rect(Roscet1, Mach) or sprite.collide_rect(Roscet1, Mach):
        if sprite.collide_rect(Roscet2, Mach) or sprite.collide_rect(Roscet2, Mach):
            speed_x *= -1
            speed-y *= 1


        if Mach.rect.y > win_height-50 or Mach.rect.y < 0:
            speed_y *= -1
                
        


        if Mach.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            Game_Over = False
        if Mach.rect.x < win_width:
            finish = True
            window.blit(lose2, (200, 200))
            Game_Over = False

        racket1.reset()
        racket2.reset()
        Mach.reset()


    display.update()




