#last changed: 200627

import DLA_External_Circle as dec
import DLA_GUI as dg

class DLA_External_Circle_GUI(dec.DLA_External_Circle, dg.DLA_GUI):
    def __init__(self, startAtoms = None):
        dec.DLA_External_Circle.__init__(self, startAtoms)
        dg.DLA_GUI.__init__(self, startAtoms)
            
    def runProcessLive(self, atomsMax = 500, surface = None):
        printcounter = 0
        for i in range(atomsMax):
            self.doAtomWalk(self.calculateRandomStartPosition())
            self.actualizeHelpingStructures()
            
            if printcounter == 10:
                self.render(surface)
                printcounter = 0
            printcounter += 1
            
            print(i)
            
