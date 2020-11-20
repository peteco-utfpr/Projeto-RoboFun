import pygame, os
from inputText import InputText 

class ObjectUse:
    def __init__(self, image, tam, pos, encaixe = [], compativel = [], hasText=False, onlyNumbers = False, typ = "None", posTextAjuste = (0,0)):
        
        self.ima = image
        self.image = pygame.image.load(os.path.join("images", "passivos", image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))

        self.imageActive = pygame.image.load(os.path.join("images", "active", image)).convert_alpha()
        self.imageActive = pygame.transform.scale(self.imageActive, (int(tam[0]), int(tam[1])))

        self.size = tam
        self.pos = pos
        self.hasText = hasText
        self.typeBlock = typ
        ## Armazena a compatibilidade do bloco
        self.fit = encaixe
        self.compatible = compativel

        ## Armazena as conexoes:
            ## Fixed: Conexoes que ao mover o bloco, devem se mover com ele
            ## Dinamic: Conexoes que nao se movem ao mover o bloco
        self.connectedFixed = []
        self.connectedDinamic = []

        ## Possivel entrada de texto (do teclado)
        
        self.posText = [pos[0] + self.size[0]/2 - 10 + posTextAjuste[0], pos[1] + self.size[1]/2 - 15 + posTextAjuste[1]]
        
        
        self.valueText = ""
        self.offsetPosText = (self.pos[0] -  self.posText[0], self.pos[1] -  self.posText[1])
        self.inputText = InputText(self.posText[0], self.posText[1], 30, 30, '1', onlyNumbers)

        self.active = False
    ## Verifica se o mouse clicou sobre o bloco, caso sim, retorna o proprio objeto
    def mouseClick(self, mousePos): 
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                self.active = True
                return self
        self.active = False
        return False

    ## Usada para detectar quando um entrada de teclado acontece
    def textEnter(self, event):
        result = False
        if self.hasText != False:
            result = self.inputText.handle_event(event)
        return result
            
    ## Mostra os bloco e seu texto na tela
    def show(self, tela):
        if self.active == True:
            tela.blit(self.imageActive, self.pos)
        else:
            tela.blit(self.image, self.pos)
            
        if self.hasText == True:
            self.inputText.show(tela)

    ## Seta a bloco para uma posicao, e reposiciona os blocos fixos dele cascateamente
    def setPos(self, pos, ajusteVisual):
        self.pos = pos
        self.inputText.setPos((pos[0] - self.offsetPosText[0], pos[1] - self.offsetPosText[1]))## = InputText(pos[0] + 30, pos[1] + 15, 30, 30, self.inputText.getText(), True)
        for i in self.connectedFixed:
            if i[1] == "O" or i[1] == "L":
                newPos = (self.pos[0] + self.size[0] - ajusteVisual , self.pos[1])
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "S" or i[1] == "N":
                newPos = (self.pos[0], self.pos[1]+ self.size[1] - ajusteVisual)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I1-op":
                newPos = (self.pos[0]+ 23, self.pos[1] + 13)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I2-op":
                newPos = (self.pos[0] + 163, self.pos[1] + 13)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I1-en":
                newPos = (self.pos[0] + 143, self.pos[1] + 15)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I2-en":
                newPos = (self.pos[0] + 283, self.pos[1] + 15)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "A-en":
                newPos = (self.pos[0] + 93, self.pos[1] + 74)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I1-se":
                newPos = (self.pos[0]+ 58, self.pos[1] + 12)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "I2-se":
                newPos = (self.pos[0] + 193, self.pos[1] + 12)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "A-se":
                newPos = (self.pos[0] + 93, self.pos[1] + 74)
                i[0].setPos(newPos, ajusteVisual)
            elif i[1] == "A-senao":
                newPos = (self.pos[0] + 93, self.pos[1] + 24)
                i[0].setPos(newPos, ajusteVisual)
            
                
                
                

    ## Retorna a posicao
    def getPos(self):
        return self.pos

    ## Retorna o tamanho
    def getSize(self):
        return self.size

    ##A diciona uma conexao
    def addConnection(self, obj, fixed = True):
        if fixed == True:
             self.connectedFixed.append(obj)
        else:
            self.connectedDinamic.append(obj)
    ## Deleta uma conexao
    def deleteConnection(self, obj, fixed = True):
        if fixed == True:
             self.connectedFixed.remove(obj)
        else:
            self.connectedDinamic.remove(obj)
        
        
            
            
        
        
    
        

        
