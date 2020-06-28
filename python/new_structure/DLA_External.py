#last changed: 200627

import DLA

import random

class DLA_External(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        
    #atom random walk from position until hitting cluster
    def doAtomWalk(self, position):
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position)) #walking on diagonal neighbours? here not
    
    def runProcess(self, atomsMax = 500):
        startPosition = 1 + 1 * 1j #how to choose starting positions? problem: mathematically they start from infinity
        for i in range(atomsMax):
            self.doAtomWalk(startPosition) #what happens if atom walks "away" from the cluster? calculation takes too long. 
            print(i)

