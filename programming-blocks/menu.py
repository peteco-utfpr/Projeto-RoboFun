from action import Action
from functions import Functions
from mathClass import Math
from variables import Variables
from bounds import Bounds
import pygame, os

## Classe que se refere ao menu lateral que apresenta as opções (Variaveis, Funções....)
class Menu:
    def __init__(self):
        ## Cria os tipos que estão disponíveis
        self.bounds = Bounds()
        self.action = Action()
        self.loop = Functions()
        self.math = Math()
        self.variables = Variables()

        ## Adicona os tipos acima em uma lista
        self.buttons = [self.bounds, self.action, self.loop, self.math, self.variables]
        
        ##Variavel que armazena o valor do botão que está ativo. Em caso de False, nenhum está
        self.buttonActive = False

        ## Define o Botão de Compilar 
        self.sizeButtonComp = [75, 50]
        self.buttonComp = pygame.image.load(os.path.join("img", "buttonCompilar.png")).convert_alpha()
        self.buttonComp = pygame.transform.scale(self.buttonComp, self.sizeButtonComp)
        self.posButtonComp = [10, 480]
        
        
    ##Mostra os botões na tela
    def show(self, tela):
        for i in self.buttons:
            i.show(tela)

        tela.blit(self.buttonComp, self.posButtonComp)

    ## Verifica se o mouse está sobre os botões (chama a função de cada botão para fazer essa verificação)
    def mouseOn(self, mousePos, tela):
        for i in self.buttons:
            i.mouseOn(mousePos, tela)

    ##Verifica se alguma coisa no Menu foi clicado
    def mouseClick(self, tela, mousePos):
        ## Verifica se foi clicado no botão de Compilar
        if mousePos[0] > self.posButtonComp[0] and mousePos[0] < self.posButtonComp[0] + self.sizeButtonComp[0]:
            if mousePos[1] > self.posButtonComp[1] and mousePos[0] < self.posButtonComp[1] + self.sizeButtonComp[1]:
                return True, "Generate Code"

        ## Verifica se um dos botões da lista foi clicado 
        clicked = False
        for i in self.buttons:
            result = i.mouseClick(tela, mousePos)
            if result == True:
                clicked = True
                self.buttonActive = i


        ## Se um botão já estiver ativado
                ## Verifica se um dos objetos dele foi clicado.
                ##Caso sim, um novo objeto é retornado (dentro da variavel Result)
        result = False
        if self.buttonActive != False and clicked == False:
            for i in self.buttonActive.things:
                aux = i.mouseClick(tela, mousePos)
                if aux != False:
                    result = aux

        ## Se nenhum botão foi clicado, seta a variavel de controle para False
        if clicked == False:
            self.buttonActive = False

        ## Retorna se algum botão foi clicado, e se há um novo objeto a ser adicionado a programação          
        return clicked, result
