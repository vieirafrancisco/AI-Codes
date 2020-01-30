import random

from .resources.matrix import Matrix
from .resources.functions import sigmoid, dsigmoid, swap

class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.1, epochs=1000, verbose=False):
        self.layers = layers
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose
        self.weights = [Matrix(y, x, True) for x, y in zip(layers[:-1], layers[1:])]
        self.bias = [Matrix(y, 1, True) for y in layers[1:]]

    def feedfoward(self, input_array):
        data = Matrix.from_array(input_array)
        memo = [data]
        for w, b in zip(self.weights, self.bias):
            data = Matrix.map(w * data + b, sigmoid)
            memo.append(data)
        return memo, data

    def train(self, x_train, y_train):
        for epoch in range(self.epochs):
            x_train, y_train = self.randomize(x_train, y_train)
            for x, y in zip(x_train, y_train):
                memo, output = self.feedfoward(x)
                label = Matrix.from_array(y)
                error = label - output
                memo = memo[::-1]

                for h, a, w in zip(memo[1:], memo[:-1], self.weights[::-1]):
                    gradient = Matrix.multiply(error, Matrix.map(a, dsigmoid)) * self.learning_rate
                    delta_w = gradient * h.T
                    idx = self.weights.index(w)
                    self.weights[idx] += delta_w
                    self.bias[idx] += gradient
                    error = w.T * error

        if self.verbose:
            print(f"epoch {epoch}:")

    def randomize(self, x_train, y_train):
        idx1, idx2 = random.randint(0,len(x_train)-1), random.randint(0,len(x_train)-1)
        swap(x_train, idx1, idx2)
        swap(y_train, idx1, idx2)
        return x_train, y_train

if __name__ == '__main__':
    mlp = MLP([2,3,1])
    #print(mlp.feedfoward([1,2,3]))
    mlp.train([[1,0], [0,1], [0,0], [1,1]], [[1], [1], [0], [0]])
    _, result = mlp.feedfoward([1,1])
    print(result)