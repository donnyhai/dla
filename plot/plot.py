# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 01:05:30 2021

@author: Tillmann Tristan Bosch
"""

import matplotlib.pyplot as plt
import numpy as np

import json
from math import log

import fractal_dimension as fd


if __name__ == "__main__":
    
    
    #read parameters.json    
    with open("data19.json") as json_file:
        data = json.load(json_file)
    
    """
    N = 1000
    cut = 1
    
    x_val = [log(x) for x in range(cut + 1, N + 1)]
    y_val = [log(x) for x in data["radius_list"][cut:]]
    
    param = np.polyfit(x_val, y_val, 1)
    """
    
    fda = fd.fractal_dimension_approximation_1(data["particles"], [1/6, 4/6])
    print(fda)
    lin = [1,2,3,4,5,6,7,8,9,10,11]
    
    x_list = fda["x_list"]
    y_list = fda["y_list"]
    params = fda["parameters"]
    
    plt.plot(x_list, y_list, "o")
    plt.plot(lin, [params[1] + params[0] * x for x in lin], color="red", linewidth = 2)
    plt.ylabel("ln(r(n))")
    plt.xlabel("ln(n), 800 < n <= 1000")
    
    plt.xlim([x_list[0] - 1, x_list[-1]])
    plt.ylim([y_list[0] - 1, y_list[-1]])
    
    plt.show()
    
    print(1/fda["parameters"][0])