import random
from utils import *

class GASolver:
    
    def __init__(self, cities, givenOrder = []):
        self.cities = cities
        self.total = len(cities)
        self.bestOrder = []
        self.bestDistance = float('inf')
        self.population = []
        self.fitness = []
        self.mutationRate = 0.01
        self.popSize = 1000
        self.genNum = 0
        order = []
        if len(givenOrder) == 0:
            for i in range(self.total):
                order.append(i)
            for i in range(self.popSize):
                p = order[:]
                random.shuffle(p)
                self.population.append(p)
        else:
            order = givenOrder
            for i in range(self.popSize-1):
                p = order[:]
                indexA = random.randrange(len(p))
                indexB = random.randrange(len(p))
                p[indexA], p[indexB] = p[indexB], p[indexA]
                self.population.append(p)
            self.population.append(givenOrder)

        
        if len(givenOrder) != 0:
            self.population[random.randrange(0, self.popSize)] = givenOrder

        for i in range(self.popSize):
            d = calcPathDistance(self.cities, self.population[i])
            if d < self.bestDistance:
                self.bestDistance = d
                self.bestOrder = self.population[i]
            self.fitness.append(1 / (d+1))

    def mutate(self, order, mutationRate):
        for i in range(len(order)):
            if(random.random() < mutationRate):
                indexA = random.randrange(len(order))
                indexB = (indexA + 1) % len(order)
                order[indexA], order[indexB] = order[indexB], order[indexA]
        return order

    def crossOver(self, orderA, orderB):
        start = random.randrange(len(orderA))
        end = random.randrange(len(orderA))
        if start > end:
            start, end = end, start
        order = orderA[start:end]

        for pos in orderB:
            if pos not in order:
                order.append(pos)

        return order

    def crossOver2(self, orderA, orderB):
        child = [None] * len(orderA)
        left = []
        for i in range(len(orderA)):
            a = orderA[i]
            b = orderB[i]
            if a == b:
                child[i] = a
                continue
            if a not in left:
                left.append(a)
            if b not in left:
                left.append(b)
        for i in range(len(orderA)):
            if child[i] != None:
                continue
            child[i] = left[0]
            del left[0]
        return child


    def calcFitness(self):
        for i in range(self.popSize):
            d = calcPathDistance(self.cities, self.population[i])
            if d < self.bestDistance:
                self.bestDistance = d
                self.bestOrder = self.population[i]
            self.fitness[i] = 1 / (d**8 + 1) #this fixed everything!

    def normalizeFitness(self):
        totalFit = sum(self.fitness)
        for i in range(len(self.fitness)):
            self.fitness[i] /= totalFit

    def makeNextPopulation(self):
        self.genNum += 1
        # if(self.genNum > 120):
        #     self.mutationRate = 0.02
        # else:
        #     self.mutationRate -= 0.00817
        newPop = []
        for i in range(self.popSize):
            orderA = random.choices(self.population, weights = self.fitness, k = 1)[0][:]
            orderB = random.choices(self.population, weights = self.fitness, k = 1)[0][:]
            while orderB == orderA:
                orderB = random.choices(self.population, weights = self.fitness, k = 1)[0][:]
            order = self.crossOver(orderA, orderB)
            # new = order[:]
            order = self.mutate(order, self.mutationRate)
            newPop.append(order)
        self.population = newPop
    
    def find(self):
        while True:
            self.makeNextPopulation()
            self.calcFitness()
            self.normalizeFitness()