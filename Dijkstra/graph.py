import random
import math

import numpy as np

from city import City
from dijkstra import dijkstra
from settings import *

def get_path(origin, target_idx, source_idx):
    path = [target_idx]
    u = origin[target_idx]
    while(True):
        path.append(u)
        if u == source_idx: break
        u = origin[u]
    return path

def get_random_position(offset=0):
    return (random.randint(offset, WIN_SHAPE[i]-offset) for i in range(2))

def euclidian_distance(x0, y0, x1, y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

def midpoint(x0, y0, x1, y1):
    return ((x0+x1)/2, (y0+y1)/2)

class Graph:

    def __init__(self, source, target, num_cities, adjacences):
        self.source = source
        self.target = target
        self.num_cities = num_cities
        self.adjacences = adjacences
        self.dist = np.zeros((num_cities, num_cities))
        self.dijkstra = dijkstra(source, num_cities, adjacences)
        self.cities = [City(i, *get_random_position(50), self.dijkstra[0][i]) for i in range(num_cities)]
    
    def draw(self, surface):
        for i in self.adjacences:
            for v in self.adjacences[i]:
                pygame.draw.line(surface, (150,150,150), self.cities[i].pos, self.cities[v[1]].pos, 4)
                text = pygame.font.Font(None, 30).render(str(v[0]), False, (125,255,125))
                surface.blit(text, midpoint(*self.cities[i].pos, *self.cities[v[1]].pos))

        path = get_path(self.dijkstra[1], self.target, self.source)
        for i, j in zip(path[:-1], path[1:]):
          pygame.draw.line(surface, (0,0,150), self.cities[i].pos, self.cities[j].pos, 4)

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