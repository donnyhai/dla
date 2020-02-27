import random
import pygame
import INT_DLA

class INT_DLA_GUI(INT_DLA.INT_DLA):
   
    #atom random walk
    def doAtomWalk(self, position, surface = None):
        value = 0
        while True:
            if not self.isInside(position):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position))
            
            #nice coloring adding
            if surface is not None:
                surface.set_at(position, (255,value % 255,0,0))
                value += 10
    
    def runProcess(self, atomsMax = 500, surface = None):
        counter = 0
        for i in range(atomsMax):
            #self.doAtomWalk(self.startPosition)
            self.doAtomWalk(self.startPosition, surface)
            
            if counter == 10:
                if surface is not None:
                    self.render(surface)
                counter = 0
            counter += 1
            
            print(i)

    def render(self, surface):
        #surface.fill((0,0,0,0))
        #for atom in self.atoms:
        #    surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()            
    