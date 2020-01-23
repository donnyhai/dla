import random

class DLAProcess:
    def __init__(self, spaceSize = [200,200]):
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
            [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh)]
            
    #neighbours, default without diagonal neighbours
    def isTouching(self, atom, withDiagonals = False):
        return len(set(self.getNeighbours(atom, withDiagonals) and self.atoms)) > 0
    
    #atom random walk, default no walk onto diagonal fields
    def startAtomWalk(self, startPosition, withDiagonals = False):
        isWalking = True
        position = startPosition
        while isWalking:
            nextNeighbours = self.getNeighbours(position, withDiagonals)
            position = random.choice(nextNeighbours)
            
            
            
    