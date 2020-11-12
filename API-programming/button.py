import pygame

class Button:
    def __init__(self, nome, cor, pos, tamRect, tamButton):
        self.name = nome
        self.color = cor
        self.pos = pos
        self.things = []
        self.sizeRect = tamRect
        self.sizeButton = tamButton

    def addThing(self, thing):
        self.things.append(thing)

    def mouseOn(self, tela, mousePos):
        if mousePos[0] >= 0 and mousePos[0] <= self.sizeButton[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.sizeButton[1]:
                  pygame.draw.rect(tela, (220,220,220), [0, self.pos[1], self.sizeButton[0], self.sizeButton[1]])
                  self.show(tela)
                
                
    def show(self, tela):
        font = pygame.font.SysFont(None, 30)
        pygame.draw.rect(tela, self.color, [self.pos[0], self.pos[1]+10, self.sizeRect[0], self.sizeRect[1]])
        text = font.render(self.name, True, (0,0,0))
        tela.blit(text, [self.pos[0]+25, self.pos[1]+20])


    def mouseClick(self, tela, mousePos):
        if mousePos[0] >= 0 and mousePos[0] <= self.sizeButton[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.sizeButton[1]:
                pygame.draw.rect(tela, (211,211,211), [100, 0, 200, 500])
                for i in self.things:
                    i.show(tela)
                return True
        return False
                
        
        

        
