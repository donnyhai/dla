import random
import pygame
import DLA

class INT_DLA(DLA.DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        self.startPosition = self.atoms[0]
        
        random.seed()
        
    def getNeighbours(self, atom):
        x,y = atom
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]

    def isInside(self, atom):
        return atom in self.atoms
    
    #atom random walk
    def doAtomWalk(self, position):
        while True:
            if not self.isInside(position):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position))
    
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(self.startPosition)
            print(i)

    def render(self, surface):
        surface.fill((0,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()            
    