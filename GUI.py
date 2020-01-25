import pygame, sys
import DLA
import random

pygame.init()
pygame.display.init()

window_size = (1000, 1000)
maxAtoms = 10000

surface = pygame.display.set_mode(window_size,0,32)

#actions

class GUI_DLAProcess(DLA.DLAProcess):
    
    def doAtomWalk(self, position):
        counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                if counter % 10 == 0:
                    self.render()
                counter += 1
                break
            position = random.choice(self.getNeighbours(position))
            
    def render(self):
        surface.fill((0,0,0,0))
                
        for i in range(self.atomRectangleSize[0]):
            for j in range(self.atomRectangleSize[1]):
                if i == 0 or i == (self.atomRectangleSize[0] - 1) or (j == 0 or j == self.atomRectangleSize[1] - 1):
                    surface.set_at((self.atomRectanglePos[0] + i, self.atomRectanglePos[1] + j), (255,0,0,0))
            
        for pos in self.calculateStartPositions():
            surface.set_at(pos, (255,255,255,255))
                
        for atom in self.atoms:
            surface.set_at(atom, (255,255,255,255))
                
        pygame.display.flip()
            
dla = GUI_DLAProcess((1000,1000))

pygame.display.update()

counter = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if counter == 0:
                counter += 1
            elif counter == 1:
                dla.runProcess(maxAtoms)
                counter = 2
            
                
    pygame.display.update()