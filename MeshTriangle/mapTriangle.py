import triangle
import math

class MapTriangle:
    def __init__(self, width, heigth, side, angle, screen):
        self.listPlaces = []
        self.width = width
        self.heigth = heigth
        self.screen = screen
        self.side = side
        self.angle = angle

        self.heightTriangle = side*math.cos(angle)
        self.baseTriangle = math.sqrt(side**2 - (self.heightTriangle**2))

        self.selectPlace = False
        self.generateMap()
        
    def generateMap(self):
        y = 0
        control = True
        posYCorrect = y
        while y < self.heigth:
            x = 0
            if control == True:
                self.listPlaces.append(triangle.Triangle((x, y), self.side, self.angle, 0, self.screen))
                first = 1
                second = 0
                
            else:
                self.listPlaces.append(triangle.Triangle((x, y), self.side, self.angle, 1, self.screen))
                first = 0
                second = 1
                
            posYCorrect = self.listPlaces[-1].getP2()[1]
            while x < self.width:
                self.listPlaces.append(triangle.Triangle((self.listPlaces[-1].getP2()[0], posYCorrect), self.side, self.angle, first, self.screen))
                self.listPlaces.append(triangle.Triangle((self.listPlaces[-1].getP2()[0], y), self.side, self.angle, second, self.screen))
                x += (2*self.baseTriangle)

            if control == True:    
                y += 2*self.heightTriangle
            control = not control

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
