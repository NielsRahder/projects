import numpy as np
import sys 
import matplotlib 

np.random.seed(0)

X = [[1, 2, 3, 2.5], 
    [2.0, 5.0, -1.0, 2.0], 
    [-1.5, 2.7, 3.3, -0.8]]

class Layer_Dense:
    def __init__ (self, n_inputs, n_neurons):
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

Layer_1 = Layer_Dense(4, 5 )
Layer_2 = Layer_Dense(5, 5 ) #input needs to be output from previous layer


Layer_1.forward(X)
print(Layer_1.output)
Layer_2.forward(Layer_1.output)
print(Layer_2.output)