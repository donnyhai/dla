#last changed: 200627

import DLA
import pygame
import random
from math import sin, cos, sqrt

#start in the center and walk to the 
class Reverse_DLA(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(spaceSize, startAtoms)
        self.atoms = []
        
        self.start_position = (0,0)
        
        self.boundary_radius = 150 #will be square or circle
        self.boundary_rect = pygame.Rect(self.start_position[0] - self.boundary_radius, self.start_position[1] - self.boundary_radius, 2 * self.boundary_radius, 2 * self.boundary_radius)
        
        self.colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]
        self.actual_color = self.colors[0]
        
        #nearest distance from cluster to middle point (useful for knowing where to alternatively start random walk in order to save calculation)
        #e.g. start at random spot on circle around middle point with radius smaller than nearest distance
        self.nearestDistance = self.boundary_radius
        
    def isOutsideBoundary(self, atom):
        return not self.boundary_rect.collidepoint(atom)
    
    def numberOfNeighboursWithParticles(self, atom):
        return len(set(self.getNeighbours(atom)).intersection(set(self.atoms)))

    def isTouching(self, atom):
        return self.numberOfNeighboursWithParticles(atom) > 0
    
    
    #start position of the next random walk
    def calculateRandomStartPosition(self):
        alpha = random.random() * 2 * 3.1416
        radius = max(self.nearestDistance - 2, 0)
        dx, dy = cos(alpha) * radius, sin(alpha) * radius
        return (self.start_position[0] + round(dx), self.start_position[1] + round(dy))
    
    def doAtomWalk(self, position):
        while True:
            old_position = position
            
            if self.isOutsideBoundary(position):
                self.addAtom(old_position)
                break
                
            if self.isTouching(position):
                self.addAtom(position)
                break
            
            position = random.choice(self.getNeighbours(position))
            
            
    def doAtomWalk2(self, position):
        isnear_counter = 0
        while True:
            old_position = position
            distance = self.distanceToMiddlePoint(position)
            
            if distance > self.boundary_radius:
                self.addAtom(old_position)
                break
                
            if self.isTouching(position):
                self.addAtom(position)
                break
            
            position = random.choice(self.getNeighbours(position))
            
            if isnear_counter == 10:
                if distance < 0.8 * self.nearestDistance:
                    position = self.calculateRandomStartPosition()
                    isnear_counter = 0
            isnear_counter += 1

    
    #square boundary        
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeNearestDistance()
            print(i)
            
            if self.atoms[-1] == self.start_position:
                break
    
    #round boundary
    def runProcess2(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk2(self.calculateRandomStartPosition())
            self.actualizeNearestDistance()
            print(i)
            
            if self.atoms[-1] == self.start_position:
                break
            
    def render(self, surface):
        surface.fill((0,0,0,0))
        offset = (surface.get_width() // 2, surface.get_height() // 2)
        #offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j #complex
        
        for i in range(len(self.atoms)):
            renderAtom = (self.atoms[i][0] + offset[0], self.atoms[i][1] + offset[1])
            #renderAtom = self.atoms[i] + offset #complex
            surface.set_at(renderAtom, self.colors[(i//250)%len(self.colors)])
            #surface.set_at((renderAtom.rel, renderAtom.imag), self.colors[(i//250)%len(self.colors)]) #complex
        #for atom in self.atoms:
        #    surface.set_at(atom, (150, 215, 182, 255))
        
        pygame.display.flip()   
        
        
        
        
        
        
    #nearest Distance from cluster to middle starting point
    def actualizeNearestDistance(self):
        new_distance = self.distanceToMiddlePoint(self.atoms[-1])
        if new_distance < self.nearestDistance:
            self.nearestDistance = new_distance
        
    def distanceToMiddlePoint(self, atom):
        return sqrt(pow(atom[0] - self.start_position[0], 2) + pow(atom[1] - self.start_position[1], 2))
    
    
    
    
    
    
    
       