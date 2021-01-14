import pygame, time, math, sys, os
from random import *
from pygame.locals import *
import boxItens

class Square:
    def __init__(self, ref, side, screen):
        self.ref = ref
        self.side = side
               
        self.screen = screen

        self.color = False
        self.itemInside = False

    def getP2(self):
        return self.p2

    def getHeight(self):
        return self.height
    
    def show(self):
        pygame.draw.rect(self.screen,(0,0,0),(self.ref[0],self.ref[1],self.side,self.side),1)
        if self.color != False:
            pygame.draw.rect(self.screen,self.color,(self.ref[0],self.ref[1],self.side,self.side))

    def checkClick(self, posMouse):
        if posMouse[0] < self.ref[0] or posMouse[0] > self.ref[0] + self.side:
            return False
        ## Equacao: y = (self.height / self.base)*x + self.ref[1]
        elif posMouse[1] < self.ref[1] or posMouse[1] > self.ref[1] + self.side:
            return False
        else:
            pygame.draw.rect(self.screen,(0,0,0),(self.ref[0],self.ref[1],self.side,self.side))
            self.openOptions()
            return self 

    def openOptions(self):
        self.selectItens = boxItens.BoxItens(self.screen)
        self.selectItens.show()
        ##self.selectItens.show()

    def checkClickItens(self, posMouse):
        self.itemInside = self.selectItens.checkClickIten(posMouse)
        if self.itemInside == "Parede":
            self.color = (139,69,19)
        elif self.itemInside == "Cone":
            self.color = (255,69,0)
        elif self.itemInside == "Caixa":
            self.color = (205,133,63)
        else:
            self.color = False
        

