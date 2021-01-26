
import DLA_External_Circle_GUI as decg
import random, cmath

class Testclass(decg.DLA_External_Circle_GUI):
    
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