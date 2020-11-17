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
        ## Armazena a compatibilidade do bloco
        self.fit = encaixe
        self.compatible = compativel

        ## Armazena as conexoes:
            ## Fixed: Conexoes que ao mover o bloco, devem se mover com ele
            ## Dinamic: Conexoes que nao se movem ao mover o bloco
        self.connectedFixed = []
        self.connectedDinamic = []

        ## Possivel entrada de texto (do teclado)
        self.valueText = ""
        self.inputText = InputText(pos[0] + 30, pos[1] + 15, 30, 30, '1', True)

    ## Verifica se o mouse clicou sobre o bloco, caso sim, retorna o proprio objeto
    def mouseClick(self, mousePos): 
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                return self
        return False

    ## Usada para detectar quando um entrada de teclado acontece
    def textEnter(self, event):
        result = False
        if self.hasText != False:
            result = self.inputText.handle_event(event)
        return result
            
    ## Mostra os bloco e seu texto na tela
    def show(self, tela):
        tela.blit(self.image, self.pos)
        if self.hasText == True:
            self.inputText.show(tela)

    ## Seta a bloco para uma posicao, e reposiciona os blocos fixos dele cascateamente
    def setPos(self, pos):
        self.pos = pos
        self.inputText = InputText(pos[0] + 30, pos[1] + 15, 30, 30, self.inputText.getText(), True)
        for i in self.connectedFixed:
            if i[1] == "O" or i[1] == "L":
                newPos = (self.pos[0] + self.size[0], self.pos[1])
                i[0].setPos(newPos)
            elif i[1] == "S" or i[1] == "N":
                newPos = (self.pos[0], self.pos[1]+ self.size[1])
                i[0].setPos(newPos)

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
        
        
            
            
        
        
    
        

        
