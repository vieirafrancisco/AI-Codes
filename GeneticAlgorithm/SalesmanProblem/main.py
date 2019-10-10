import random

import pygame

from ball import Ball
from population import Population
from settings import *

class App:

    def __init__(self):
        self.size = self.width, self.height = WIN_WIDTH, WIN_HEIGHT
        self.running = False
        self.display_surf = None

    def on_init(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode(self.size)
        self.population = [Ball(random.randint(0,self.width), random.randint(0,self.height)) for i in range(20)]
        self.pop = Population(10, pop_size=100)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        for element in self.population:
            element.draw(self.display_surf)

        for e1, e2 in zip(self.population[:-1], self.population[1:]):
            pygame.draw.line(self.display_surf, (0,125,0), e1.pos, e2.pos)

    def on_loop(self):
        pass

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False


if __name__ == '__main__':
    app = App()
    app.on_execute()