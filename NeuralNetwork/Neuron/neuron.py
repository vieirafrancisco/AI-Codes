import random

import numpy as np

def limiar(x):
    if x > 0:
        return 1
    return -1

class Neuron:
    def __init__(self, learning_rate=0.01, epochs=100, verbose=False):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose

    def train(self, X, y):
        self.input = np.array(X)
        self.weights = [random.uniform(-1,1) for i in range(X.shape[1])]
    
        i = 0
        while(i < self.epochs):
            prediction = self.feedfoward(self.input, self.weights)
            error = 0
            for answer, guess, input_X in zip(y, prediction, self.input):
                if answer != guess:
                    error += 1
                    for idx in range(len(self.weights)):
                        self.weights[idx] += (answer - guess) * input_X[idx] * self.learning_rate 
            if self.verbose:
                print(f"error: {error/len(y)}")
            if error == 0: break
            i += 1

    def feedfoward(self, a, w):
        return np.array([limiar(s) for s in np.dot(a, w)])


if __name__ == '__main__':
    n = Neuron(learning_rate=0.001, epochs=10, verbose=True)
    X = np.array([[1,30,50],[1,20,33],[1,55,35], [1,2,3], [1,6,7], [1, 8, 2]])
    y = [1, 1, 1, -1, -1, -1]
    n.train(X, y)