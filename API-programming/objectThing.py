import pygame, os
from objectUse import ObjectUse

class ObjectThing:
    def __init__(self, image, tam, pos):
        self.ima = image
        self.image = pygame.image.load(os.path.join("images", image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))
        self.size = tam
        self.pos = pos
      

    def mouseClick(self, tela, mousePos):
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                print("Clicou")
                newObject = ObjectUse(self.ima, self.size, (300,300))
                newObject.show(tela)
                return newObject

        return False
    
    def show(self, tela):
        tela.blit(self.image, self.pos)
    
        

        
