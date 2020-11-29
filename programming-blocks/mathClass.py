import button
from objectThing import ObjectThing

##Todos os objetos da classe Matematica estão aqui
class Math(button.Button):
    def __init__(self):
        ##Inicializa a classe pai: Button
        super().__init__("Matemática", (227,6,19), (5,160), (10, 40), (100, 50))

        ##Define quais componentes estão disponíveis para o usuário
        ##Cada objeto é uma instancia da classe ObjectThing
        ##Os parametros a serem passados são: imagem, tamanho, posicao, quais encaixes ele ofere, quais encaixes ele recebe, se o usuário pode digitar texto
        ##quais o caracteres permitidos, se tiver texto, e o nome do objeto 
        self.cte = ObjectThing("constante.png", [75, 50], [110, 30],[("O", "macho-normal"), ("I", "macho-normal")],[("L", "femea-normal"), ("I", "femea-normal")], True, ["1", "2", "3", "4", "5", "6", "7", "8", "9"], "constante")
        self.operacao = ObjectThing("operacao.png", [253, 75], [110, 100], [("O", "macho-normal"), ("I", "femea-normal")],[("L", "femea-normal"), ("I", "macho-normal")], True, ["+", "-", "/", "%", "*"], "operacao")
        
        ## Adiciona os itens na lista de coisas
        self.things.append(self.cte)
        self.things.append(self.operacao)
        
