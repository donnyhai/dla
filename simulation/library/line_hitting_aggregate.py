# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:04:51 2020

@author: Tillmann Bosch

We reference the set of complex numbers as CC
"""


import geometry as geom
import random


class Line_Hitting_Aggregate:
    
    
    def __init__(self):
        
        self.particles = [0]
        self.boundary_set = self.get_neighbours(0)
        
        self.max_distance = 1 # maximum of all distances from 0 to the clusters boundary positions
        
        self.missed_counter = 0
        
        
    def run_process(self, iterations):
        
        for k in range(iterations):
            
            line_hits_cluster = False
            
            while not line_hits_cluster:
        
                random_line = geom.Line(self.get_random_line())
            
                if self.line_hits_cluster(random_line):
                    
                    next_position = self.get_next_particle_position(random_line)
                    
                    """
                    add particle at next_position to the cluster, remove it from the boundary_set and add its empty neighbours to it,
                    actualize max_distance, so the next random line can be chosen correct accordingly
                    """
                    
                    self.particles.append(next_position)
                    self.actualize_boundary_set(next_position)
                    self.actualize_max_distance(next_position)
                    
                    line_hits_cluster = True
                    print(k)
                
                else:
                    self.missed_counter += 1 #counts how often a random line missed the current cluster, as described in the paper
                    print("line missed cluster")
        print("number of misses: " + str(self.missed_counter))
    
    
    def get_random_line(self):
        
        """
        We choose uniform random parameters (alpha, p) in [0, pi) x [0, 20/19 * self.max_distance) 
        which is equivalent to choosing a B-isotropic line where B is a circle with radius 20/19 * self.max_distance with center 0
        and by contstruction therefore certainly contains the current cluster. 
        random.random() chooses uniformly in [0, 1.0)
        return is the parameters pair (alpha, p)
        """
     
        alpha = 3.1416 * random.random()
        p = 20/19 * (2 * self.max_distance * random.random() - self.max_distance)
        
        return (alpha, p)
    
    
    def line_hits_cluster(self, line):
        for k in range(len(self.particles)):
            if line.intersects_with_polygon(self.get_position_square_polygon(self.particles[-k])):
                return True
        return False
    
    
    def get_position_square_polygon(self, position):
        
        """
        return is a square polygon around position as defined in the paper, with segments starting 
        from right top vertex of the square moving clockwise
        """
        
        return geom.Polygon([position + 1/2 * (1+1j), position + 1/2 * (1-1j), position + 1/2 * (-1-1j), position + 1/2 * (-1+1j)])
    

    def get_next_particle_position(self, line):
        
        """
        Choose next particle according to the random line hitting distribution as described in the paper.
        """
        
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
            if line.intersects_with_polygon(self.get_position_square_polygon(position)):
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
    
    
    def actualize_max_distance(self, position):
        new_distance = self.get_distance(position, 0)
        if new_distance > self.max_distance:
            self.max_distance = new_distance
    
    
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
        
        """
        return is True iff x is lower than y according to the total ordered relation on vertices in CC as defined in the paper
        """
        
        x_0, x_1 = x.real, x.imag
        y_0, y_1 = y.real, y.imag
        
        if alpha == 3.1416/2: # Case 1
            return x_0 < y_0
        elif alpha == 0: # Case 2
            return x_1 < y_1
        elif 3.1416/2 < alpha < 3.1416: # Case 3 
            if x_0 == y_0:
                return x_1 < y_1
            else:
                return x_0 < y_0
        elif 0 < alpha < 3.1416/2: # Case 4
            if x_0 == y_0:
                return x_1 > y_1
            else:
                return x_0 < y_0




