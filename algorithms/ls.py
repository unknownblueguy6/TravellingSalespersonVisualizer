import itertools
from utils import *

class LocalSearchSolver:
    def __init__(self, cities, order, d):
        self.cities = cities
        self.total = len(cities)
        self.bestOrder = order[:]
        self.bestDistance = calcPathDistance(self.cities, self.bestOrder)
        self.d = d
    
    def foo(self, bestO, bestD):
        indexList = [i for i in range(self.total)]
        for indices in itertools.combinations(indexList, self.d):
            copyO = bestO[:]
            indices = list(indices)
            c = [copyO[i] for i in indices]
            for shuffled in itertools.permutations(c):
                currOrder = copyO[:]
                for i, num in zip(indices, shuffled):
                    currOrder[i] = num
                d = calcPathDistance(self.cities, currOrder)
                if d < bestD:
                    bestD = d
                    bestO = currOrder
        return bestO, bestD 

    def find(self):
        o, d = self.bestOrder, self.bestDistance
        o, d = self.foo(o, d)
        while(o != self.bestOrder and d != self.bestDistance):
            o, d = self.foo(o, d)
            if d < self.bestDistance:
                self.bestDistance = d
                self.bestOrder = o