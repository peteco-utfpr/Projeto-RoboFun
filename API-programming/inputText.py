import pygame

pygame.init()
COLOR_INACTIVE = (211,211,211)
COLOR_ACTIVE = (255,255,255)
 
FONT = pygame.font.SysFont(None, 25)


class InputText:
    def __init__(self, x, y, w, h, text='1', onlyNumbers = False, qtdMax = 3):
        self.rect = pygame.Rect(x, y, w, h)

        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, (0,0,0))
        self.active = False
        self.onlyNumbers = onlyNumbers
        self.numbers = "0123456789"
        self.maxCar = qtdMax

    def handle_event(self, event):
        result = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
                result = True
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                result = True
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.onlyNumbers == True:
                        if event.unicode in self.numbers and len(self.text) < self.maxCar:
                            self.text += event.unicode
                    else:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, (0, 0, 0))
        self.update()
        return result

    def update(self):
        # Resize the box if the text is too long.
        width = max(35, self.txt_surface.get_width()+10)
        self.rect.w = width

    def show(self, screen):
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect)
         # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

    def getText(self):
        return self.text

    def setPos(self, pos):
         self.rect.x = int(pos[0])
         self.rect.y = int(pos[1])
        


##
##def main():
##    clock = pg.time.Clock()
##    input_box1 = InputBox(30, 30, 20, 20, '1', True)
##  
##    input_boxes = [input_box1]
##    done = False
##
##    while not done:
##        for event in pg.event.get():
##            if event.type == pg.QUIT:
##                done = True
##            for box in input_boxes:
##                box.handle_event(event)
##
##       
##
##        screen.fill((30, 30, 30))
##        for box in input_boxes:
##            box.draw(screen)
##
##        pg.display.flip()
##        clock.tick(30)
##
##
##if __name__ == '__main__':
##    main()
##    pg.quit()
