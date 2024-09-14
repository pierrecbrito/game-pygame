from pages.screen import Screen
import pygame
from elements.button import Button
from util import path_assets
from elements.Missile import Missile

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
                "Version 1.0",
                "@pierrecbrito",
                "Objective: Defend the tower against enemy missiles.",
                "Controls: Use the mouse to direct the missiles.",
                "Good luck and have fun!"
            ]

            

    def screenUpdate(self):
        if self.CurrentState:
            # Preencher o fundo com a cor preta
            self.screen.fill(self.background_color)
            
            # Renderizar e desenhar o texto na tela
            y_offset = 50
            for line in self.text_lines:
                text_surface = self.font.render(line, True, (255, 255, 255))
                self.screen.blit(text_surface, (50, y_offset))
                y_offset += 40  # Espaçamento entre as linhas de texto

            self.btn_back = Button((0, 0, 0), 50, y_offset, 180, 45, 'Back')
            self.btn_back.draw(self.screen, (0, 0, 0))

            return_to_index = self.btn_back.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_index):
                self.endCurrentScreen()
                return 1
            return 0
