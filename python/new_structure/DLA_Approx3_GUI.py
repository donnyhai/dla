#last changed: 200627

import DLA_Approx3 as da
import DLA_GUI as dg

class DLA_Approx3_GUI(da.DLA_Approx3, dg.DLA_GUI):
    def __init__(self, startAtoms = None):
        da.DLA_Approx3.__init__(self, startAtoms)
        dg.DLA_GUI.__init__(self, startAtoms)
        
    def runProcessLive(self, maxAtoms = 100, surface = None):
        printcounter = 0
        for i in range(maxAtoms):
            start_point = self.calculateStartPosition()
            hitPoint = self.getLineClusterHitPoint(start_point, self.chooseRandomAngle(self.calculateAnglesIntervall(start_point)))
            self.addAtom(hitPoint)
            self.actualizeHelpingStructures()
            
            if printcounter == 10:
                self.render(surface)
                printcounter = 0
            printcounter += 1
            
            print(i)