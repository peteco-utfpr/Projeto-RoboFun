import pygame, time, math, sys, os
from random import *
from pygame.locals import *
import boxItens

class Triangle:
    def __init__(self, ref, side, angle, typeT, screen):
        self.ref = ref
        self.side = side
        self.height = side*math.cos(angle)
        self.base = 2 * (math.sqrt(side**2 - ( self.height**2)))
        self.typeT = typeT
        self.p1 = ref
        if typeT == 0:
            self.p2 = (int(ref[0] + self.base/2), int(ref[1] + self.height))
            self.p3 = (int(ref[0] - self.base/2), int(ref[1] + self.height))
        else:
            self.p2 = (int(ref[0] + self.base/2), int(ref[1] - self.height))
            self.p3 = (int(ref[0] - self.base/2), int(ref[1] - self.height))
            
        self.screen = screen

        self.color = False
        self.itemInside = False

    def getP2(self):
        return self.p2

    def getHeight(self):
        return self.height
    
    def show(self):
        pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3), 1)
        if self.color != False:
            pygame.draw.polygon(self.screen,self.color,(self.p1,self.p2,self.p3))
            
            

    def checkClick(self, posMouse):

        if self.typeT == 0:
            if posMouse[0] < self.ref[0] - self.base/2 or posMouse[0] > self.ref[0] + self.base/2:
                return False
            ## Equacao: y = (self.height / self.base)*x + self.ref[1]
            elif posMouse[1] < self.ref[1] or posMouse[1] > self.ref[1] + self.height:
                return False
            else:
                if posMouse[1] < self.ref[1] + (2*self.height/self.base)*(abs(posMouse[0]-self.ref[0])):
                    return False
                else:
                    pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3))
                    self.openOptions()
                    return self
            
        elif self.typeT == 1:
            if posMouse[0] < self.ref[0] - self.base/2 or posMouse[0] > self.ref[0] + self.base/2:
                return False
            elif posMouse[1] > self.ref[1] or posMouse[1] < self.ref[1] - self.height:
                return False
            else:
                if posMouse[1] > self.ref[1] - (2*self.height/self.base)*(abs(posMouse[0]-self.ref[0])):
                    return False
                else:
                    pygame.draw.polygon(self.screen,(0,0,0),(self.p1,self.p2,self.p3))
                    self.openOptions()
                    return self 
        return False

    def openOptions(self):
        self.selectItens = boxItens.BoxItens(self.screen)
        self.selectItens.show()

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



