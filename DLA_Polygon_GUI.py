import DLA_Polygon as dp
import random
import pygame



class DLA_Polygon_GUI(dp.DLA_Polygon):
    
    #atom random walk
    def doAtomWalk(self, position, surface = None):
        position0 = position
        counter = 0
        value = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            if counter == 10:
                if not self.isInsidePolygon(position):
                    position = position0
                counter = 0
            counter += 1    
            position = random.choice(self.getNeighbours(position))
            if surface is not None:
                surface.set_at(position, (255,value % 255,0,0))
                value += 10
                
    def runProcess(self, atomsMax = 500, surface = None):
        counter = 0
        counter2 = 0
        randomRotation = 0
        for i in range(atomsMax):
            #self.doAtomWalk(random.choice(self.calculateStartPositions()), surface)
            self.doAtomWalk(random.choice(self.calculateStartPositions()))
            
            #actualizce atomRectangle depending on the last added atom 
            x,y = self.atoms[-1]
            self.minX = min(self.minX, x)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, y)
            self.maxY = max(self.maxY, y)
            
            if counter2 == 5:
                randomRotation = random.choice([0,1,2,3,4,5]) * self.middleAngle / 6
                counter2 = 0
            self.actualizeHelpSpace(randomRotation)
            
            if counter == 7:
                if surface is not None:
                    self.render(surface)
                counter = 0
            
            counter += 1
            counter2 += 1
            print(i)
            
    def render2(self, surface):
        for pos in self.calculateStartPositions():
            surface.set_at(pos, (255,0,0,0))
        pygame.display.flip()
            
    