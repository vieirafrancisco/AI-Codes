import random

import pygame

from graph import Graph
from dijkstra import dijkstra
from settings import *

def user_input():
    input_lines = []
    with open("in.txt", "r") as f:
        input_lines = f.readlines()
    n, m, s, t = map(int, input_lines[0].split())
    graph = {}
    for i in range(1, m+1):
        u, v, c = map(int, input_lines[i].split())
        if u not in graph.keys(): graph[u] = []
        if v not in graph.keys(): graph[v] = []
        graph[u].append((c, v))
        graph[v].append((c, u))
    return s, t, n, graph

class App:

    def __init__(self):
        self.size = self.width, self.height = WIDTH, HEIGHT
        self.running = False
        self.display_surf = None

    def on_init(self):
        pygame.init()
        self.running = True
        self.display_surf = pygame.display.set_mode(self.size)
        self.graph = Graph(*user_input())

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.graph.draw(self.display_surf)

    def on_loop(self):
        pass

    def on_execute(self):
        self.on_init()

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()

        self.on_cleanup()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False


if __name__ == '__main__':
    app = App()
    app.on_execute()