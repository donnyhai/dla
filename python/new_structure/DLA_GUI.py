#last changed: 200627

import DLA

import pygame

class DLA_GUI(DLA.DLA):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        
        self.colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]
        self.actual_color = self.colors[0]
        
        
    def render(self, surface = None):
        if surface is not None:
            surface.fill((0,0,0))
            offset = surface.get_width() // 2 + (surface.get_height() // 2) * 1j
            
            for i in range(len(self.atoms)):
                renderAtom = self.atoms[i] + offset
                surface.set_at((int(renderAtom.real), int(renderAtom.imag)), self.colors[(i // 250) % len(self.colors)])
                #surface.set_at((int(renderAtom.real), int(renderAtom.imag)), (255,255,255)) 
            
            pygame.display.flip()   
        
