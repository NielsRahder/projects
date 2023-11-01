import numpy as np
import sys 
import matplotlib 

inputs = [[1, 2, 3, 2.5], 
          [2.0, 5.0, -1.0, 2.0], 
          [-1.5, 2.7, 3.3, -0.8]]

#for each input there is a unique weight, but the bias is for each neuron specifically so it is only one

weights = [[0.2, 0.8, -0.5, 1.0 ], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

weights2 = [[0.1, -0.14, -0.5 ], 
           [-0.5, 0.12, -0.33], 
           [-0.44, 0.73, -0.13]]

biases2 = [-1, 2, -0.5]

layer1_ouputs = np.dot(inputs, np.array(weights).T) + biases #watch shape errors
layer2_ouputs = np.dot(layer1_ouputs, np.array(weights2).T) + biases2 #watch shape errors

print(layer2_ouputs)






 

