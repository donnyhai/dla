# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 01:05:30 2021

@author: Tillmann Tristan Bosch
"""
import matplotlib.pyplot as plt
import numpy as np
import json
from math import log
import pygame
import fractal_dimension as fd
def convert_hex_to_vector(hexa):
    def hex_to_int(letter):
        return int(letter, 16)
    r = 16 * hex_to_int(hexa[0]) + hex_to_int(hexa[1])
    g = 16 * hex_to_int(hexa[2]) + hex_to_int(hexa[3])
    b = 16 * hex_to_int(hexa[4]) + hex_to_int(hexa[5])
    return (r,g,b)

if __name__ == "__main__":
    
    infoname = "2021_03_04_18_00_18__information_lha_50000"
    
    
    #read parameters.json    
    with open(infoname + ".json") as json_file:
        data = json.load(json_file)
        
    #create_pygame_image(data)
    
    newdata = {"time":                         data["time"],
            "runtime":                      data["runtime"],
            "linear_reg_parameters":        data["linear_reg_parameters"],
            "last_fractal_dimension_value": data["last_fractal_dimension_value"],
            "volumina_ratio":               fd.volumina_ratio(data["particles"], [0.2, 0.75]),
            "particles":                    data["particles"]}
    
    f = open(infoname + ".json", "w+")
    json.dump(newdata, f)
    f.close()
    
    
    
    
    
    
    
    """
    y_val = [1.8601, 1.8679,
              1.9135, 1.9273,
              1.9071, 1.9191,
              1.9518, 1.9173,
              1.9311, 1.9381,
              1.9283, 1.9187,
              1.9257, 1.9184,
              1.9135, 1.9463,
              1.9420, 1.9344,
              1.9065, 1.9344]
    x_val = [10000, 10000,
             20000, 20000,
             30000, 30000,
             40000, 40000,
             50000, 50000,
             60000, 60000,
             70000, 70000,
             80000, 80000,
             90000, 90000,
             100000, 100000]
    
    plt.plot(x_val, y_val, "o")
    #plt.scatter( 0 , 0 , s=10000 ,  facecolors='none', edgecolors='blue' )
    
    plt.ylabel("linear regression estimation for d_f")
    plt.xlabel("particles")
    
    plt.xlim([0, 110000])
    plt.ylim([1.80, 2])
    
    plt.show()
    """

    
    
    """
    N = 1000
    cut = 1
    
    x_val = [log(x) for x in range(cut + 1, N + 1)]
    y_val = [log(x) for x in data["radius_list"][cut:]]
    
    param = np.polyfit(x_val, y_val, 1)
    
    
    fda = fd.fractal_dimension_approximation_1(data["particles"], [1/6, 4/6])
    print(fda)
    
    
    lin = [1,2,3,4,5,6,7,8,9,10,11]
    
    x_list = fda["x_list"]
    y_list = fda["y_list"]
    params = fda["parameters"]
    
    plt.plot(x_list, y_list, "o")
    
    
    plt.plot(lin, [params[1] + params[0] * x for x in lin], color="red", linewidth = 2)
    
    plt.scatter( 0 , 0 , s=10000 ,  facecolors='none', edgecolors='blue' ) 
    
    
    
    
    plt.ylabel("ln(r(n))")
    plt.xlabel("ln(n), 800 < n <= 1000")
    
    plt.xlim([x_list[0] - 1, x_list[-1]])
    plt.ylim([y_list[0] - 1, y_list[-1]])
    
    plt.show()
    
    """
    
    
    

def create_pygame_image(data):
    pygame.init()
    pygame.display.init()
    surface = pygame.display.set_mode((300, 300))
    
    
    particles = [x[0] + x[1] * 1j for x in data["particles"]]
    radius = max([abs(x) for x in particles])
    
    background_color = convert_hex_to_vector("ffffff")
    particle_color = convert_hex_to_vector("000000")
    
    #surface = pygame.Surface((300, 300))
    surface.fill(background_color)
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(particles)):
        render_atom = particles[i] + offset
        surface.set_at((int(render_atom.real), int(render_atom.imag)), particle_color) 
        
    low_radius = radius * 0.2
    high_radius = radius * 0.75
    circle_color = convert_hex_to_vector("ff0000")
    
    #pygame.draw.circle(surface, circle_color, (offset.real, offset.imag), low_radius, width = 2)
    #pygame.draw.circle(surface, circle_color, (offset.real, offset.imag), high_radius, width = 2)
    pygame.draw.circle(surface, circle_color, (offset.real, offset.imag), radius +3, width = 2)
    
    while True:
        pygame.display.flip()
    
    
