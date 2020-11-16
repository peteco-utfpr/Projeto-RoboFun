import pygame, os
from inputText import InputText 

class ObjectUse:
    def __init__(self, image, tam, pos, encaixe = [], compativel = [], hasText=False):
        self.ima = image
        self.image = pygame.image.load(os.path.join("images", image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))
        self.size = tam
        self.pos = pos
        self.hasText = hasText
        self.fit = encaixe
        self.compatible = compativel
        self.connectedFixed = []
        self.connectedDinamic = []
      
        self.valueText = ""
        self.inputText = InputText(pos[0] + 30, pos[1] + 15, 30, 30, '1', True)

    def mouseClick(self, mousePos): 
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                return self
        return False


    def textEnter(self, event):
        result = False
        if self.hasText != False:
            result = self.inputText.handle_event(event)
            
        return result
            
                     
    def show(self, tela):
        tela.blit(self.image, self.pos)
        if self.hasText == True:
            self.inputText.show(tela)

    def setPos(self, pos):
        self.pos = pos
        self.inputText = InputText(pos[0] + 30, pos[1] + 15, 30, 30, self.inputText.getText(), True)

        
    def getPos(self):
        return self.pos

    def getSize(self):
        return self.size

    def addConnection(self, obj, fixed = True):
        if fixed == True:
             self.connectedFixed.append(obj)
        else:
            self.connectedDinamic.append(obj)

    def deleteConnection(self, obj, fixed = True):
        if fixed == True:
             self.connectedFixed.remove(obj)
        else:
            self.connectedDinamic.remove(obj)
        
        
            
            
        
        
    
        

        
