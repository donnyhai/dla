
class DLA:
    def __init__(self, spaceSize = (100,100)):
        self.spaceSize = spaceSize
        self.startAtom = (self.spaceSize[0]//2, self.spaceSize[1]//2)
        self.atoms = [self.startAtom]
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
    
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    def getNeighbours(self, atom):
        x,y = atom
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]

    def doAtomWalk(self, position):
        pass
    
    def runProcess(self, atomsMax = 500):
        pass

    def render(self, surface):
        pass        
    