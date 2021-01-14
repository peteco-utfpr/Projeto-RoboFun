import pygame, time, math, sys
from random import *
from pygame.locals import *

class Triangle:
    def __init__(self, ref, size, typeT):
        self.ref = ref
        self.size = size
        self.hipho = math.sqrt(2*(size*size))
        self.typeT = typeT
        self.p1 = ref
        if typeT == 0:
            self.p2 = (ref[0] + size, ref[1] + size)
            self.p3 = (ref[0], ref[1] + size)
        elif typeT == 1:
            self.p2 = (ref[0] + size, ref[1])
            self.p3 = (ref[0] + size, ref[1] + size)
        elif typeT == 2:
            self.p2 = (ref[0] + size, ref[1])
            self.p3 = (ref[0], ref[1] + size)
        elif typeT == 3:
            self.p1 = (ref[0], ref[1] + size)
            self.p2 = (ref[0] + size, ref[1] + size)
            self.p3 = (ref[0], ref[1] + size)
        self.poly = pygame.polygon(self.p1,self.p2,self.p3)

    def show(self, surface):
        pygame.draw.polygon(surface,(0,0,0),(self.p1,self.p2,self.p3), 1)

    def checkClick(self, posMouse):
        if
        
        return False
        ##if clickableObject.collidepoint(mousePosition):





largura = 600
altura = 300
window = pygame.display.set_mode((largura, altura)) ##Cria uma tela.. X e Y
pygame.display.set_caption("Robo Fun Simulator")##Nomeia a Janela
tela = pygame.display.get_surface()##)
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_cinza = (128,128,128)
window.fill(cor_branca)

##a = Triangle( (0,0), 30, 0)
##b = Triangle( (0,0), 30, 1)
##c = Triangle( (60,0), 30, 2)
##d = Triangle( (90,00), 30, 3)
##a.show(tela)
##b.show(tela)
##c.show(tela)
##d.show(tela)

listTriangles = []
size = 30
y = 0
tipStart = 0
while y < altura:
    x = 0
    if tipStart > 2:
        tipStart = 0
    print (tipStart)
    
    tip = tipStart
    while x < largura:
        if tip > 3:
            tip = 0
        
        listTriangles.append(Triangle((x, y), size, tip))
        listTriangles.append(Triangle((x, y), size, tip +1))
        tip += 2
        x += size
        
    y += size
    tipStart += 2


for i in listTriangles:
    i.show(tela)
pygame.display.flip()
pygame.display.update()




