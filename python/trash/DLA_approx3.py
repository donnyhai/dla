# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 10:47:00 2020

@author: donnykong
"""

import DLA
import random
import math, cmath
import pygame

class DLA_approx3(DLA.DLA):
    def __init__(self, spaceSize = (100,100), startAtoms = None):
        super().__init__(spaceSize, startAtoms)
        
        self.maxDistance = 0
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        self.atoms = [self.atoms[0] + self.atoms[1] * 1j] #particles representation as complex numbers
        
        self.middlePoint = self.atoms[0]
        self.helpSpaceDelta = 4 #how far shall be the helpSpace be away of the outest atoms ?
        self.circleRadius = self.helpSpaceDelta
        
        self.calculateStartCluster() #after this the cluster has three particles (chosen uniformly, symmetry)
        
        self.lineDelta = 0.5 #determines the step sizes of going along the line until hitting the cluster
        




       
    #point has to be complex number
    def getNeighbours(self, point):
        return [point + 1, point - 1, point + 1j, point - 1j]
    
    def calculateStartCluster(self):
        self.addAtom(random.choice(self.getNeighbours(self.atoms[0])))
        self.actualizeExtremeCoordinates()
        self.actualizeMiddlePoint()
        self.actualizeCircleRadius()
        
        l = list(set(self.getNeighbours(self.atoms[0]) + self.getNeighbours(self.atoms[1])))
        l.remove(self.atoms[0])
        l.remove(self.atoms[1])
        self.addAtom(random.choice(l))
        self.actualizeExtremeCoordinates()
        self.actualizeMiddlePoint()
        self.actualizeCircleRadius()
        
    
    # (self.middlePoint, self.circleRadius) describe a circle around the current cluster (with ca distance self.helpSpacedelta)
    # in there we take a random point and choose a random radius big enough to cover the whole circle
    def getRandomSurroundingCircle(self):
        p = self.middlePoint + cmath.rect(random.random() * self.circleRadius, random.random() * 2 * 3.14)
        return (int(p.real) + int(p.imag) * 1j, random.uniform(3 * self.circleRadius, 4 * self.circleRadius))
        
    
    def calculateStartPosition(self):
        middle_point, radius = self.getRandomSurroundingCircle()
        w = random.random() * 2 * 3.14
        return int(middle_point[0] + math.cos(w) * radius) + int(middle_point[1] + math.sin(w) * radius) * 1j
        
    #a lot here and especially the different cases with specialSituation etc correlate strongly with cmath.phase (values from -pi to pi)
    def calculateAnglesIntervall(self, point):
        allAngles = []
        specialSituation = False #exists particle in the cluster with point[1] == particle[1] & point[0] > particle[0] (phase break)
        
        for particle in self.atoms:
            if point.imag == particle.imag & point.real > particle.real: #this condition correlates strongly with the function cmath.phase (values from -pi to pi)
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
        if intervall[1] - intervall[0] >= 3.142: #equivalent to specialSituation see in calculateAnglesInvervall
            randAngle = random.uniform(intervall[1] - 3.142, intervall[0] + 3.142)
            if randAngle > 0:
                return round(randAngle - 3.142, 3)
            else:
                round(randAngle + 3.142, 3)
        else:
            return round(random.uniform(intervall[0], intervall[1]), 3)
            
    def getLineClusterHitPoint(self, startPoint, angle):
        relPoint = cmath.rect(10, angle)
        unnormedLineDirection = (relPoint.real - startPoint[0]) + (relPoint.imag - startPoint[1]) * 1j #direction is startPoint -> relPoint
        length = math.sqrt(pow(unnormedLineDirection.real, 2) + pow(unnormedLineDirection.imag, 2))
        normedLineDirection = unnormedLineDirection/length
        
        actualPlace = startPoint
        steps = 1
        smallCondition = len(self.atoms) < 10
        
        while True:
            
            nextPlace = (math.ceil(startPoint[0] + steps * self.lineDelta * normedLineDirection.real), math.ceil(startPoint[1] + steps * self.lineDelta * normedLineDirection.imag))
            print(nextPlace)
            if nextPlace in self.atoms:
                print("test3")
                if actualPlace in self.getNeighbours(nextPlace):
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
            break
            self.addAtom(hitPoint)
            
            self.actualizeExtremeCoordinates()
            self.actualizeMiddlePoint()
            self.actualizeCircleRadius()
            
            print(i)
                
                
                
                
                
    def actualizeExtremeCoordinates(self):
        x,y = self.atoms[-1]
        self.minX = min(self.minX, x)
        self.maxX = max(self.maxX, x)
        self.minY = min(self.minY, y)
        self.maxY = max(self.maxY, y)
    
    def actualizeMiddlePoint(self):
        self.middlePoint = ((self.minX + self.maxX) // 2, (self.minY + self.maxY) // 2)
    
    def actualizeCircleRadius(self):
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        self.circleRadius = int(self.circleparameter * math.sqrt(dx*dx + dy*dy) // 2 + self.helpSpaceDelta)
        
    def render(self, surface):
        surface.fill((0,0,0,0))
        offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j #complex
        
        for i in range(len(self.atoms)):
            renderAtom = self.atoms[i] + offset #complex
            surface.set_at((renderAtom.rel, renderAtom.imag), self.colors[(i//250)%len(self.colors)]) #complex
            #surface.set_at((renderAtom.rel, renderAtom.imag), (255,255,255)) 
        
        pygame.display.flip()   