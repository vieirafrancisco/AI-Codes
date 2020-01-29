from resources.matrix import Matrix
from resources.functions import sigmoid

class MLP:
    def __init__(self, layers, learning_rate=0.1, epochs=100, verbose=False):
        self.layers = layers
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.verbose = verbose
        self.weights = [Matrix(y, x, True) for x, y in zip(layers[:-1], layers[1:])]
        self.bias = [Matrix(y, 1, True) for y in layers[1:]]

    def feedfoward(self, input_array):
        data = Matrix.from_array(input_array)
        for w, b in zip(self.weights, self.bias):
            data = Matrix.map(w * data + b, sigmoid)
        return data.to_array()

    def train(self, x_train, y_train):
        for epoch in range(self.epochs):
            for x, y in zip(x_train, y_train):
                output = self.feedfoward(x_train)

                ## compare output with de answer

                ## update weights and bias

        if self.verbose:
            pass


if __name__ == '__main__':
    mlp = MLP([3,4,2,2])
    print(mlp.feedfoward([1,2,3]))