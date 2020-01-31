import os

import pygame

from .settings import *
from .bird import Bird
from .pipe import Pipe

class Game:
    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()
        self.high_score = 0
        self.score = 0

    def start_objects(self):
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.bird = Bird(HEIGHT/2, (255,255,255))
        self.pipes = [Pipe(WIDTH + i*230) for i in range(2)]
        self.font = pygame.font.Font(None, 20)

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Flappy Bird")
        self.start_objects()

    def on_cleanup(self):
        pygame.quit()
        pygame.font.quit()

    def on_render(self):
        self.bird.draw(self._disp_window)
        for pipe in self.pipes:
            pipe.draw(self._disp_window)
        self._disp_window.blit(self.font.render(f"Highscore: {self.high_score}", True, (255,255,255)), (0,0))
        self._disp_window.blit(self.font.render(f"Score: {self.score}", True, (255,255,255)), (0,20))

    def on_loop(self):
        self.bird.update()
        for pipe in self.pipes:
            if self.bird.collide(pipe):
                self.start_objects()
            pipe.update()

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