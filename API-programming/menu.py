from action import Action
from functions import Functions
from mathClass import Math
from variables import Variables
from bounds import Bounds
class Menu:
    def __init__(self):
        self.bounds = Bounds()
        self.action = Action()
        self.loop = Functions()
        self.math = Math()
        self.variables = Variables()
        self.buttons = [self.bounds, self.action, self.loop, self.math, self.variables]
        self.buttonActive = False
        

    def show(self, tela):
        for i in self.buttons:
            i.show(tela)

    def mouseOn(self, mousePos, tela):
        for i in self.buttons:
            i.mouseOn(mousePos, tela)

    def mouseClick(self, mousePos, tela):
        
        clicked = False
        for i in self.buttons:
            result = i.mouseClick(mousePos, tela)
            if result == True:
                clicked = True
                self.buttonActive = i
        result = False
        
        
        if self.buttonActive != False and clicked == False:
            for i in self.buttonActive.things:
                aux = i.mouseClick(mousePos, tela)
                if aux != False:
                    result = aux

        if clicked == False:
            self.buttonActive = False
                    
                        
        
        return clicked, result
