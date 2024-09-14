import pygame

class Screen():
 
    # HERE (0,0,255) IS A COLOUR CODE
    def __init__(self, title, width=440, height=445):
        # HEIGHT OF A WINDOW
        self.height = height
        # TITLE OF A WINDOW
        self.title = title
        # WIDTH OF A WINDOW
        self.width = width
        # CURRENT STATE OF A SCREEN
        self.CurrentState = False
 
    # DISPLAY THE CURRENT SCREEN OF
    # A WINDOW AT THE CURRENT STATE
    def makeCurrentScreen(self):
        # SET THE TITLE FOR THE CURRENT STATE OF A SCREEN
        pygame.display.set_caption(self.title)
        # SET THE STATE TO ACTIVE
        self.CurrentState = True
        # ACTIVE SCREEN SIZE
        self.screen = pygame.display.set_mode((self.width,
                                           self.height))
 
    # THIS WILL SET THE STATE OF A CURRENT STATE TO OFF
 
    def endCurrentScreen(self):
        self.CurrentState = False
 
    # THIS WILL CONFIRM WHETHER THE NAVIGATION OCCURS
    def checkUpdate(self, fill):
        return self.CurrentState
 
    # THIS WILL UPDATE THE SCREEN WITH THE NEW NAVIGATION TAB
    def screenUpdate(self):
        if self.CurrentState:
            #Do something
            pass
 
    # RETURNS THE TITLE OF THE SCREEN
    def returnTitle(self):
        return self.screen
    
    def handle_events(self, events):
        pass