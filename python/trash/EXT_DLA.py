import random
import pygame
import DLA

class EXT_DLA(DLA.DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        self.multiple_steps = 0
        self.colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]
        self.actual_color = self.colors[0]
        
        random.seed()
        
    def getNeighbours(self, atom):
        x,y = atom
        return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] #just up, down, left, right
        #return [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
        #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]

    def numberOfNeighboursWithParticles(self, atom):
        return len(set(self.getNeighbours(atom)).intersection(set(self.atoms)))

    def isTouching(self, atom):
        return self.numberOfNeighboursWithParticles(atom) > 0
    
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
        
        for i in range(len(self.atoms)):
            surface.set_at(self.atoms[i], self.colors[(i//250)%len(self.colors)])
        #for atom in self.atoms:
        #    surface.set_at(atom, (150, 215, 182, 255))
        
        pygame.display.flip()            
    