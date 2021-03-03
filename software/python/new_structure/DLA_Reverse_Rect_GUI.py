#last changed: 200627

import DLA_GUI as dg
import DLA_Reverse_Rect as drr

class DLA_Reverse_Rect_GUI(dg.DLA_GUI, drr.DLA_Reverse_Rect):
    def __init__(self, startAtoms = None):
        dg.DLA_GUI.__init__(self, startAtoms)
        drr.DLA_Reverse_Rect.__init__(self, startAtoms)
        
    def runProcessLive(self, atomsMax = 500, surface = None):
        printcounter = 0
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeNearestDistance()
            
            if printcounter == 10:
                self.render(surface)
                printcounter = 0
            printcounter += 1
            
            print(i)
            
            if self.atoms[-1] == self.start_position:
                break
        
    