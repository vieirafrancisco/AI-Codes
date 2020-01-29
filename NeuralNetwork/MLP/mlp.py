from resources.matrix import Matrix
from resources.functions import sigmoid

class MLP:
    def __init__(self, layers, learning_rate=0.1):
        self.layers = layers
        self.learning_rate = learning_rate
        self.weights = [Matrix(y, x, True) for x, y in zip(layers[:-1], layers[1:])]
        self.bias = [Matrix(y, 1, True) for y in layers[1:]]

    def feedfoward(self, input_array):
        input = Matrix.from_array(input_array)
        for w, b in zip(self.weights, self.bias):
            input = Matrix.map(w * input + b, sigmoid)
        return input


if __name__ == '__main__':
    mlp = MLP([3,4,2,2])
    print(mlp.feedfoward([1,2,3]))