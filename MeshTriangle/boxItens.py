import pygame, time, math, sys, os
from random import *
from pygame.locals import *
import item


class BoxItens:
    def __init__(self, screen):
        self.size = (300, 500)
        ## Imagem Padrão
        ##self.background = pygame.image.load(os.path.join("img", "backToSelectItem.jpg")).convert_alpha()
        ##self.background = pygame.transform.scale(self.background, (self.size[0], self.size[1]))
        self.screen = screen
        print(self.screen.get_width())
        print(self.screen.get_height())
        self.posBackground = (self.screen.get_width()/2 - self.size[0]/2, self.screen.get_height()/2 - self.size[1]/2)
        

        self.items = []
        self.items.append(item.Item("Cone", "Cone.png", (50, 65), (self.posBackground[0] + 20, self.posBackground[1] + 70 ), self.screen))
        self.items.append(item.Item("Parede", "wall.png", (60, 60), (self.posBackground[0] + 90, self.posBackground[1] + 70 ), self.screen))
        self.items.append(item.Item("Caixa", "box.png", (60, 60), (self.posBackground[0] + 170, self.posBackground[1] + 70 ), self.screen))
       
        
    def show(self):
        pygame.draw.rect(self.screen, (255,255,255), [self.posBackground[0], self.posBackground[1], self.size[0], self.size[1]])
        pygame.draw.rect(self.screen, (0,0,0), [self.posBackground[0], self.posBackground[1], self.size[0], self.size[1]], 1)
        ##self.screen.blit(self.background, self.posBackground)
        for i in self.items:
            i.show()

    def checkClickIten(self, posMouse):
        for i in self.items:
            itemClicked = i.checkClick(posMouse)
            if itemClicked != False:
                break
        print(itemClicked)
        return itemClicked
        
