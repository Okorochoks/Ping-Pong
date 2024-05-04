from pygame import *
from random import randint
from time import time as timer

win_width = 700
win_height = 500

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
    def update_l(self):

        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.y < win_width - 80:
            self.rect.x += self.speed
    def update_r(self):

        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption("Пинг-Понг кирпичём")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(ing_back), (win_width, win_height))


if rel_time == True:
            now_time = timer()



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



while run:







    for e in event.get():
            if e.type == QUIT:
            run = False
 
    
    if finish != True:
        window.fiil(back)
        Roscet1.update_i()
        Roscet2.update_r()
        Mach.rect.x += speed_x
        ball.rect.y = speed_y

        if sprite.collide_rect(Roscet, Mach) or sprite.collide_rect(Roscet2, Mach):
            speed_x *= -1
            speed-y *= 1


        if Mach.rect.y > win_height-50 or Mach.rect.y < 0:
            speed_y *= -1
                
    
        if Mach.rect.x < 0:
            finish = True
            window.blit(losel, (200, 200))
            Game_Over = False




