import button
from objectThing import ObjectThing

## Essa classe engloba os elementos de Fim e Inicio
class Bounds(button.Button):
    def __init__(self):
        ##Inicializa a classe pai: Button
        super().__init__("Inicio-Fim", (255,140,0), (5,10), (10, 40), (100, 50))

        ##Define quais componentes estão disponíveis para o usuário
        ##Cada objeto é uma instancia da classe ObjectThing
        ##Os parametros a serem passados são: imagem, tamanho, posicao, quais encaixes ele ofere, quais encaixes ele recebe, se o usuário pode digitar texto
        ##quais o caracteres permitidos, se tiver texto, e o nome do objeto 
        self.start = ObjectThing("inicio.png",[50, 31], [110, 30], [("S", "macho-normal")], [("N", "femea-normal")], False, False, "inicio")
        self.end = ObjectThing("fim.png",[50, 25], [110, 65], [("N", "femea-normal")], [("S", "macho-normal")], False, False, "fim")
        
        ##Adiciona os elementos na lista de coisas
        self.things.append(self.start)
        self.things.append(self.end)
        
