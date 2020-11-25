# -*- coding: cp1252 -*-
import pygame, time, math, sys
from random import *
from pygame.locals import *


class View:
    """Desenha o ambiente (o que está representado no Model) em formato texto."""
    def __init__(self, model):
        self.model = model
        ##Define a posicao do agente
        self.posRob = None

        ## Desvio utilizado para dar espaco para colocar a numeracao no grid
        self.desv = 50

        ## Tamanho dos quadrados
        self.square_size = 50

        ##Inicia os módulos do PYGAME
        pygame.init() 

        ## Define o tamanho do grid
        self.largura = (1+self.model.columns)*self.square_size
        self.altura = (1+self.model.rows)*self.square_size

        ## Cria a tela, somando 300 na largura para colocar a parte de mostrar a saida
        self.window = pygame.display.set_mode((self.largura + 300, self.altura)) ##Cria uma tela.. X e Y
        pygame.display.set_caption("Robo Fun Simulator")##Nomeia a Janela
        self.tela = pygame.display.get_surface()##)
        self.cor_branca = (255, 255, 255)
        self.cor_preta = (0, 0, 0)
        self.cor_cinza = (128,128,128)
        self.window.fill(self.cor_branca)
        pygame.display.flip()
        pygame.display.update()
        

        ##Imagens utilizadas
        self.robo = pygame.image.load('img/robo.png').convert_alpha()
        self.robo = pygame.transform.scale(self.robo, (self.square_size - 2, self.square_size - 2))

        self.goal = pygame.image.load('img/goal.png').convert_alpha()
        self.goal = pygame.transform.scale(self.goal, (self.square_size - 2, self.square_size - 2))

        self.log = pygame.image.load('img/log.png').convert_alpha()
        self.log = pygame.transform.scale(self.log, (299, 550))

        self.goalSucess = pygame.image.load('img/goalSucess.png').convert_alpha()
        self.goalSucess = pygame.transform.scale(self.goalSucess, (self.square_size - 2, self.square_size - 2))

        ## Variavel para permitir construir a parte estatica do ambiente uma unica vez
        self.strutucteGenerate = False
        
    ## Metodo usado para construir a parte estatica do ambiente
    def drawStructure(self):

        ## Gera o contorno do grid
        for x in range(self.largura):
            for y in range(self.altura):
                rect = pygame.Rect(x*self.square_size + self.desv, y*self.square_size + self.desv,
                                   self.square_size, self.square_size)            
                pygame.draw.rect(self.tela, self.cor_preta, rect, 1)

        ## Preenche os obstaculos
        for row in range(self.model.maze.maxRows):   
            for col in range(self.model.maze.maxColumns):
                
                if self.model.maze.walls[row][col] == 1:
                    rect = pygame.Rect(row*self.square_size + self.desv +1, col*self.square_size + self.desv +1,
                                   self.square_size-2, self.square_size-2)            
                    pygame.draw.rect(self.tela, self.cor_cinza, rect)

        ## Coloca a numeracao nas colunas
        for x in range(1, self.largura):           
            txt = str(x)
            fonte=pygame.font.SysFont("Arial", 20, True, False)           ##### usa a fonte padrão
            txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
            self.tela.blit(txttela,(20 + x*50,15))            

        ## Coloca a numeracao nas linhas
        for x in range(1, self.altura):           
            txt = str(x)
            fonte=pygame.font.SysFont("Arial", 20, True, False)           ##### usa a fonte padrão
            txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
            self.tela.blit(txttela,(30, 20 + x*50))

    
    def draw(self):
        ## Verifica se a parte estatisca ja foi desenhada, caso nao, constroi e nao precisa mais chamar
        if self.strutucteGenerate == False:
            self.drawStructure()
            self.strutucteGenerate = True

        ## Limpa as mensagens do robo
        self.tela.blit(self.log, (self.largura, 5))

        ## Apaga a posicao antiga do robo
        if self.posRob != None:
            rect = pygame.Rect(self.posRob[0] + self.desv, self.posRob[1]+self.desv,
                               self.square_size-2, self.square_size-2)            
            pygame.draw.rect(self.tela, self.cor_branca, rect)
        ## Desenha o robo na nova posicao, e mostra a mensagem do robo no lado
        self.tela.blit(self.robo, (self.model.agentPos[0] *self.square_size+1+self.desv, self.model.agentPos[1]*self.square_size+1 +self.desv) )
        self.posRob = (self.model.agentPos[0] *self.square_size+1, self.model.agentPos[1]*self.square_size+1 )
        txt = "Estou em: " + str(self.model.agentPos[0]) + ", " + str(self.model.agentPos[1]) +  " Cambio..."
        fonte=pygame.font.SysFont("Times New Roman", 20, False, False)           ##### usa a fonte padrão
        txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
        self.tela.blit(txttela,(self.largura+6, 170))

        ##Desenha o objetivo
        self.tela.blit(self.goal, (self.model.goalPos[0] * self.square_size+1 + self.desv, self.model.goalPos[1]*self.square_size+1 + self.desv) )

        ## Verifica se o robo chegou no lugar, e se sim, mostra uma mensagem diferente
        if self.model.goalPos[0] == self.model.agentPos[0] and self.model.goalPos[1] == self.model.agentPos[1]:
            self.tela.blit(self.log, (self.largura, 5))
            self.tela.blit(self.goalSucess, (self.model.goalPos[0] * self.square_size+1 + self.desv, self.model.goalPos[1]*self.square_size+1 + self.desv))
            txt = "UFA.... Finalmente cheguei!"
            fonte=pygame.font.SysFont("Times New Roman", 20, False, False)           ##### usa a fonte padrão
            txttela = fonte.render(txt, 0, (0,0,0))  ##### renderiza o texto na cor desejada
            self.tela.blit(txttela,(self.largura+6, 170))
           
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       
        pygame.display.update()

    def rotateRobotImage(self, direction):
        if direction == "A":
            self.robo = pygame.transform.rotate(self.robo, 90)
        elif direction == "H":
            self.robo = pygame.transform.rotate(self.robo, 270)
