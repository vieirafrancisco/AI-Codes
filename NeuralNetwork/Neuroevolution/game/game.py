import os
import random

import pygame

from game.settings import *
from game.population import Population
from game.bird import Bird
from game.pipe import Pipe
from network.network import NeuralNetwork

class Game:
    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()
        self.high_score = 0
        self.score = 0
        self.generation = 1
        self.population = Population(200)
        self.birds = self.population.birds

    def start_objects(self):
        self.high_score = max(self.high_score, self.score)
        self.score = 0
        self.distance = 0
        self.pipes = [Pipe(WIDTH + i*230) for i in range(2)]
        self.pipe = self.pipes[0]
        self.birds_dead = [0 for _ in self.birds]
        for bird in self.birds:
            bird.alive = True

    def on_init(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 20)
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Flappy Bird")
        self.start_objects()

    def on_cleanup(self):
        pygame.quit()
        pygame.font.quit()

    def on_render(self):
        for bird in self.birds:
            bird.draw(self._disp_window)
        for pipe in self.pipes:
            pipe.draw(self._disp_window)
        self._disp_window.blit(self.font.render(f"Highscore: {self.high_score}", True, (255,255,255)), (0,0))
        self._disp_window.blit(self.font.render(f"Score: {self.score}", True, (255,255,255)), (0,20))
        self._disp_window.blit(self.font.render(f"Generation: {self.generation}", True, (255,255,255)), (0,40))

    def on_loop(self):
        self.distance += 1

        for idx, pipe in enumerate(self.pipes):
            pipe.update()
            if pipe.top_rect.x + pipe.width - 100 == 0:
                self.pipe = self.pipes[1-idx]
            print(self.pipe)

        for idx, bird in enumerate(self.birds):
            if bird.collide(self.pipe):
                self.birds_dead[idx] = 1
                bird.alive = False
                bird.fitness += self.distance
            if bird.is_score(self.pipe):
                bird.score += 1
                bird.fitness += 5000
                self.score = max(self.score, bird.score)
            bird.update(self.pipe)

        if all(self.birds_dead):
            self.birds = self.population.new_pop()
            print(self.population.fitness_list)
            self.generation += 1
            self.start_objects()

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