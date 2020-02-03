import random

import pygame

from .settings import *

class Pipe:
    def __init__(self, posx):
        self.speed = -1
        self.posx = posx
        self.space = 80
        self.width = 5
        self.height = random.randint(HEIGHT/5, 4*HEIGHT/5 - 10)
        self.top_rect = pygame.Rect(self.posx, 0, self.width, self.height)
        self.btn_rect = pygame.Rect(self.posx, self.height + self.space, self.width, HEIGHT)
        self.rects = [self.top_rect,  self.btn_rect]

    def draw(self, surface):
        pygame.draw.rect(surface, (0,125,0), self.top_rect)
        pygame.draw.rect(surface,  (0,125,0), self.btn_rect)

    def update(self):
        for rect in self.rects:
            rect.x += self.speed
            if rect.x + self.width < 0:
                rect.x = WIDTH
                randy = random.randint(HEIGHT/5, 4*HEIGHT/5 - 10)
                self.top_rect.height = randy
                self.btn_rect.y = randy + self.space

