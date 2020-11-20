import button
from objectThing import ObjectThing

class Variables(button.Button):
    def __init__(self):
        super().__init__("Variáveis", (0,159,227), (5,160), (10, 40), (100, 50))
        self.createVariable = ObjectThing("criarVariavel.png", [151, 63], [110, 30], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                                     [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")])
        
        self.setVariable = ObjectThing("setarVariavel.png", [188, 63], [110, 100], [("L", "femea-normal"), ("N", "femea-normal"), ("S", "macho-normal")],
                                                                                   [("O", "macho-normal"), ("S", "macho-normal"), ("N", "femea-normal")])
        
        self.useVariable = ObjectThing("variavel.png", [75, 50], [110, 170], [("O", "macho-normal")],[("L", "femea-normal")], True)

        
        self.things.append(self.createVariable)
        self.things.append(self.setVariable)
        self.things.append(self.useVariable)
        
