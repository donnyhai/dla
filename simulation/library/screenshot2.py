# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 16:17:40 2020

@author: Tillmann Tristan Bosch

INFO
Here we provide basic geometrical features we need to simulate the line hitting aggregate. 
"""

from math import sin, cos

class Segment:
    def __init__(self, A = 0, B = 1):
        self.A = A
        self.B = B
        
class Polygon:
    def __init__(self, vertices = [0, 1, 1j, 1+1j]):
        self.vertices = vertices
        self.segments = self.init_segments()
    def init_segments(self):
        segments = []
        l = len(self.vertices)
        for k in range(l):
            segments.append(Segment(self.vertices[k], self.vertices[(k+1) % l]))
        return segments
        

class Line:
    def __init__(self, parameters = (0,0)):
        self.alpha = parameters[0]
        self.p = parameters[1]
    
    def intersects_with_segment(self, segment):
        cos_alpha = cos(self.alpha)
        sin_alpha = sin(self.alpha)
        A_alpha = segment.A.real * cos_alpha + segment.A.imag * sin_alpha # <A,e_alpha>
        B_alpha = segment.B.real * cos_alpha + segment.B.imag * sin_alpha # <B,e_alpha>
        if (A_alpha >= self.p and B_alpha <= self.p) or (A_alpha <= self.p and B_alpha >= self.p):
            return True
        return False
    
    def intersects_with_polygon(self, polygon):
        for segment in polygon.segments:
            if self.intersects_with_segment(segment):
                return True
        return False





# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 17:38:03 2020

@author: Tillmann Tristan Bosch

INFO
Here we provide the code for running the aggregate process and creating exports such as images and fractal dimension results. 
"""

#systemic imports
import json
import create_data as cd

import line_hitting_aggregate as lha
import external_dla as dla
    

if __name__ == "__main__":
    
    with open("parameters.json") as json_file:
        data = json.load(json_file)
    
    if data["aggregate"] == "lha":
        aggregate = lha.Line_Hitting_Aggregate()
    elif data["aggregate"] == "dla":
        aggregate = dla.External_DLA()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    aggregate.run_process(data["cluster_size"] - 1)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    cd.export_data(lha, data)

    
    
    
    