import random

import pygame

from .settings import *

class Bar:
    def __init__(self, posx):
        self.rand_h = random.randint(HEIGHT/5, 4*HEIGHT/5 - 10)
        self.speed = -1
        self.posx = posx
        self.width = 35

    def draw(self, surface):
        pygame.draw.rect(surface, (255,255,255), (self.posx, 0, self.width, self.rand_h))
        pygame.draw.rect(surface, (255,255,255), (self.posx, self.rand_h + 80, self.width, HEIGHT))

    def update(self):
        self.posx += self.speed
        if self.posx + self.width < 0:
            self.posx = WIDTH
            self.rand_h = random.randint(HEIGHT/5, 4*HEIGHT/5 - 10)

