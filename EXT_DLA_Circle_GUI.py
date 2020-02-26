import EXT_DLA_Circle as dc
import random
import pygame



class EXT_DLA_Circle_GUI(dc.EXT_DLA_Circle):
    
    #atom random walk
    def doAtomWalk(self, position, surface = None):
        position0 = position
        counter = 0
        #value = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            if counter == 10:
                #check, if atom is still near enough to the clusters center
                if not self.isNear(position):
                    position = position0 #reput on original starting position ? 
                    #position = self.calculateRandomStartPosition() #reput on a new random start position ?
                    #print(position)
                counter = 0
            counter += 1    
            position = random.choice(self.getNeighbours(position))
            
            ##nice coloring adding
            #if surface is not None:
            #    surface.set_at(position, (255,value % 255,0,0))
            #    value += 10
                
    def runProcess(self, atomsMax = 500, surface = None):
        counter = 0
        for i in range(atomsMax):
            newpos = self.calculateRandomStartPosition()
            print(newpos)
            self.doAtomWalk(newpos)
            
            #actualize values
            self.actualizeExtremeCoordinates()
            self.actualizeMiddlePoint()
            self.actualizeCircleRadius()
            
            if counter == 7:
                if surface is not None:
                    self.render2(surface)
                counter = 0
            
            counter += 1
            print(i)
            
    def render2(self, surface):
        surface.fill((0,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        if self.circleRadius > 0:
            pygame.draw.circle(surface, (255,0,0,0), self.middlePoint, self.circleRadius, 1)
        surface.set_at(self.middlePoint, (255,0,0,0))
        pygame.display.flip() 
            
    