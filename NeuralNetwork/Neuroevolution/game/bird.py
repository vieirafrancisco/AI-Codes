import pygame

from .settings import *

class Bird:
    def __init__(self, posy, color):
        self.posx = 100
        self.posy = posy
        self.color = color
        self.gravity = 0.3
        self.velocity = 0
        self.lift = -1

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.posx, self.posy, 20, 20))

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.velocity += self.lift
            print(self.posy, self.velocity)

        self.velocity += self.gravity
        self.velocity *= 0.9 
        self.posy += self.velocity

        if self.posy > HEIGHT:
            self.velocity = 0
            self.posy = HEIGHT/2
        if self.posy < 0:
            self.velocity = 0
            self.posy = 0
