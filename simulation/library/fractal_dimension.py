# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:08:41 2021

@author: Tillmann Tristan Bosch
"""

from numpy import polyfit
from math import log

def fractal_dimension_approximation_1(particles, ratio_range = [0,1], number_of_values = 200):
    radius = max([abs(x + y*1j) for x,y in particles])
    
    if ratio_range[0] >= ratio_range[1]:
        return {"alpha": 0, "lnc": 0}
    
    else:
        min_radius, max_radius = ratio_range[0] * radius, ratio_range[1] * radius
        delta = (max_radius - min_radius) / (number_of_values + 1)
        
        radius_list = []
        cardinal_list = []
        
        radius_value = min_radius
        while radius_value < max_radius:
            radius_list.append(radius_value)
            cardinal = 0
            for x,y in particles:
                if abs(x + y*1j) < radius_value:
                    cardinal += 1
            cardinal_list.append(cardinal)
            
            radius_value += delta
            
        x_list = [log(x) for x in cardinal_list]
        y_list = [log(x) for x in radius_list]
        
        if len(x_list) > 0:
            params = polyfit(x_list, y_list, 1)
            return {"alpha": params[0], "lnc": params[1]}
        else:
            return {"alpha": 0, "lnc": 0}

            
    
        
    