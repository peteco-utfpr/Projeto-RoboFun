import pygame, time, math, sys
from random import *
from pygame.locals import *
from menu import Menu
##Inspiracao
##https://developers.google.com/blockly/


class Main:
    def __init__(self):
        pygame.init() 
        ## Define o tamanho da tela
        self.largura = 700
        self.altura = 500

        self.window = pygame.display.set_mode((self.largura, self.altura)) ##Cria uma tela.. X e Y
        pygame.display.set_caption("Block Program")##Nomeia a Janela
        self.tela = pygame.display.get_surface()##)
        self.cor_branca = (255, 255, 255)
        self.cor_preta = (0, 0, 0)
        self.cor_cinza = (128,128,128)

        self.window.fill(self.cor_branca)
        ##Cria um menu com as opções dos blocos
        self.menu = Menu()
        ##Uma lista que armazena todos os blocos inseridos para a programação
        self.objects = []


    ##Metodo usado para a execucao do programa
    def run(self):
        ##Variavel usada para verificar se um bloco esta sendo carregado
        draging = False
        tip = False
        stop = False
        dist = 99999
        orient = False
        block = False
        newPos = False
        while not stop:
            ##Desenha o retangulo cinza que contem o menu lateral
            pygame.draw.rect(self.tela, (192,192,192), [0, 0, 100, self.altura])
            ##Mostra os botoes do menu
            self.menu.show(self.tela)
            ##Faz a animacao se caso o mouse estiver emcima de algum botao
            self.menu.mouseOn(self.tela, pygame.mouse.get_pos())
             
            pygame.display.flip()
            pygame.display.update()
            for i in self.objects:
                i.show(self.tela)
                
            for event in pygame.event.get():
            
                ##Verifica se o um bloco foi clicado para ser adicionado a tela de programacao
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0] != 0:
                    buttonClicked, newObject = self.menu.mouseClick(self.tela, pygame.mouse.get_pos())
                    
                    ##Se foi clicado, apaga o menu lateral que abriu
                    if buttonClicked == False:
                        self.window.fill(self.cor_branca)
                    ##Se foi criado um novo bloco, adiciona ele na lista de blocos
                    if newObject != False:
                        self.objects.append(newObject)


                ##Deletar algum bloco
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DELETE and objectClicked != False:
                        self.objects.remove(objectClicked)
                        self.window.fill(self.cor_branca)
                        print("REMOVIDO!")
                        objectClicked = False

                textWrite = False
                for i in self.objects:
                    textI = i.textEnter(event)
                    if textI == True:
                        textWrite = textI
            ####Funcionamento do Drag and Drop dos blocos adicionados
                ##Verifica se o objeto foi clicado, e salva ele em uma variavel
                if event.type == pygame.MOUSEBUTTONDOWN and textWrite == False:
                    if event.button == 1:
                        objectClicked = False
                        for i in self.objects:
                            aux = i.mouseClick(pygame.mouse.get_pos())####----------------------------------------------------------------
                            if aux != False:
                                objectClicked = aux
                        ##Salva os dados da posicao do objeto, para o calculo do desvio do clique do mouse em relacao ao canto esquerdo dele
                        if objectClicked != False:
                            draging = True
                            mouse_x, mouse_y = event.pos
                            posOb = objectClicked.getPos()
                            offset_x = posOb[0] - mouse_x
                            offset_y = posOb[1] - mouse_y

                ##Verifica se o botao do mouse parou de ser clicado
                elif event.type == pygame.MOUSEBUTTONUP and textWrite == False:
                        if event.button == 1:            
                            draging = False
                            
                            if dist != 99999 and newPos != False:
                                print ("TENHO SUGESTÃO!")
                                self.window.fill(self.cor_branca)
                                objectClicked.setPos(newPos)
                                
                ##Durante o momento de arrastar o mouse com o objeto selecionado 
                elif event.type == pygame.MOUSEMOTION and textWrite == False:
                    if draging:
                        mouse_x, mouse_y = event.pos
                        objectClicked.setPos((mouse_x + offset_x, mouse_y + offset_y))

                        #####SUGESTÃO DE ENCAIXEEE
                        dist = 99999
                        orient = False
                        block = False
                        newPos = False
                        posCarry = objectClicked.getPos()
                        sizeCarry = objectClicked.getSize()
                        for i in self.objects:
                            if i != objectClicked:
                                posStop = i.getPos()
                                sizeStop = i.getSize()
                                for j in objectClicked.fit:
                                    for k in i.compatible:
                                        if j == k:                                                
                                            if j[0] == "N":
                                                distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[1])
                                                typ = "N"
                                                bl = i
                                                np = (posStop[0], posStop[1] + sizeStop[1])
                                            elif j[0] == "S":
                                                distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeCarry[1])
                                                typ = "S"
                                                bl = i
                                                np = (posStop[0], posStop[1]-sizeCarry[1])
                                            elif j[0] == "L":
                                                distCalc = abs(abs(posCarry[0] - posStop[0] ) + abs(posCarry[1] - posStop[1]) - sizeCarry[0])
                                                typ = "L"
                                                bl = i
                                                np = (posStop[0] - sizeCarry[0], posStop[1])
                                                print(distCalc)
                                            elif j[0] == "O":
                                                distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[0])
                                                typ = "O"
                                                bl = i
                                                np = (posStop[0] + sizeStop[0], posStop[1])
                                            if distCalc < dist:
                                                dist = distCalc
                                                orient = typ
                                                block = bl
                                                newPos = np
                                                
          
                        
                        if dist > 10:
                            dist = 99999
                            orient = False
                            block = False
                            newPos = False
            ######
      
                        
                        

                if event.type == pygame.QUIT: ## Verifica se o usuario clicou no X vermelho para fechar
                    pygame.quit()
                    stop = True

                        
     
               
main = Main()
main.run()
