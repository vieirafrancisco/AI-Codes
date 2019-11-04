import pygame

from settings import *

class City:

    def __init__(self, label, pos_x, pos_y, dist, radius=20, color=(255,255,255)):
        self.label = label
        self.pos = self.pos_x, self.pos_y = pos_x, pos_y
        self.radius = radius
        self.color = color
        self.dist = dist
        self.text = pygame.font.Font(None, 30).render(str(label), False, (0,0,0))
        if dist == INF:
            self.dist_text = pygame.font.Font(None, 30).render("INF", False, (255,255,255))
        else:
            self.dist_text = pygame.font.Font(None, 30).render(str(dist), False, (255,255,255))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.pos_x, self.pos_y), self.radius)
        surface.blit(self.text, (self.pos_x - self.radius//2, self.pos_y - self.radius//2))
        surface.blit(self.dist_text, (self.pos_x - self.radius//2, self.pos_y - self.radius - 20))