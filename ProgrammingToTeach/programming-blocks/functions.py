import button
from objectThing import ObjectThing

##Todos os objetos da classe Função estão aqui
class Functions(button.Button):
    def __init__(self):
        ## Inicializa a construtora da classe pai: Button
        super().__init__("Funções", (102,36,131), (5,110), (10, 40), (100, 50))

        ##Define quais componentes estão disponíveis para o usuário
        ##Cada objeto é uma instancia da classe ObjectThing
        ##Os parametros a serem passados são: imagem, tamanho, posicao, quais encaixes ele ofere, quais encaixes ele recebe, se o usuário pode digitar texto
        ##quais o caracteres permitidos, se tiver texto, o nome do objeto, e o ajuste da posição do texto a ser escrito (em relação ao padrão, que é no meio) 
        self.loop = ObjectThing("enquanto.png",[191, 63], [110, 30], [("N", "femea-normal"), ("I", "femea-normal"), ("S", "macho-normal")], [("S", "macho-normal"), ("I","macho-normal"), ("N", "femea-normal")], True, [">", "=", "<"], "enquanto",(28, -10))
        self.se = ObjectThing("se.png",[150, 63], [110, 98], [("N", "femea-normal"), ("I", "femea-normal"), ("S", "macho-normal")], [("S", "macho-normal"), ("I","macho-normal"), ("N", "femea-normal")], True, [">", "=", "<"], "se",(3, -13))
        self.senao = ObjectThing("senao.png",[109, 38], [110, 165], [("S", "macho-normal")], [("N", "femea-normal")], False, False, "senao")

        ##Adiciona os itens na lista de coisas
        self.things.append(self.loop)
        self.things.append(self.se)
        self.things.append(self.senao)
        
