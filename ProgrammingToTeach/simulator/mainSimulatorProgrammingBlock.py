import sys
import os
import time

## Importa as classes que serão usadas
sys.path.append(os.path.join("simulator", "pkg"))
from model import Model
from agent import Agent

class MainSimulatorProgrammingBlock:
    def __init__(self, rows = 8, columns = 8, mesh = "square", loadMaze = False):
         # Cria o ambiente (modelo) = Labirinto com suas paredes
        self.mazeRows = rows
        self.mazeColumns = columns
        self.mesh = mesh
        self.loadMaze = loadMaze
        self.model = Model(self.mazeRows, self.mazeColumns, self.mesh, self.loadMaze)
        ##Executa a parte que o usuário clica nos lugares e define o que terá em cada um.
        ## Sai dessa parte quando apertado o ENTER
        self.buildMaze()

        
    ## Metodo utilizado para permitir que o usuario construa o labirindo clicando em cima
    def buildMaze(self):
        self.model.drawToBuild()
        step = self.model.getStep()
        while step == "build":
            self.model.drawToBuild()
            step = self.model.getStep()
        ## Atualiza o labirinto
        self.model.updateMaze()

    
    def execution(self, plan):
        # Define a posição inicial do agente no ambiente - corresponde ao estado inicial
        self.model.setAgentPos(self.model.maze.board.posAgent[0],self.model.maze.board.posAgent[1])
        self.model.setGoalPos(self.model.maze.board.posGoal[0],self.model.maze.board.posGoal[1])        
        self.model.draw()
        # Cria um agente
        self.agent = Agent(self.model)
        self.agent.addPlan(plan)
        print("\n Início do ciclo de raciocínio do agente \n")
        while self.agent.deliberate() != -1:
            self.model.draw()
            time.sleep(0.3)
        self.model.draw()    
        

