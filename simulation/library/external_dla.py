# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 00:50:43 2020

@author: donnykong
"""
import cmath, random

class External_DLA:
    
    
    def __init__(self):
        self.particles = [0] #particles will be presented as complex numbers
        self.init_helping_structures()
        self.isnotnear_counter = 0
        
        
    def run_process(self, iterations):
        for i in range(iterations):
            self.do_particle_walk(self.get_random_start_position())
            self.actualize_helping_structures()
            print(i)
        
        
    #particle walk with noise reduction
    def do_particle_walk(self, position):
        isnear_counter = 0
        while True:
            if self.is_touching(position):
                self.particles.append(position)
                break
            else: 
                position = random.choice(self.get_neighbours(position))
                
            if isnear_counter == 2 * int(self.surroundCircle["radius"]):
                if not self.isNear(position):
                    self.calculateRandomBigStartCircle()
                    position = self.get_random_start_position()
                    self.isnotnear_counter += 1
                isnear_counter = 0
            isnear_counter += 1        
        
        
    #start position of the next random walk
    def get_random_start_position(self):
        startpos = self.bigStartCircle["middlePoint"] + cmath.rect(self.bigStartCircle["radius"], random.random() * 2 * 3.1416)
        return int(startpos.real) + int(startpos.imag) * 1j
        
        
    def calculateRandomBigStartCircle(self):
        m = self.surroundCircle["middlePoint"] + cmath.rect(1/2 * random.random() * self.surroundCircle["radius"], random.random() * 2 * 3.142)
        self.bigStartCircle = {"middlePoint": m, "radius": random.uniform(1.5, 2) * self.surroundCircle["radius"]}


    def init_helping_structures(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0
        
        self.helpSpaceDelta = 1 #how far shall be the surroundCircle be away of the outest particles?
        self.surroundCircle = {"middlePoint": self.particles[0], "radius": self.helpSpaceDelta} #this a circle closely around the cluster
        
        self.bigStartCircle = {"middlePoint": None, "radius": None} #this is a circle certainly containing the surroundCircle. on this circles boundary particles will start their random walks
        self.calculateRandomBigStartCircle()
        
    def actualize_helping_structures(self):
        x,y = self.particles[-1].real, self.particles[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.surroundCircle["middlePoint"] = ((self.minX + self.maxX) / 2) + ((self.minY + self.maxY) / 2) * 1j
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.surroundCircle["radius"] = abs(dx + dy * 1j) / 2 + self.helpSpaceDelta

        self.calculateRandomBigStartCircle() 
        
        
    def isNear(self, pos):
        return abs(pos) < self.bigStartCircle["radius"]

    
    def get_neighbours(self, position):
        return [position + 1, position - 1, position + 1j, position - 1j]
        
    
    def is_touching(self, particle):
        for neighbour in self.get_neighbours(particle):
            if neighbour in self.particles:
                return True
        return False
            
