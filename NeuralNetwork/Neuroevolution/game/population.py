import random

from game.settings import *
from game.bird import Bird

class Population:
    def __init__(self, num_ind):
        self.num_ind = num_ind
        self.birds = [Bird(COLORS[random.randint(0, 3)]) for i in range(num_ind)]
        self.fitness_list = [0 for _ in range(num_ind)]

    def new_pop(self):
        b1, b2 = self.selection()
        b1.score, b2.score = 0, 0
        new_birds = [b1, b2]
        for i in range(self.num_ind - 2):
            new_bird = Bird.cross_over(b1,b2)
            new_birds.append(Bird.mutate(new_bird))
        self.birds = new_birds
        return self.birds

    def selection(self):
        parents = [(0, None), (0, None)]
        for idx, bird in enumerate(self.birds):
            self.fitness_list[idx] = bird.fitness
            if bird.fitness >= parents[1][0]:
                if parents[1][1] == None:
                    parents[1] = (bird.fitness, bird)
                else:
                    parents[0] = parents[1]
                    parents[1] = (bird.fitness, bird)
        parents[0][1].fitness, parents[1][1].fitness = 0, 0 
        return (parents[0][1], parents[1][1])