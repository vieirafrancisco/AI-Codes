import random

from game.settings import *
from game.bird import Bird

class Population:
    def __init__(self, num_ind):
        self.num_ind = num_ind
        self.birds = [Bird(COLORS[random.randint(0, 3)]) for i in range(num_ind)]
        self.fitness_list = [0 for _ in range(num_ind)]

    def new_pop(self):
        b1 = self.selection()
        b1.score = 0
        new_birds = []
        #new_bird = Bird.cross_over(b1,b2)
        for i in range(self.num_ind):
            new_birds.append(Bird.mutate(b1))
        self.birds = new_birds
        return self.birds

    def selection(self):
        parent = (0, None)
        for idx, bird in enumerate(self.birds):
            self.fitness_list[idx] = bird.fitness
            if bird.fitness >= parent[0]:
                parent = (bird.fitness, bird)
        best_bird = parent[1]
        best_bird.fitness = 0
        return best_bird