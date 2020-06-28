#last changed: 200627


import DLA_Reverse as dr


class DLA_Reverse_Rect(dr.DLA_Reverse):
    def __init__(self, startAtoms = None):
        super().__init__(startAtoms)
        self.initializeBoundaryRect(width = 100, height = 100) #rectangle around the start_position
        self.setNearestDistance(min(self.boundary_rect["width"], self.boundary_rect["height"]) // 2)
        
    def initializeBoundaryRect(self, width = 100, height = 100):
        self.boundary_rect = {"left_bottom": self.start_position - (width // 2 + height // 2 * 1j), "width": width, "height": height}
        
    def isInsideBoundary(self, point):
        minX, maxX = self.boundary_rect["left_bottom"].real, self.boundary_rect["left_bottom"].real + self.boundary_rect["width"]
        minY, maxY = self.boundary_rect["left_bottom"].imag, self.boundary_rect["left_bottom"].imag + self.boundary_rect["height"]
        return (minX <= point.real <= maxX) & (minY <= point.imag <= maxY)
    
    
    
            
            
