import pygame, sys
import saveObjects as so
import DLA
import DLA_Rectangle
import DLA_Polygon      
import math          
  
pygame.init()
pygame.display.init()

windowSize = (1000, 1000)
atomsMax = 3000

dlaStandard = DLA.DLA(windowSize)
dlaRectangle = DLA_Rectangle.DLA_Rectangle(windowSize)
dlaPolygon = DLA_Polygon.DLA_Polygon(windowSize)

def printProcess(dla, live = False, atomsMax = None):
    surface = pygame.display.set_mode(windowSize,0,32)
    pygame.display.update()
    counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if counter == 0:
                    if live and atomsMax is not None:
                        dla.runProcess(atomsMax, render = True, surface = surface)
                    else:
                        dla.render(surface)
                    counter += 1
                    
        pygame.display.update()
    
    




def testPoly():
    
    n = 10
    p1,p2 = None, None
    p = None
    
    #you have two points p1, p2. calculate the n polygon with these two points as opposite laying points (n has to be even)
    def calculatePolygonPoints(p1, p2):
        if p1[0] > p2[0]:
            c = p2
            p2 = p1
            p1 = c
        r = math.sqrt(math.pow(p1[0] - p2[0], 2) + math.pow(p1[1] - p2[1], 2)) / 2 #radius
        innerAngle = 2 * math.pi / n #Innenwinkel am Mittelpunkt
        if p2[0] - p1[0] == 0: rotationAngle = math.pi / 2
        else: rotationAngle = math.atan((p2[1] - p1[1])/abs(p2[0] - p1[0])) #Verdrehungswinkel des polygons
        center = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
        polygonPoints = []
        for i in range(n):
            beta = i * innerAngle + rotationAngle
            polygonPoints.append((round(r * math.cos(beta) + center[0]), round(-r * math.sin(beta) + center[1])))
        return polygonPoints
    
    def isInsidePolygon(position):
        
        if position in p:
            return True
        
        def euclideanMetric(vector):
            return math.sqrt(sum([x*x for x in vector]))
        def scalarProduct(vec1, vec2):
            return sum([vec1[i] * vec2[i] for i in range(len(vec1))])
        innerAngle = math.pi - 2* math.pi / n
        for i in range(n):
            bvec = (p[(i+1)%n][0] - p[i][0], p[(i+1)%n][1] - p[i][1])
            cvec = (position[0]-p[i][0], position[1]-p[i][1])
            if scalarProduct(bvec, cvec) / (euclideanMetric(bvec) * euclideanMetric(cvec)) <= math.cos(innerAngle):
                return False
        return True
    
    surface = pygame.display.set_mode(windowSize,0,32)
    pygame.display.update()
    running = True
    counter = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if counter == 0:
                   p1 = event.pos 
                   surface.set_at(p1, (255,255,255,255))
                   counter += 1
                elif counter == 1:
                    p2 = event.pos
                    surface.set_at(p2, (255,255,255,255))
                    counter += 1
                    p = calculatePolygonPoints(p1,p2)
                    for pos in p:
                        surface.set_at(pos, (255,0,0,0))
                elif counter == 2:
                    surface.set_at(event.pos, (255,255,255,255))
                    print(isInsidePolygon(event.pos))
                    counter += 1
                elif counter == 3:
                    surface.fill((0,0,0,0))
                    p,p1,p2 = None, None, None
                    counter = 0
                
                    
        pygame.display.update()




def printPoints(points):
    surface = pygame.display.set_mode(windowSize,0,32)
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                for point in points:
                    surface.set_at(point, (255,255,255,255))
                    
        pygame.display.update()



#newfile = "objects/dla2.p"
#so.saveObject(dla, newfile)
#getdla = so.getObject("objects/")



