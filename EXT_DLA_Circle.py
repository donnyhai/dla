import random
import math
import EXT_DLA

class EXT_DLA_Circle(EXT_DLA.EXT_DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        self.middlePoint = self.atoms[0]
        self.helpSpaceDelta = 1 #how far shall be the helpSpace be away of the outest atoms ?
        self.circleRadius = self.helpSpaceDelta
        
        random.seed()
    
    def actualizeExtremeCoordinates(self):
        x,y = self.atoms[-1]
        self.minX = min(self.minX, x)
        self.maxX = max(self.maxX, x)
        self.minY = min(self.minY, y)
        self.maxY = max(self.maxY, y)
    
    def actualizeMiddlePoint(self):
        self.middlePoint = ((self.minX + self.maxX) // 2, (self.minY + self.maxY) // 2)
    
    def actualizeCircleRadius(self):
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        self.circleRadius = int(math.sqrt(dx*dx + dy*dy) // 2 + self.helpSpaceDelta)
        
    def isNear(self, pos):
        return math.sqrt((pos[0] - self.middlePoint[0])**2 + (pos[1] - self.middlePoint[1])**2) < self.circleRadius
        
    #start position of the next random walk
    def calculateRandomStartPosition(self):
        alpha = random.random() * 2 * 3.1416
        dx, dy = math.cos(alpha) * self.circleRadius, math.sin(alpha) * self.circleRadius
        return (self.middlePoint[0] + round(dx), self.middlePoint[1] + round(dy))
    
    #atom random walk
    def doAtomWalk(self, position):
        #position0 = position
        counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            if counter == 10:
                #check, if atom is still near enough to the clusters center
                if not self.isNear(position):
                    #position = position0 #reput on original starting position postion0 ? 
                    position = self.calculateRandomStartPosition() #reput on a new random start position ?
                counter = 0
            counter += 1    
            position = random.choice(self.getNeighbours(position))
    
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            
            #actualize values
            self.actualizeExtremeCoordinates()
            self.actualizeMiddlePoint()
            self.actualizeCircleRadius()
            
            print(i)
            
    