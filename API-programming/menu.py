from action import Action
from loop import Loop
from mathClass import Math

class Menu:
    def __init__(self):
        self.action = Action()
        self.loop = Loop()
        self.math = Math()
        self.buttons = [self.action, self.loop, self.math]
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
