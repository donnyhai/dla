import pygame, sys
import saveObjects as so
import DLA

class GUI_DLAProcess(DLA.DLAProcess):
    def render(self, surface):
        surface.fill((0,0,0,0))
        for i in range(self.atomRectangleSize[0]):
            for j in range(self.atomRectangleSize[1]):
                if i == 0 or i == self.atomRectangleSize[0] - 1 or j == 0 or j == self.atomRectangleSize[1] - 1:
                    surface.set_at((self.atomRectanglePos[0] + i, self.atomRectanglePos[1] + j), (255, 117, 71, 255))
        for pos in self.calculateStartPositions(simple = False):
            surface.set_at(pos, (150, 215, 182, 255))
        for atom in self.atoms:
            surface.set_at(atom, (150, 215, 182, 255))
        pygame.display.flip()
        
        
        
pygame.init()
pygame.display.init()

window_size = (1000, 1000)
atomsMax = 40000

dla = GUI_DLAProcess(window_size)
#dla.runProcess(atomsMax)


def printProcess(dla, live = False, atomsMax = None):
    surface = pygame.display.set_mode(window_size,0,32)
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
    
    

#newfile = "objects/dla2.p"
#so.saveObject(dla, newfile)
#getdla = so.getObject("objects/")



