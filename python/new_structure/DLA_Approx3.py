#last changed: 200627

import DLA
import random
import math, cmath


class DLA_Approx3(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        
        self.initializeHelpingStructures()        
        self.calculateStartCluster() #after this the cluster has three particles (chosen uniformly, symmetry)
        
        self.nothitcounter = 0
        

    def calculateStartCluster(self):
        self.addAtom(random.choice(self.getNeighbours(self.atoms[0], withDiagonal = True)))
        self.actualizeHelpingStructures()
        
        l = list(set(self.getNeighbours(self.atoms[0], withDiagonal = True) + self.getNeighbours(self.atoms[1], withDiagonal = True)))
        l.remove(self.atoms[0])
        l.remove(self.atoms[1])
        self.addAtom(random.choice(l))
        self.actualizeHelpingStructures()
        
    
    #(self.middlePoint, self.circleRadius) describe a circle around the current cluster (with distance self.helpSpacedelta to a potential 
    #outest particle of the cluster). In there we take a random point and choose a random radius big enough to cover the whole circle
    def getRandomSurroundingCircle(self):
        p = self.middlePoint + cmath.rect(random.random() * self.circleRadius, random.random() * 2 * 3.14)
        return (int(p.real) + int(p.imag) * 1j, random.uniform(2.5 * self.circleRadius, 3 * self.circleRadius))
        
    
    def calculateStartPosition(self):
        middle_point, radius = self.getRandomSurroundingCircle()
        p = middle_point + cmath.rect(radius, random.random() * 2 * 3.14)
        return int(p.real) + int(p.imag) * 1j
        
    #a lot here and especially the different cases with specialSituation etc correlate strongly with cmath.phase (values from -pi to pi)
    def calculateAnglesIntervall(self, point):
        allAngles = []
        specialSituation = False #exists particle in the cluster with point[1] == particle[1] & point[0] > particle[0] (phase break)
        
        for particle in self.atoms:
            if (point.imag == particle.imag) & (point.real > particle.real): #this condition correlates strongly with the function cmath.phase (values from -pi to pi)
                specialSituation = True
            allAngles.append(round(cmath.phase(particle - point), 3)) #vector point -> particle as complex number
            
        if specialSituation:
            negAngles = [angle for angle in allAngles if angle < 0]
            posAngles = [angle for angle in allAngles if angle > 0]
            if len(negAngles) == 0:
                minAngle = min(posAngles)
                maxAngle = max(posAngles)
            else:
                minAngle = max(negAngles)
                maxAngle = min(posAngles)
        else:
            minAngle = min(allAngles)
            maxAngle = max(allAngles)
            
        return (minAngle, maxAngle)


    def chooseRandomAngle(self, intervall):
        if intervall[1] - intervall[0] > 3.142: #equivalent to specialSituation see in calculateAnglesInvervall
            randAngle = random.uniform(intervall[1] - 3.142, intervall[0] + 3.142)
            if randAngle > 0:
                return round(randAngle - 3.142, 3)
            else:
                return round(randAngle + 3.142, 3)
        else:
            return round(random.uniform(intervall[0], intervall[1]), 3)
            
    def getLineClusterHitPoint(self, init_position, angle):
        unnormedLineDirection = cmath.rect(10, angle)
        normedLineDirection = unnormedLineDirection/abs(unnormedLineDirection)
        steps = 1
        walkcounter = 0
        while True:
            position = init_position + steps * self.lineDelta * normedLineDirection
            position = int(round(position.real, 0)) + int(round(position.imag, 0)) * 1j
            #print(position)
            if self.isTouching(position, withDiagonal = True):
                return position
            steps += 1
            
            #if walked by the cluster (which should not happen), reset randomly position and angle
            if walkcounter == 10000:
                init_position = self.calculateStartPosition()
                angle = self.chooseRandomAngle(self.calculateAnglesIntervall(position))
                steps = 1
                walkcounter = 0
                self.nothitcounter += 1
            walkcounter += 1
    
    def runProcess(self, maxAtoms = 100):
        for i in range(maxAtoms):
            start_point = self.calculateStartPosition()
            hitPoint = self.getLineClusterHitPoint(start_point, self.chooseRandomAngle(self.calculateAnglesIntervall(start_point)))
            self.addAtom(hitPoint)
            self.actualizeHelpingStructures()
            print(i)
                
    def initializeHelpingStructures(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0
        
        self.middlePoint = self.atoms[0]
        self.helpSpaceDelta = 2 #how far shall be the helpSpace be away of the outest atoms?
        self.circleRadius = self.helpSpaceDelta
        
        self.circleparameter = 1         
        self.lineDelta = 0.2 #determines the step sizes of going along the line until hitting the cluster
                
                
    def actualizeHelpingStructures(self):
        x,y = self.atoms[-1].real, self.atoms[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.middlePoint = (self.minX + self.maxX) // 2 +  ((self.minY + self.maxY) // 2) * 1j
        
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        self.circleRadius = int(self.circleparameter * abs(dx + dy * 1j) // 2 + self.helpSpaceDelta)
        
                
