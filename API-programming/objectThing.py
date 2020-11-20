import pygame, os
from objectUse import ObjectUse

class ObjectThing:
    def __init__(self, image, tam, pos, encaixe = [], compativel = [],hasText=False, onlyNumbers = False, typ = "None",  posTextAjuste = (0,0)):
        self.ima = image
        self.image = pygame.image.load(os.path.join("images","passivos" ,image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))
        self.size = tam
        self.pos = pos
        self.hasText = hasText
        self.onlyNumbers = onlyNumbers
        self.typ = typ
        self.posTextAjuste = posTextAjuste
        self.fit = encaixe
        self.compatible = compativel
      

    def mouseClick(self, tela, mousePos):
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                newObject = ObjectUse(self.ima, self.size, (300,300),self.fit, self.compatible,  self.hasText, self.onlyNumbers, self.typ, self.posTextAjuste)
                newObject.show(tela)
                return newObject

        return False
    
    def show(self, tela):
        tela.blit(self.image, self.pos)
    
        

        
