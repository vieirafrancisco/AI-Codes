import random
import math

import numpy as np

from city import City
from dijkstra import dijkstra
from settings import *

def get_random_position(offset=0):
    return (random.randint(offset, WIN_SHAPE[i]-offset) for i in range(2))

def euclidian_distance(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

class Graph:

    def __init__(self, source, target, num_cities, adjacences):
        self.source = source
        self.target = target
        self.num_cities = num_cities
        self.adjacences = adjacences
        self.cities = [City(*get_random_position(50)) for _ in range(num_cities)]
        self.dist = np.zeros((num_cities, num_cities))
        self.dijkstra = dijkstra(source, target, num_cities, adjacences)
    
    def draw(self, surface):
        for i in self.adjacences:
            for v in self.adjacences[i]:
                pygame.draw.line(surface, (150,150,150), self.cities[i].pos, self.cities[v[1]].pos, 2)

        u = self.dijkstra[1][self.target]
        while(u != self.source):
            pygame.draw.line(surface, (125,125,255), self.cities[self.target].pos, self.cities[u].pos, 6)
            v = u
            u = self.dijkstra[1][u]
        pygame.draw.line(surface, (125,125,255), self.cities[v].pos, self.cities[self.source].pos, 6)

        for idx, city in enumerate(self.cities):
            if idx == self.source: city.color=(200,0,0)
            if idx == self.target: city.color=(0,0,200)
            city.draw(surface)

    def store_distances(self):
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                x0, y0 = self.cities[i].pos
                x1, y1 = self.cities[j].pos
                if(not (np.any(self.dist[i]) or np.any(self.dist[j])) or random.uniform(0, 1) > 0.8):
                    self.dist[i][j] = euclidian_distance(x0, y0, x1, y1)


