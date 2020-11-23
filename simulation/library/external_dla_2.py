# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:50:43 2020

@author: donnykong
"""


import random
"""
pi = 3.1416, e = 2.7183
"""

class External_DLA:
    
    
    def __init__(self):
        self.particles = [0] #particles will be presented as complex numbers

        self.max_distance = 0
        self.constraint_radius = 40
        
        
    def run_process(self, iterations):
        moving_particles = self.init_moving_particles(iterations)
        particles_moving = True    
        stuck_counter = 0
        
        while particles_moving: 
            new_moving_particles = []

            for particle in moving_particles:
                
                if particle in self.particles:
                    new_moving_particles.append(self.get_random_position())
                    
                else:
                    if self.is_touching(particle):
                        
                        self.particles.append(particle)
                        
                        new_distance = abs(particle)
                        if new_distance > self.max_distance:
                            self.max_distance = new_distance
                            
                        if self.max_distance > self.constraint_radius - 2:
                            self.constraint_radius += 3
                            
                        print(stuck_counter)
                        stuck_counter += 1
                        
                    else:
                        while True:
                            new_position = random.choice(self.get_neighbours(particle))
                        
                            if abs(new_position) < self.constraint_radius + 1:
                                new_moving_particles.append(new_position)
                                break
                        
            moving_particles = new_moving_particles.copy()
            particles_moving = any(moving_particles)
        
        print(len(list(set(self.particles))))
            
        
    def init_moving_particles(self, iterations):
        moving_particles = []
        
        for k in range(iterations):
            moving_particles.append(self.get_random_position())
            
        return moving_particles
            
    def get_random_position(self):
        
        random_angle = 2 * 3.1416 * random.random()
        random_p = self.constraint_radius * random.random()
        #random_p = 20 + (self.constraint_radius - 20) * random.random()
        random_position = random_p * pow(2.7183, random_angle * 1j)
        
        return int(random_position.real) + int(random_position.imag) * 1j
        
    def get_neighbours(self, position):
        return [position + 1, position - 1, position + 1j, position - 1j]
        
    
    def is_touching(self, particle):
        for neighbour in self.get_neighbours(particle):
            if neighbour in self.particles:
                return True
        return False
            
    
