import random

from game.settings import *
from game.bird import Bird

class Population:
    def __init__(self, num_ind):
        self.num_ind = num_ind
        self.num_mutation = num_ind//2
        self.birds = [Bird(COLORS[random.randint(0, 3)]) for i in range(num_ind)]
        self.fitness_list = [(idx, 0) for idx,_ in enumerate(range(num_ind))]

    def new_pop(self):
        self.fitness_list = [(idx, bird.fitness) for idx, bird in enumerate(self.birds)]
        for bird in self.birds:
            bird.fitness = 0
            bird.score = 0
        birds = self.selection()
        new_birds = [bird for bird, _ in birds]
        for bird, rate in birds:
            new_birds.append(Bird.mutate(bird, rate))
        self.birds = new_birds
        #print(birds[30][0].nn.weights)
        #print(new_birds[self.num_mutation+30].nn.weights)
        return self.birds

    def selection(self):
        ordered_fitness = sorted(self.fitness_list, key=lambda x: x[0], reverse=True)
        mutate_fitness = ordered_fitness[:self.num_mutation]
        fitness = [fitness for _, fitness in mutate_fitness]
        max_v = max(fitness)
        min_v = min(fitness)

        prob_mutation = [(self.birds[idx], (max_v-fitness)/(max_v-min_v)) for idx, fitness in mutate_fitness]
        #print([[fitness, (max_v-fitness)/(max_v-min_v)] for idx, fitness in mutate_fitness])
        return prob_mutation