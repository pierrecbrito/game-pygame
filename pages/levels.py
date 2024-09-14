from pages.screen import Screen
import pygame
from elements.button import Button

class Levels(Screen):
 
    def __init__(self):
        super().__init__("Defense Tower", 1200, 650)
       
    def mount(self):
        if self.CurrentState:
            self.background_color = (0, 0, 0)
            # Inicializar a fonte
            self.font = pygame.font.Font(None, 50)  # Fonte padrão com tamanho 36
            self.btns = []

    def screenUpdate(self):
        if self.CurrentState:
            # Preencher o fundo com a cor preta
            self.screen.fill(self.background_color)
            
            # Renderizar e desenhar o texto na tela
            y_offset = 220
            x_offset = 330

            for i in range(1, 11):
                self.btns.append(Button((0, 0, 0), x_offset, y_offset, 45, 45, f'{i}'))
                self.btns[i-1].draw(self.screen, (0, 0, 0), 40)
                
                x_offset += 100

                if(i == 5):
                    y_offset += 100
                    x_offset = 330
            
            for btn in self.btns:
                return_to_game = btn.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
                if(return_to_game):
                    self.endCurrentScreen()
                    return int(btn.text)
            
            title = self.font.render("Levels", True, (255, 255, 255))
            self.screen.blit(title, (525, 50))

            
            self.btn_back = Button((0, 0, 0), 500, 580, 180, 45, 'Back')
            self.btn_back.draw(self.screen, (0, 0, 0))

            return_to_index = self.btn_back.focusCheck(pygame.mouse.get_pos(), pygame.mouse.get_pressed())
            if(return_to_index):
                self.endCurrentScreen()
                return -1
        return 0
               
