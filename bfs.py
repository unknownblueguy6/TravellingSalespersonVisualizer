import itertools
from utils import *

class BruteForceSolver:
    def __init__(self, cities):
        self.cities = cities
        self.total = len(cities)
        self.bestOrder = []
        self.bestDistance = float('inf')
    
    def find(self):
        start = [i for i in range(self.total)]
        for order in itertools.permutations(start):
            d = calcPathDistance(self.cities, order)
            if d < self.bestDistance:
                self.bestDistance = d
                self.bestOrder = list(order)