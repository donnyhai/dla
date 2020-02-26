import random
import pygame
import DLA

class INT_DLA(DLA.DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        self.startPosition = self.atoms[0]
        
        random.seed()
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
    
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    def getNeighbours(self, atom):
        x,y = atom
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]

    def isOutside(self, atom):
        return len(set(self.getNeighbours(atom)).intersection(set(self.atoms))) > 0
    
    #atom random walk
    def doAtomWalk(self, position):
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position))
    
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(random.choice(self.calculateStartPositions()))
            print(i)

    def render(self, surface):
        surface.fill((0,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()            
    