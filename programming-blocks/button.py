import pygame
## Classe Button
## Essa classe é usada como uma classe Pai, para ser especializada pelas classes de objetos (Matematica, funções, variaveis...)
## Todas as funções são implementadas aqui, e os objetos definidos são criados em cada classe herdeira
class Button:
    def __init__(self, nome, cor, pos, tamRect, tamButton):
        ## Define os paramentros do botão
        self.name = nome
        self.color = cor
        self.pos = pos
        self.sizeRect = tamRect
        self.sizeButton = tamButton
        ## Esta lista contem todos os itens que irão aparecer no momento em que o botão for clicado
        self.things = []

    ##Método para adicionar um novo elemento
    def addThing(self, thing):
        self.things.append(thing)

    ## Método para verificar se o mouse está sobre algum botão
        ##Se estiver, ele faz uma animação (mostrando um outro retangulo cinza), para mostrar para o usuário
    def mouseOn(self, tela, mousePos):
        if mousePos[0] >= 0 and mousePos[0] <= self.sizeButton[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.sizeButton[1]:
                  pygame.draw.rect(tela, (220,220,220), [0, self.pos[1], self.sizeButton[0], self.sizeButton[1]])
                  self.show(tela)
                
    ##Método para mostrar o botão na tela
    def show(self, tela):
        font = pygame.font.SysFont(None, 21)
        pygame.draw.rect(tela, self.color, [self.pos[0], self.pos[1]+5, self.sizeRect[0], self.sizeRect[1]])
        text = font.render(self.name, True, (0,0,0))
        tela.blit(text, [self.pos[0]+12, self.pos[1]+18])

    ## Verifica se o botão foi clicado:
        ## Se caso sim, então ele irá percorrer toda a lista de objetos, e irá mostra-los na tela (chamando a função deles de show())
    def mouseClick(self, tela, mousePos):
        if mousePos[0] >= 0 and mousePos[0] <= self.sizeButton[0]:
            if mousePos[1] >= self.pos[1] and mousePos[1] <= self.pos[1] + self.sizeButton[1]:
                pygame.draw.rect(tela, (211,211,211), [100, 0, 400, 600])
                for i in self.things:
                    i.show(tela)
                return True
        return False
                
        
        

        
