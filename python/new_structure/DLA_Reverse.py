#last changed: 200627

import DLA

import random
import cmath

#start in the center (start_position) and walk until hit a boundary around the start_position
class DLA_Reverse(DLA.DLA):
    def __init__(self, startAtoms = None):
        if startAtoms is None:
            self.atoms = []
        else:
            self.atoms = startAtoms
        
        self.start_position = 0 #coords representation with complex numbers
        
        #nearest distance from cluster to the start_position (useful for knowing where to alternatively start random walk in order to save calculation)
        #e.g. start at random spot on circle around middle point with radius smaller than nearest distance
        self.nearestDistance = None 
        
        
    def isInsideBoundary(self, atom):
        pass
    
    def setNearestDistance(self, nearestDistance):
        self.nearestDistance = nearestDistance
    
    #start position of the next random walk (on a circle around start_position with radius smaller than the nearestDistance of cluster from start_position)
    def calculateRandomStartPosition(self):
        p = self.start_position + cmath.rect(max(self.nearestDistance - 2, 0), random.random() * 2 * 3.1416)
        return int(p.real) + int(p.imag) * 1j
    
    
    def doAtomWalk(self, position):
        isnear_counter = 0
        while True:
            old_position = position
            
            if not self.isInsideBoundary(position):
                self.addAtom(old_position)
                break
                
            if self.isTouching(position):
                self.addAtom(position)
                break
            
            position = random.choice(self.getNeighbours(position))
            
            if isnear_counter == 10:
                if abs(position - self.start_position) < 0.8 * self.nearestDistance:
                    position = self.calculateRandomStartPosition()
                    isnear_counter = 0
            isnear_counter += 1
    
    
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeNearestDistance()
            print(i)
            
            if self.atoms[-1] == self.start_position:
                break
            
        
    #nearest Distance from cluster to middle starting point
    def actualizeNearestDistance(self):
        self.nearestDistance = min(self.nearestDistance, abs(self.atoms[-1] - self.start_position))
    
    
    
    
       