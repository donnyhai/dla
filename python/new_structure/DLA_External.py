#last changed: 200627

import DLA

import random, cmath

class DLA_External(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        self.initializeHelpingStructures()
        
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
            
            
            
            
    def calculateRandomBigStartCircle(self):
        m = self.surroundCircle["middlePoint"] + cmath.rect(1/2 * random.random() * self.surroundCircle["radius"], random.random() * 2 * 3.142)
        self.bigStartCircle = {"middlePoint": m, "radius": random.uniform(1.5, 2) * self.surroundCircle["radius"]}
    
    #start position of the next random walk
    def calculateRandomStartPosition(self):
        startpos = self.bigStartCircle["middlePoint"] + cmath.rect(self.bigStartCircle["radius"], random.random() * 2 * 3.1416)
        return int(startpos.real) + int(startpos.imag) * 1j

    def initializeHelpingStructures(self):
        self.minX, self.maxX = 0, 0
        self.minY, self.maxY = 0, 0
        
        self.helpSpaceDelta = 1 #how far shall be the surroundCircle be away of the outest atoms?
        self.surroundCircle = {"middlePoint": self.atoms[0], "radius": self.helpSpaceDelta} #this a circle closely around the cluster
        
        self.bigStartCircle = {"middlePoint": None, "radius": None} #this is a circle certainly containing the surroundCircle. on this circles boundary atoms will start their random walks
        self.calculateRandomBigStartCircle()
        
    def actualizeHelpingStructures(self):
        x,y = self.atoms[-1].real, self.atoms[-1].imag
        self.minX, self.maxX = min(self.minX, x), max(self.maxX, x)
        self.minY, self.maxY  = min(self.minY, y), max(self.maxY, y)
        
        self.surroundCircle["middlePoint"] = ((self.minX + self.maxX) / 2) + ((self.minY + self.maxY) / 2) * 1j
        dx, dy = self.maxX - self.minX, self.maxY - self.minY
        self.surroundCircle["radius"] = abs(dx + dy * 1j) / 2 + self.helpSpaceDelta
    
        self.calculateRandomBigStartCircle()        