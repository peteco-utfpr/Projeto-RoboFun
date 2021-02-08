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
        self.norte = ObjectThing("norte.png", [125, 32], [110, 30], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "norte")
        self.sul = ObjectThing("sul.png", [125, 32], [110, 65],[("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "sul")
        self.leste = ObjectThing("leste.png", [125, 32], [110, 100], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "leste")
        
        self.oeste = ObjectThing("oeste.png", [125, 32], [110, 135],  [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")], False, False, "oeste")
        

        ##Adiciona o elemento na lista de coisas
        self.things.append(self.norte)
        self.things.append(self.sul)
        self.things.append(self.leste)
        self.things.append(self.oeste)
        
