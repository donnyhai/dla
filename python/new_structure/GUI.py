import pygame, sys
#import saveObjects as so
import DLA
#import DLA_Rectangle
#import EXT_DLA_Polygon   
#import DLA_Polygon_GUI  
#import EXT_DLA_Circle 
#import EXT_DLA_Circle_GUI
#import INT_DLA
#import INT_DLA_GUI
import math, cmath
#import DLA_approx1
#import DLA_approx1_GUI
#import Reverse_DLA
#import DLA_approx3
import DLA_GUI
import DLA_External_Circle as dec
import DLA_External_Circle_GUI as decg
import DLA_Reverse_Circle as drc
import DLA_Reverse_Circle_GUI as drcg
import DLA_Reverse_Rect as drr
import DLA_Reverse_Rect_GUI as drrg
import DLA_Approx3_GUI as dag
  
pygame.init()
pygame.display.init()

windowSize = (1000, 1000)
atomsMax = 3000

#d = DLA.DLA(windowSize)
#ec = EXT_DLA_Circle.EXT_DLA_Circle(windowSize)
#ecg = EXT_DLA_Circle_GUI.EXT_DLA_Circle_GUI(windowSize)
#i = INT_DLA.INT_DLA(windowSize)
#ig = INT_DLA_GUI.INT_DLA_GUI(windowSize)

#rd = Reverse_DLA.Reverse_DLA(windowSize)

#approx1: very bad approximation
#1 = DLA_approx1.DLA_approx1(windowSize)
#a1g = DLA_approx1_GUI.DLA_approx1_GUI(windowSize)

#a3 = DLA_approx3.DLA_approx3(windowSize)

d0 = decg.DLA_External_Circle_GUI()
d0.runProcess(350)
#dg = DLA_GUI.DLA_GUI(dc.atoms)

#d1 = decg.DLA_External_Circle_GUI()
#d1.runProcess(300)

#d2 = drcg.DLA_Reverse_Circle_GUI()
#d2.runProcess(300)

#d3 = drrg.DLA_Reverse_Rect_GUI()
#d3.runProcess(300)

#d4 = dag.DLA_Approx3_GUI()
#d4.runProcess(200)

def printProcess(dla, atomsMax = None):
    surface = pygame.display.set_mode(windowSize,0,32)
    surface.fill((0,0,0,0))
    pygame.display.update()
    counter = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if counter == 0:
                    if atomsMax is not None:
                        #dla.runProcess2(atomsMax, surface = surface) #nice coloring
                        dla.runProcessLive(atomsMax, surface = surface)
                    else:
                        dla.render(surface)
                    counter += 1
                    
        pygame.display.update()
    
    





























###################### Test functions ############################


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



#newfile = "objects/reverse_dla_radius250_particles7879.p"
#so.saveObject(rd, newfile)
#getdla = so.getObject(newfile)


#checking function calculateAnglesIntervall in DLA_approx3
def checkLines(dla, point):
    surface = pygame.display.set_mode(windowSize,0,32)
    surface.fill((0,0,0,0))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                dla.render(surface)
                
                angleIntervall = dla.calculateAnglesIntervall(point)
                maxRel = cmath.rect(50, angleIntervall[1])
                minRel = cmath.rect(50, angleIntervall[0])
                maxPoint = maxRel - point + 500 + 500 * 1j
                maxPoint = int(maxPoint.real) + int(maxPoint.imag) * 1j
                minPoint = minRel - point + 500 + 500 * 1j
                minPoint = int(minPoint.real) + int(minPoint.imag) * 1j
                
                print(maxPoint)
                print(minPoint)
                
                pygame.draw.line(surface, (255,0,0), (point.real, point.imag), (minPoint.real, minPoint.imag))
                pygame.draw.line(surface, (255,0,0), (point.real, point.imag), (maxPoint.real, maxPoint.imag))
                
                pygame.draw.line(surface, (255,255,0), (500,500), (cmath.rect(10, -0.7).real, cmath.rect(10, -0.7).imag))
                
                surface.set_at((int(point.real), int(point.imag)), (255,255,255))
                
        pygame.display.update()


