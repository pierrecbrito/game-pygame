from pages.screen import Screen
import pygame
from elements.button import Button
from util import path_assets
import sys

class Index(Screen):
 
    def __init__(self):
        super().__init__("Defense Tower", 1200, 650)

    def mount(self):
        # Load the background image
        self.background = pygame.image.load(path_assets / 'img/background.jpeg').convert()
        self.background = pygame.transform.scale(self.background, (1200, 650))
        pygame.mixer.init()
        pygame.mixer.music.load(path_assets / 'music/drama.mp3')
        pygame.mixer.music.play(-1)
        # Load the buttons
        self.btn_start = Button((0, 0, 0), 900, 200, 180, 45, 'Start')
        self.btn_levels = Button((0, 0, 0), 900, 255, 180, 45, 'Levels')
        self.btn_about = Button((0, 0, 0), 900, 310, 180, 45, 'About')
        self.btn_exit = Button((0, 0, 0), 900, 365, 180, 45, 'Exit')
       
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.blit(self.background, (0, 0))
            self.btn_start.draw(self.screen, (0, 0, 0))
            self.btn_levels.draw(self.screen, (0, 0, 0))
            self.btn_exit.draw(self.screen, (0, 0, 0))
            self.btn_about.draw(self.screen, (0, 0, 0))
            
            return_to_game = self.btn_start.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_game):
                self.endCurrentScreen()
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                return 1
            
            return_to_about = self.btn_about.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_about):
                self.endCurrentScreen()
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                return 2
            
            return_to_levels = self.btn_levels.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_levels):
                self.endCurrentScreen()
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                return 3

            return_to_exit = self.btn_exit.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed());
            if(return_to_exit):  
                pygame.quit()
                self.endCurrentScreen()
                sys.exit(0)
            
            return 0
                
