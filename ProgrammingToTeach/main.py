import pygame, time, math, sys, os
from random import *
from pygame.locals import *
sys.path.append('programming-blocks')
from menu import Menu
import objectUse
import importlib
from mainSimulator import MainSimulator

##Inspiracao
##https://developers.google.com/blockly/


##Variavel utilizada para armazenar o resultado do código gerado na programação
plano = []
class Main:
    def __init__(self):
        pygame.init() 
        ## Define o tamanho da tela total: Programação + simulador
        self.largura = 1300
        self.altura = 550

        ## Define até onde vai a area para a programação
        self.larguraProgramming = 600

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

        ## Define um ajuste para os blocos se encaixarem melhor
        self.ajusteVisual = 12

        ## Cria o simulador
        self.executionSimulator = MainSimulator()
        self.executionSimulator.main()
        

    ## Método utilizado para a interpretação e geração do código feito em blocos
    def generateCode(self):
        ## Ordena os blocos de acordo com a posição em Y e X
        blocosOrdenados = sorted(self.objects, key = objectUse.ObjectUse.getPosInversed)
        ## A interpretação vai ser feita toda dentro de uma string, e depois será convertida para código
        codigoPython = "\ndef generate():"
        codigoPython += "\n  plano = []"

        
        cont = 0
        ##Define a identação atual
        ident = 2
        blockIdent = []
        ##Salva o bloco anterior
        anterior = False
        ##Percorre todos os blocos 
        while cont < len(blocosOrdenados):
            ###### AJUSTE DA IDENTAÇÃO####
            
            ##Verifica se existe um bloco anterior
            if anterior != False:

                noConnection = True
                ## Percorre todos os que estão acoplados no bloco anterior
                for i in anterior.connectedFixed:
                    ## Define se bloco atual está conectado com o anterior
                    if i[0] == blocosOrdenados[cont]:
                        noConnection = False

                ## Verifica se esse bloco está conectado com o anterior 
                if noConnection == True:
                    ##Se entrar, significa que NÃO está conectado

                    ##Portanto, será necessário verificar identação do bloco
                    ##Fazemos isso verificando a distância em X em relação aos outros blocos
                    minimo = 1000000000000
                    aliged = False
                    valueIde = -1
                    valueCont = 0
                    
                    ## Percorrermos a lista de blocos identados
                    for i in blockIdent:
                        ## Calcula a distância, e armazena a menor delas
                        distIdent = abs(i.getPos()[0] - blocosOrdenados[cont].getPos()[0])
                        if distIdent <= (minimo):   
                            minimo = distIdent
                            aliged = i
                            valueIde = valueCont
                        valueCont += 1
                    aux = 0
                    listAux = []
                    ## Atualiza a lista de idents. Deixando apenas aqueles que tem a identação correta com o atual bloco
                    
                    while aux <= valueIde:
                        listAux.append(blockIdent[aux])
                        aux += 1
                    blockIdent = listAux.copy()
                    ident = len(blockIdent) + 2
            ##########FIM DO AJUSTE DE IDENTAÇÃO########################
                    
            ## Nesse momento a identação já está correta
            ## Já seta o anterior como o bloco atual
            anterior = blocosOrdenados[cont]

            ####### VERIFICAÇÃO DOS BLOCOS ######

            ## Verifica se o bloco atual é do tipo SE
            if blocosOrdenados[cont].getType() == "se":
                ##Pega o texto escrito no bloco (que será o operador da condição)
                operador = blocosOrdenados[cont].getText()
                ## Passa para o próximo bloco, que será o primeiro encaixe dele, o valor 1 da condição
                cont += 1
                value1 = blocosOrdenados[cont].getText()
                ## Passa para o outro bloco, que será o segundo encaixe dele, o valor 2 da condição
                cont += 1
                value2 = blocosOrdenados[cont].getText()
                ## Soma tudo na string
                codigoPython += "\n" + ident*" " + "if " + value1 + " " + operador + " " + value2 + ":"
                ## Por se tratar de um Se, existe identação. Então, aumenta um nível de identação
                ident += 1
                ## Adiciona esse bloco na lista de blocos identados
                blockIdent.append(blocosOrdenados[cont-2])

            ## Verifica se o bloco atual é do tipo SENAO    
            elif blocosOrdenados[cont].getType() == "senao":
                ##Adiciona na string
                codigoPython += "\nelse:"
                ## Aumenta um nível a identação
                ident += 1
                blockIdent.append(blocosOrdenados[cont])
                 
            ## Verifica se o bloco é do tipo MOVER 
            elif blocosOrdenados[cont].getType() == "mover":
                cont += 1
                ## Verifica se o proximo bloco (aquele que esta encaixado lateralmente nele) é do tipo OPERACAO 
                if blocosOrdenados[cont].getType() == "operacao":
                    ## Se for do tipo Operação, pega o texto escrito (que vai ser a operação a ser realizada) 
                    ope = blocosOrdenados[cont].getText()
                    ## Pega os dois proximos blocos:
                    cont += 1
                    ## Primeiro bloco encaixado (valor 1)
                    val1 = blocosOrdenados[cont].getText()
                    cont += 1
                    ## Segundo bloco encaixado (valor 2)
                    val2 = blocosOrdenados[cont].getText()

                    ## Soma tudo em uma unica operação
                    value1 = val1 + " " + ope + " " + val2
                else:
                    ## Caso não for uma operação, pega apenas o valor (seja ele constante e variavel)
                    value1 = blocosOrdenados[cont].getText()

                ## Une tudo na string
                codigoPython += "\n" + ident*" " + "cont = 0"
                codigoPython += "\n" + ident*" " + "while cont < " + value1 + ":"
                codigoPython += "\n" + ident*" " + " " + "plano.append('M')"
                codigoPython += "\n" + ident*" " + " " + "cont += 1" 

            ## Verifica se o bloco é do tipo GIRAR Antihorario                
            elif blocosOrdenados[cont].getType() == "girarAnti":
                cont += 1
                ## Verifica se tem uma operação acoplada nele
                if blocosOrdenados[cont].getType() == "operacao":
                    ## Igual anteriormente, pega os valores de operação e dos dois blocos de dentro dele
                    ope = blocosOrdenados[cont].getText()
                    cont += 1
                    val1 = blocosOrdenados[cont].getText()
                    cont += 1
                    val2 = blocosOrdenados[cont].getText()
                    ## Une em uma string
                    value1 = val1 + " " + ope + " " + val2
                else:
                    ## Senão for uma operação, apenas pega o valor
                    value1 = blocosOrdenados[cont].getText()

                ## Une tudo na string de código
                codigoPython += "\n" + ident*" " + "cont = 0"
                codigoPython += "\n" + ident*" " + "while cont < " + value1 + ":"
                codigoPython += "\n" + ident*" " + " " + "plano.append('GA')"
                codigoPython += "\n" + ident*" " + " " + "cont += 1" 

            ## Igual anterior, mas agora verifica se o bloco é GIRAR Horario    
            elif blocosOrdenados[cont].getType() == "girarHor":
                cont += 1
                ## Verifica se está acoplado a uma operação
                if blocosOrdenados[cont].getType() == "operacao":
                    ## Pega a operação e os dois valores
                    ope = blocosOrdenados[cont].getText()
                    cont += 1
                    val1 = blocosOrdenados[cont].getText()
                    cont += 1
                    val2 = blocosOrdenados[cont].getText()
                    ## Une em uma string
                    value1 = val1 + " " + ope + " " + val2
                else:
                    ## Se não for uma operação, apenas pega o valor
                    value1 = blocosOrdenados[cont].getText()

                ## Une tudo na string de código     
                codigoPython += "\n" + ident*" " + "cont = 0"
                codigoPython += "\n" + ident*" " + "while cont < " + value1 + ":"
                codigoPython += "\n" + ident*" " + " " + "plano.append('GH')"
                codigoPython += "\n" + ident*" " + " " + "cont += 1" 

            ## Verifica se o bloco é um ENQUANTO
            elif blocosOrdenados[cont].getType() == "enquanto":
                ## Pega o texto do bloco (que é o operador) 
                operador = blocosOrdenados[cont].getText()
                ## Pega os dois valores dos que estão dentro do enquanto
                cont += 1
                value1 = blocosOrdenados[cont].getText()
                cont += 1
                value2 = blocosOrdenados[cont].getText()
                ## Une na string de código 
                codigoPython += "\n" + ident*" " +"while " + value1 + " " + operador + " " + value2 + ":"
                ## Aumenta um nível de identação
                ident += 1
                blockIdent.append(blocosOrdenados[cont-2])

            ## Verifica se o bloco é do tipo CRIAR VARIAVEL
            elif blocosOrdenados[cont].getType() == "criarVariavel":
                ## Pega o valor do bloco que está conectado a ele
                cont += 1
                value1 = blocosOrdenados[cont].getText()
                ## Adiciona na string de código
                codigoPython += "\n" + ident*" " + value1 + " = 0" 

            ## Verifica se o bloco é do tipo SETAR VARIAVEL
            elif blocosOrdenados[cont].getType() == "setarVariavel":
                ## Pega o valor do bloco (que será o nome da variavel)     
                variavel = blocosOrdenados[cont].getText()
                cont += 1
                ## Verifica se o bloco acoplado é uma operacao
                if blocosOrdenados[cont].getType() == "operacao":
                    ## Se for, pega o valor do texto (operação) e os dois valores (que são os proximos dois blocos)
                    ope = blocosOrdenados[cont].getText()
                    cont += 1
                    val1 = blocosOrdenados[cont].getText()
                    cont += 1
                    val2 = blocosOrdenados[cont].getText()
                    ## Adiciona tudo em uma string
                    value1 = val1 + " " + ope + " " + val2
                else:
                    ## Caso não for uma operação, apenas pega o valor 
                    value1 = blocosOrdenados[cont].getText()
                ## Adiciona tudo na string de código
                codigoPython += "\n" + ident*" " + variavel + " = " + value1
                
            cont += 1

        ## Encerra o método criado, e faz a chamada da função
        codigoPython += "\n  return plano"
        codigoPython += "\nplano=generate()"
         
        ## Salva o código em um arquivo .py 
        arquivo = open("codeBlock.py", "w")
        arquivo.write(codigoPython)
        arquivo.close()


        arquivo2 = open(os.path.join("API-Connection", "codeBlockCompRobot.py"), "w")
        arquivo2.write(codigoPython)
        arquivo2.close()

        ## Faz a execução do código da string através da função exec()
        ## Passa o parametro global para as variaveis que ele usar no exec, serem do tipo globais
        ## O plano resultante saira na variavel: plano
        exec(codigoPython, globals())

        ## Passa o plano resultante para o simulador
        self.executionSimulator.addNewPlan(plano)
         

    ##Metodo usado para a execucao do programa
    def run(self):
        ##Variavel usada para verificar se um bloco esta sendo carregado
        draging = False
      
        
        ## Variaveis para o controle da sugestão de encaixe
        ## Distancia do encaixe
        dist = 99999
        ## Orientacao do encaixe (N, S, O....)
        orient = False
        ## Bloco parada que será encaixado
        block = False
        ## Nova posição do bloco ao ser solto (ajustado com o encaixe)
        newPos = False

        ##Variavel para o controle do loop de execução
        stop = False


       
        ## Loop de execução
        while not stop:

            ## Variavel que controla se um novo bloco foi gerado. Serve para evitar realizar algumas comparacoes mais adiante
            newBlockCreated = False


            ## Váriavel que define se é necessário redesenhar os blocos da programação
            reDraw = False
          
            ##Faz a animacao se caso o mouse estiver emcima de algum botao
            self.menu.mouseOn(self.tela, pygame.mouse.get_pos())

            ## Em caso de algum evento ocorrer
            for event in pygame.event.get():
            
                ##Verifica se foi clicado no menu, e se um bloco foi clicado para ser adicionado a tela de programacao
                if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.get_pressed()[0] != 0:
                    ## buttonClicked indica qual bloco foi clicado (do menu)
                    ## newObject retorna um novo objeto (se caso o usuário clicou no objeto para criar um novo)
                    buttonClicked, newObject = self.menu.mouseClick(self.tela, pygame.mouse.get_pos())

                    ##Se foi clicado, apaga o menu lateral que abriu
                    if buttonClicked == False:
                        reDraw = True
                        ## Desenha apenas um retangulo branco para evitar apagar apenas a parte da programação, e não do simulador
                        pygame.draw.rect(self.tela, self.cor_branca, [0, 0, self.larguraProgramming,self.altura])
                        
                    ## Verifica se foi clicado no botão de Compilar. Se caso sim, chama o método para gerar o código
                    if  newObject == "Generate Code":
                        self.generateCode()
                        reDraw = True
                        ## Para o loop de eventos, pois nesse momento, o foco está na execução do que foi programado e sendo executado no simulador
                        break

                    ##Se foi criado um novo bloco, adiciona ele na lista de blocos
                    elif newObject != False:
                        reDraw = True
                        
                        self.objects.append(newObject)
                        ## Ordena os objetos de acordo com a area ocupadas por eles, deixando os que tem menores areas na frente
                        ## Faz isso para facilitar a visualização, e nenhum bloco menor ficar escondido atras de outro maior
                        self.objects.sort(key = objectUse.ObjectUse.getArea)
                        newBlockCreated = True

                        ## Tira a seleção de algum bloco, se ele estiver selecionado
                        if objectClicked != False:
                            objectClicked.mouseClick((0,0))
                            objectClicked = False

                ##--------------------------------------------------------------------------------------------##
                ######## REMOÇÃO DE BLOCOS  #####      
                ## Verifica se alguma tecla foi apertada
                if event.type == pygame.KEYDOWN:
                    ## Se a tecla for o DELETE e haver algum objeto selecionado
                    if event.key == K_DELETE and objectClicked != False:
                        ## Retira da da lista de objetos o bloco selecionado 
                        self.objects.remove(objectClicked)
                        ## Desenha o retangulo branco para apagar todos os blocos
                        pygame.draw.rect(self.tela, self.cor_branca, [0, 0, self.larguraProgramming,self.altura])
                        ## Faz a remoção dos blocos que estão ligados a ele
                        for i in self.objects:
                            ## Remove a conexão com todos os blocos conectados de maneira Fixed
                            ## Percorre a lista de conexões fixas
                            for j in i.connectedFixed:
                                ## Remove a conexão fixed com o bloco deletado
                                if j[0] == objectClicked:
                                    i.connectedFixed.remove(j)
                                    break
                            ## Remoce a conexão Dinamic com todos os blocos que a tiverem
                            for j in i.connectedDinamic:
                                ## Remove a conexão
                                if j[0] == objectClicked:
                                    i.connectedDinamic.remove(j)
                        ## Define que não há nenhum objeto selecionado
                        objectClicked = False
                        ## Seta a variavel para redesenhar os blocos na tela como True
                        reDraw = True
                ###### FIM DA REMOÇÃO DE BLOCOS #######

                ##--------------------------------------------------------------------------------------------##

                ##### ESCRITA DENTRO DOS BLOCOS #####
                ## Percorre todos os blocos
                for i in self.objects:
                    ## E passa o evento para ele, para verificar se alguma ação de escrita ou seleção da caixa de texto foi feita
                    ## Se for feita alguma alteração, o retorno é True. E então seta a variavel para desenhar os blocos como True tbm
                    texti = i.textEnter(event)
                    if texti == True:
                        reDraw = True 
                #### FIM DA ESCRITA DOS BLOCOS ######

                ##--------------------------------------------------------------------------------------------##

                #### DRAG AND DROP DOS BLOCOS #####        
                ####Funcionamento do Drag and Drop dos blocos adicionados
                    
                ## Verifica o momento em que o usuário apertou o botão do mouse (MOUSEBUTTONDOWN) e se não foi seleciona uma caixa de texto
                if event.type == pygame.MOUSEBUTTONDOWN and newBlockCreated == False:
                    ## Verifica se o botão da direita foi clicado
                    if event.button == 1:
                        ## Variavel que irá armazenar o bloco selecionado
                        objectClicked = False
                        ## Percorre os objetos e verifica se o objeto foi clicado
                        aux = False
                        for i in self.objects:
                            if objectClicked == False:
                                aux = i.mouseClick(pygame.mouse.get_pos())
                            ## Se caso foi clicado, o objeto se encontra em aux
                            ## Irá salvar o primeiro bloco que encontrar (dando preferencia aos que aparecem na frente) em caso de blocos um sobre o outro
                                objectClicked = aux
                            else:
                                break
                        ##Salva os dados da posicao do objeto, para o calculo do desvio do clique do mouse em relacao ao canto esquerdo dele
                        if objectClicked != False:
                            ## Define que um objeto está em processo de Drag and drop
                            draging = True
                            mouse_x, mouse_y = event.pos
                            posOb = objectClicked.getPos()
                            offset_x = posOb[0] - mouse_x
                            offset_y = posOb[1] - mouse_y

                ##Verifica se o botao do mouse parou de ser clicado
                elif event.type == pygame.MOUSEBUTTONUP and newBlockCreated == False:
                        ## Verifica se é o botão da direita que deixou de de ser apertado
                        if event.button == 1:
                            ## Define que nenhum bloco está em processo de drag and drop
                            draging = False
                            ## Desativa todas as conexões que tinham esse bloco como fixed
                            if objectClicked != False:
                                ## Para o objeto que estava sendo carregado, a conexão é do tipo Dinamic. Para o outro bloco, é do tipo fixed
                                for i in objectClicked.connectedDinamic:
                                    for j in i[0].connectedFixed:
                                        if j[0] == objectClicked:
                                            i[0].connectedFixed.remove(j)
                                            break

                                ## Limpa a lista de conexões dinamic
                                objectClicked.connectedDinamic = []
                                ## Define para desenhar os blocos novamente
                                reDraw = True
                                                  
                          
                                
                            ## Verifica se existe algum encaixe sugerido disponível
                            if dist != 99999 and newPos != False and objectClicked != False:
                               
                                ##Verifica se o que esta sendo movido eh dependente do outro
                                ## Os tipos dependentes são: N (norte), O (oeste), I1-op, I2-op (interno 1 e 2 da opereção)
                                ## I1-en, I2-en (interno 1 e 2 do enquanto), A-en (aninhado ao enquanto), I1-se, I2-se (interno 1 e 2 do se)
                                ## A-se (aninhado ao se), A-senao (aninhado ao senão)

                                ## Verifica se não um bloco não está se conectando com ele mesmo
                                enableConnect = True
                                if block == objectClicked:
                                    enableConnect = False
                                
                                if enableConnect:
                                    if orient == "N" or orient == "O" or orient == "I1-op" or orient == "I2-op" or orient == "I1-en" or orient == "I2-en" or orient == "A-en" or orient == "I1-se" or orient == "I2-se" or orient == "A-se" or orient == "A-senao":
                                        ## Se for dependende, adiciona como sendo uma conexão dinamic para o objeto clicado
                                        ## E uma conexão fixed para o objeto que recebe o encaixe
                                        objectClicked.addConnection([block, orient], False)
                                        block.addConnection( [objectClicked, orient], True)

                                        ## Seta a posição do objeto atual para ser a definida pelo do encaixe
                                        ## O ajuste visual é passado como parametro visando encaixar melhor os blocos visualmente (por causa do encaixezinho como peça de quebra-cabeça)
                                        objectClicked.setPos(newPos, self.ajusteVisual)
                                        objectClicked.mouseClick((0,0))
                                        
                                        dist = 99999
                                        newPos = False
                                    else:
                                        ## Faz ao contrário da parte acima:
                                        ## Adiciona como sendo fixed para o bloco clicado
                                        ## E dinamic para o outro bloco
                                        objectClicked.addConnection([block , orient], True)
                                        block.addConnection([objectClicked, orient], False)

                                        ## Seta a posição do objeto atual para ser a definida pelo do encaixe
                                        ## O ajuste visual é passado como parametro visando encaixar melhor os blocos visualmente (por causa do encaixezinho como peça de quebra-cabeça)
                                        objectClicked.setPos(newPos, self.ajusteVisual)
                                        objectClicked.mouseClick((0,0))
                                       
                                        dist = 99999
                                        newPos = False
                                   
                                    ## Apaga todos os blocos (limpa a tela)
                                pygame.draw.rect(self.tela, self.cor_branca, [0, 0, self.larguraProgramming,self.altura])
                                   
                            
                ##Durante o momento de arrastar o mouse com o objeto selecionado
                ## Verifica se o mouse está se movendo
                elif event.type == pygame.MOUSEMOTION and newBlockCreated == False:
                    ## Verifica se está carregando algum objeto
                    if draging:
                        ## Se estiver, verifica se o objeto não passa dos limites da borda da tela
                        reDraw = True
                        mouse_x, mouse_y = event.pos
                        size = objectClicked.getSize()
                        ## Faz a verificação dos limites laterais e superior da area de programação
                        if not ((mouse_x + size[0] + offset_x) >= self.larguraProgramming or (mouse_x + offset_x) < 100 or mouse_y + offset_y < 0):
                            objectClicked.setPos((mouse_x + offset_x, mouse_y + offset_y), self.ajusteVisual)
                        
                        ##### GERANDO A SUGESTÃO DE ENCAIXE ####
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
                            
                            ## Verifica se o objeto é diferente do conectado
                            if i != objectClicked:
                                posStop = i.getPos()
                                sizeStop = i.getSize()

                                for l in objectClicked.connectedFixed:
                                    ## Verifica se o objeto que esta sendo percorrido ja esta conectado com o objeto que está sendo carregado
                                    if i == l[0]:
                                        ## Se ja estiver conectado, ignora esse bloco e parte para o proximo
                                        connected = True
                                        break
                                    
                                ##Caso nao esteja conectado ainda
                                if connected == False:
                                   
                                    ## Percorre todas as possibilidades que o objeto clicado fornece de encaixe
                                    for j in objectClicked.fit:
                                        ## Percorre todas as possibilidaes de encaixe do objeto que esta sendo percorrido pelo for
                                        for k in i.compatible:
                                            ## Se for compativel (o encaixe com o recebimento)
                                            if j == k:
                                                ## Devido as diversas formas de conexão, será necessário verificar cada tipo de bloco e de encaixe
                                                ## Isso se da pelo fato dos blocos terem tamanhos diferentes, e ser necessário um ajuste visual para
                                                ## cada tipo de objeto
                                                
                                                ## Verifica se o bloco parado é do tipo operacao
                                                ## E se o tipo de conexão disponível é INTERNO (I) e do tipo macho-normal 
                                                if i.typeBlock == "operacao" and j == ("I", "macho-normal"):
                                                    ## Calcula a distância do primeiro encaixe
                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0]-23) + abs(posCarry[1] - posStop[1] - 13))
                                                    ## Calcula a distância do segundo encaixe
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-163) + abs(posCarry[1] - posStop[1] - 13))
                                                    ## Salva o bloco
                                                    bl = i
                                                    ## Verifica qual das duas distâncias é menor, e armazena ela, e seta a possível nova posição do bloco de acordo
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 23, posStop[1] + 13)
                                                        typ = "I1-op"
                                                    else:
                                                        np = (posStop[0] + 163, posStop[1] + 13)
                                                        typ = "I2-op"
                                                        distCalc = distCalc2

                                                ## Verifica se o bloco parado é um Enquanto
                                                ## E se conexão disponível em Interno (I), macho-normal
                                                elif i.typeBlock == "enquanto" and j == ("I", "macho-normal"):
                                                    ## Calcula a distâncias para os dois encaixes disponíveis
                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0]-143) + abs(posCarry[1] - posStop[1] - 13))
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-283) + abs(posCarry[1] - posStop[1] - 13))
                                                    ## Salva o bloco
                                                    bl = i
                                                    ## Selecina a que apresentar a menor distâncias, e seta a possível nova posição do bloco de acordo 
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 143, posStop[1] + 15)
                                                        typ = "I1-en"
                                                    else:
                                                        np = (posStop[0] + 283, posStop[1] + 15)
                                                        typ = "I2-en"
                                                        distCalc = distCalc2


                                                ## Verifica se o bloco é do tipo enquanto
                                                ## e se a conexão é do tipo N (norte) e femea-normal
                                                ## Essa conexão indica que o bloco estara aninhado com o enquanto
                                                elif i.typeBlock == "enquanto" and j == ("N", "femea-normal"):
                                                    ## Calcula a distancia 
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 74))
                                                    ## Salva o bloco
                                                    bl = i
                                                    ## Seta a possível nova posição
                                                    np = (posStop[0]+ 93, posStop[1] + 74)
                                                    ## Define o tipo de encaixe
                                                    typ = "A-en"

                                                ## Verifica se o bloco é do tipo SE
                                                ## E se aconexão é interna (I) e macho normal
                                                elif i.typeBlock == "se" and j == ("I", "macho-normal"):
                                                    ## Calcula as duas distâncias (interno 1 e inter 2) 
                                                    distCalc1 = abs(abs(posCarry[0] - posStop[0] - 58) + abs(posCarry[1] - posStop[1] - 12))
                                                    distCalc2 = abs(abs(posCarry[0] - posStop[0]-193) + abs(posCarry[1] - posStop[1] - 12) )
                                                    ## Salva o bloco
                                                    bl = i
                                                    ## Verifica qual tem a menor distância e seta a possível nova posição do bloco de acordo
                                                    if distCalc1 < distCalc2:
                                                        distCalc = distCalc1
                                                        np = (posStop[0] + 58, posStop[1] + 12)
                                                        typ = "I1-se"
                                                    else:
                                                        np = (posStop[0] + 193, posStop[1] + 13)
                                                        typ = "I2-se"
                                                        distCalc = distCalc2

                                                ## Vefica se é bloco do tipo SE
                                                ## E se a conexão é N (norte) e femea-normal
                                                ## Essa conexão indica que o bloco estara aninhado com o se
                                                elif i.typeBlock == "se" and j == ("N", "femea-normal"):
                                                    ## Calcula a distância, salva o bloco, seta a nova posição... Igual os demais acima
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 74))
                                                    bl = i
                                                    np = (posStop[0]+ 93, posStop[1] + 74)
                                                    typ = "A-se"


                                                ## Vefica se é bloco do tipo senao
                                                ## E se a conexão é N (norte) e femea-normal
                                                ## Essa conexão indica que o bloco estara aninhado com o senao
                                                elif i.typeBlock == "senao" and j == ("N", "femea-normal"):
                                                    ## Calcula a distância, salva o bloco, seta a nova posição... Igual os demais acima
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]-91) + abs(posCarry[1] - posStop[1] - 24))
                                                    bl = i
                                                    np = (posStop[0]+ 93, posStop[1] + 24)
                                                    typ = "A-senao"

                                                ## Se não for nenhuma das conexões especiais definidas acima, verifica agora de maneira mais geral
                                                ## para as conexões iguais a todos
                                                    
                                                ##Verifica em qual das posicoes ele se encaixa, e calcula assim a distancia ate o encaixe
                                                ## O processo é o mesmo para todos encaixes, variando apenas a maneira como é calculado a distância
                                                ## e a posição para o encaixe

                                                ## Verifica uma conexão N (norte)
                                                elif j[0] == "N":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[1])
                                                    typ = "N"
                                                    bl = i
                                                    np = (posStop[0], posStop[1] + sizeStop[1] - self.ajusteVisual)
                                                ## Verifica uma conexão S (sul)
                                                elif j[0] == "S":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeCarry[1])
                                                    typ = "S"
                                                    bl = i
                                                    np = (posStop[0], posStop[1]-sizeCarry[1] + self.ajusteVisual)
                                                ## Verifica uma conexão L (leste)
                                                elif j[0] == "L":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0] ) + abs(posCarry[1] - posStop[1]) - sizeCarry[0])
                                                    typ = "L"
                                                    bl = i
                                                    np = (posStop[0] - sizeCarry[0] + self.ajusteVisual, posStop[1])  
                                                ## Verifica uma conexão O (oeste)
                                                elif j[0] == "O":
                                                    distCalc = abs(abs(posCarry[0] - posStop[0]) + abs(posCarry[1] - posStop[1]) - sizeStop[0])
                                                    typ = "O"
                                                    bl = i
                                                    np = (posStop[0] + sizeStop[0] - self.ajusteVisual, posStop[1])

                                                ## Salva os dados se a distancia encontrada for a menor de todas
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
                                                            

                                                    ## Salva os dados
                                                    dist = distCalc
                                                    orient = typ
                                                    block = bl
                                                    newPos = np
                                                    
              
 
                            ## Verifica se já não há alguma outra conexão naquele lugar. Caso sim, então cancela a sugestão
                            otherConnect = False
                            for i in self.objects:
                                if i != objectClicked and newPos == i.getPos():
                                    otherConnect = True
                                    break

                            ## Compara a menor distância encontrada com um limiar (no caso, 20). Se for menor, ira sugerir como opcao para conexao
                            ## E verifica se aquele bloco já não está conectado a outro
                            if dist > 20 or len(objectClicked.connectedDinamic) > 0 or otherConnect == True:
                                ## Se for superior a esse valor, reseta os valores encontrados e não tem nenhuma sugestão
                                dist = 99999
                                orient = False
                                block = False
                                newPos = False
                            else:
                                ## Se tiver uma sugestão, desenha o bloco cinza na possível nova posição
                                objectClicked.drawSuggestion(newPos, self.tela)
                                
                ##Desenha o retangulo cinza que contem o menu lateral
                pygame.draw.rect(self.tela, (192,192,192), [0, 0, 100, self.altura])
                ##Mostra os botoes do menu
                self.menu.show(self.tela)

                ## Verifica se é para desenhar todos os blocos na tela (novamente)
                if reDraw == True:
                    cont = len(self.objects) - 1
                    while cont >= 0:
                        self.objects[cont].show(self.tela)
                        cont -= 1
                        
                ## Atualiza a tela 
                pygame.display.flip()
                pygame.display.update()
                
                ## Verifica se o usuario clicou no X vermelho para fechar
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    stop = True

## Realiza a instanciação da classe                                   
main = Main()
## Executa
main.run()

