import pygame
from pygame import *
pygame.init()
import sys
class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0
screen = pygame.display.set_mode((1920, 1000))
player = pygame.image.load('icons/X.jpg').convert()
background = pygame.image.load('icons/1C.jpg').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(1):                    #create 10 objects</i>
    o = GameObject(player, x, x)
    objects.append(o)
while 1:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
        o.move()
        screen.blit(o.image, o.pos)
        pygame.display.update()
    pygame.time.delay(100)