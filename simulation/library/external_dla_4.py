# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:50:43 2020

@author: donnykong
"""

"""
pi = 3.1416, e = 2.7183
"""

import random

class External_DLA:
    
    
    def __init__(self):
        self.particles = [0] #particles will be presented as complex numbers
        
        self.max_distance = 0
        self.constraint_radius = 5
        
        
    def run_process(self, iterations):
        for i in range(iterations):
            self.do_particle_walk(self.get_random_start_position())
            print(i)
            
        print(len(list(set(self.particles))))
        print(self.max_distance)
        print(self.constraint_radius)
        
        
    #particle walk with noise reduction
    def do_particle_walk(self, position):
        
        while True:
            if self.is_touching(position):
                self.particles.append(position)
                
                new_distance = abs(position)
                if new_distance > self.max_distance:
                    self.max_distance = new_distance
                
                if self.max_distance > self.constraint_radius - 2:
                    self.constraint_radius += 1
                
                break
            
            else: 
                while True:
                    new_position = random.choice(self.get_neighbours(position))
                    
                    if abs(new_position) < self.constraint_radius + 1:
                        break
                    
                position = new_position
                
    def get_random_start_position(self):
        
        random_angle = 2 * 3.1416 * random.random()
        random_position = (self.constraint_radius - 1) * pow(2.7183, random_angle * 1j)
        
        return int(random_position.real) + int(random_position.imag) * 1j
    
        
    def get_neighbours(self, position):
        return [position + 1, position - 1, position + 1j, position - 1j]
        
    
    def is_touching(self, particle):
        for neighbour in self.get_neighbours(particle):
            if neighbour in self.particles:
                return True
        return False
            
