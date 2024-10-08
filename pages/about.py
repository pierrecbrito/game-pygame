from pages.screen import Screen
import pygame
from elements.button import Button

class About(Screen):
 
    def __init__(self):
        super().__init__("Defense Tower", 1200, 650)
       
    def mount(self):
        if self.CurrentState:
            self.background_color = (0, 0, 0)
            # Inicializar a fonte
            self.font = pygame.font.Font(None, 20)  # Fonte padrão com tamanho 36

            # Informações textuais sobre o jogo
            self.text_lines = [
                "Defense Tower",
                "Game developed at Kodland's request in a selection process for tutor. by @pierrecbrito",
                "Objective: Destroy the PC player at each level (up to level 10) by hitting missiles at their base. Each missile can damage the enemy by 10 points of health.",
                "You can also intercept missiles coming towards your base, but each player has a limit of 10 missiles in the air.",
                "Control: use the mouse and click on point 1 where the missile should go and on the second point where the missile should hit (a missile is launched every two mouse clicks).",
                "Good luck and have fun!"
            ]

    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.background_color)
            
            y_offset = 50
            for line in self.text_lines:
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (50, y_offset))
                y_offset += 40 

            self.btn_back = Button((0, 0, 0), 50, y_offset, 180, 45, 'Back')
            self.btn_back.draw(self.screen, (0, 0, 0))

            return_to_index = self.btn_back.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_index):
                self.endCurrentScreen()
                return 1
            return 0
