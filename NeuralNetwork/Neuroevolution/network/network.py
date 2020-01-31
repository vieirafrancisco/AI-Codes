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

if __name__ == '__main__':
    pass