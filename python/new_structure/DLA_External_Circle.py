#last changed: 200627

import DLA_External as de

import random

#for now this simulation considers neighbours of particles up, down, left, right. 
#therefore no diagonal neighbours when a particle is moving, or when considering touching the cluster
class DLA_External_Circle(de.DLA_External):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        self.initializeHelpingStructures()
        
        self.isnotnear_counter = 0


    def isNear(self, pos):
        return abs(pos) < self.bigStartCircle["radius"]
    
    #atom walk with noise reduction
    def doAtomWalk(self, position):
        isnear_counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            else: 
                position = random.choice(self.getNeighbours(position))
                
            if isnear_counter == 2 * int(self.surroundCircle["radius"]):
                if not self.isNear(position):
                    self.calculateRandomBigStartCircle()
                    position = self.calculateRandomStartPosition()
                    self.isnotnear_counter += 1
                isnear_counter = 0
            isnear_counter += 1
    
    def runProcess(self, atomsMax = 300):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeHelpingStructures()
            print(i)
            
