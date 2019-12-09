import random

import numpy as np
import matplotlib.pyplot as plt

def euclidian_distance(a, b):
    return np.linalg.norm(a-b)

def gaussian(x, mu=0, sig=1):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

class SOM:

    def __init__(self, num_clusters, array, num_iterations=100, learning_rate=0.01, verbose=False):
        self.num_clusters = num_clusters
        self.array = np.array(array)
        self.num_iterations = num_iterations
        self.learning_rate = learning_rate
        self.verbose = verbose
        self.weights = np.random.rand(num_clusters, self.array.shape[1])

    def train(self):
        s = 0
        while(s < self.num_iterations):
            for idx, input_i in enumerate(self.array):
                nodes = [euclidian_distance(input_i, weight) for weight in self.weights]
                bmu_idx = nodes.index(min(nodes))
                for j in range(self.num_clusters):
                    for i in range(self.array.shape[1]):
                        theta = euclidian_distance(self.array[bmu_idx], self.weights[j])
                        #print(self.weights[j][i], theta, self.learning_rate, (self.array[idx][i] - self.weights[j][i]))
                        self.weights[j][i] = self.weights[j][i] + theta * self.learning_rate * (self.array[idx][i] - self.weights[j][i])
            if self.verbose:
                print(f"Epoch: {s}")
                print(self.weights)
            s += 1

    def predict(self, input_x):
        print(input_x, self.weights)
        nodes = [euclidian_distance(input_x, weight) for weight in self.weights]
        print(nodes)
        return nodes.index(min(nodes))

if __name__ == '__main__':
    arr = np.array([[2,3],[2,4],[4,5], [4,6], [7,8],[9,1], [9,4], [87,75],[70,56],[50,88], [90, 67]])
    #arr = arr / np.linalg.norm(arr)
    #for x, y in arr:
        #plt.scatter(x, y, c='b')
    #plt.show()
    net = SOM(2, arr, num_iterations=20, learning_rate=0.001, verbose=False)
    net.train()
    y1 = net.predict([8,10])
    y2 = net.predict([90,88])
    print(y1, y2)