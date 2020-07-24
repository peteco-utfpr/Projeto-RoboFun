from view import View
from maze import Maze
from cardinal import *

class Model:
    """Model implementa um ambiente na forma de um labirinto com paredes e com um agente.
     A indexação da posição do agente é feita sempre por um par ordenado (lin, col). Ver classe Labirinto."""

    def __init__(self, rows, columns):
        """Construtor de modelo do ambiente físico (labirinto)
        @param rows: número de linhas do labirinto
        @param columns: número de colunas do labirinto
        """
        if rows <= 0:
            rows = 5
        if columns <= 0:
            columns = 5

        self.rows = rows
        self.columns = columns

        self.agentPos = [0,0]
        self.goalPos = [0,0]

        self.view = View(self)
        self.maze = Maze(rows,columns)

    def draw(self):
        """Desenha o labirinto em formato texto."""
        self.view.draw()

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

    def go(self, action):
        result = action.do()
        position = result[0]
        
        row = position[0]
        col = position[1]
        self.setAgentPos(row, col)
        return result[1]
