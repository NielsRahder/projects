url = " https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3"

import numpy as np
import sys 
import matplotlib 

print("python", sys.version)
print("Numpy", np.__version__)
print("matplotlib:", matplotlib.__version__)

inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7] #for each input there is a unique weight
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)