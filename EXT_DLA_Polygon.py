import random
import math
import EXT_DLA

class EXT_DLA_Polygon(EXT_DLA.EXT_DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        self.helpSpaceDelta = 4 #how far shall be the helpSpace be away of the outest atoms ?
        
        self.polygonSize = 12 #number of polygon points, must be even
        self.middleAngle = 2 * math.pi / self.polygonSize #Mittelpunktswinkel
        self.polygonPoints = self.calculatePolygonPoints((self.startAtom[0] - self.helpSpaceDelta, self.startAtom[1]), (self.startAtom[0] + self.helpSpaceDelta, self.startAtom[1]))
        
        random.seed()
        
    #you have two points p1, p2. calculate the n polygon with these two points as opposite laying points (n has to be even)
    def calculatePolygonPoints(self, p1, p2, randomRotation = 0):
        if p1[0] > p2[0]:
            c = p2
            p2 = p1
            p1 = c
        r = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)) / 2 #radius
        if p2[0] == p1[0]: rotationAngle = math.pi / 2
        else: rotationAngle = math.atan((p2[1] - p1[1])/abs(p2[0] - p1[0])) #Verdrehungswinkel des polygons
        center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        polygonPoints = []
        for i in range(self.polygonSize):
            beta = i * self.middleAngle + rotationAngle + randomRotation
            polygonPoints.append((round(r * math.cos(beta) + center[0]), round(-r * math.sin(beta) + center[1])))
        return polygonPoints
    
    def isInsidePolygon(self, position):
        if position in self.polygonPoints:
            return True
        def euclideanMetric(vector):
            return math.sqrt(sum([x*x for x in vector]))
        def scalarProduct(vec1, vec2):
            return sum([vec1[i] * vec2[i] for i in range(len(vec1))])
        n = self.polygonSize
        p = self.polygonPoints
        innerAngle = math.pi - 2* math.pi / n
        for i in range(n):
            bvec = (p[(i+1)%n][0] - p[i][0], p[(i+1)%n][1] - p[i][1])
            cvec = (position[0]-p[i][0], position[1]-p[i][1])
            if scalarProduct(bvec, cvec) / (euclideanMetric(bvec) * euclideanMetric(cvec)) <= math.cos(innerAngle):
                return False
        return True
        
    def calculateStartPositions(self):
        return self.polygonPoints
    
    def getNeighbours(self, atom):
        x,y = atom
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh)]
        #return [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)]
            
    def actualizeHelpSpace(self, addRotation = False):
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        r = math.sqrt(dx*dx + dy*dy) / self.helpSpaceDelta
        p1, p2 = (round(self.minX - dx/r), round(self.minY - dy/r)), (round(self.maxX + dx/r), round(self.maxY + dy/r))
        self.polygonPoints = self.calculatePolygonPoints(p1, p2, addRotation)
    
    #atom random walk
    def doAtomWalk(self, position):
        position0 = position
        counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                break
            if counter == 10:
                if not self.isInsidePolygon(position):
                    position = position0
                counter = 0
            counter += 1    
            position = random.choice(self.getNeighbours(position))
    
    def runProcess(self, atomsMax = 500):
        counter = 0
        randomRotation = 0
        for i in range(atomsMax):
            #self.doAtomWalk(random.choice(self.calculateStartPositions()), render, surface)
            self.doAtomWalk(random.choice(self.calculateStartPositions()))
            
            #actualizce atomRectangle depending on the last added atom 
            x,y = self.atoms[-1]
            self.minX = min(self.minX, x)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, y)
            self.maxY = max(self.maxY, y)
            
            if counter == 5:
                randomRotation = random.choice([0,1,2,3,4,5]) * self.middleAngle / 6
                counter = 0
            self.actualizeHelpSpace(randomRotation)
            
            counter += 1
            print(i)
            
    