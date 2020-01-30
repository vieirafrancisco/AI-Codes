import os

import pygame

from .settings import *
from .bird import Bird
from .bar import Bar

class Game:
    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Flappy Bird")
        self.bird = Bird(HEIGHT/2, (255,255,255))
        self.bar1 = Bar(2*WIDTH/3)
        self.bar2 = Bar(2*WIDTH/3 + 230)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.bird.draw(self._disp_window)
        self.bar1.draw(self._disp_window)
        self.bar2.draw(self._disp_window)

    def on_loop(self):
        self.bar1.update()
        self.bar2.update()
        self.bird.update()

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self._disp_window.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            self.clock.tick(60)

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False