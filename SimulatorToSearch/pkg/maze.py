import sys
import os
import math

## Importa os tipos de malha disponíveis
sys.path.append(os.path.join("pkg", "mesh"))
import mapSquare, mapTriangle

## Classe que define o labirinto onde o agente esta
class Maze:
    """Maze representa um labirinto com paredes. A indexação das posições do labirinto é dada por par ordenado (linha, coluna).
    A linha inicial é zero e a linha máxima é (maxLin - 1). A coluna inicial é zero e a máxima é (maxCol - 1)."""

    def __init__(self, maxRows, maxColumns, mesh = "square", screen = False, load = False):
        """Construtor do labirinto
        @param maxRows: número de linhas do labirinto
        @param maxColumns: número de colunas do labirinto
        @param mesh: String com o nome da malha
        @param screen: Screen do pygame para a execucao
        """
        self.maxRows = maxRows
        self.maxColumns = maxColumns
        self.screen = screen
        # Matriz que representa o labirinto sendo as posições = 1 aquelas que contêm paredes
        self.walls = [[0 for j in range(maxColumns)] for i in range(maxRows)]         

        ## A depender do tipo de malha, os parametros mudam
        if mesh == "square":
            ## Cria uma malha com quadradaos
            ## Passa a largura e altura que deve ser preenchida por quadrados de determinado lado, a tela, e a posicao inicial para comecar
            self.board = mapSquare.MapSquare(maxRows*50, maxColumns*50, 50, self.screen, (50,50), load)
        elif mesh == "triangle":
            ## Define o tamanho dos dois lados iguais do triangulo isoceles
            side = 78
            ## Define o angulo de abertura dos dois lados com o tamanho acima (em radianos)
            angle = 0.261799
            ## Cria uma malha retangular
            ## Passa a quantidade de retangulos em X e em Y, o lado, o angulo, a rela e a posicao inicial para comecar
            self.board = mapTriangle.MapTriangle(maxColumns, maxRows, side, angle, self.screen, (50,50), load)
        else:
            self.board = False

    ## Metodo que atualiza a lista dos objetos que estao no labirinto
    def updateWalls(self):
        ## Pega a matriz com todos os lugares (seja quadrado ou triangulo)
        aux = self.board.getListPlaces()
        for i in aux:
            for j in i:
                ## Verifica o tipo do objeto, e coloca sua identificacao na matriz walls 
                if j.itemInside == "Parede":
                    pos = j.ide
                    self.walls[pos[0]][pos[1]] = 1
                ##ELIF....
                """
                    Se tiver outros tipos de blocos, colocar aqui com elif.....
                """
                
    ## Metodo que retorna a instancia criada da mesh
    def getBoard(self):
        return self.board
