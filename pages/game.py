from pages.screen import Screen
import pygame
from elements.button import Button
from util import path_assets
from elements.Missile import Missile
import random
import sys

class Game(Screen):
 
    def __init__(self):
        super().__init__("Defense Tower", 1200, 650)
        self.to_x1 = -1
        self.to_y1 = -1
        self.to_x2 = -1
        self.to_y2 = -1
        self.missiles_counter = 0
        self.your_points = 100
        self.pc_points = 100
        

    def mount(self):
        # Load the background image
        self.background = pygame.image.load(path_assets / 'img/background-game.png').convert()
        self.background = pygame.transform.scale(self.background, (1200, 650))
        self.your_missiles = pygame.sprite.Group()
        self.pc_missiles = pygame.sprite.Group()
        self.targets = pygame.sprite.Group() 
        self.all_missiles = []

        if self.CurrentState:
            self.send_random_missile()
            self.SEND_MISSILE_EVENT = pygame.USEREVENT + 1
            pygame.time.set_timer(self.SEND_MISSILE_EVENT, 800)
            self.font = pygame.font.Font(None, 18)  # Fonte padrão com tamanho 36

    def screenUpdate(self):
        if self.CurrentState:
            self.screen.blit(self.background, (0, 0))
            self.your_missiles.update()
            self.your_missiles.draw(self.screen)
            self.pc_missiles.update()
            self.pc_missiles.draw(self.screen)

            for missile in self.your_missiles:
                missile.check_collision(self.targets, self.pc_missiles)

            for missile in self.pc_missiles:
                missile.check_collision(self.targets, self.your_missiles)

            your_missiles = 0
            pc_missiles = 0
            for missile in self.all_missiles:
                if missile.end:
                    if missile.x >= 1089 and  missile.x <= 1200 and missile.y >= 520 and missile.y <= 608 and missile.owner == 'You':
                        your_missiles += 1
                    elif missile.x >= 0 and  missile.x <= 111 and missile.y >= 520 and missile.y <= 608 and missile.owner == 'PC':
                        pc_missiles += 1
                
                
            self.pc_points = 100 - your_missiles * 10
            self.your_points = 100 - pc_missiles * 10
            self.update_infos()  
          
    def update_infos(self):
        # Renderizar texto no canto superior esquerdo
        text_left = self.font.render("You", True, (255, 255, 255))
        self.screen.blit(text_left, (20, 20))
        score_left = self.font.render("Life: " + str(self.your_points), True, (255, 255, 255))
        self.screen.blit(score_left, (20, 40))

        # Renderizar texto no canto superior direito
        text_right = self.font.render("PC", True, (255, 255, 255))
        self.screen.blit(text_right, (self.width - 80, 20))
        score_right = self.font.render("Life: " + str(self.pc_points), True, (255, 255, 255))
        self.screen.blit(score_right, (self.width - 75, 40))

    

    def clickCheck(self, mousepos):
        # Verificar se o clique está dentro de uma área específica 
        # # Verifica se o botão esquerdo do mouse foi clicado
        area_x, area_y, area_width, area_height = 0, 0, 1200, 600
        print(mousepos[0], mousepos[1])
        if(self.to_x1 == -1):
            self.to_x1 = mousepos[0]
            self.to_y1 = mousepos[1]
        elif (self.to_x2 == -1):
            self.to_x2 = mousepos[0]
            self.to_y2 = mousepos[1]
            if (area_x <= mousepos[0] <= area_x + area_width and
                area_y <= mousepos[1] <= area_y + area_height):
                self.missiles_counter += 1
                new_missile = Missile(75, 536, self.to_x1, self.to_y1, self.to_x2, self.to_y2, 15, 0.1, 80, 'You')
                self.your_missiles.add(new_missile)
                self.all_missiles.append(new_missile)
            self.to_x1 = -1
            self.to_y1 = -1
            self.to_x2 = -1
            self.to_y2 = -1

            # Execute a ação desejada aqui

    def send_random_missile(self):
        self.missiles_counter += 1
        start_x = 1123 #random.randint(0, 1200)
        start_y = 535 #random.randint(0, 650)
        to_x1 = random.randint(50, 1100)
        to_y1 = random.randint(0, 580)
        to_x2 = 75
        to_y2 = 536
        new_missile = Missile(start_x, start_y, to_x1, to_y1, to_x2, to_y2, 15, 0.10, 80, 'PC')
        self.pc_missiles.add(new_missile)
        self.all_missiles.append(new_missile)
    
    def handle_events(self, event):
        if self.CurrentState:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Verifica se o botão esquerdo do mouse foi clicado
                    mousepos = pygame.mouse.get_pos()
                    self.clickCheck(mousepos)
            elif event.type == self.SEND_MISSILE_EVENT:
                self.send_random_missile()
        return True