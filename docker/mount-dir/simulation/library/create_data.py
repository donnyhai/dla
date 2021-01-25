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


def export_data(aggregate, data):
    
    #create foldername and filenames for image file, fractal information file and parameters file
    foldername = ("\\" + current_time + "_" + data["aggregate"] + "_" + str(data["cluster_size"]) + "_" + str(data["color_generation_size"]))
    foldername = foldername.replace(":","_")
    
    filename_image = (current_time + "_" + "image" + "_" + data["aggregate"] + "_" + str(data["cluster_size"]) + "_" + str(data["color_generation_size"]) + ".png")
    filename_image = filename_image.replace(":","_")
    
    filename_information = (current_time + "_" + "information"  + "_" + data["aggregate"] + "_" + str(data["cluster_size"]) + "_" + str(data["color_generation_size"]) + ".json")
    filename_information = filename_information.replace(":","_")
    
    filename_parameters = (current_time + "_" + "parameters"  + "_" + data["aggregate"] + "_" + str(data["cluster_size"]) + "_" + str(data["color_generation_size"]) + ".json")
    filename_parameters = filename_parameters.replace(":","_")
    
    #create exports
    create_pygame_image(filename_image, aggregate, data)
    create_information(filename_information, aggregate)
    create_parameters_file(filename_parameters)
    
    #move exports into a folder
    os.mkdir(current_dir + foldername)
    for filename in [filename_image, filename_information, filename_parameters]:
        shutil.move(current_dir + "\\" + filename, current_dir + foldername + "\\" + filename)
    
    #move folder to exports
    move_folder_dir = os.path.dirname(current_dir) + "\\exports"
    shutil.move(current_dir + foldername, move_folder_dir)
    
    sys.exit()
    
    
def create_parameters_file(filename):
    os.rename(current_dir + "\\parameters.json", current_dir + "\\" + filename)
    
    
def create_information(filename, aggregate):
    #convert complex numbers into vectors
    particles = [(particle.real, particle.imag) for particle in aggregate.particles]
    
    information = {"time":                  current_time,
                   "last_fractal_value":    aggregate.fractal_dimension_values[-1],
                   "fractal_values":        aggregate.fractal_dimension_values,
                   "particles":             particles
                           }
    f = open(filename, "w+")
    json.dump(information, f)
    f.close()
    
    
def create_pygame_image(filename, aggregate, data):
    pygame.init()
    
    background_color = convert_hex_to_vector(data["background_color"])
    particle_color = [convert_hex_to_vector(color) for color in data["particle_color"]]
    
    surface = pygame.Surface((data["image_width"], data["image_height"]))
    surface.fill(background_color)
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(aggregate.particles)):
        render_atom = aggregate.particles[i] + offset
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



    
    