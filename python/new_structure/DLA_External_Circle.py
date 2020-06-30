#last changed: 200627

import DLA_External as de

import random
import cmath

#for now this simulation considers neighbours of particles up, down, left, right. 
#therefore no diagonal neighbours when a particle is moving, or when considering touching the cluster
class DLA_External_Circle(de.DLA_External):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        self.initializeHelpingStructures()


    def isNear(self, pos):
        return abs(pos) < self.circleRadius
        
    #start position of the next random walk
    def calculateRandomStartPosition(self):
        startpos = cmath.rect(self.circleRadius, random.random() * 2 * 3.1416)
        return int(startpos.real) + int(startpos.imag) * 1j
    
    
    #atom walk with noise reduction
    def doAtomWalk(self, position):
        isnear_counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            else: 
                position = random.choice(self.getNeighbours(position))
                
            if isnear_counter == 10:
                if not self.isNear(position):
                    position = self.calculateRandomStartPosition()
                isnear_counter = 0
            isnear_counter += 1
            
    
    def runProcess(self, atomsMax = 300):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeHelpingStructures()
            print(i)
            
    
    def initializeHelpingStructures(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0
        
        self.middlePoint = self.atoms[0]
        self.helpSpaceDelta = 2 #how far shall be the helpSpace be away of the outest atoms?
        self.circleRadius = self.helpSpaceDelta
        
        self.circleparameter = 1
    
    def actualizeHelpingStructures(self):
        x,y = self.atoms[-1].real, self.atoms[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.middlePoint = ((self.minX + self.maxX) // 2) + ((self.minY + self.maxY) // 2) * 1j
        
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.circleRadius = int(self.circleparameter * (abs(dx + dy * 1j) // 2) + self.helpSpaceDelta)
        
