import random
import pygame

class DLA:
    def __init__(self, spaceSize = (100,100)):
        self.spaceSize = spaceSize
        self.startAtom = (self.spaceSize[0]//2, self.spaceSize[1]//2)
        self.atoms = [self.startAtom]
        
        random.seed()
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
    
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    #three helpSpace modes: rectangle, simple and polygon
    def calculateStartPositions(self):
        return [(0,0), (0, self.spaceSize[1] - 1), (self.spaceSize[0] - 1, 0), (self.spaceSize[0] - 1, self.spaceSize[1] - 1)]
    
    #diagonal neighbours not considered
    def getNeighbours(self, atom):
        x,y = atom
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]

    #get the neighbours
    def isTouching(self, atom):
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
        for pos in self.calculateStartPositions():
            surface.set_at(pos, (255,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()            
    