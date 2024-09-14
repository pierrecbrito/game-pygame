from pages.screen import Screen
import pygame
from elements.button import Button
from util import path_assets
from elements.Missile import Missile
import random
import sys
import math

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
        self.your_max_missiles = 10
        self.pc_max_missiles = 10
        
    def mount(self, start_level):
        # Load the background image
        self.background = pygame.image.load(path_assets / 'img/background-game.png').convert()
        self.background = pygame.transform.scale(self.background, (1200, 650))
        self.your_missiles = pygame.sprite.Group()
        self.pc_missiles = pygame.sprite.Group()
        self.targets = pygame.sprite.Group() 
        self.all_missiles = []
        self.level = start_level

        if self.CurrentState:
            self.send_random_missile()
            self.SEND_MISSILE_EVENT = pygame.USEREVENT + 1
            pygame.time.set_timer(self.SEND_MISSILE_EVENT, 2000 - (190 * self.level))
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

            if self.level <= 10:
                if self.your_points <= 0:
                    self.your_points = 100
                    self.all_missiles.clear()
                    self.your_missiles.empty()
                    self.pc_missiles.empty()
                    self.level = 1
                    pygame.time.set_timer(self.SEND_MISSILE_EVENT, 2000 -  (190 * self.level))
                elif self.pc_points <= 0:
                    self.pc_points = 100
                    self.all_missiles.clear()
                    self.your_missiles.empty()
                    self.pc_missiles.empty()
                    self.level += 1
                    pygame.time.set_timer(self.SEND_MISSILE_EVENT, 2000 -  (190 * self.level))
            else:
                self.endCurrentScreen()
                return 1
                
          
    def update_infos(self):
        # Renderizar texto no canto superior esquerdo
        text_left = self.font.render("You", True, (255, 255, 255))
        self.screen.blit(text_left, (20, 20))
        score_left = self.font.render("Life: " + str(self.your_points), True, (255, 255, 255))
        self.screen.blit(score_left, (20, 40))
        max_missiles_left = self.font.render("Max missiles: " + str(self.your_max_missiles), True, (255, 255, 255))
        self.screen.blit(max_missiles_left, (20, 60))
        active_missiles_left = self.font.render("Missiles in the air: " + str(len(self.your_missiles)), True, (255, 255, 255))
        self.screen.blit(active_missiles_left, (20, 80))

        # Renderizar texto no canto superior direito
        text_right = self.font.render("PC", True, (255, 255, 255))
        self.screen.blit(text_right, (self.width - 150, 20))
        score_right = self.font.render("Life: " + str(self.pc_points), True, (255, 255, 255))
        self.screen.blit(score_right, (self.width - 150, 40))
        max_missiles_right = self.font.render("Max missiles: " + str(self.pc_max_missiles), True, (255, 255, 255))
        self.screen.blit(max_missiles_right, (self.width - 150, 60))
        active_missiles_right = self.font.render("Missiles in the air: " + str(len(self.pc_missiles)), True, (255, 255, 255))
        self.screen.blit(active_missiles_right, (self.width - 150, 80))


        text_level = self.font.render("Level " + str(self.level), True, (255, 255, 255))
        self.screen.blit(text_level, (self.width / 2, 60))


    

    def clickCheck(self, mousepos):
        if len(self.your_missiles) < self.pc_max_missiles:
            area_x, area_y, area_width, area_height = 0, 0, 1200, 600
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

    def send_random_missile(self):
        if len(self.pc_missiles) < self.pc_max_missiles:
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