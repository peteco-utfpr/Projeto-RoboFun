import pygame, os
from objectUse import ObjectUse

## Classe para definir os objetos que aparecem como opções depois que um botão é clicado no menu inicial (Variaveis, matematica...)
class ObjectThing:
    def __init__(self, image, tam, pos, encaixe = [], compativel = [],hasText=False, only = False, typ = "None",  posTextAjuste = (0,0)):
        ## Define os parametros principais
        self.ima = image
        self.image = pygame.image.load(os.path.join("img","passivos" ,image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(tam[0]), int(tam[1])))
        self.size = tam
        self.pos = pos
        ##Define se tem texto
        self.hasText = hasText
        ## Define quais caracteres podem ser escritos
        self.only = only
        ## Define o nome/tipo do objeto
        self.typ = typ
        ## Define o ajuste a ser utilizado no texto (de acordo com a posição padrao definida)
        self.posTextAjuste = posTextAjuste
        ## Define quais tipos de encaixe esse bloco fornece 
        self.fit = encaixe
        ## Define quais tipos de encaixe esse bloco aceita dos demais
        self.compatible = compativel
      
    ## Método usado para verificar se foi clicado em cima 
    def mouseClick(self, tela, mousePos):
        if mousePos[0] >= self.pos[0] and mousePos[0] <= self.pos[0] + self.size[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.size[1]:
                ## Se foi clicado, cria um novo objeto, do tipo ObjectUse
                ## Para como parametros todos os utilizados nesse mesmo bloco
                ## Define a posição inicial na área de trabalho como sendo (100,300)
                newObject = ObjectUse(self.ima, self.size, (130,300),self.fit, self.compatible,  self.hasText, self.only, self.typ, self.posTextAjuste)
                newObject.show(tela)
                ## Cria um novo objeto visando um maior desacoplamento
                ## Retorna esse objeto criado 
                return newObject

        return False

    ## Método usado para mostrar na tela
    def show(self, tela):
        tela.blit(self.image, self.pos)
    
        

        
