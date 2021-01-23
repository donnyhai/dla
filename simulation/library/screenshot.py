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
        
        self.cluster_radius = 0 #radius of the current cluster = maximum of all distances from 0 to the cluster points
        
        self.fractal_dimension_values = [1.5] #start with one neutral value to have equal sizes of particles and fractal_dimension_values 
        
        self.missed_counter = 0
        
        
    def run_process(self, iterations):
        
        for k in range(iterations):
            
            line_hits_cluster = False
            
            while not line_hits_cluster:
                random_line = geom.Line(self.get_random_line())
            
                if self.line_hits_cluster(random_line):
                    line_hits_cluster = True
                    
                    next_particle = self.get_next_particle(random_line)
                    """
                    add particle at next_particle to the cluster, remove it from the boundary_set and add its empty neighbours to it,
                    actualize cluster_radius, so the next random line can be chosen correct accordingly
                    """
                    self.particles.append(next_particle)
                    self.actualize_boundary_set(next_particle)
                    self.actualize_cluster_radius(next_particle)
                    
                    self.add_fractal_dimension_value()
                    
                    print(k)
                
                else:
                    self.missed_counter += 1 #counts how often a random line missed the current cluster, as described in the paper
                    print("line missed cluster")
        print("number of misses: " + str(self.missed_counter))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def add_fractal_dimension_value(self):
        radius = max(self.cluster_radius, 2)
        value = log(len(self.particles))/log(radius)
        self.fractal_dimension_values.append(value)
    
    
    
    
    
    
    
    
    
    
    
    def get_random_line(self):
        
        """
        We choose uniform random parameters (alpha, p) in [0, pi) x [0, 20/19 * self.cluster_radius) 
        which is equivalent to choosing a B-isotropic line where B is a circle with radius 20/19 * self.cluster_radius with center 0
        and by contstruction therefore certainly contains the current cluster. 
        random.random() chooses uniformly in [0, 1.0)
        return is the parameters pair (alpha, p)
        """
     
        alpha = pi * random.random()
        radius = self.cluster_radius + 2 #radius of a circle which certainly surrounds the current cluster
        p = 2 * radius * random.random() - radius
        
        return (alpha, p)
    
    
    def line_hits_cluster(self, line):
        for k in range(len(self.particles)):
            if line.intersects_with_polygon(self.get_square(self.particles[-k])):
                return True
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_square(self, pos):
        return geom.Polygon([pos + 1/2 * (1+1j), pos + 1/2 * (1-1j), pos + 1/2 * (-1-1j), pos + 1/2 * (-1+1j)])
    




























    def get_next_particle(self, line):
        hit_positions = self.get_boundary_hit_positions(line)
        min_position = self.get_min(line.alpha, hit_positions)
        max_position = self.get_max(line.alpha, hit_positions)
        return random.choice([min_position, max_position])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def get_boundary_hit_positions(self, line):
        
        """
        calculate all the positions in the boundary set which the current line hits
        """
        
        boundary_hit_positions = []
        for position in self.boundary_set:
            if line.intersects_with_polygon(self.get_square(position)):
                boundary_hit_positions.append(position)
        return boundary_hit_positions
        

    def actualize_boundary_set(self, position):
        
        """ 
        suppose that position is part of the current boundary set and a particle
        comes to sit there now. therefore delete position of the current boundary set and add its empty neighbours to it
        """
    
        self.boundary_set.remove(position)
        for neighbour in self.get_neighbours(position):
            if neighbour not in self.boundary_set and neighbour not in self.particles:
                self.boundary_set.append(neighbour)
    
    
    def actualize_cluster_radius(self, position):
        new_radius = self.get_distance(position, 0)
        if new_radius > self.cluster_radius:
            self.cluster_radius = new_radius

    
    
    def get_neighbours(self, particle):
        return [particle + 1, particle - 1, particle + 1j, particle - 1j]
    
    
    def get_distance(self, x, y):
        return abs(x - y)   
    
    
    def get_max(self, alpha, positions):
        
        """
        maximum according to self.is_lower (as defined in the paper)
        """
        
        max_position = positions[0]
        for position in positions:
            if not self.is_lower(alpha, position, max_position):
                max_position = position
        return max_position
    
    
    def get_min(self, alpha, positions):
        
        """
        minimum according to self.is_lower (as defined in the paper)
        """
        
        min_position = positions[0]
        for position in positions:
            if self.is_lower(alpha, position, min_position):
                min_position = position
        return min_position
    
    
    
    
    
    
    
    
    
    
    
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




