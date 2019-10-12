import random
import time

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
        self.population = Population(20, pop_size=100)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.display_surf.fill((0,0,0))
        self.population.draw(self.display_surf, self.population.curr_best, color=(255,255,255))
        self.population.draw(self.display_surf, self.population.best[0], (255,105,180), 6)

    def on_loop(self):
        self.population.make_mutation()

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()
        
            #time.sleep(1)

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False


if __name__ == '__main__':
    app = App()
    app.on_execute()