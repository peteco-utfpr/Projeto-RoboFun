import button
from objectThing import ObjectThing

## Todos os objetos da classe Variaveis estão aqui
class Variables(button.Button):
    def __init__(self):
        ## Inicializa a classe pai: Button 
        super().__init__("Variáveis", (0,159,227), (5,210), (10, 40), (100, 50))

        ##Define quais componentes estão disponíveis para o usuário
        ##Cada objeto é uma instancia da classe ObjectThing
        ##Os parametros a serem passados são: imagem, tamanho, posicao, quais encaixes ele ofere, quais encaixes ele recebe, se o usuário pode digitar texto
        ##quais o caracteres permitidos, se tiver texto, e o nome do objeto 

        self.createVariable = ObjectThing("criarVariavel.png", [151, 63], [110, 30], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "criarVariavel")
        self.setVariable = ObjectThing("setarVariavel.png", [188, 63], [110, 100], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                                   [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], True, False, "setarVariavel")
        self.useVariable = ObjectThing("variavel.png", [75, 50], [110, 170], [("O", "macho-normal"), ("I", "macho-normal")],[("L", "femea-normal"), ("I", "femea-normal")], True, False, "variavel")

        ## Adiciona os itens na lista de coisas
        self.things.append(self.createVariable)
        self.things.append(self.setVariable)
        self.things.append(self.useVariable)
        
