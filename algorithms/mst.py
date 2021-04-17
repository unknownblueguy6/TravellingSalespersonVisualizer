from utils import *

class ApproxMSTSolver:
    def __init__(self, cities): 
        self.cities = cities
        self.total = len(cities)
        self.bestOrder = []
        self.bestDistance = float('inf')
        self.graph = makeGraphFromCityList(cities)
        self.parent = [None] * self.total

    def printMST(self): 
        print("Edge")
        for i in range(1, self.total): 
            print(i, "-", self.parent[i], "\t") 
   
    def minKey(self, key, mstSet):  
        mini = float('inf') 
        for v in range(self.total): 
            if key[v] < mini and mstSet[v] == False: 
                mini = key[v] 
                min_index = v 
        return min_index

    def primMST(self):  
        key = [float('inf')] * self.total
        key[0] = 0 
        mstSet = [False] * self.total 
        self.parent[0] = -1
        for cout in range(self.total): 
            u = self.minKey(key, mstSet)  
            mstSet[u] = True
            for v in range(self.total):  
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        self.parent[v] = u
    
    def getListOfIndices(self, l):
        listOfIndices = []
        for i in range(len(l) + 1):
            indices = []
            for j in range(len(l)):
                if i == l[j]:
                    indices.append(j+1)
            listOfIndices.append(indices)
        return listOfIndices

    def preorder(self, l, i, ind):
        if len(l[i]) <= ind:
            return 
        for j in range(len(l[i])):
            self.bestOrder.append(l[i][j])
            self.preorder(l, l[i][j], 0)


    def find(self):
        self.primMST()
        listOfIndices = self.getListOfIndices(self.parent[1:])
        root = 0
        self.bestOrder.append(0)
        self.preorder(listOfIndices, 0, 0)
        self.bestDistance = calcPathDistance(self.cities, self.bestOrder)