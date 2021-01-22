# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:04:51 2020

@author: Tillmann Tristan Bosch

We reference the set of complex numbers as CC
"""

#mathematical imports
import random
from math import pi, log #log is the natural logarithm with base e

import geometry as geom


class Line_Hitting_Aggregate:
    
    
    
    
    
    
    
    
    def __init__(self):
        self.particles = [0]
        self.boundary_set = self.get_neighbours(0)
        self.cluster_radius = 0 
        self.fractal_dimension_values = [1.5] 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def run_process(self, iterations):
        for k in range(iterations):
            line_hits_cluster = False
            
            while not line_hits_cluster:
                random_line = geom.Line(self.get_random_line())
            
                if self.line_hits_cluster(random_line):
                    line_hits_cluster = True
                    next_position = self.get_next_particle_position(random_line)
                    
                    self.particles.append(next_position)
                    self.actualize_boundary_set(next_position)
                    self.actualize_cluster_radius(next_position)
                    self.add_fractal_dimension_value()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def add_fractal_dimension_value(self):
        radius = max(self.cluster_radius, 2)
        value = log(len(self.particles))/log(radius)
        self.fractal_dimension_values.append(value)
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_random_line(self):
        alpha = pi * random.random()
        radius = self.cluster_radius + 2
        p = 2 * radius * random.random() - radius
        return (alpha, p)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_square(self, position):
        return geom.Polygon([position + 1/2 * (1+1j), position + 1/2 * (1-1j), position + 1/2 * (-1-1j), position + 1/2 * (-1+1j)])
    

    def get_next_particle_position(self, line):
        hit_positions = self.get_boundary_hit_positions(line)
        min_position = self.get_min(line.alpha, hit_positions)
        max_position = self.get_max(line.alpha, hit_positions)
        return random.choice([min_position, max_position])
    
    
    
    

    
    
    def is_lower(self, alpha, x, y):
        x_0, x_1 = x.real, x.imag
        y_0, y_1 = y.real, y.imag
        
        if alpha == pi/2: # Case 1
            return x_0 < y_0
        elif alpha == 0: # Case 2
            return x_1 < y_1
        elif pi/2 < alpha < pi: # Case 3 
            if x_0 == y_0:
                return x_1 < y_1
            else:
                return x_0 < y_0
        elif 0 < alpha < pi/2: # Case 4
            if x_0 == y_0:
                return x_1 > y_1
            else:
                return x_0 < y_0




