import sys
import os
import time

## Importa as classes que serão usadas
sys.path.append('pkg')
from model import Model
from agent import Agent


## Metodo utilizado para permitir que o usuario construa o labirindo clicando em cima
def buildMaze(model):
    model.drawToBuild()
    step = model.getStep()
    while step == "build":
        model.drawToBuild()
        step = model.getStep()
    ## Atualiza o labirinto
    model.updateMaze()

def main():
    # Cria o ambiente (modelo) = Labirinto com suas paredes
    mazeRows = 8
    mazeColumns = 8
    mesh = "triangle"
    model = Model(mazeRows, mazeColumns, mesh)
    ##Executa a parte que o usuário clica nos lugares e define o que terá em cada um.
    ## Sai dessa parte quando apertado o ENTER
    buildMaze(model)

    model.maze.board.posAgent
    model.maze.board.posGoal
    # Define a posição inicial do agente no ambiente - corresponde ao estado inicial
    model.setAgentPos(model.maze.board.posAgent[0],model.maze.board.posAgent[1])
    model.setGoalPos(model.maze.board.posGoal[0],model.maze.board.posGoal[1])

    
    model.draw()
    # Cria um agente
    agent = Agent(model)

    print("\n Início do ciclo de raciocínio do agente \n")
    while agent.deliberate() != -1:
        model.draw()
        time.sleep(0.3)
    model.draw()    
        
if __name__ == '__main__':
    main()
