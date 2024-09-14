import math
from util import path_assets
import pygame

class Missile(pygame.sprite.Sprite):

    def __init__(self, x, y, to_x1, to_y1, to_x2, to_y2, angle, speed, damage, owner):
        super().__init__()
        self.x = x
        self.y = y
        self.to_x1 = to_x1
        self.to_y1 = to_y1
        self.to_x2 = to_x2
        self.to_y2 = to_y2
        self.angle = angle
        self.speed = speed
        self.damage = damage
        self.owner = owner
        self.original_image = pygame.image.load(path_assets / 'img/missile.png').convert_alpha()
        self.image = self.original_image #pygame.image.load(path_assets / 'img/missile.png').convert()
        self.rect = self.image.get_rect(center=(x, y))

        self.launch_sound = pygame.mixer.Sound(str(path_assets / 'music/missile-sent.mp3'))
        self.launch_sound.play()
        
         # Carregar o som de explosão
        self.explosion_sound = pygame.mixer.Sound(str(path_assets / 'music/explosion.mp3'))

        # Carregar a imagem de explosão
        self.explosion_image = pygame.image.load(str(path_assets / 'img/explosion.png')).convert_alpha()

        # Calcular a direção do movimento
        dx1 = to_x1 - x
        dy1 = to_y1 - y
        distance1 = math.hypot(dx1, dy1)
        self.dir_x1 = dx1 / distance1
        self.dir_y1 = dy1 / distance1
        self.angle1 = math.degrees(math.atan2(-dy1, dx1)) - 90


        if(to_x1 == to_x2 and to_y2 == to_y1):
            to_x2 += 1
            to_y2 += 1

        dx2 = to_x2 - to_x1
        dy2 = to_y2 - to_y1

        distance2 = math.hypot(dx2, dy2)
        self.dir_x2 = dx2 / distance2
        self.dir_y2 = dy2 / distance2

        self.angle2 = math.degrees(math.atan2(-dy2, dx2)) - 90

        self.route1 = True
        self.route2 = False
        self.explosion_start_time = None
        self.end = False

    def move(self):
        if self.route1:
            self.x += self.dir_x1 * self.speed
            self.y += self.dir_y1 * self.speed
            self.rect.center = (self.x, self.y)
            #Rotacionar a imagem do míssil
            self.image = pygame.transform.rotate(self.original_image, self.angle1)
            self.rect = self.image.get_rect(center=self.rect.center)
        elif self.route2:
            self.x += self.dir_x2 * self.speed
            self.y += self.dir_y2 * self.speed
            self.rect.center = (self.x, self.y)
            #Rotacionar a imagem do míssil
            self.image = pygame.transform.rotate(self.original_image, self.angle2)
            self.rect = self.image.get_rect(center=self.rect.center)
        
        if math.hypot(self.to_x1 - self.x, self.to_y1 - self.y) < self.speed:
            self.route1 = False
            self.route2 = True

        if math.hypot(self.to_x2 - self.x, self.to_y2 - self.y) < self.speed:
            self.route2 = False
            self.missile_end()

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        
    def check_collision(self, target_group, missile_group):
        if pygame.sprite.spritecollideany(self, target_group):
            self.missile_end()
            return True
        
        collided_missile = pygame.sprite.spritecollideany(self, missile_group)
        if collided_missile and collided_missile != self:
            self.missile_end()
            collided_missile.missile_end()
            return True
        
        return False
           
    def missile_end(self):
        if not self.end:
            self.explosion_sound.play()
            # Mostrar a imagem de explosão
            self.image = self.explosion_image
            self.original_image = self.image
            self.rect = self.image.get_rect(center=self.rect.center)
            # Remover o míssil após a explosão
            self.explosion_start_time = pygame.time.get_ticks()
            self.end = True

    def update(self):
        self.move()

        if self.explosion_start_time:
            current_time = pygame.time.get_ticks()
            if current_time - self.explosion_start_time > 500:  # 1200 milissegundos (1.2 segundos)
                self.kill()