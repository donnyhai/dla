import EXT_DLA_Circle as dc
import random
import pygame
from math import pow



class EXT_DLA_Circle_GUI(dc.EXT_DLA_Circle):
    
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
            
    #atom walk with noise reduction
    def doAtomWalk(self, position, bogoya = False):
        init_position = position
        isnear_counter = 0
        noise_counter = self.multiple_steps 
        move_direction = (0,0)
        aggregate_cond = True #decides whether neighbouring atom will be added to the cluster (in case of sticking probabilites like in bogoya MR2212061)
        bogoya_power = 2
        while True:
            if self.isTouching(position):
                if bogoya:
                    if random.random() < pow(self.numberOfNeighboursWithParticles(position) / len(self.getNeighbours(position)), bogoya_power):
                        aggregate_cond = True
                    else:
                        aggregate_cond = False
                
                if aggregate_cond:
                    self.addAtom(position)
                    break
                else:
                    position = self.calculateRandomStartPosition()
            
            if isnear_counter == 10:
                if not self.isNear(position):
                    position = self.calculateRandomStartPosition()
                isnear_counter = 0
            isnear_counter += 1
            
            if noise_counter == self.multiple_steps:
                new_position = random.choice(self.getNeighbours(position))
                move_direction = (new_position[0] - position[0], new_position[1] - position[1])
                position = new_position
                noise_counter = 0
            else:
                position = (position[0] + move_direction[0], position[1] + move_direction[1])
                noise_counter += 1
            
            
    def runProcess(self, atomsMax = 500, surface = None):
        counter = 0
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition(), True)
            
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
        
        for i in range(len(self.atoms)):
            surface.set_at(self.atoms[i], self.colors[(i//250)%len(self.colors)])
        #for atom in self.atoms:
        #    surface.set_at(atom, (150, 215, 182, 255))
            
        surface.set_at(self.middlePoint, (255,0,0,0))
        #if self.circleRadius > 0:
        #    pygame.draw.circle(surface, (255,0,0,0), self.middlePoint, self.circleRadius, 1)
        
        update_rect = pygame.Rect(self.minX, self.minY, self.maxX - self.minX, self.maxY - self.minY)
        pygame.display.update(update_rect) 
        
        
        
        
        
        
        
        
    #run process and render at the same time (with coloring) NEEDS SURFACE (this is quicker)
    def runProcess2(self, atomsMax = 500, surface = None):
        
        surface.fill((0,0,0,0))
        
        counter = 0
        for i in range(atomsMax):
            newpos = self.calculateRandomStartPosition()
            print(newpos)
            #if i > 200:
            #    self.doAtomWalk(newpos, surface, True)
            #else:
            #    self.doAtomWalk(newpos, surface)
            
            self.doAtomWalk(newpos, surface)
            
            #actualize values
            self.actualizeExtremeCoordinates()
            self.actualizeMiddlePoint()
            self.actualizeCircleRadius()
            
            
            surface.set_at(self.atoms[-1], self.colors[(i//100)%len(self.colors)])
            #if self.circleRadius > 0:
            #    pygame.draw.circle(surface, (255,0,0,0), self.middlePoint, self.circleRadius, 1)
            surface.set_at(self.middlePoint, (255,0,0,0))
            pygame.display.flip() 
            
            counter += 1
            print(i)
            
    