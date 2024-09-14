import pygame

class Screen():
 
    def __init__(self, title, width=440, height=445):
        self.height = height
        self.title = title
        self.width = width
        self.CurrentState = False
 
    def makeCurrentScreen(self):
        pygame.display.set_caption(self.title)
        self.CurrentState = True
        self.screen = pygame.display.set_mode((self.width,
                                           self.height))
 
    def endCurrentScreen(self):
        self.CurrentState = False
 
    def checkUpdate(self, fill):
        return self.CurrentState
    
    def screenUpdate(self):
        if self.CurrentState:
            #Do something
            pass
 
    def returnTitle(self):
        return self.screen
    
    def handle_events(self, events):
        pass