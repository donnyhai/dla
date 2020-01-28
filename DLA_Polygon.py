import random
import math
import pygame
import DLA

class DLA_Polygon(DLA.DLA):
    def __init__(self, spaceSize = (100,100)):
        super().__init__(spaceSize)
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        self.helpSpaceDelta = 6 #how far shall be the helpSpace be away of the outest atoms ?
        
        self.polygonSize = 10 #number of polygon points, must be even
        self.polygonPoints = self.calculatePolygonPoints((self.startAtom[0] - self.helpSpaceDelta, self.startAtom[1]), (self.startAtom[0] + self.helpSpaceDelta, self.startAtom[1]))
        
        random.seed()
        
    #you have two points p1, p2. calculate the n polygon with these two points as opposite laying points (n has to be even)
    def calculatePolygonPoints(self, p1, p2):
        r = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)) / 2 #radius
        innerAngle = 2 * math.pi / self.polygonSize #Innenwinkel am Mittelpunkt
        if p2[0] - p1[0] == 0: rotationAngle = math.pi / 2
        elif p2[1] - p1[1] == 0: rotationAngle = 0
        else: rotationAngle = math.atan(abs((p2[1] - p1[1])/(p2[0] - p1[0]))) #Verdrehungswinkel des polygons
        center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        polygonPoints = []
        for i in range(self.polygonSize):
            beta = i * innerAngle + rotationAngle
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
        
    #three helpSpace modes: rectangle, simple and polygon
    def calculateStartPositions(self):
        return self.polygonPoints
    
    #diagonal neighbours not considered
    def getNeighbours(self, atom):
        x,y = atom
        #diagonal neighbours or not ?
        return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh) and self.isInsidePolygon(neigh)]
        #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh) and self.isInsidePolygon(neigh)]
            
    def actualizeHelpSpace(self):
        dx = self.maxX - self.minX
        dy = self.maxY - self.minY
        r = math.sqrt(dx*dx + dy*dy) / self.helpSpaceDelta
        p1, p2 = (round(self.minX - dx/r), round(self.minY - dy/r)), (round(self.maxX + dx/r), round(self.maxY + dy/r))
        self.polygon = self.calculatePolygonPoints(p1, p2)
    
    def runProcess(self, atomsMax = 500, mode = "rectangle", render = False, surface = None):
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
        for pos in self.calculateStartPositions():
            surface.set_at(pos, (255,0,0,0))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()
            
    