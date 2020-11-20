import button
from objectThing import ObjectThing

class Bounds(button.Button):
    def __init__(self):
        super().__init__("Inicio-Fim", (255,140,0), (5,10), (10, 40), (100, 50))
        self.start = ObjectThing("inicio.png",[100, 62], [110, 30], [("S", "macho-normal")], [("N", "femea-normal")], False, False, "inicio",(55, -20))
        self.end = ObjectThing("fim.png",[100, 50], [110, 136], [("N", "femea-normal")], [("S", "macho-normal")], False, False, "fim",(5, -25))
        

        self.things.append(self.start)
        self.things.append(self.end)
        
