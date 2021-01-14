import square

class MapSquare:
    def __init__(self, width, heigth, sideSquare, screen):
        self.listPlaces = []
        self.width = width
        self.heigth = heigth
        self.screen = screen
        self.sideSquare = sideSquare
        self.selectPlace = False
        self.generateMap()
        
    def generateMap(self):
        y = 0
        while y < self.heigth:
            x = 0
            while x < self.width:
                self.listPlaces.append(square.Square((x, y), self.sideSquare, self.screen))
                x += self.sideSquare
            y += self.sideSquare

    def checkClick(self, posMouse):
        if self.selectPlace != False:
            self.selectPlace.checkClickItens(posMouse)
            self.selectPlace = False
            return True  
        else:
            for i in self.listPlaces:
                if self.selectPlace != False:
                    break
                self.selectPlace = i.checkClick(posMouse)
            return False
        
    
    def show(self):
        for i in self.listPlaces:
            i.show()
