
import json, sys
import pygame
import random


def create_pygame_image(data, background_color, colors, image_size, color_generation):
    pygame.init()
    
    num = random.choice([i for i in range(10000)])
    filename_image = (data["time"] + "__" + str(len(data["particles"])) + "__" + str(color_generation) + "__" + str(num) + ".png")
    
    particles = data["particles"]
    
    background_color = convert_hex_to_vector(background_color)
    colors = [convert_hex_to_vector(color) for color in colors]
    
    surface = pygame.Surface(image_size)
    surface.fill(background_color)
    offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
    
    for i in range(len(particles)):
        render_atom = particles[i][0] + particles[i][1] * 1j
        render_atom += offset
        #render_atom = particles[i] + offset
        ncolors = len(colors)
        if ncolors > 1:
            surface.set_at((int(render_atom.real), int(render_atom.imag)), colors[(i // color_generation) % ncolors])
        elif ncolors == 1:
            surface.set_at((int(render_atom.real), int(render_atom.imag)), colors[0]) 
    
    pygame.image.save(surface, filename_image)
    pygame.quit()
    sys.exit()
    
def convert_hex_to_vector(hexa):
    def hex_to_int(letter):
        return int(letter, 16)
    r = 16 * hex_to_int(hexa[0]) + hex_to_int(hexa[1])
    g = 16 * hex_to_int(hexa[2]) + hex_to_int(hexa[3])
    b = 16 * hex_to_int(hexa[4]) + hex_to_int(hexa[5])
    return (r,g,b)


if __name__ == "__main__":
    
    filename = "2021_03_04_15_58_28__information_lha_50000.json"
    backgroundcolor = "ffffff"
    #colors = ["7FFF00", "7FFF00", "00FF00", "32CD32", "32CD32", "228B22", "008000", "008000", "006400",  "006400", "006400"]
    colors = ["EFEFFB", "E0E0F8", "CECEF6", "A9A9F5", "8181F7", "5858FA", "5858FA", "2E2EFE", "0000FF", "0000FF"]
    image_size = (500, 500)
    color_generation = 5000
    
    with open(filename) as json_file:
        data = json.load(json_file)
        
    create_pygame_image(data, backgroundcolor, colors, image_size, color_generation)



