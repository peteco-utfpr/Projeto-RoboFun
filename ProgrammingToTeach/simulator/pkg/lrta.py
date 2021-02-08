from random import randint
from state import State

class Lrta:
    def __init__(self, maxRows, maxColumns, goal, initialState, name = "none", mesh = "square"):
        """
        Define as variaveis necessárias para a utilização do LRTA* por um unico agente.
        """
        self.matrix = [[0 for j in range(maxColumns)] for i in range(maxRows)] # Matriz que representa a heurística do labirinto
        self.goalPos = goal
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.initialState = initialState
        self.currentState = initialState
        self.name = name
        self.mesh = mesh

    def startManhattanHeuristic(self, walls):
        """
        Método utilizado para a inicialização da heurística
        Nesse método, a heurística inicial utilizada é a distância Manhattan
        O método percorre toda a matriz, e aplica a heurística em cada uma das posições

        A heurística de cada posição (Xi, Yi) é igual a: |Xi - Xo| + |Yi - Yo|, onde (Xo, Yo) é o estado objetivo
        """
        row = 0
        col = 0
        for i in walls:
            col = 0
            for j in i:
                if j == 1:
                    self.matrix[row][col] = 9999
                else:
                    self.matrix[row][col] = abs(self.goalPos.row - row) + abs(self.goalPos.col - col)
                col += 1
            row += 1

       
    def updateCurrentState(self, state):
         self.currentState = state
        

    def move(self):
        """
        Método utilizado para a realização de um movimento pelo agente

        Esse método pega as posições adjacentes (cima, baixo, direita e esquerda) da posição atual do agente
        Após, seleciona a que tem o menor valor de heurística na matriz (em caso de empate, a escolha é aleatória entre as menores)
        Após isso, atualiza o valor da heurística na posição atual como sendo o valor da heurística na posição selecionada anteriormente + o custo da ação (1)
        Ao final, define essa como sendo o seu próximo movimento
        """
        cRow = self.currentState.row
        cCol = self.currentState.col
        heuristic = [10000, 10000, 10000, 10000]
        direction = [0,0,0,0]


        if self.goalPos == self.currentState:
            print ("Já está na posição objetivo------------------------------------------------!")
            return [cRow, cCol]
        ###--Seleciona o valor das heuristicas das posições adjacentes--###
        """
            Caso não haja uma posição adjacente, isto e, o agente esta na borda do grid
            o valor da heurística é considerado muito alto (já inicializado na lista heuristic)
            e a posição receve o valor False
        """


        doGo = True
        upGo = True

        if self.mesh == "triangle":
                  
            posAdd = self.currentState.row + self.currentState.col
            if posAdd % 2 == 0:
                upGo = False
            else:
                doGo = False


        if  cRow > 0 and upGo == True:
            up = [cRow - 1, cCol]
            heuristic[0] = self.matrix[cRow - 1][cCol]
        else:
            up = False
        direction[0] = up
        
        if  cRow < self.maxRows-1 and doGo == True:
            down = [cRow + 1, cCol]
            heuristic[1] = self.matrix[cRow + 1][cCol]
        else:
            down = False
        direction[1] = down
                
        if  cCol > 0:
            left = [cRow, cCol - 1]
            heuristic[2] = self.matrix[cRow][cCol - 1]
        else:
            left = False
        direction[2] = left

        if  cCol < self.maxColumns-1:
            right = [cRow, cCol + 1]
            heuristic[3] = self.matrix[cRow][cCol + 1]
        else:
            right = False
        direction[3] = right
        ######------------------------#####

        ###--Seleciona a posição com menor valor de heuristica--###
        minValue = []
        minPos = []
        minor = 9998
        cont = 0
        for i in heuristic:
            
            if i < minor:
                minValue = [i]
                minPos = [cont]
                minor = i
            elif i == minor:
                minValue.append(i)
                minPos.append(cont)
            cont += 1

        print("VALOR MENOR:", minValue)
        ###--Faz a escolha aleatoria--##
        if len(minValue) > 1:
            choice = randint(0,len(minValue) - 1)
        else:
            choice = 0
        ######------------------------#####
      
        
        nextPosition = direction[minPos[choice]]
        ######------------------------#####

        ##--Atualiza o valor da heurística da posição atual--##
        self.matrix[cRow][cCol] = minValue[choice] + 1



        arquivo = open("Matriz-" + self.name + ".txt", "w")
        for i in self.matrix:
            arquivo.write(str(i))
            arquivo.write("\n")
        arquivo.write("-------------------------------------------------------------")
        arquivo.close()

        xComp = self.currentState.row - nextPosition[0]
        yComp = self.currentState.col - nextPosition[1]
        print(xComp)
        print(yComp)
        mov = False
        if xComp == -1 and yComp == 0:
            mov = "S"
        elif xComp == 1 and yComp == 0:
            mov = "N"
        elif xComp == 0 and yComp == 1:
            mov = "O"
        elif xComp == 0 and yComp == -1:
            mov = "L"
        print("MOVIMENTOOOOOOO: ", mov)
        

        
        return nextPosition, mov


    def do(self):
        """
        Método utilizado para o polimorfismo dos planos

        Retorna o movimento e o estado do plano (False = nao concluido, True = Concluido)
        """
        nextMove = self.move()
        return (nextMove[1], self.goalPos == State(nextMove[0][0], nextMove[0][1]))   
            
     
        

        
       
        
        
