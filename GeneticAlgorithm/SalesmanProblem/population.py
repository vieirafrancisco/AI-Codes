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

def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)*n

class Population:

    def __init__(self, size, pop_size=100):
        self.size = size
        self.pop_size = min(pop_size, factorial(size))
        self.elements = [Ball(random.randint(0, WIN_WIDTH), random.randint(0, WIN_HEIGHT)) for _ in range(size)]
        self.orders = self.init_orders()
        self.fitness = pop_size*[0]
        self.best = (0, INF)
        self.curr_order = None
        self.calculate_fitness()

    def init_orders(self):
        iter_orders = itertools.permutations(range(self.size))
        return [next(iter_orders) for _ in range(self.pop_size)]

    def calculate_fitness(self):
        m, total_fitness = INF, 0
        min_idx = 0
        for idx,order in enumerate(self.orders):
            fitness = 0
            for i1, i2 in zip(order[:-1], order[1:]):
                x0, y0 = self.elements[i1].pos
                x1, y1 = self.elements[i2].pos
                fitness += euclidian_distance(x0, y0, x1, y1)
            self.fitness[idx] = fitness
            total_fitness += fitness
            if fitness < m:
                m = fitness
                min_idx = idx
        for idx in range(self.pop_size):
            self.fitness[idx] /= total_fitness
            self.fitness[idx] = 1-self.fitness[idx]
        if self.fitness[min_idx] < self.best[1]:
            self.best = (self.orders[min_idx], self.fitness[min_idx])
        self.curr_order = self.orders[min_idx]
        print(self.fitness)

    def draw(self, surface, order, color=(0,125,0), line_width=1):
        tmp_order = order
        for idx in tmp_order:
            self.elements[idx].draw(surface)

        for i1, i2 in zip(tmp_order[:-1], tmp_order[1:]):
            pygame.draw.line(surface, color, self.elements[i1].pos, self.elements[i2].pos, line_width)

    def make_selection(self):
        idx = 0
        r = random.random()
        while(r > 0):
            r -= self.fitness[idx]
            idx+=1
        idx-=1
        return self.orders[idx]

    def make_mutation(self):
        new_population = []
        for _ in range(self.pop_size):
            order = self.make_selection()
            order = self.mutate(order)
            new_population.append(order)
        for idx, element in enumerate(new_population):
            self.orders[idx] = element
        self.calculate_fitness()

    def mutate(self, element):
        idx_x, idx_y = 0, 0
        while(idx_x == idx_y):
            idx_x = random.randint(0, len(element)-1)
            idx_y = random.randint(0, len(element)-1)
        return swap(element, idx_x, idx_y)