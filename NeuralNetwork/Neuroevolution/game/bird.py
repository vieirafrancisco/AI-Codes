import pygame

from .settings import *

class Bird:
    def __init__(self, posy, color):
        self.posx = 100
        self.posy = posy
        self.color = color
        self.gravity = 0.4
        self.velocity = 0
        self.lift = -2
        self.rect = pygame.Rect(self.posx, self.posy, 20, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.velocity += self.lift
            print(self.rect.y, self.velocity)

        self.velocity += self.gravity
        self.velocity *= 0.9 
        self.rect.y += self.velocity

    def collide(self, pipe):
        offset_window = self.rect.y > HEIGHT or self.rect.y < 0
        if self.rect.colliderect(pipe.top_rect) or self.rect.colliderect(pipe.btn_rect) or offset_window:
            return True
        else:
            return False
