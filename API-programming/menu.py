from action import Action
from functions import Functions
from mathClass import Math
from variables import Variables
from bounds import Bounds
import pygame, os
class Menu:
    def __init__(self):
        self.bounds = Bounds()
        self.action = Action()
        self.loop = Functions()
        self.math = Math()
        self.variables = Variables()
        self.buttons = [self.bounds, self.action, self.loop, self.math, self.variables]
        self.buttonActive = False

        self.sizeButtonComp = [75, 50]
        self.buttonComp = pygame.image.load(os.path.join("images", "buttonCompilar.png")).convert_alpha()
        self.buttonComp = pygame.transform.scale(self.buttonComp, self.sizeButtonComp)
        self.posButtonComp = [10, 480]
        
        

    def show(self, tela):
        for i in self.buttons:
            i.show(tela)

        tela.blit(self.buttonComp, self.posButtonComp)

    def mouseOn(self, mousePos, tela):
        for i in self.buttons:
            i.mouseOn(mousePos, tela)

    def mouseClick(self, tela, mousePos):

        if mousePos[0] > self.posButtonComp[0] and mousePos[0] < self.posButtonComp[0] + self.sizeButtonComp[0]:
            if mousePos[1] > self.posButtonComp[1] and mousePos[0] < self.posButtonComp[1] + self.sizeButtonComp[1]:
                return True, "Generate Code"
        
        clicked = False
        for i in self.buttons:
            result = i.mouseClick(tela, mousePos)
            if result == True:
                clicked = True
                self.buttonActive = i
        result = False
        
        
        if self.buttonActive != False and clicked == False:
            for i in self.buttonActive.things:
                aux = i.mouseClick(tela, mousePos)
                if aux != False:
                    result = aux

        if clicked == False:
            self.buttonActive = False
                    
                        
        
        return clicked, result
