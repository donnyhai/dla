import pygame, sys
import DLA
import random

pygame.init()
pygame.display.init()

window_size = (100, 100)
maxAtoms = 3000

surface = pygame.display.set_mode(window_size,0,32)

#actions

class GUI_DLAProcess(DLA.DLAProcess):
    
    def doAtomWalk(self, startPosition, withDiagonals = False):
        position = startPosition
        counter = 0
        while True:
            if self.isTouching(position):
                self.addAtom(position)
                surface.set_at(position, (255,255,255,255))
                if counter % 10 == 0:
                    pygame.display.flip()
                counter += 1
                break
            nextNeighbours = self.getNeighbours(position, withDiagonals)
            position = random.choice(nextNeighbours)
            
dla = GUI_DLAProcess(window_size)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            dla.runProcess(maxAtoms)
            
                
    pygame.display.update()