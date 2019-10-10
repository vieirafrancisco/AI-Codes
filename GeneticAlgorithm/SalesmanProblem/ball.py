import pygame

class Ball:
    
    def __init__(self, pos_x, pos_y, radius=8, color=(0,125,0)):
        self.pos = self.pos_x, self.pos_y = pos_x, pos_y
        self.radius = radius
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radius)