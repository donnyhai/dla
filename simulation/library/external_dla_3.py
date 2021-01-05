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
        self.init_helping_structures()
        
        
    def run_process(self, iterations):
        for i in range(iterations):
            self.do_particle_walk(self.get_random_start_position())
            self.actualize_helping_structures()
            print(i)
        
        print(len(list(set(self.particles))))

        
    #particle walk with noise reduction
    def do_particle_walk(self, position):
        is_near_counter = 0
        while True:
            if self.is_touching(position):
                self.particles.append(position)
                break
            
            else: 
                position = random.choice(self.get_neighbours(position))
                
            if is_near_counter == 10:
                if not self.is_near(position):
                    position = self.get_random_start_position()
                    
                is_near_counter = 0
                
            is_near_counter += 1        
        
        
    #start position of the next random walk
    def get_random_start_position(self):
        
        random_angle = 2 * 3.1416 * random.random()
        position = self.surround_circle["middlePoint"] + self.surround_circle["radius"] * pow(2.7183, random_angle * 1j)
        
        return int(position.real) + int(position.imag) * 1j
        
        
    def init_helping_structures(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0
        
        self.helpSpaceDelta = 1 #how far shall be the surround_circle be away of the outest particles?
        self.surround_circle = {"middlePoint": self.particles[0], "radius": self.helpSpaceDelta} #this a circle closely around the cluster
        
        
    def actualize_helping_structures(self):
        x,y = self.particles[-1].real, self.particles[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.surround_circle["middlePoint"] = ((self.minX + self.maxX) / 2) + ((self.minY + self.maxY) / 2) * 1j
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.surround_circle["radius"] = abs(dx + dy * 1j) / 2 + self.helpSpaceDelta

        
    def is_near(self, pos):
        return abs(pos) < self.surround_circle["radius"]

    
    def get_neighbours(self, position):
        return [position + 1, position - 1, position + 1j, position - 1j]
        
    
    def is_touching(self, particle):
        for neighbour in self.get_neighbours(particle):
            if neighbour in self.particles:
                return True
        return False
            
