import triangle
import math

## Método que cria a malha de triangulos
class MapTriangle:
    def __init__(self, qtdWidth, qtdHeigth, side, angle, screen, posBegin = (50,50)):
        """
        @param qtdWidth: qtd de triangulos em cada linha
        @param qtdHeigth: qtd de linhas (1 triangulo por linha
        @param side: Tamanho dos dois lados iguais do triangulo isóceles
        @param angle: Angulo de abertura dos dois lados iguais
        @param screen: Screen do Pygame
        @param posBegin: Posicao inicial
        """
        
        self.qtdWidth = qtdWidth
        self.qtdHeigth = qtdHeigth
        self.screen = screen
        self.side = side
        self.angle = angle
        self.posBegin = posBegin
        ## Calcula a altura dos triangulos
        self.heightTriangle = side*math.cos(angle)
        ## Calcula a base dos triangulos
        self.baseTriangle = math.sqrt(side**2 - (self.heightTriangle**2))

        ## Variavel que armazena o triangulo que foi clicado
        self.selectPlace = False
        ## Lista de todos os triangulos
        self.listPlaces = []

        ## Posicao do agente e do objetivo
        self.posAgent = (0,0)
        self.posGoal = (1,1)
        ## Chama o metodo para gerar a malha de triangulos
        self.generateMap()

    ## Metodo para gerar a malha de triangulos
    def generateMap(self):
        y = self.posBegin[1]
        control = True
        posYCorrect = y
        contY = 0
        ## Percorre as linhas
        while contY < self.qtdHeigth:
            x = self.posBegin[0]
            contX = 0
            line = []
            ## Fica invertendo entre os dois tipos de triangulos (para cima e para baixo)
            if control == True:
                line.append(triangle.Triangle((x, y), self.side, self.angle, 0, self.screen, (contY, contX)))
                first = 1
                second = 0
                
            else:
                line.append(triangle.Triangle((x, y), self.side, self.angle, 1, self.screen, (contY, contX)))
                first = 0
                second = 1
                
            posYCorrect = line[-1].getP2()[1]
            x += self.baseTriangle
            contX = 1
            ## Percorre as colunas
            while contX < self.qtdWidth:
                """
                OBS: Como os triangulos tem seus lados com números não inteiros, se colocar pela posição sozinha, vai acabar ficando torto a linha.
                Por isso colocamos o próximo triangulo de acordo com o eixo X do anterior, para todos ficarem alinhados
                """
                line.append(triangle.Triangle((line[-1].getP2()[0], posYCorrect), self.side, self.angle, first, self.screen, (contY, contX)))
                contX += 1
                if contX >= self.qtdWidth:
                    break
                line.append(triangle.Triangle((line[-1].getP2()[0], y), self.side, self.angle, second, self.screen, (contY, contX)))
                x += (2*self.baseTriangle)
                contX += 1
            self.listPlaces.append(line)
            ## Soma a base a cada dois triangulos
            if control == True:    
                y += 2*self.heightTriangle
            ## Inverte o tipo do triangulo que começa a linha
            control = not control
            contY += 1

    
    ## Metodo que verifica o clique do mouse
    def checkClick(self, posMouse):
        ## Se já tiver selecionado um quadrado antes
        if self.selectPlace != False:
            obj = self.selectPlace.checkClickItens(posMouse)
            if obj != False:
                print(obj)
                if obj.itemInside == "Robô":                   
                    self.listPlaces[self.posAgent[0]][self.posAgent[1]].agent = False
                    self.posAgent = obj.ide
                    obj.agent = True
                elif obj.itemInside == "Objetivo":
                    
                    self.listPlaces[self.posGoal[0]][self.posGoal[1]].goal = False
                    self.posGoal = obj.ide
                    obj.goal = True
                obj.itemInside = False
            self.selectPlace = False
            return True  
        else:
            ## Se não, verifica os quadrados e ve se algum deles foi clicado
            for i in self.listPlaces:
                for j in i:
                    if self.selectPlace != False:
                        break
                    ## Se sim, seta ele para a variavel
                    self.selectPlace = j.checkClick(posMouse)
            return False

    ## Metodo que mostra os quadrados na tela
    def show(self):
        for i in self.listPlaces:
            for j in i:
                j.show()

    ## Metodo que retorna a lista de quadrados
    def getListPlaces(self):
        return self.listPlaces
