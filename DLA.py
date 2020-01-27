import random
import math

class DLAProcess:
    def __init__(self, spaceSize = (100,100)):
        self.spaceSize = spaceSize
        self.startAtom = (self.spaceSize[0]//2, self.spaceSize[1]//2)
        self.atoms = [self.startAtom]
        self.helpSpaceDelta = 6 #how far shall be the helpSpace be away of the outest atoms ?
        
        self.atomRectanglePos = (self.startAtom[0] - 3, self.startAtom[1] - 3)
        self.atomRectangleSize = (6,6)
        
        self.polygonSize = 10 #number of polygon points, must be even
        self.polygon = self.calculatePolygonPoints((self.startAtom[0] - self.helpSpaceDelta, self.startAtom[1]), (self.startAtom[0] + self.helpSpaceDelta, self.startAtom[1]))
        
        self.minX, self.maxX = self.startAtom[0],self.startAtom[0]
        self.minY, self.maxY = self.startAtom[1],self.startAtom[1]
        
        random.seed()
        
    def isInsideWorld(self, atom):
        return 0 <= atom[0] < self.spaceSize[0] and 0 <= atom[1] < self.spaceSize[1]
    
    def isInsideAtomRectangle(self, atom):
        return self.atomRectanglePos[0] <= atom[0] < self.atomRectanglePos[0] + self.atomRectangleSize[0] and self.atomRectanglePos[1] <= atom[1] < self.atomRectanglePos[1] + self.atomRectangleSize[1]
        
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    #you have two points p1, p2. calculate the n polygon with these two points as opposite laying points (n has to be even)
    def calculatePolygonPoints(self, p1, p2):
        n = self.polygonSize
        standardCenter = (0,0)
        standardPoints = []
        for i in range(n):
            pass
        alpha = 2 * math.pi / self.polygonSize #Innenwinkel
        a = math.sqrt((p1[0] - p2[0])^2 + (p1[1] - p2[1])^2) * math.tan(math.pi / self.polygonSize) #Seitenlänge
        polygonPoints = [p1, p2]
        for i in range(self.polygonSize/2):
            pass
    
    def isInsidePolygon(self, position):
        pass
    
    #three helpSpace modes: rectangle, simple and polygon
    def calculateStartPositions(self, mode = "rectangle"):
        if mode == "rectangle":
            #x0,y0 = (0,0) #in case of using the full space as starting area
            #x,y = self.spaceSize
            x0,y0 = self.atomRectanglePos
            x,y = self.atomRectangleSize
            #return [self.atomRectanglePos, (x0 + x-1, y0 + y-1)]
            l1 = [(x0, y0), (x0, y0 + y//10), (x0, y0 + y//6), (x0, y0 + y//5), (x0, y0 + y//4), (x0, y0 + y//3), (x0, y0 + y//2), (x0, y0 + 2*y//3), (x0, y0 + 3*y//4), (x0, y0 + 4*y//5), (x0, y0 + 5*y//6), (x0, y0 + 9*y//10), (x0, y0 + y-1)] 
            l2 = [(x0 + x-1, y0), (x0 + x-1, y0 + y//10), (x0 + x-1, y0 + y//6), (x0 + x-1, y0 + y//5), (x0 + x-1, y0 + y//4), (x0 + x-1, y0 + y//3), (x0 + x-1, y0 + y//2), (x0 + x-1, y0 + 2*y//3), (x0 + x-1, y0 + 3*y//4), (x0 + x-1, y0 + 4*y//5), (x0 + x-1, y0 + 5*y//6), (x0 + x-1, y0 + y-1)]
            l3 = [(x0 + x//10, y0), (x0 + x//6, y0), (x0 + x//5, y0), (x0 + x//4, y0), (x0 + x//3, y0), (x0 + x//2, y0), (x0 + 2*x//3, y0), (x0 + 3*x//4, y0), (x0 + 4*x//5, y0), (x0 + 5*x//6, y0), (x0 + 9*x//10, y0)]
            l4 = [(x0 + x//10, y0 + y-1), (x0 + x//6, y0 + y-1), (x0 + x//5, y0 + y-1), (x0 + x//4, y0 + y-1), (x0 + x//3, y0 + y-1), (x0 + x//2, y0 + y-1), (x0 + 2*x//3, y0 + y-1), (x0 + 3*x//4, y0 + y-1), (x0 + 4*x//5, y0 + y-1), (x0 + 5*x//6, y0 + y-1), (x0 + 9*x//10, y0 + y-1)]
            return l1 + l2 + l3 + l4
        elif mode == "simple": #just the corners of the polygon
            x0,y0 = self.atomRectanglePos
            x,y = self.atomRectangleSize
            return [(x0, y0), (x0, y0 + y-1), (x0 + x-1, y0), (x0 + x-1, y0 + y-1)]
        elif mode == "polygon":
            return self.polygon
    
    #diagonal neighbours not considered
    def getNeighbours(self, atom, mode = "rectangle"):
        x,y = atom
        if mode == "rectangle" or "simple":
            #diagonal neighbours or not ?
            return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh) and self.isInsideAtomRectangle(neigh)]
            #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh) and self.isInsideAtomRectangle(neigh)]
        elif mode == "polygon":
            #diagonal neighbours or not ?
            return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1), (x-1,y+1), (x+1,y-1), (x+1,y+1)] if self.isInsideWorld(neigh) and self.isInsidePolygon(neigh)]
            #return [neigh for neigh in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)] if self.isInsideWorld(neigh) and self.isInsidePolygon(neigh)]
            
    #get the neighbours, default is neighbours in atomRectangle
    def isTouching(self, atom, mode = "rectangle"):
        return len(set(self.getNeighbours(atom, mode)).intersection(set(self.atoms))) > 0
    
    def actualizeHelpSpace(self, mode = "rectangle"):
        if mode == "rectangle":
            self.atomRectanglePos = (self.minX - self.helpSpaceDelta, self.minY - self.helpSpaceDelta)
            self.atomRectangleSize = (self.maxX - self.minX + 2*self.helpSpaceDelta, self.maxY - self.minY + 2*self.helpSpaceDelta)
        elif mode == "polygon":
            dx = self.maxX - self.minX
            dy = self.maxY - self.minY
            r = math.sqrt(dx^2 + dy^2) / self.helpSpaceDelta
            p1, p2 = (self.minX - dx//r, self.minY - dy//r), (self.maxX + dx//r, self.maxY + dy//r)
            self.polygon = self.calculatePolygonPoints(p1, p2)
    
    #atom random walk
    def doAtomWalk(self, position, mode = "rectangle"):
        while True:
            if self.isTouching(position, mode):
                self.addAtom(position)
                break
            position = random.choice(self.getNeighbours(position, mode))
    
    def runProcess(self, atomsMax = 500, mode = "rectangle", render = False, surface = None):
        counter = 0
        for i in range(atomsMax):
            self.doAtomWalk(random.choice(self.calculateStartPositions(mode)), mode)
            
            #actualizce atomRectangle depending on the last added atom 
            x,y = self.atoms[-1]
            self.minX = min(self.minX, x)
            self.maxX = max(self.maxX, x)
            self.minY = min(self.minY, y)
            self.maxY = max(self.maxY, y)
            
            self.actualizeHelpSpace(mode)
            
            counter += 1
            if counter == 7:
                if render and surface is not None:
                    self.render(surface)
                counter = 0
            
            print(i)
            
    def render(self, surface):
        pass
            
    