import random

class DLAProcess:
    def __init__(self, spaceSize = (100,100)):
        self.spaceSize = spaceSize
        self.startAtom = (self.spaceSize[0]//2, self.spaceSize[1]//2)
        self.atoms = [self.startAtom]
        
        random.seed()
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
        
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    def getNeighbours(self, atom, withDiagonals = False):
        x = atom[0]
        y = atom[1]
        if withDiagonals:
            return [neigh for neigh in [(x+1,y), (x+1,y-1), (x+1,y+1), (x-1,y), (x-1,y-1), (x-1,y+1),(x,y+1), (x,y-1)] if self.isInsideWorld(neigh)]
        else: 
            return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh)]
            
    #neighbours, default without diagonal neighbours
    def isTouching(self, atom, withDiagonals = False):
        return len(set(self.getNeighbours(atom, withDiagonals)).intersection(set(self.atoms))) > 0
    
    #atom random walk, default no walk onto diagonal fields
    def doAtomWalk(self, startPosition, withDiagonals = False):
        position = startPosition
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            nextNeighbours = self.getNeighbours(position, withDiagonals)
            position = random.choice(nextNeighbours)
    
    def runProcess(self, atomsMax = 20, withDiagonals = False):
        startPositions = [(0, 0), (0, self.spaceSize[1]//2), (0, self.spaceSize[1]-1), (self.spaceSize[0]-1, 0), (self.spaceSize[0]//2, 0), (self.spaceSize[0]//2, self.spaceSize[1]-1), (self.spaceSize[0]-1, self.spaceSize[1]//2), (self.spaceSize[0]-1, self.spaceSize[1]-1)]
        for i in range(atomsMax):
            startPosition = random.choice(startPositions)
            self.doAtomWalk(startPosition, withDiagonals)
            
dla = DLAProcess()
dla.runProcess()
            
            
            
    