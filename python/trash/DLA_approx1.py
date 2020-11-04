import DLA
from math import sqrt
import random
import pygame

class DLA_approx1(DLA.DLA):
    def __init__(self, spaceSize = (100,100), startAtoms = None):
        super().__init__(spaceSize, startAtoms)
        self.p_value = 1.001 #shall be > 1, see in latex document, approx1
        self.allNeighboursDict = self.attachDistancesToNeighbours(self.getAllNeighbours()) #dict with keys neighbours, values their distances to startAtom
        self.actualizeMaxDistance()
        
        random.seed()
    
    #neighbours of one atom
    def getNeighbours(self, atom):
        x,y = atom
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
        #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]

    #all neighbours of all atoms in self.atoms
    def getAllNeighbours(self):
        allNeighbours = []
        for atom in self.atoms:
            for neigh in self.getNeighbours(atom):
                if not neigh in self.atoms:
                    allNeighbours.append(neigh)
        return allNeighbours

    #return is a dict, with all neighbours as keys and their distances as values
    def attachDistancesToNeighbours(self, allNeighbours):
        neighdist = {}
        for neigh in allNeighbours:
            neighdist[neigh] = self.getDistance(neigh)
        return neighdist
    
    #rounded distance of atom to startAtom
    def getDistance(self, atom):
        d = (self.startAtom[0] - atom[0])**2 + (self.startAtom[1] - atom[1])**2
        return int(sqrt(d))
    
    def actualizeMaxDistance(self):
        self.maxDistance = max(self.allNeighboursDict.values())
    
    #suppose an atom was added to self.atoms, then actualiz allNeighbours
    def actualizeAllNeighbours(self, addedAtom):
        for neigh in self.getNeighbours(addedAtom):
            if neigh not in self.atoms and neigh not in self.allNeighboursDict:
                self.allNeighboursDict[neigh] = self.getDistance(neigh)
        del self.allNeighboursDict[addedAtom]
    
    #return is a dict with keys the possible distances, and values the probability area accroding to the calculation in approx1, see latex
    def calculateDistribution(self):
        A = {} #probability areas of [0,1] (see latex document at approx1)
        A[0] = (self.p_value - 1) / (self.p_value**(self.maxDistance + 1) - 1)
        for i in range(1, self.maxDistance + 1):
            A[i] = self.p_value * A[i-1]
        return A
           
    def chooseNextAtom(self, distribution, allNeighbours):
        neighdistri = {} #is a dict, keys are all neighbours, values are the probabilites for each neighbour
        for neigh in allNeighbours:
            dist = allNeighbours[neigh]
            nr = list(self.allNeighboursDict.values()).count(dist)
            neighdistri[neigh] = distribution[dist] / nr
        
        weightedList = []
        roundfactor = 4
        for neigh in neighdistri:
            amount = int(10**roundfactor * round(neighdistri[neigh], roundfactor))
            weightedList += [neigh for i in range(amount)]
            
        return random.choice(weightedList)
            
    
    def runProcess(self, atomsMax = 500):
        for k in range(atomsMax):
            #calculate distribution, choose next atom and add it
            addAtom = self.chooseNextAtom(self.calculateDistribution(), self.allNeighboursDict)
            self.addAtom(addAtom)
            
            #actualize structures
            self.actualizeAllNeighbours(addAtom)
            self.actualizeMaxDistance()
            
            print(k)
            

    def render(self, surface):
        surface.fill((0,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()        
    
