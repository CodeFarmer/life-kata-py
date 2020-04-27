


class Arena:


    def __init__(self):
        self._aliveSet = set()

        
    def alive(self, x, y):
        return (x, y) in self._aliveSet
        

    def setAlive(self, x, y):
        self._aliveSet.add((x, y))

    def setDead(self, x, y):
        point = (x, y)
        if point in self._aliveSet:
            self._aliveSet.remove(point)

    def countNeighbours(self, x, y):
        count = 0
        
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if (not (i, j) == (0, 0)) and self.alive(x + i, y + j):
                    count = count + 1

        return count

    
    def survives(self, x, y):
        
        if self.alive(x, y):
            if self.countNeighbours(x, y) in [2, 3]:
                return True
        else:
            if self.countNeighbours(x, y) == 3:
                return True
        
        return False


    def next(self):
        
        interestingCells = set()
        for (x, y) in self._aliveSet:
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    interestingCells.add((x + i, y + j))

        nextAlive = set()
        for (x, y) in interestingCells:
            if self.survives(x, y):
                nextAlive.add((x, y))

        self._aliveSet = nextAlive

    
    def __eq__(self, other):
        return isinstance(other, Arena) and self._aliveSet == other._aliveSet


