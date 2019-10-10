import random
import math
import itertools

import pygame

from ball import Ball
from settings import *

def euclidian_distance(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

def swap(arr, x, y):
    temp_arr = [i for i in arr]
    aux = temp_arr[x]
    temp_arr[x] = temp_arr[y]
    temp_arr[y] = aux
    return tuple(temp_arr)

class Population:

    def __init__(self, size, pop_size=100):
        self.size = size
        self.pop_size = pop_size
        self.elements = [Ball(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT)) for _ in range(size)]
        self.orders = self.init_orders()
        self.fitness = pop_size*[0]
        self.best = None
        self.calculate_fitness()

    def init_orders(self):
        iter_orders = itertools.permutations(range(self.size))
        return [next(iter_orders) for _ in range(self.pop_size)]

    def calculate_fitness(self):
        m = 0
        max_index = 0
        for idx,order in enumerate(self.orders):
            fitness = 0
            for i1, i2 in zip(order[:-1], order[1:]):
                x0, y0 = self.elements[i1].pos
                x1, y1 = self.elements[i2].pos
                fitness += euclidian_distance(x0, y0, x1, y1)
            self.fitness[idx] = fitness
            if fitness > m:
                m = fitness
                max_idx = idx
        self.best = self.orders[max_idx]

    def draw_best_order(self, surface):
        for idx in self.best:
            self.elements[idx].draw(surface)

        for i1, i2 in zip(self.best[:-1], self.best[1:]):
            pygame.draw.line(surface, (255,105,180), self.elements[i1].pos, self.elements[i2].pos, 4)

    def make_selection(self):
        m1, m2, max_idx1, max_idx2 = 0,0,0,0
        for idx, fitness in enumerate(self.fitness):
            if fitness > m1:
                m2 = m1
                max_idx2 = max_idx1
                m1 = fitness
                max_idx1 = idx
        return (self.orders[max_idx1], self.orders[max_idx2])

    def make_mutation(self):
        parents = self.make_selection()
        s = set()
        s.add(parents[0])
        s.add(parents[1])

        while(len(s) < self.pop_size):
            print(len(s), self.pop_size)
            p_idx = random.randint(0,1)
            order = parents[p_idx]
            x, y = 0, 0
            while(x == y):
                x, y = random.randint(0,self.size-1), random.randint(0,self.size-1)
            order = swap(order, x, y)
            s.add(order)

        self.calculate_fitness()