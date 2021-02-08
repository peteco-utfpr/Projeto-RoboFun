import pygame

pygame.init()
COLOR_INACTIVE = (211,211,211)
COLOR_ACTIVE = (255,255,255)
 
FONT = pygame.font.SysFont(None, 15)

##Classe utilizada para permitir adicionar texto no meio dos blocos
class InputText:
    def __init__(self, x, y, w, h, text='', only = False, qtdMax = 3):
        ##Define os parametros principais
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, (0,0,0))
        self.active = False
        ## Only é uma lista contendo os caracteres permitidos de serem escritos. Em caso de False, significa que todos os caracteres são permitidos
        self.only = only
        ##Define a quantidade maxima de caractertes
        self.maxCar = qtdMax

    ##Método usado para verificar os eventos sobre a caixa de texto. O parametro passado é event do pygame
    def handle_event(self, event):
        result = False
        ## Verifica se foi um clique de mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica se o clique ocorreu sobre a caixa
            # E muda a cor de fundo da caixa de texto de acordo com tal
            if self.rect.collidepoint(event.pos):
                # Habilita a escrita na caixa de texto 
                self.active = True
                self.color = COLOR_ACTIVE
                result = True
            ##Caso contrário, desabilita
            else:
                self.active = False
                self.color = COLOR_INACTIVE
                
        ## Verifica se alguma tecla foi apertada 
        if event.type == pygame.KEYDOWN:
            ## Verifica se a escrita esta habilitada
            if self.active:
                result = True
                ## Verifica se apertou o enter. Se sim, desabilita a escrita
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
                ## Verifica se apertou o backspace. Se sim, apaga o ultimo caracterer
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                ## Se foi outra tecla, verifica se o caracter pertence aqueles permitidos, e se
                ## o tamanho maximo de caracteres já nao foi esgotado
                else:
                    if self.only != False:
                        if event.unicode in self.only and len(self.text) < self.maxCar:
                            self.text += event.unicode
                    else:
                        if len(self.text) < self.maxCar:
                            self.text += event.unicode
                            
                # Renderiza novamente o texto
                self.txt_surface = FONT.render(self.text, True, (0, 0, 0))
        self.update()
        return result

    # Método para mudar o tamanho do retangulo que contem o texto, de acordo com a quantidade de caracteres
    def update(self):
        width = max(18, self.txt_surface.get_width()+5)
        self.rect.w = width

    ## Método usado para mostrar o retangulo e o texto
    def show(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    ## Método para retornar o texto escrito até o momento
    def getText(self):
        return self.text

    ##Método para retornar setar a posição do texto
    def setPos(self, pos):
         self.rect.x = int(pos[0])
         self.rect.y = int(pos[1])
        
