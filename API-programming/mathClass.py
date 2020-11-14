import button
from objectThing import ObjectThing

class Math(button.Button):
    def __init__(self):
        super().__init__("Matemática", (112,128,144), (10,110), (20, 40), (100, 50))
        self.cte = ObjectThing("constante.png", [70, 50], [110, 30],[("O", "macho-normal")],[("L", "femea-normal")], True)
        
        
        
        self.things.append(self.cte)
        
