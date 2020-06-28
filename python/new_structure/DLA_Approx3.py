#last changed: 200627

import DLA
import random
import math, cmath


class DLA_Approx3(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        
        self.maxDistance = 0
        self.initializeHelpingStructures()        
        self.calculateStartCluster() #after this the cluster has three particles (chosen uniformly, symmetry)
        self.lineDelta = 0.5 #determines the step sizes of going along the line until hitting the cluster
        

    def calculateStartCluster(self):
        self.addAtom(random.choice(self.getNeighbours(self.atoms[0])))
        self.actualizeHelpingStructures()
        
        l = list(set(self.getNeighbours(self.atoms[0]) + self.getNeighbours(self.atoms[1])))
        l.remove(self.atoms[0])
        l.remove(self.atoms[1])
        self.addAtom(random.choice(l))
        self.actualizeHelpingStructures()
        
    
    #(self.middlePoint, self.circleRadius) describe a circle around the current cluster (with distance self.helpSpacedelta to a potential 
    #outest particle of the cluster). In there we take a random point and choose a random radius big enough to cover the whole circle
    def getRandomSurroundingCircle(self):
        p = self.middlePoint + cmath.rect(random.random() * self.circleRadius, random.random() * 2 * 3.14)
        return (int(p.real) + int(p.imag) * 1j, random.uniform(3 * self.circleRadius, 4 * self.circleRadius))
        
    
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
            minAngle = max([angle for angle in allAngles if angle < 0])
            maxAngle = min([angle for angle in allAngles if angle > 0])
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
                round(randAngle + 3.142, 3)
        else:
            return round(random.uniform(intervall[0], intervall[1]), 3)
            
    def getLineClusterHitPoint(self, startPoint, angle):
        unnormedLineDirection = cmath.rect(10, angle)
        normedLineDirection = unnormedLineDirection/abs(unnormedLineDirection)
        
        actualPlace = startPoint
        steps = 1
        smallCondition = len(self.atoms) < 10
        
        while True:
            nextPlace = startPoint + steps * self.lineDelta * normedLineDirection
            nextPlace = math.ceil(nextPlace.real) + math.ceil(nextPlace.imag) * 1j
            if nextPlace in self.atoms:
                print("test3")
                if actualPlace in self.getNeighbours(nextPlace, True):
                    return actualPlace
                else:
                    x = nextPlace[0] + 0.25 * (-1) * normedLineDirection[0] #move a bit back to certainly get a neighbour
                    y = nextPlace[1] + 0.25 * (-1) * normedLineDirection[1]
                    return (math.ceil(x), math.ceil(y))
            
            if smallCondition:
                for parti in self.atoms:
                    for neigh in self.getNeighbours(parti):
                        if nextPlace == neigh:
                            return nextPlace
            
            actualPlace = nextPlace
            steps += 1
    
    def runProcess(self, maxAtoms = 100):
        for i in range(maxAtoms):
            start_point = self.calculateStartPosition()
            print(start_point)
            angleIntervall = self.calculateAnglesIntervall(start_point)
            print(angleIntervall)
            angle = self.chooseRandomAngle(angleIntervall)
            print(angle)
            hitPoint = self.getLineClusterHitPoint(start_point, angle)
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
                
                
    def actualizeHelpingStructures(self):
        x,y = self.atoms[-1].real, self.atoms[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.middlePoint = (self.minX + self.maxX) // 2 +  ((self.minY + self.maxY) // 2) * 1j
        
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        self.circleRadius = int(self.circleparameter * abs(dx + dy * 1j) // 2 + self.helpSpaceDelta)
        
                
