import random

class DLAProcess:
    def __init__(self, spaceSize = (100,100)):
        self.spaceSize = spaceSize
        self.startAtom = (self.spaceSize[0]//2, self.spaceSize[1]//2)
        self.atoms = [self.startAtom]
        
        self.atomRectanglePos = (self.startAtom[0] - 3, self.startAtom[1] - 3)
        self.atomRectangleSize = (6,6)
        self.atomRectangleDelta = 10 #how far shall be the atomRectangle be away of the outest atoms ?
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        random.seed()
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
    
    def isInsideAtomRectangle(self, atom):
        return self.atomRectanglePos[0] <= atom[0] < self.atomRectanglePos[0] + self.atomRectangleSize[0] and self.atomRectanglePos[1] <= atom[1] < self.atomRectanglePos[1] + self.atomRectangleSize[1]
        
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    def getAtomRectangleCoords(self):
        pass
    
    def calculateStartPositions(self, useAtomRectangle = True):
        if useAtomRectangle:
            x0,y0 = self.atomRectanglePos
            x,y = self.atomRectangleSize
        else:
            x0,y0 = (0,0)
            x,y = self.spaceSize
        l1 = [(x0, y0), (x0, y0 + y//10), (x0, y0 + y//6), (x0, y0 + y//5), (x0, y0 + y//4), (x0, y0 + y//3), (x0, y0 + y//2), (x0, y0 + 2*y//3), (x0, y0 + 3*y//4), (x0, y0 + 4*y//5), (x0, y0 + 5*y//6), (x0, y0 + 9*y//10), (x0, y0 + y-1)] 
        l2 = [(x0 + x-1, y0), (x0 + x-1, y0 + y//10), (x0 + x-1, y0 + y//6), (x0 + x-1, y0 + y//5), (x0 + x-1, y0 + y//4), (x0 + x-1, y0 + y//3), (x0 + x-1, y0 + y//2), (x0 + x-1, y0 + 2*y//3), (x0 + x-1, y0 + 3*y//4), (x0 + x-1, y0 + 4*y//5), (x0 + x-1, y0 + 5*y//6), (x0 + x-1, y0 + y-1)]
        l3 = [(x0 + x//10, y0), (x0 + x//6, y0), (x0 + x//5, y0), (x0 + x//4, y0), (x0 + x//3, y0), (x0 + x//2, y0), (x0 + 2*x//3, y0), (x0 + 3*x//4, y0), (x0 + 4*x//5, y0), (x0 + 5*x//6, y0), (x0 + 9*x//10, y0)]
        l4 = [(x0 + x//10, y0 + y-1), (x0 + x//6, y0 + y-1), (x0 + x//5, y0 + y-1), (x0 + x//4, y0 + y-1), (x0 + x//3, y0 + y-1), (x0 + x//2, y0 + y-1), (x0 + 2*x//3, y0 + y-1), (x0 + 3*x//4, y0 + y-1), (x0 + 4*x//5, y0 + y-1), (x0 + 5*x//6, y0 + y-1), (x0 + 9*x//10, y0 + y-1)]
        return l1 + l2 + l3 + l4
    
    #diagonal neighbours not considered
    def getNeighbours(self, atom, useAtomRectangle = True):
        x,y = atom
        if useAtomRectangle:
            return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh) and self.isInsideAtomRectangle(neigh)]
        else:
            return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh)]
            
    #get the neighbours, default is neighbours in atomRectangle
    def isTouching(self, atom):
        return len(set(self.getNeighbours(atom)).intersection(set(self.atoms))) > 0
    
    #atom random walk
    def doAtomWalk(self, position):
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position))
    
    def runProcess(self, atomsMax = 20):
        for i in range(atomsMax):
            self.doAtomWalk(random.choice(self.calculateStartPositions()))
            
            #actualizce atomRectangle depending on the last added 
            x,y = self.atoms[-1]
            self.minX = min(self.minX, x)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, y)
            self.maxY = max(self.maxY, y)
            
            self.atomRectanglePos = (self.minX - self.atomRectangleDelta, self.minY - self.atomRectangleDelta)
            self.atomRectangleSize = (self.maxX - self.minX + 2*self.atomRectangleDelta, self.maxY - self.minY + 2*self.atomRectangleDelta)
            
        
            
            
            
    