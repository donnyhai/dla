# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 14:17:52 2021

@author: Tillmann Tristan Bosch
"""

#systemic imports
import pygame, json, sys, time, os, shutil


def export_data(aggregate, data):
    
    #get current system time
    current_time = time.ctime()
    
    #create foldername and filenames for image file, fractal information file and parameters file
    foldername = ("\\" + current_time + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]))
    foldername = foldername.replace(":","_")
    
    filename_image = (current_time + "__" + "image" + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]) + ".png")
    filename_image = filename_image.replace(":","_")
    
    filename_fractal_info = (current_time + "__" + "fractalinfo"  + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]) + ".json")
    filename_fractal_info = filename_fractal_info.replace(":","_")
    
    filename_parameters = (current_time + "__" + "parameters"  + "__" + data["aggregate"] + "__" + str(data["cluster_size"]) + "__" + str(data["color_generation_size"]) + ".json")
    filename_parameters = filename_parameters.replace(":","_")
    
    #get current working directory
    current_dir = os.getcwd()
    
    #create exports
    create_pygame_image(filename_image, aggregate, data)
    create_fractal_info(filename_fractal_info, aggregate)
    create_parameters_file(filename_parameters, current_dir)
    
    #move exports into a folder
    os.mkdir(current_dir + foldername)
    for filename in [filename_image, filename_fractal_info, filename_parameters]:
        shutil.move(current_dir + "\\" + filename, current_dir + foldername + "\\" + filename)
    
    #move folder to exports
    move_folder_dir = os.path.dirname(current_dir) + "\\exports"
    shutil.move(current_dir + foldername, move_folder_dir)
    
    sys.exit()
    
    
def create_parameters_file(filename, current_dir):
    os.rename(current_dir + "\\parameters.json", current_dir + "\\" + filename)
    
    
def create_fractal_info(filename, aggregate):
    all_values = aggregate.fractal_dimension_values #list of all calculated fractal dimension values during the process
    all_average = sum(all_values)/len(all_values) if len(all_values) > 0 else 0
    
    last_value = all_values[-1]
    
    every_1000th_value = [] #we create a list here of every 1000th value in all_values
    for k in range(len(all_values)):
        if (k+1) % 1000 == 0:
            every_1000th_value.append(all_values[k])
    every_1000th_value_average = sum(every_1000th_value)/len(every_1000th_value) if len(every_1000th_value) > 0 else 0
    
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


    
    