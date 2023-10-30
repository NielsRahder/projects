url = " https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3"

import numpy as np
import sys 
import matplotlib 

print("python", sys.version)
print("Numpy", np.__version__)
print("matplotlib:", matplotlib.__version__)

inputs = [1, 2, 3, 2.5]

#for each input there is a unique weight, but the bias is for each neuron specifically so it is only one

weights = [[0.2, 0.8, -0.5, 1.0 ], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87 ]]

biases = [2, 3, 0.5]

output = np.dot(weights, inputs ) + biases #weights should come first in order to prevent a shape error

print("this is dot prod output:", output)


layer_outputs = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 
    for n_input, weight in zip (inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)


 

