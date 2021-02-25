# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 01:05:30 2021

@author: Tillmann Tristan Bosch
"""

import matplotlib.pyplot as plt
import numpy as np

import json
from math import log


if __name__ == "__main__":
    
    #read parameters.json    
    with open("data.json") as json_file:
        data = json.load(json_file)
        
    N = 1000
    cut = 1
    
    x_val = [log(x) for x in range(cut + 1, N + 1)]
    y_val = [log(x) for x in data["radius_list"][cut:]]
    lin = [1,2,3,4,5,6,7,8,9,10,11]
    
    param = np.polyfit(x_val, y_val, 1)
    
    plt.plot(x_val, y_val, "o")
    plt.plot(lin, [param[1] + param[0] * x for x in lin], color="red", linewidth = 2)
    plt.ylabel("ln(r(n))")
    plt.xlabel("ln(n), 800 < n <= 1000")
    
    plt.xlim([0, x_val[-1]])
    plt.ylim([0, y_val[-1]])
    
    plt.show()