# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:38:03 2020

@author: Tillmann Bosch

INFO
Here we provide the code for running the aggregate process and creating images. 
"""

import pygame, sys, json, time
import line_hitting_aggregate_simulation as lhas


colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]


def create_image(aggregate, data):
    
    pygame.init()
    
    surface = pygame.Surface((data["image_size_x"], data["image_size_y"]))
    surface.fill((0,0,0))
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(aggregate.particles)):
        render_atom = aggregate.particles[i] + offset
        if data["color"] == "yes":
            surface.set_at((int(render_atom.real), int(render_atom.imag)), colors[(i // data["color_generation_size"]) % len(colors)])
        elif data["color"]  == "no":
            surface.set_at((int(render_atom.real), int(render_atom.imag)), (255,255,255)) 

    pygame.image.save(surface, (time.ctime() + ".png").replace(":","_"))

    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    
    with open("parameters.txt") as json_file:
        data = json.load(json_file)
  
    lha = lhas.Line_Hitting_Aggregate_Simulation()
    lha.run_process(data["iterations"])
    
    create_image(lha, data)