#last changed: 200627

import DLA_External as de
import random, cmath

class DLA_External_Approx3(de.DLA_External):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        
        self.calculateStartCluster() #after this the cluster has three particles (chosen uniformly, symmetry)
        
        self.lineDelta = 0.25
        self.nothitcounter = 0
        
        
    def runProcess(self, maxAtoms = 100):
        for i in range(maxAtoms):
            start_point = self.calculateRandomStartPosition()
            hitPoint = self.getLineClusterHitPoint(start_point, self.chooseRandomAngle(self.calculateAnglesIntervall(start_point)))
            self.addAtom(hitPoint)
            self.actualizeHelpingStructures()
            print(i)

    def calculateStartCluster(self):
        self.addAtom(random.choice(self.getNeighbours(self.atoms[0], withDiagonal = True)))
        self.actualizeHelpingStructures()
        
        l = list(set(self.getNeighbours(self.atoms[0], withDiagonal = True) + self.getNeighbours(self.atoms[1], withDiagonal = True)))
        l.remove(self.atoms[0])
        l.remove(self.atoms[1])
        self.addAtom(random.choice(l))
        self.actualizeHelpingStructures()
    
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
                self.calculateRandomBigStartCircle()
                init_position = self.calculateRandomStartPosition()
                angle = self.chooseRandomAngle(self.calculateAnglesIntervall(position))
                steps = 1
                walkcounter = 0
                self.nothitcounter += 1
            walkcounter += 1
    

                
