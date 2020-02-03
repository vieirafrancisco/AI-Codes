import pygame

from .settings import *

from network.network import NeuralNetwork

class Bird:
    def __init__(self, color, nn=None):
        self.posx = 100
        self.posy = HEIGHT/2
        self.color = color
        self.gravity = 0.4
        self.velocity = 0
        self.lift = -1.8
        self.rect = pygame.Rect(self.posx, self.posy, 20, 20)
        self.score = 0
        self.fitness = 0
        if nn: 
            self.nn = nn
        else: 
            self.nn = NeuralNetwork([2, 6, 1])

    @staticmethod
    def cross_over(b1, b2):
        return Bird(b1.color, NeuralNetwork.cross_over(b1.nn, b2.nn))

    @staticmethod
    def mutate(b1):
        return Bird(b1.color, NeuralNetwork.mutate(b1.nn))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def update(self, pipe):
        input_array = self.get_distances(pipe)
        output = self.nn.feedfoward(input_array)

        if output[0] > 0.5:
            self.velocity += self.lift
            #print(self.rect.y, self.velocity)
        
        '''
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.velocity += self.lift
        '''

        self.velocity += self.gravity
        self.velocity *= 0.9 
        self.rect.y += self.velocity

    def collide(self, pipe):
        offset_window = self.rect.y > HEIGHT or self.rect.y < 0
        if self.rect.colliderect(pipe.top_rect) or self.rect.colliderect(pipe.btn_rect) or offset_window:
            return True
        else:
            return False

    def is_score(self, pipe):
        if self.rect.x == pipe.top_rect.x + pipe.width//2:
            return True
        else:
            return False

    def get_distances(self, pipe):
        x = pipe.top_rect.x - self.rect.x
        y = pipe.top_rect.y + pipe.height - self.rect.y
        if x+y == 0: s = 1
        else: s = x+y
        return [x/s, y/s]