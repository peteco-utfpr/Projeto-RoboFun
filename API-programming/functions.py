import button
from objectThing import ObjectThing

class Functions(button.Button):
    def __init__(self):
        super().__init__("Funções", (102,36,131), (5,110), (10, 40), (100, 50))
        self.loop = ObjectThing("enquanto.png",[381, 126], [110, 30], [("N", "femea-normal"), ("I", "femea-normal"), ("S", "macho-normal")], [("S", "macho-normal"), ("I","macho-normal"), ("N", "femea-normal")], True, False, "enquanto",(55, -20))
        self.se = ObjectThing("se.png",[300, 125], [110, 200], [("N", "femea-normal"), ("I", "femea-normal"), ("S", "macho-normal")], [("S", "macho-normal"), ("I","macho-normal"), ("N", "femea-normal")], True, False, "se",(5, -25))
        self.senao = ObjectThing("senao.png",[218, 75], [110, 369], [("S", "macho-normal")], [("N", "femea-normal")], False, False, "senao")

        self.things.append(self.loop)
        self.things.append(self.se)
        self.things.append(self.senao)
        
