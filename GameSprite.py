import pygame
import random
import math
from pygame.locals import RLEACCEL

from screen import Screen


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class GameSprite(pygame.sprite.Sprite):
    def __init__(self):   
        super().__init__()
        
    def clone(self):
        pass


class Bird(GameSprite):
    Max_Speed = 10
    Min_Speed = 5

    def __init__(self):
        super(Bird, self).__init__()
        self.surf = pygame.image.load("icons/bird.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                random.randint(0, Screen.height),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)
        self.time = 0
    
    def update(self):
        self.time += 1
        speed_x = -self.speed
        speed_y = 0.75 * self.speed \
                  * math.cos(2 * math.pi * self.time / (0.05 * Screen.width))
        self.rect.move_ip(speed_x, speed_y)
        if self.rect.right < 0:
            self.kill()
    
    def clone(self):
        print("New bird")
        return Bird()

class Cloud(GameSprite):
    def __init__(self):
        super(Cloud,self).__init__()
        self.surf = pygame.image.load("icons/cloud.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.height + 20, Screen.width + 100),
                random.randint(0, Screen.height),
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

    def clone(self):
        print("New cloud")
        return Cloud()
    
class Umbrella(GameSprite):
    Max_Speed_y = 10
    Min_Speed_y = 5
    
    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(0, Screen.width),
                0,
            )
        )
        self.speed = random.randint(self.Min_Speed_y, self.Max_Speed_y)
        self.time = 0

    def update(self):
        self.time += 1
        speed_x = 0
        speed_y = self.speed
        self.rect.move_ip(speed_x, speed_y)
        if self.rect.bottom < 0:
            self.kill()
    
    def clone(self):
        print("Umbrella Academy")
        return Umbrella()
    

class Mountain(GameSprite):
    def __init__(self):
        super(Mountain,self).__init__()
        self.surf = pygame.image.load("icons/mountain.png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                Screen.width,
                random.randint(Screen.height-50, Screen.height),
                
            )
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
 
    def clone(self):
        return Mountain()