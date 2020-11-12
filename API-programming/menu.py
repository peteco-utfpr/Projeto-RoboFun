from action import Action
from loop import Loop

class Menu:
    def __init__(self):
        self.action = Action()
        self.loop = Loop()
        self.buttons = [self.action, self.loop]
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
        result = False    
        if self.buttonActive == True and clicked == False:
            
            for i in self.buttons:
                for j in i.things:
                    aux = j.mouseClick(mousePos, tela)
                    if aux != False:
                        result = aux
                        
        self.buttonActive = clicked
        return clicked, result
