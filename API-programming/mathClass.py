import button
from objectThing import ObjectThing

class Math(button.Button):
    def __init__(self):
        super().__init__("Matemática", (227,6,19), (5,160), (10, 40), (100, 50))
        self.cte = ObjectThing("constante.png", [75, 50], [110, 30],[("O", "macho-normal"), ("I", "macho-normal")],[("L", "femea-normal"), ("I", "femea-normal")], True, True, "constante")
        ##Esse encaixe do operacao esta errado
        self.operacao = ObjectThing("operacao.png", [253, 75], [110, 100], [("O", "macho-normal"), ("I", "femea-normal")],[("L", "femea-normal"), ("I", "macho-normal")], True, False, "operacao")
        
        
        self.things.append(self.cte)
        self.things.append(self.operacao)
        
