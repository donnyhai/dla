#last changed: 200627

import DLA_Reverse as dr


class DLA_Reverse_Circle(dr.DLA_Reverse):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        self.boundary_radius = 90
        self.setNearestDistance(self.boundary_radius)
        
    def isInsideBoundary(self, point):
        return abs(point - self.start_position) < self.boundary_radius
    
