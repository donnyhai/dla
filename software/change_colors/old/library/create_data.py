# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:17:52 2021

@author: Tillmann Tristan Bosch

Here data like image, cluster information and process parameters are captured and exported. 
"""

#systemic imports
import pygame, json, sys, datetime, os, shutil


def format_time():
    time = datetime.datetime.now()
    values = [str(time.year), str(time.month), str(time.day), str(time.hour), str(time.minute), str(time.second)]
    
    #concat values, add 0 if value is just one digit (like "02" instead of just "2")
    time_format = ""
    for value in values:
        if len(value) == 1:
            value = "0" + value
        time_format += value + "_"
    return time_format


#get current system time and put into good format
current_time = format_time()
current_dir = os.getcwd()


def export_data(aggregate, data, separator):
    
    filename_image = (data["time"] + ".png")
    create_pygame_image(filename_image, aggregate, data)
    
    sys.exit()
    
    
def create_pygame_image(filename, aggregate, data):
    pygame.init()
    
    background_color = convert_hex_to_vector(data["background_color"])
    particle_color = [convert_hex_to_vector(color) for color in data["new-colors"]]
    particles = data["particles"]
    
    surface = pygame.Surface((data["image_width"], data["image_height"]))
    surface.fill(background_color)
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(particles)):
        render_atom = particles[i][0] + particles[i][1] * 1j
        render_atom += offset
        #render_atom = particles[i] + offset
        ncolors = len(particle_color)
        if ncolors > 1:
            surface.set_at((int(render_atom.real), int(render_atom.imag)), particle_color[(i // data["color_generation_size"]) % ncolors])
        elif ncolors == 1:
            surface.set_at((int(render_atom.real), int(render_atom.imag)), particle_color[0]) 
    
    pygame.image.save(surface, filename)
    pygame.quit()


def convert_hex_to_vector(hexa):
    def hex_to_int(letter):
        return int(letter, 16)
    r = 16 * hex_to_int(hexa[0]) + hex_to_int(hexa[1])
    g = 16 * hex_to_int(hexa[2]) + hex_to_int(hexa[3])
    b = 16 * hex_to_int(hexa[4]) + hex_to_int(hexa[5])
    return (r,g,b)


    
    