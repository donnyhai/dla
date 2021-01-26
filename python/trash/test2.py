# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:18:43 2020

@author: donnykong
"""

def render3(surface):
    surface.fill((0,0,0,0))    
    for i in range(len(ec.atoms)):
        surface.set_at(ec.atoms[i], ec.colors[(i//250)%len(ec.colors)])
    #for atom in self.atoms:
    #    surface.set_at(atom, (150, 215, 182, 255))
        
    pygame.display.flip()    

ec.colors = [(255,255,0), (255,128,0), (255,0,0), (255,0,128), (255,0,255), (128,0,255), (0,0,255), (0,128,255), (0,255,255), (0,255,128), (0,255,0), (128,255,0)]
ec.actual_color = ec.colors[0]
ec.render = render3