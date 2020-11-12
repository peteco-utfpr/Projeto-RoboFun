import button
from objectThing import ObjectThing

class Action(button.Button):
    def __init__(self):
        super().__init__("Ação", (0,255,127), (10,10), (20, 40), (100, 50))
        self.andar = ObjectThing("andarAc.png", [100, 50], [110, 30])
        self.girarAnti = ObjectThing("girarAntiAc.png", [100, 50], [110, 100])
        self.girarHora = ObjectThing("girarHorAc.png", [100, 50], [110, 170])
        
        
        self.things.append(self.andar)
        self.things.append(self.girarAnti)
        self.things.append(self.girarHora)
        
