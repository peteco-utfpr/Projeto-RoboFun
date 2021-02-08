import sys

## Importa Classes necessarias para o funcionamento
from model import Model
from problem import Problem
from state import State

## Importa o algoritmo para o plano
from lrta import Lrta

##Importa o Planner
sys.path.append('pkg\planner')
from planner import Planner

## Classe que define o Agente
class Agent:
    def __init__(self, model):
        """Construtor do agente.
        @param model: Referência do ambiente onde o agente atuará."""
        self.model = model

        ## Pega o tipo de mesh, que está no model (influência na movimentação)
        self.mesh = self.model.mesh


        ## Cria a instância do problema para o agente
        self.prob = Problem()
        self.prob.createMaze(model.rows, model.columns, model.maze)
    
        
        # Posiciona fisicamente o agente no estado inicial
        initial = self.positionSensor()
        self.prob.defInitialState(initial.row, initial.col)
        
        # Define o estado atual do agente = estado inicial
        self.currentState = self.prob.initialState

        # Define o estado objetivo
        self.prob.defGoalState(model.goalPos[0], model.goalPos[1])


        """
        DEFINE OS PLANOS DE EXECUÇÃO DO AGENTE
        """
        ##Para usar o Planner online, exemplo abaixo:
        ##plann = Planner()
        ##print(plann.generate())

        
        # Plano de busca - inicialmente vazio (equivale a solucao)
        self.plan = []
        ##Custo da solução
        self.costAll = 0

        ## Cria a instancia do algoritmo LRTA*
        self.planToGoal = Lrta(model.rows, model.columns, self.prob.goalState, initial, "goal", self.mesh)
        self.planToGoal.startManhattanHeuristic(self.prob.mazeBelief.walls)  
        
        ## Coloca na biblioteca de planos todos os planos possíveis
        self.libPlan = [self.planToGoal] 

        ## Coloca dentro do plano as ações, nesse caso, ele deve executar o LRTA
        self.plan = [self.planToGoal]


    ## Metodo que define a deliberacao do agente 
    def deliberate(self):
        ## Verifica se há algum plano a ser executado
        if len(self.plan) == 0:
            return -1
        print ("******************************Inicio do ciclo***************")
        print("Posição agente  : {0},{1}".format(self.model.agentPos[0],self.model.agentPos[1]))

        ## Define a proxima acao a ser realizada como a primeira do plano
        currentAction = self.plan[0]
        ## Executa esse acao, atraves do metodo executeGo 
        self.executeGo(currentAction)
        ## Redefine o estado atual do agente
        self.currentState = self.positionSensor()
        ## Atualiza a biblioteca de planos
        self.updateLibPlan()

        ## Soma o custo da acao com o total 
        self.costAll += self.prob.getActionCost(currentAction)
        print ("Custo até o momento (com a ação escolhida):", self.costAll) 
        print ("***************************************************************")
        return 1

    ## Metodo que executa as acoes
    def executeGo(self, action):
        """Atuador: solicita ao agente físico para executar a acao.
        @param direction: Direcao da acao do agente
        @return 1 caso movimentacao tenha sido executada corretamente."""
        ## Passa a acao para o modelo
        result = self.model.go(action)
        ## Se o resultado for True, significa que a acao foi completada com sucesso, e ja pode ser removida do plano
        if (result):
            del self.plan[0]
            
        return 1

    ## Metodo que pega a posicao real do agente no ambiente
    def positionSensor(self):
        """Simula um sensor que realiza a leitura do posição atual no ambiente e traduz para uma instância da classe Estado.
        @return estado que representa a posição atual do agente no labirinto."""
        pos = self.model.agentPos
        return State(pos[0],pos[1])

    ## Metodo que atualiza a biblioteca de planos, de acordo com o estado atual do agente
    def updateLibPlan(self):
        for i in self.libPlan:
            i.updateCurrentState(self.currentState)

    def actionDo(self, posAction, action = True):
        self.model.do(posAction, action)
