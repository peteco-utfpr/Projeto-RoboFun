import pygame, os
from inputText import InputText 

## Classe usada para os blocos sendo usados na programção
class ObjectUse:
    def __init__(self, image, tam, pos, encaixe = [], compativel = [], hasText=False, only = False, typ = "None", posTextAjuste = (0,0)):
        ## Define os parametros iniciais

        self.size = tam
        self.area = self.size[0]*self.size[1]
        self.pos = pos
        ## Define se tem texto
        self.hasText = hasText
        ## Define o nome/tipo do bloco
        self.typeBlock = typ

        self.ima = image
        ## Imagem Padrão
        self.image = pygame.image.load(os.path.join("img", "passivos", image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))

        ## Imagem usada para quando clicar em cima do bloco
        self.imageActive = pygame.image.load(os.path.join("img", "active", image)).convert_alpha()
        self.imageActive = pygame.transform.scale(self.imageActive, (int(tam[0]), int(tam[1])))

        ## Imagem usada para a sugestão de encaixe do bloco
        self.imageSuggestion = pygame.image.load(os.path.join("img", "suggestion", image)).convert_alpha()
        self.imageSuggestion = pygame.transform.scale(self.imageSuggestion, (int(tam[0]), int(tam[1])))
        
        ## Define quais são os encaixes que são fornecidos pelo bloco
        self.fit = encaixe
        ## Define quais encaixes o bloco aceita de outros blocos
        self.compatible = compativel

        ## Armazena as conexoes: 
        ## Fixed: Conexoes que ao mover o bloco, devem se mover com ele
        self.connectedFixed = []
        ## Dinamic: Conexoes que nao se movem ao mover o bloco
        self.connectedDinamic = []

        ## Define a posição em que a entrada de texto do bloco (como ocorrem em alguns casos) ficaria
        ## As constantes foram definidas visando a melhor maneira visual
        self.posText = [pos[0] + self.size[0]/2 - 10 + posTextAjuste[0], pos[1] + self.size[1]/2 - 15 + posTextAjuste[1]]
        ## Valor do texto escrito
        self.valueText = ""
        ## Offset da posição do texto em relação a posição do bloco
        self.offsetPosText = (self.pos[0] -  self.posText[0], self.pos[1] -  self.posText[1])
        ## Cria o objeto para escrever o texto
        self.inputText = InputText(self.posText[0], self.posText[1], 30, 30, '1', only)

        ## Armazena se o bloco está selecionado
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
        self.inputText.setPos((pos[0] - self.offsetPosText[0], pos[1] - self.offsetPosText[1]))
        ## Para todos os objetos conectados da maneira Fixed, depende da maneira como a conexão é realizada para fazer o ajuste
        for i in self.connectedFixed:
            ## Encaixe normal lateral
            if i[1] == "O" or i[1] == "L":
                newPos = (self.pos[0] + self.size[0] - ajusteVisual , self.pos[1])
                i[0].setPos(newPos, ajusteVisual)
            ## Encaixe normal superior
            elif i[1] == "S" or i[1] == "N":
                newPos = (self.pos[0], self.pos[1]+ self.size[1] - ajusteVisual)
                i[0].setPos(newPos, ajusteVisual)
            ## Primeiro encaixe interior do bloco Operacao
            elif i[1] == "I1-op":
                newPos = (self.pos[0]+ 23, self.pos[1] + 13)
                i[0].setPos(newPos, ajusteVisual)
            ## Segundo encaixe interior do bloco Operacao
            elif i[1] == "I2-op":
                newPos = (self.pos[0] + 163, self.pos[1] + 13)
                i[0].setPos(newPos, ajusteVisual)
            ## Primero encaixe interior do bloco Enquanto
            elif i[1] == "I1-en":
                newPos = (self.pos[0] + 143, self.pos[1] + 15)
                i[0].setPos(newPos, ajusteVisual)
            ## Segundo encaixe interior do bloco Enquanto
            elif i[1] == "I2-en":
                newPos = (self.pos[0] + 283, self.pos[1] + 15)
                i[0].setPos(newPos, ajusteVisual)
            ## Primeiro bloco encaixado aninhado com o Enquanto
            elif i[1] == "A-en":
                newPos = (self.pos[0] + 93, self.pos[1] + 74)
                i[0].setPos(newPos, ajusteVisual)
            ## Primeiro encaixe interior do bloco Se
            elif i[1] == "I1-se":
                newPos = (self.pos[0]+ 58, self.pos[1] + 12)
                i[0].setPos(newPos, ajusteVisual)
            ## Segundo encaixe interior do bloco Se
            elif i[1] == "I2-se":
                newPos = (self.pos[0] + 193, self.pos[1] + 12)
                i[0].setPos(newPos, ajusteVisual)
            ## Primeiro bloco encaixado aninhado com o Se
            elif i[1] == "A-se":
                newPos = (self.pos[0] + 93, self.pos[1] + 74)
                i[0].setPos(newPos, ajusteVisual)
            ## Primeiro bloco encaixado aninhado com senão
            elif i[1] == "A-senao":
                newPos = (self.pos[0] + 93, self.pos[1] + 24)
                i[0].setPos(newPos, ajusteVisual)
            
    ## Retorna a posicao
    def getPosInversed(self):
        return (self.pos[1], self.pos[0])

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

    ## Desenha a sugestão de encaixe (imagem toda cinza do bloco)
    def drawSuggestion(self, pos, tela):
        tela.blit(self.imageSuggestion, pos)

    ## Retorna o tipo/nome do bloco
    def getType(self):
        return self.typeBlock

    ## Retorna o texto escrito
    def getText(self):
        return self.inputText.getText()

    ## Retorna a area ocupado pelo bloco
    def getArea(self):
        return self.area
            
            
        
        
    
        

        
