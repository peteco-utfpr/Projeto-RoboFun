import button
from objectThing import ObjectThing

class Functions(button.Button):
    def __init__(self):
        super().__init__("Funções", (102,36,131), (5,60), (10, 40), (100, 50))
        self.loop = ObjectThing("enquanto.png",[381, 126], [110, 30], [("N", "femea-normal")], [("S", "macho-normal")])
        self.se = ObjectThing("se.png",[300, 125], [110, 150])
        self.senao = ObjectThing("senao.png",[218, 75], [110, 270])

        self.things.append(self.loop)
        self.things.append(self.se)
        self.things.append(self.senao)
        
