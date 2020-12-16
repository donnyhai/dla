import DLA
from math import sqrt
import random
import pygame
import DLA_approx1

class DLA_approx1_GUI(DLA_approx1.DLA_approx1):
    def __init__(self, spaceSize = (100,100), startAtoms = None):
        super().__init__(spaceSize, startAtoms)
        self.p_value = 1.5 #shall be > 1, see in latex document, approx1
        self.allNeighboursDict = self.attachDistancesToNeighbours(self.getAllNeighbours()) #dict with keys neighbours, values their distances to startAtom
        self.actualizeMaxDistance()
        
        random.seed()
    
    def runProcess(self, atomsMax = 500, surface = None):
        counter = 0
        for i in range(atomsMax):
            #calculate distribution, choose next atom and add it
            addAtom = self.chooseNextAtom(self.calculateDistribution(), self.allNeighboursDict)
            self.addAtom(addAtom)
            
            #actualize structures
            self.actualizeAllNeighbours(addAtom)
            self.actualizeMaxDistance()
            
            if counter == 7:
                if surface is not None:
                    self.render(surface)
                counter = 0
            
            counter += 1
            print(i)
                
            

    def render(self, surface):
        surface.fill((0,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()        
    
