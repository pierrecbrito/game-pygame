import pygame

class Button():

    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.CurrentState = True
        self.sx = self.x + self.width
        self.sy = self.y + self.height

    def draw(self, screen, outline=None, font_size=16):
        if(self.CurrentState):
            if outline:
                pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('Arial', font_size)
                text = font.render(self.text, 1, (255, 255, 255))
                screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    
    def focusCheck(self, mousepos, mouseclick):
        if(mousepos[0] >= self.x and mousepos[0] <= 
                self.sx and mousepos[1] >= self.y and mousepos[1]
                <= self.sy):
           
            # IF MOUSE BUTTON CLICK THEN
            # NAVIGATE TO THE NEXT OR PREVIOUS TABS
            return mouseclick[0]
 
        else:
            # ELSE LET THE CURRENT STATE TO BE OFF
           
            return False