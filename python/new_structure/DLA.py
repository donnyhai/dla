#last changed: 200627

class DLA:
    def __init__(self, startAtoms = None):
        if not startAtoms is None:
            self.atoms = startAtoms
        else:
            self.atoms = [0] #particles (atoms) will be presented as complex numbers
        
    def addAtom(self, atom):
        self.atoms.append(atom)
    
    def getNeighbours(self, atom, withDiagonal = False):
        if withDiagonal:
            return [atom + 1, atom - 1, atom + 1j, atom - 1j, atom + 1 + 1j, atom + 1 - 1j, atom - 1 + 1j, atom - 1 - 1j] # with diagonal neighbours
        else:
            return [atom + 1, atom - 1, atom + 1j, atom - 1j]  #only up, down, right, left neighbours
        
    def numberOfNeighboursWithParticles(self, atom):
        return len(set(self.getNeighbours(atom)).intersection(set(self.atoms))) #touching diagonal neighbours included? here not

    def isTouching(self, atom):
        return self.numberOfNeighboursWithParticles(atom) > 0

    def runProcess(self, atomsMax = 500):
        pass

    