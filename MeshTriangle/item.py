import pygame, time, math, sys, os
from random import *
from pygame.locals import *

from pygame import font
class Item:
    def __init__(self, text, img, size, pos, screen):
        self.image = pygame.image.load(os.path.join("img", img)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (size[0], size[1]))
        self.text = text
        self.pos = pos
        self.size = size
        self.screen = screen

    def show(self):
        self.screen.blit(self.image, (self.pos[0], self.pos[1] + 40))

        pygame.font.init() # you have to call this at the start, 
                           # if you want to use this module.
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(self.text, False, (0, 0, 0))
        self.screen.blit(textsurface,(self.pos[0],self.pos[1]))

    def checkClick(self, posMouse):
        if posMouse[0] < self.pos[0] or posMouse[0]> self.pos[0]+self.size[0] or posMouse[1] < self.pos[1] or posMouse[1]> self.pos[1]+self.size[1]+40:
            return False
        else:
            return self.text
            
