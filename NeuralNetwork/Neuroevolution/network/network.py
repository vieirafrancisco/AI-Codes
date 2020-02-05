import random

from .resources.matrix import Matrix
from .resources.functions import sigmoid, swap

class NeuralNetwork:
    def __init__(self, layers):
        self.layers = layers
        self.weights = [Matrix(y, x, True) for x, y in zip(layers[:-1], layers[1:])]
        self.bias = [Matrix(y, 1, True) for y in layers[1:]]

    def feedfoward(self, input_array):
        data = Matrix.from_array(input_array)
        for w, b in zip(self.weights, self.bias):
            data = Matrix.map(w * data + b, sigmoid)
        return data.to_array()

    def copy(self):
        nn = NeuralNetwork(self.layers)
        for idx, w in enumerate(self.weights):
            nn.weights[idx] = w.copy()
        for idx, b in enumerate(self.bias):
            nn.bias[idx] = b.copy()
        return nn

    @staticmethod
    def cross_over(n1, n2):
        nn = NeuralNetwork(n1.layers)
        ## crossover weights
        for k, w in enumerate(nn.weights):
            for i in range(w.rows):
                for j in range(w.cols):
                    if j%2 == 0:
                        nn.weights[k].matrix[i][j] = n1.weights[k].matrix[i][j]
                    else:
                        nn.weights[k].matrix[i][j] = n2.weights[k].matrix[i][j]
        # crossover bias
        for k, b in enumerate(nn.bias):
            for i in range(b.rows):
                if i%2 == 0:
                    nn.bias[k].matrix[i][0] = n1.bias[k].matrix[i][0]
                else:
                    nn.bias[k].matrix[i][0] = n2.bias[k].matrix[i][0]
        return nn

    @staticmethod
    def mutate(n1, rate):
        nn = n1.copy()
        for idx, w in enumerate(nn.weights):
            r = random.random()
            if r < rate:
                i = random.randint(0, w.rows-1)
                j = random.randint(0, w.cols-1)
                nn.weights[idx].matrix[i][j] = random.random() * 2 - 1
        for idx, b in enumerate(nn.bias):
            r = random.random()
            if r < rate:
                i = random.randint(0, b.rows-1)
                nn.bias[idx].matrix[i][0] = random.random() * 2 - 1
        return nn


if __name__ == '__main__':
    pass