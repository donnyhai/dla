import DLA
import random
import math
import pygame

class DLA_Rectangle(DLA.DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        self.helpSpaceDelta = 6 #how far shall be the helpSpace be away of the outest atoms ?
        
        self.atomRectanglePos = (self.startAtom[0] - 3, self.startAtom[1] - 3)
        self.atomRectangleSize = (6,6)
        
        random.seed()
        
    def isInsideAtomRectangle(self, atom):
        return self.atomRectanglePos[0] <= atom[0] < self.atomRectanglePos[0] + self.atomRectangleSize[0] and self.atomRectanglePos[1] <= atom[1] < self.atomRectanglePos[1] + self.atomRectangleSize[1]
        
    #three helpSpace modes: rectangle, simple and polygon
    def calculateStartPositions(self):
        #x0,y0 = (0,0) #in case of using the full space as starting area
        #x,y = self.spaceSize
        x0,y0 = self.atomRectanglePos
        x,y = self.atomRectangleSize
        #return [self.atomRectanglePos, (x0 + x-1, y0 + y-1)]
        l1 = [(x0, y0), (x0, y0 + y//10), (x0, y0 + y//6), (x0, y0 + y//5), (x0, y0 + y//4), (x0, y0 + y//3), (x0, y0 + y//2), (x0, y0 + 2*y//3), (x0, y0 + 3*y//4), (x0, y0 + 4*y//5), (x0, y0 + 5*y//6), (x0, y0 + 9*y//10), (x0, y0 + y-1)] 
        l2 = [(x0 + x-1, y0), (x0 + x-1, y0 + y//10), (x0 + x-1, y0 + y//6), (x0 + x-1, y0 + y//5), (x0 + x-1, y0 + y//4), (x0 + x-1, y0 + y//3), (x0 + x-1, y0 + y//2), (x0 + x-1, y0 + 2*y//3), (x0 + x-1, y0 + 3*y//4), (x0 + x-1, y0 + 4*y//5), (x0 + x-1, y0 + 5*y//6), (x0 + x-1, y0 + y-1)]
        l3 = [(x0 + x//10, y0), (x0 + x//6, y0), (x0 + x//5, y0), (x0 + x//4, y0), (x0 + x//3, y0), (x0 + x//2, y0), (x0 + 2*x//3, y0), (x0 + 3*x//4, y0), (x0 + 4*x//5, y0), (x0 + 5*x//6, y0), (x0 + 9*x//10, y0)]
        l4 = [(x0 + x//10, y0 + y-1), (x0 + x//6, y0 + y-1), (x0 + x//5, y0 + y-1), (x0 + x//4, y0 + y-1), (x0 + x//3, y0 + y-1), (x0 + x//2, y0 + y-1), (x0 + 2*x//3, y0 + y-1), (x0 + 3*x//4, y0 + y-1), (x0 + 4*x//5, y0 + y-1), (x0 + 5*x//6, y0 + y-1), (x0 + 9*x//10, y0 + y-1)]
        return l1 + l2 + l3 + l4
    
    #diagonal neighbours not considered
    def getNeighbours(self, atom):
        x,y = atom
        #diagonal neighbours or not ?
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh) and self.isInsideAtomRectangle(neigh)]
        #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh) and self.isInsideAtomRectangle(neigh)]
            
    def actualizeHelpSpace(self):
        self.atomRectanglePos = (self.minX - self.helpSpaceDelta, self.minY - self.helpSpaceDelta)
        self.atomRectangleSize = (self.maxX - self.minX + 2*self.helpSpaceDelta, self.maxY - self.minY + 2*self.helpSpaceDelta)
    
    def runProcess(self, atomsMax = 500, render = False, surface = None):
        counter = 0
        for i in range(atomsMax):
            self.doAtomWalk(random.choice(self.calculateStartPositions()))
            
            #actualizce atomRectangle depending on the last added atom 
            x,y = self.atoms[-1]
            self.minX = min(self.minX, x)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, y)
            self.maxY = max(self.maxY, y)
            
            self.actualizeHelpSpace()
            
            counter += 1
            if counter == 7:
                if render and surface is not None:
                    self.render(surface)
                counter = 0
            
            print(i)
            
    def render(self, surface):
        surface.fill((0,0,0,0))
        for i in range(self.atomRectangleSize[0]):
            for j in range(self.atomRectangleSize[1]):
                if i == 0 or i == self.atomRectangleSize[0] - 1 or j == 0 or j == self.atomRectangleSize[1] - 1:
                    surface.set_at((self.atomRectanglePos[0] + i, self.atomRectanglePos[1] + j), (255, 117, 71, 255))
        for pos in self.calculateStartPositions():
            surface.set_at(pos, (150, 215, 182, 255))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()
            
    