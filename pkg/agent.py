import sys


from model import Model
from problem import Problem
from state import State
from cardinal import action
from tree import TreeNode
from lrta import Lrta

from codeBlock import CodeBlock

sys.path.append('pkg/planner')
from planner import Planner

class Agent:
    """"""
    counter = -1 # Contador de passos no plano, usado na deliberação

    def __init__(self, model):
        """Construtor do agente.
        @param model: Referência do ambiente onde o agente atuará."""
        self.model = model

        self.prob = Problem()
        # @TODO T_AAFP - criar crencas sobre as pareded do labirinto
        self.prob.createMaze(9, 9)
        self.prob.mazeBelief.putVerticalWall(0,1,0)
               
        self.prob.mazeBelief.putVerticalWall(0,0,1)
        self.prob.mazeBelief.putVerticalWall(5,8,1)
        self.prob.mazeBelief.putVerticalWall(5,5,2)
        self.prob.mazeBelief.putVerticalWall(8,8,2)

        self.prob.mazeBelief.putHorizontalWall(4,7,0)
        self.prob.mazeBelief.putHorizontalWall(7,7,1)
        self.prob.mazeBelief.putHorizontalWall(3,5,2)
        self.prob.mazeBelief.putHorizontalWall(3,5,3)
        self.prob.mazeBelief.putHorizontalWall(7,7,3)

        self.prob.mazeBelief.putVerticalWall(6,7,4)
        self.prob.mazeBelief.putVerticalWall(5,6,5)
        self.prob.mazeBelief.putVerticalWall(5,7,7)

        # Posiciona fisicamente o agente no estado inicial
        initial = self.positionSensor()
        self.prob.defInitialState(initial.row, initial.col)
        
        # Define o estado atual do agente = estado inicial
        self.currentState = self.prob.initialState

        # @TODO T_AAFP - defina estado objetivo
        # Define o estado objetivo
        self.prob.defGoalState(2, 8)

        # o metodo abaixo serve apenas para a view desenhar a pos objetivo
     
      
        # Plano de busca - inicialmente vazio (equivale a solucao)
        self.plan = []

        self.costAll = 0


##        self.planToGoal = Lrta(9, 9, self.prob.goalState, initial, "goal")
##        self.planToGoal.startManhattanHeuristic(self.prob.mazeBelief.walls)  
##
##        self.planToBegin = Lrta(9, 9, initial, initial, "begin")
##        self.planToBegin.startManhattanHeuristic(self.prob.mazeBelief.walls)

        self.libPlan = []
        
        code = CodeBlock()
        self.plan = code.generate()

        ##plann = Planner()
        ##print(plann.generate())

    def deliberate(self):
        # Primeira chamada, realiza busca para elaborar um plano
        # @TODO T_AAFP: Implementação do aluno
        print ("******************************Inicio do ciclo***************")
        
            
        if len(self.plan) == 0:
            return -1
        print("Posição agente  : {0},{1}".format(self.model.agentPos[0],self.model.agentPos[1]))

        currentAction = self.plan[0]
        self.executeGo(currentAction)
        self.currentState = self.positionSensor()
        self.updateLibPlan()
        
        self.costAll += self.prob.getActionCost(currentAction)
        print ("Custo até o momento (com a ação escolhida):", self.costAll) 
        print ("***************************************************************")
        return 1

    def executeGo(self, direction):
        """Atuador: solicita ao agente física para executar a ação.
        @param direction: Direção da ação do agente
        @return 1 caso movimentação tenha sido executada corretamente."""
        result = self.model.go(direction)
        print("SAIIIDAAAA: ", result)
        if (result):
            del self.plan[0]
        return 1

    def positionSensor(self):
        """Simula um sensor que realiza a leitura do posição atual no ambiente e traduz para uma instância da classe Estado.
        @return estado que representa a posição atual do agente no labirinto."""
        pos = self.model.agentPos
        return State(pos[0],pos[1])


    def updateLibPlan(self):
        for i in self.libPlan:
            i.updateCurrentState(self.currentState)
