import pygame
import random
import math
from pygame.locals import RLEACCEL

from screen import Screen


# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite):   
        super(sprite, self).__init__()
        
    def clone(self):
        pass


class Bird(GameSprite):
    Max_Speed = 10
    Min_Speed = 5
    def __init__(self):
        super().__init__(Bird)