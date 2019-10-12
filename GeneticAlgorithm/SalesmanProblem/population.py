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
        self.curr_best = None
        self.calculate_fitness()

    def init_orders(self):
        iter_orders = itertools.permutations(range(self.size))
        return [next(iter_orders) for _ in range(self.pop_size)]

    def calculate_fitness(self):
        total_fitness = 0
        for idx,order in enumerate(self.orders):
            fitness = 0
            for i1, i2 in zip(order[:-1], order[1:]):
                x0, y0 = self.elements[i1].pos
                x1, y1 = self.elements[i2].pos
                fitness += euclidian_distance(x0, y0, x1, y1)
            self.fitness[idx] = 1 / (fitness + 1)
            total_fitness += self.fitness[idx]
            if fitness < self.best[1]:
                self.best = (self.orders[idx], fitness)
            self.curr_best = self.orders[idx]
        
        for idx in range(self.pop_size):
            self.fitness[idx] /= total_fitness

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

    def cross_over(self, order_a, order_b):
        split_size = len(order_a)//2
        r = random.randint(0,1)
        if r == 0:
            new_order = list(order_a[:split_size])
            order = order_b
        else:
            new_order = list(order_b[:split_size])
            order = order_a
        for o_i in order:
            if o_i not in new_order:
                new_order.append(o_i)
        return tuple(new_order)

    def mutate(self, element):
        idx_x, idx_y = 0, 0
        while(idx_x == idx_y):
            idx_x = random.randint(0, len(element)-1)
            idx_y = random.randint(0, len(element)-1)
        return swap(element, idx_x, idx_y)

    def generate_new_population(self):
        new_population = []
        for _ in range(self.pop_size):
            order_a = self.make_selection()
            order_b = self.make_selection()
            new_order = self.cross_over(order_a, order_b) 
            new_order = self.mutate(new_order)
            new_population.append(new_order)
        for idx, order in enumerate(new_population):
            self.orders[idx] = order
        self.calculate_fitness()