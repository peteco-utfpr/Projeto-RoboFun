import sys
import os
import time
sys.path.append('pkg')
from model import Model
from agent import Agent

class MainSimulator:
    def buildMaze(self, model):
        self.model.maze.putVerticalWall(0,1,0)
        self.model.maze.putVerticalWall(0,0,1)
        self.model.maze.putVerticalWall(5,8,1)
        self.model.maze.putVerticalWall(5,5,2)
        self.model.maze.putVerticalWall(8,8,2)

        self.model.maze.putHorizontalWall(4,7,0)
        self.model.maze.putHorizontalWall(7,7,1)
        self.model.maze.putHorizontalWall(3,5,2)
        self.model.maze.putHorizontalWall(3,5,3)
        self.model.maze.putHorizontalWall(7,7,3)

        self.model.maze.putVerticalWall(6,7,4)
        self.model.maze.putVerticalWall(5,6,5)
        self.model.maze.putVerticalWall(5,7,7)

    def main(self):
        # Cria o ambiente (modelo) = Labirinto com suas paredes
        mazeRows = 9
        mazeColumns = 9
        self.model = Model(mazeRows, mazeColumns)
        self.buildMaze(self.model)

        # Define a posição inicial do agente no ambiente - corresponde ao estado inicial
        self.model.setAgentPos(8,0)

        self.model.setGoalPos(2,8)
        # Cria um agente
        self.agent = Agent(self.model)

        self.model.draw()
        print("\n Início do ciclo de raciocínio do agente \n")
        while self.agent.deliberate() != -1:
            print("Pensando!")
            self.model.draw()
            time.sleep(0.3)
        return 1

    def addNewPlan(self, plan):
        self.agent.addPlan(plan)
        self.model.draw()
        print("\n Início do ciclo de raciocínio do agente \n")
        while self.agent.deliberate() != -1:
            print("Pensando!")
            self.model.draw()
            time.sleep(0.3)
        return 1
        

##        
##if __name__ == '__main__':
##    main()
