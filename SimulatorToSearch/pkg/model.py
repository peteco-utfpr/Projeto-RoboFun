from view import View
from maze import Maze

class Model:
    """Model implementa um ambiente na forma de um labirinto com paredes e com um agente.
     A indexação da posição do agente é feita sempre por um par ordenado (lin, col). Ver classe Labirinto."""

    def __init__(self, rows, columns, mesh, load):
        """Construtor de modelo do ambiente físico (labirinto)
        @param rows: número de linhas do labirinto
        @param columns: número de colunas do labirinto
        @param mesh: define o tipo malha a ser usado
        @param load: define o nome do arquivo que contém o mapa a ser usado
        """
        if rows <= 0:
            rows = 5
        if columns <= 0:
            columns = 5

        self.rows = rows
        self.columns = columns
        self.mesh = mesh

        ## Sera a posicao do agente
        self.agentPos = [0,0]
        ## Seta a posicao do objetivo
        self.goalPos = [0,0]

        ## Cria a view
        self.view = View(self)
        ## Cria o labirinto
        self.maze = Maze(rows,columns, self.mesh, self.view.getScreen(), load)
        ## Seta para o view o labirinto criado
        self.view.setBoard(self.maze.getBoard())

    ## Metodo que desenha tudo no pygame
    def draw(self):
        self.view.draw()

    ## Metodo que desenha o labirinto no pygame
    def drawToBuild(self):
        self.view.drawToBuild()

    ## Metodo que retorna o step do view
    def getStep(self):
        return self.view.getStep()

    ## Metodo que atualiza o labirinto
    def updateMaze(self):
        self.maze.updateWalls()

    ## Metodo que atualiza a posicao do agente
    def setAgentPos(self, row, col):
        """Utilizada para colocar o agente na posição inicial.
        @param row: a linha onde o agente será situado.
        @param col: a coluna onde o agente será situado.
        @return 1 se o posicionamento é possível, -1 se não for."""
        if (col < 0 or row < 0):
            return -1
        if (col >= self.maze.maxColumns or row >= self.maze.maxRows):
            return -1
        
        if self.maze.walls[row][col] == 1:
            return -1

        self.agentPos[0] = row
        self.agentPos[1] = col
        return 1

    ## Metodo que define a posicao do objetivo
    def setGoalPos(self, row, col):
        """Utilizada para colocar o objetivo na posição inicial.
        @param row: a linha onde o objetivo será situado.
        @param col: a coluna onde o objetivo será situado.
        @return 1 se o posicionamento é possível, -1 se não for."""
        if (col < 0 or row < 0):
            return -1
        if (col >= self.maze.maxColumns or row >= self.maze.maxRows):
            return -1
        if self.maze.walls[row][col] == 1:
            return -1

        self.goalPos[0] = row
        self.goalPos[1] = col
        return 1

    ## Metodo que executa a acao de movimento do plano 
    def go(self, action):
        """
            Esse metodo deve ser alterado de acordo com o action a ser passado
        """
        result = action.do()
        step = result[0]
        if step == "N":
            row = self.agentPos[0] - 1
            col = self.agentPos[1]
        elif step == "S":
            row = self.agentPos[0] + 1
            col = self.agentPos[1]
        elif step == "O":
            row = self.agentPos[0]
            col = self.agentPos[1]  - 1
        elif step == "L":
            row = self.agentPos[0]
            col = self.agentPos[1] + 1
        
        self.setAgentPos(row, col)            
            
        return result[1]

    ## Metodo que executa uma acao (de não movimento)
    def do(self, posAction, action = True):
        ## Pega o bloco que deve ser executado a ação, e chama o metodo de execucao dela
        self.maze.board.listPlaces[posAction[0]][posAction[1]].doAction(action)
        return True

        
