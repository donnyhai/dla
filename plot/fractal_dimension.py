# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:08:41 2021

@author: Tillmann Tristan Bosch
"""

from numpy import polyfit
from math import log

#try to approximate "full" fractal dimension
def fractal_dimension_approximation_1(particles, ratio_range = [0,1]):
    radius = max([abs(x + y*1j) for x,y in particles])
    
    if ratio_range[0] >= ratio_range[1]:
        return {"parameters": (0,0),
                "x_list": [], 
                "y_list": []}
    
    else:
        min_radius, max_radius = ratio_range[0] * radius, ratio_range[1] * radius
        
        radius_list, cardinal_list = [], []
        
        radius_value = min_radius
        while radius_value < max_radius:
            radius_list.append(radius_value)
            cardinal_list.append(len([(x,y) for (x,y) in particles if abs(x + y*1j) < radius_value]))
            radius_value += 1
            
        x_list = [log(x) for x in cardinal_list]
        y_list = [log(x) for x in radius_list]
        
        if len(x_list) > 0:
            return {"parameters":   polyfit(x_list, y_list, 1),
                    "x_list":       x_list, 
                    "y_list":       y_list}
        else:
            return {"parameters": (0,0),
                    "x_list": [], 
                    "y_list": []}
                    

            
    
        
    