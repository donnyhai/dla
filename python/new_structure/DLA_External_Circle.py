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
            
            
    #a lot here and especially the different cases with specialSituation etc correlate strongly with cmath.phase (values from -pi to pi)
    def calculateAnglesIntervall(self, point):
        allAngles = []
        specialSituation = False #exists particle in the cluster with point[1] == particle[1] & point[0] > particle[0] (phase break)
        
        for particle in self.atoms:
            if (point.imag == particle.imag) & (point.real > particle.real): #this condition correlates strongly with the function cmath.phase (values from -pi to pi)
                specialSituation = True
            allAngles.append(round(cmath.phase(particle - point), 3)) #vector point -> particle as complex number
            
        if specialSituation:
            minAngle = max([angle for angle in allAngles if angle < 0])
            maxAngle = min([angle for angle in allAngles if angle > 0])
        else:
            minAngle = min(allAngles)
            maxAngle = max(allAngles)
            
        return (minAngle, maxAngle)
            
        return (minAngle, maxAngle)
    
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
        
