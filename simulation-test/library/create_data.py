# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:17:52 2021

@author: Tillmann Bosch
"""
#systemic imports
import pygame, json, sys, time


colors2 = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]
colors3 = [(255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (128,255,0)]
colors = [(0,0,255), (255,0,0)]

def export_data(aggregate, data):
    
    current_time = time.ctime()
    
    filename_image = (current_time + "__" + "image" + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]) + ".png")
    filename_image = filename_image.replace(":","_")
    
    filename_fractal_info = (current_time + "__" + "fractalinfo"  + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]) + ".txt")
    filename_fractal_info = filename_fractal_info.replace(":","_")
    
    create_pygame_image(filename_image, aggregate, data)
    create_fractal_info(filename_fractal_info, aggregate)
    
    sys.exit()
    
    
def create_fractal_info(filename, aggregate):
    all_values = aggregate.fractal_dimension_values #list of all calculated fractal dimension values during the process
    all_average = sum(all_values)/len(all_values)
    
    last_value = all_values[-1]
    
    every_1000th_value = [] #we create a list here of every 1000th value in all_values
    for k in range(len(all_values)):
        if (k+1) % 1000 == 0:
            every_1000th_value.append(all_values[k])
    every_1000th_value_average = sum(every_1000th_value)/len(every_1000th_value)
    
    
    fractal_info = {"last_value": last_value,
                    "every_1000th_value_average": every_1000th_value_average,
                    "all_average" : all_average,
                    "every_1000th_value": every_1000th_value,
                    "all_values": all_values
                    }
    
    f = open(filename, "w+")
    json.dump(fractal_info, f)
    f.close()
    
    
def create_pygame_image(filename, aggregate, data):
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
    
    pygame.image.save(surface, filename)

    pygame.quit()
    


def convert_hex_to_vector(hexa):
    def hex_to_int(letter):
        return int(letter, 16)
    
    r = 16 * hex_to_int(hexa[0]) + hex_to_int(hexa[1])
    g = 16 * hex_to_int(hexa[2]) + hex_to_int(hexa[3])
    b = 16 * hex_to_int(hexa[4]) + hex_to_int(hexa[5])
    
    return (r,g,b)
    
    