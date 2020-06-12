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
        
        self.circleparameter = 0.85
        
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
        self.circleRadius = int(self.circleparameter * math.sqrt(dx*dx + dy*dy) // 2 + self.helpSpaceDelta)
        
    def isNear(self, pos):
        return math.sqrt((pos[0] - self.middlePoint[0])**2 + (pos[1] - self.middlePoint[1])**2) < self.circleRadius
        
    #start position of the next random walk
    def calculateRandomStartPosition(self):
        alpha = random.random() * 2 * 3.1416
        dx, dy = math.cos(alpha) * self.circleRadius, math.sin(alpha) * self.circleRadius
        return (self.middlePoint[0] + round(dx), self.middlePoint[1] + round(dy))
    
    
    
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
    
    
    def runProcess(self, atomsMax = 500):
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition(), True)
            
            #actualize values
            self.actualizeExtremeCoordinates()
            self.actualizeMiddlePoint()
            self.actualizeCircleRadius()
            
            print(i)
            
    