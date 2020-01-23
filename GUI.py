import pygame, sys
import DLA

pygame.init()
pygame.display.init()

window_size = (100, 100)
dla = DLA.DLAProcess()

surface = pygame.display.set_mode(window_size,0,32)

#actions

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            dla.runProcess()
            
        for atom in dla.atoms:
            surface.set_at(atom, (255,255,255,255))
                
    pygame.display.update()