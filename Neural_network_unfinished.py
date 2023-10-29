url = " https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3"

import numpy as np
import sys 
import matplotlib 

print("python", sys.version)
print("Numpy", np.__version__)
print("matplotlib:", matplotlib.__version__)

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0 ] #for each input there is a unique weight, but the bias is for each neuron specifically so it is only one
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87 ]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] +  inputs[3] * weights1[3] + bias1, 
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] +  inputs[3] * weights2[3] + bias2, 
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] +  inputs[3] * weights3[3] + bias3] #with using this we are essentially modelling 3 seperate neurons with each 4 inputs, each neuron still has only one bias (so 3 in total)

print(output)

