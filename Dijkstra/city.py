import pygame

from settings import *

class City:

    def __init__(self, pos_x, pos_y, radius=8, color=(255,255,255)):
        self.pos = self.pos_x, self.pos_y = pos_x, pos_y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radius)