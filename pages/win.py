from pages.screen import Screen
import pygame
from elements.button import Button

class Win(Screen):
 
    def __init__(self):
        super().__init__("Defense Tower", 1200, 650)
       
    def mount(self):
        if self.CurrentState:
            self.background_color = (0, 0, 0)
            # Inicializar a fonte
            self.font = pygame.font.Font(None, 20)  # Fonte padrão com tamanho 36

            # Informações textuais sobre o jogo
            self.text_lines = [
                "Congratulations.",
                "You won the game."
            ]
    
    def screenUpdate(self):
        if self.CurrentState:
            self.screen.fill(self.background_color)
        
            y_offset = 230
            for line in self.text_lines:
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (350, y_offset))
                y_offset += 40 

            self.btn_back = Button((0, 0, 0), 350, y_offset, 180, 45, 'to menu')
            self.btn_back.draw(self.screen, (0, 0, 0))

            return_to_index = self.btn_back.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_index):
                self.endCurrentScreen()
                return 1
            return 0