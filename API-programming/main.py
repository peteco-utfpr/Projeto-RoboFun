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
        self.largura = 1200
        self.altura = 600

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

        self.ajusteVisual = 12

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
                        for i in self.objects:
                            for j in i.connectedFixed:
                                if j[0] == objectClicked:
                                    i.connectedFixed.remove(j)
                                    break
                                
                            for j in i.connectedDinamic:
                                if j[0] == objectClicked:
                                    i.connectedDinamic.remove(j)
                                
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
                            if objectClicked != False:
                                for i in objectClicked.connectedDinamic:
                                    for j in i[0].connectedFixed:
                                        if j[0] == objectClicked:
                                            i[0].connectedFixed.remove(j)
                                            break
                                    
                                objectClicked.connectedDinamic = []
                            
                            if dist != 99999 and newPos != False and objectClicked != False:
                                print ("TENHO SUGESTÃO!")
                                ##Verifica se o que esta sendo movido eh dependente do outro
                                if orient == "N" or orient == "O" or orient == "I1-op" or orient == "I2-op" or orient == "I1-en" or orient == "I2-en" or orient == "A-en" or orient == "I1-se" or orient == "I2-se" or orient == "A-se" or orient == "A-senao":
                                    print("DEPENDENTE 1")
                                    objectClicked.addConnection( [block, orient], False)
                                    block.addConnection( [objectClicked, orient], True)
                                else:
                                    print("DEPENDENTE 2")
                                    objectClicked.addConnection([block , orient], True)
                                    block.addConnection([objectClicked, orient], False)
                                    
                                self.window.fill(self.cor_branca)
                                objectClicked.setPos(newPos, self.ajusteVisual)
                                
                ##Durante o momento de arrastar o mouse com o objeto selecionado 
                elif event.type == pygame.MOUSEMOTION and textWrite == False:
                    if draging:
                        mouse_x, mouse_y = event.pos
                        objectClicked.setPos((mouse_x + offset_x, mouse_y + offset_y), self.ajusteVisual)

                        ## Gerando a sugestao de conexao
                        dist = 99999
                        distCalc = 999999
                        orient = False
                        block = False
                        newPos = False
                        posCarry = objectClicked.getPos()
                        sizeCarry = objectClicked.getSize()
                        ## Percorre todos os objetos presentes
                        for i in self.objects:
                            connected = False
                            ## Verifica se o objeto eh diferente do conectado
                            if i != objectClicked:
                                posStop = i.getPos()
                                sizeStop = i.getSize()


                                for l in objectClicked.connectedFixed:
                                    ## Se o objeto que esta sendo percorrido ja esta conectado
                                    if i == l[0]:
                                        connected = True
                                        break
                                ## Se ja estiver conectado, ignora esse bloco e parte para o proximo
                                if connected == False:
                                    ##Caso nao esteja conectado ainda
                                    ## Percorre todas as possibilidades que o objeto clicado fornece de encaixe
                                    for j in objectClicked.fit:
                                        ## Percorre todas as possibilidaes de encaixe do objeto que esta sendo percorrido pelo for
                                        for k in i.compatible:
                                            ## Se for compativel (o encaixe com o recebimento)
                                            if j == k:
                                               
                                                ## Verifica se eh do tipo operacao
                                                if i.typeBlock == "operacao" and j == ("I", "macho-normal"):

                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0]-23) + abs(posCarry[1] - posStop[1] - 13))
                                                    bl = i
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-163) + abs(posCarry[1] - posStop[1] - 13) )                                            
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 23, posStop[1] + 13)
                                                        typ = "I1-op"
                                                    else:
                                                        np = (posStop[0] + 163, posStop[1] + 13)
                                                        typ = "I2-op"
                                                        distCalc = distCalc2
                                                elif i.typeBlock == "enquanto" and j == ("I", "macho-normal"):
                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0]-143) + abs(posCarry[1] - posStop[1] - 13))
                                                    bl = i
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-283) + abs(posCarry[1] - posStop[1] - 13))
                                                    
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 143, posStop[1] + 15)
                                                        typ = "I1-en"
                                                    else:
                                                        np = (posStop[0] + 283, posStop[1] + 15)
                                                        typ = "I2-en"
                                                        distCalc = distCalc2
                                                elif i.typeBlock == "enquanto" and j == ("N", "femea-normal"):
                                                    
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 74))
                                                    bl = i
                                                    np = (posStop[0]+ 93, posStop[1] + 74)
                                                    typ = "A-en"

                                                elif i.typeBlock == "se" and j == ("I", "macho-normal"):

                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0] - 58) + abs(posCarry[1] - posStop[1] - 12))
                                                   
                                                    bl = i
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-193) + abs(posCarry[1] - posStop[1] - 12) )

            
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 58, posStop[1] + 12)
                                                        typ = "I1-se"
                                                    else:
                                                        np = (posStop[0] + 193, posStop[1] + 13)
                                                        typ = "I2-se"
                                                        distCalc = distCalc2
                                                
                                                elif i.typeBlock == "se" and j == ("N", "femea-normal"):
                                                    
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 74))
                                                    
                                                    bl = i
                                                    np = (posStop[0]+ 93, posStop[1] + 74)
                                                    typ = "A-se"
                                                    
                                                elif i.typeBlock == "senao" and j == ("N", "femea-normal"):
                        
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 24))
                                                    bl = i
                                                    np = (posStop[0]+ 93, posStop[1] + 24)
                                                    typ = "A-senao"
                                                    
                                                ##Verifica em qual das posicoes ele se encaixa, e calcula assim a distancia ate o encaixe
                                                elif j[0] == "N":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[1])
                                                    typ = "N"
                                                    bl = i
                                                    np = (posStop[0], posStop[1] + sizeStop[1] - self.ajusteVisual)
                                                    
                                                elif j[0] == "S":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeCarry[1])
                                                    typ = "S"
                                                    bl = i
                                                    np = (posStop[0], posStop[1]-sizeCarry[1] + self.ajusteVisual)
                                                  
                                                elif j[0] == "L":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0] ) + abs(posCarry[1] - posStop[1]) - sizeCarry[0])
                                                    typ = "L"
                                                    bl = i
                                                    np = (posStop[0] - sizeCarry[0] + self.ajusteVisual, posStop[1])  
                                                elif j[0] == "O":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[0])
                                                    typ = "O"
                                                    bl = i
                                                    np = (posStop[0] + sizeStop[0] - self.ajusteVisual, posStop[1])

                                                ## Salva os dados se a distancia encontrada for a menor
                                                if distCalc < dist:
                                                    ## Quando os objetos tem o mesmo tamanho, as distancias N e S são iguais. Entao usamos esse ajuste
                                                    ## para saber se a imagem deve se posicionar acima ou abaixo
                                                    if typ == "N" or typ == "S" and orient == "N" or orient == "S":
                                                        distCalcSigned = posCarry[1] - posStop[1]
                                                        if distCalcSigned < 0:
                                                            typ = "S"
                                                            np = (posStop[0], posStop[1]-sizeCarry[1] + self.ajusteVisual)
                                                        else:
                                                            typ = "N"
                                                            np = (posStop[0], posStop[1]+sizeStop[1] - self.ajusteVisual)
                                                            

                                                
                                                    dist = distCalc
                                                    orient = typ
                                                    block = bl
                                                    newPos = np
                                                    
              
                            ## Compara a menor distância encontrada com um limiar (no caso, 10). Se for menor, ira sugerir como opcao para conexao
                            if dist > 20:
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
