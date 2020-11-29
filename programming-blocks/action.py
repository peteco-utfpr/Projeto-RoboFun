import button
from objectThing import ObjectThing

## Todos os objetos referentes ao tipo: AÇÃO estão dentro dessa parte
class Action(button.Button):
    def __init__(self):
        ##Chama a construtora da classe pai: Button
        super().__init__("Ação", (0,150,64), (5,60), (10, 40), (100, 50))

        ##Define quais componentes estão disponíveis para o usuário
        ##Cada objeto é uma instancia da classe ObjectThing
        ##Os parametros a serem passados são: imagem, tamanho, posicao, quais encaixes ele ofere, quais encaixes ele recebe, se o usuário pode digitar texto
        ##quais o caracteres permitidos, se tiver texto, e o nome do objeto 
        self.andar = ObjectThing("mover.png", [125, 63], [110, 30], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "mover")
        self.girarAnti = ObjectThing("girarAnti.png", [125, 63], [110, 100],[("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "girarAnti")
        self.girarHora = ObjectThing("girarHor.png", [125, 63], [110, 170], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "girarHor")
        self.lerDistancia = ObjectThing("lerDistancia.png", [138, 50], [110, 240], [("O", "macho-normal")],[("L", "femea-normal")], False, False, "lerDitancia")
        

        ##Adiciona o elemento na lista de coisas
        self.things.append(self.andar)
        self.things.append(self.girarAnti)
        self.things.append(self.girarHora)
        self.things.append(self.lerDistancia)
        
