import square
## Classe que define o Mesh de quadrados
class MapSquare:
    def __init__(self, width, heigth, sideSquare, screen, posBegin = (0,0)):
        """
        @param width: Largura que a malha vai ter
        @param heigth: Altura que a malha vai ter
        @param sideSquare: Lado de cada quadrado
        @param screen: Screen do Pygame
        @param posBegin: Posicao de inicio
        """
        
        self.width = width
        self.heigth = heigth
        self.screen = screen
        self.sideSquare = sideSquare
        self.posBegin = posBegin

        ## Lista de quadrados
        self.listPlaces = []
        ## Variavel que armeza qual quadrado foi selecionado
        self.selectPlace = False

        ## Posicao do agente e do objetivo
        self.posAgent = (0,0)
        self.posGoal = (1,1)
        
        ## Chama o metodo para gerar a malha
        self.generateMap()

    ## Metodo que gera a malha de triangulos
    def generateMap(self):
        yr = 0
        y = self.posBegin[1]
        ## Percorre as linhas
        while y < self.heigth + self.posBegin[1]:
            x = self.posBegin[0]
            xr = 0
            line = []
            ## Percorre as colunas
            while x < self.width  + self.posBegin[0]:
                line.append(square.Square((x, y), self.sideSquare, self.screen, (yr, xr)))
                x += self.sideSquare
                xr += 1
            yr += 1
            y += self.sideSquare
            self.listPlaces.append(line)

    ## Metodo que verifica o clique do mouse
    def checkClick(self, posMouse):
        ## Se já tiver selecionado um quadrado antes
        if self.selectPlace != False:
            obj = self.selectPlace.checkClickItens(posMouse)
            if obj != False:
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
