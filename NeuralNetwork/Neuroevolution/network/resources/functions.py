import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dsigmoid(y):
    return y * (1 - y)

def relu(x):
    if x < 0:
        return 0
    else:
        return x

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]