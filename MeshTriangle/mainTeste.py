import pygame, time, math, sys, os
from random import *
from pygame.locals import *

import mapSquare, mapTriangle


largura = 900
altura = 600
window = pygame.display.set_mode((largura, altura)) ##Cria uma tela.. X e Y
pygame.display.set_caption("Robo Fun Simulator")##Nomeia a Janela
tela = pygame.display.get_surface()##)
cor_branca = (255, 255, 255)
cor_preta = (0, 0, 0)
cor_cinza = (128,128,128)
window.fill(cor_branca)

##width, heigth, sideSquare, screen
##execution = mapSquare.MapSquare(largura, altura, 30, tela)
##execution.show()




##width, heigth, side, angle, screen
execution = mapTriangle.MapTriangle(largura, altura, 78, 0.261799, tela)
execution.show()

pygame.display.flip()
pygame.display.update()
while True:
    ## Em caso de algum evento ocorrer
    for event in pygame.event.get():
         if event.type == pygame.MOUSEBUTTONDOWN:
            redraw = execution.checkClick(pygame.mouse.get_pos())
            if redraw:
                window.fill((255, 255, 255))
                execution.show()
            
    ## Atualiza a tela 
    pygame.display.flip()
    pygame.display.update()
                
    ## Verifica se o usuario clicou no X vermelho para fechar
    if event.type == pygame.QUIT: 
        pygame.quit()



