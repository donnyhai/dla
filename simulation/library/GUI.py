# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:38:03 2020

@author: Tillmann Bosch

INFO
Here we provide the code for running the aggregate process and creating images. 
"""

import pygame, sys, json, time
import line_hitting_aggregate as lha
import external_dla as dla
import external_dla_2 as dla2
import external_dla_3 as dla3
import external_dla_4 as dla4


colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]


def create_image(aggregate, data):
    
    pygame.init()
    
    surface = pygame.Surface((data["image_size_x"], data["image_size_y"]))
    if data["background_color"] == "white":
        background_color = (255,255,255)
    elif data["background_color"] == "black":
        background_color = (0,0,0)
    surface.fill(background_color)
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(aggregate.particles)):
        render_atom = aggregate.particles[i] + offset
        if data["color"] == "yes":
            surface.set_at((int(render_atom.real), int(render_atom.imag)), colors[(i // data["color_generation_size"]) % len(colors)])
        elif data["color"]  == "no":
            if data["particle_color"] == "white":
                particle_color = (255,255,255)
            elif data["particle_color"] == "black":
                particle_color = (0,0,0)
            surface.set_at((int(render_atom.real), int(render_atom.imag)), particle_color) 

    filename = (time.ctime() + "__" + data["aggregate"] + "__" + str(data["iterations"]) + "__" + str(data["color_generation_size"]) + "__" + ".png")
    filename = filename.replace(":","_")
    pygame.image.save(surface, filename)

    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    
    with open("parameters.txt") as json_file:
        data = json.load(json_file)
  
    if data["aggregate"] == "lha":
        
        lha = lha.Line_Hitting_Aggregate()
        lha.run_process(data["iterations"])
        create_image(lha, data)
        
    elif data["aggregate"] == "dla":
        
        dla = dla.External_DLA()
        dla.run_process(data["iterations"])
        create_image(dla, data)
        
    elif data["aggregate"] == "dla2":
        
        dla = dla2.External_DLA()
        dla.run_process(data["iterations"])
        create_image(dla, data)
    
    
    elif data["aggregate"] == "dla3":
        
        dla = dla3.External_DLA()
        dla.run_process(data["iterations"])
        create_image(dla, data)
    

    elif data["aggregate"] == "dla4":
        
        dla = dla4.External_DLA()
        dla.run_process(data["iterations"])
        create_image(dla, data)
    
    
    
    