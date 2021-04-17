from utils import *

class BranchAndBoundSolver:
    def __init__(self, cities):
        self.total = len(cities)
        self.cities = cities
        self.graph = makeGraphFromCityList(cities)
        self.bestOrder = [None] * (self.total + 1)
        self.bestDistance = float('inf')
        self.visited = [False] * self.total

    def copyToFinal(self, curr_path): 
        self.bestOrder[:self.total + 1] = curr_path[:] 
        self.bestOrder[self.total] = curr_path[0] 
   
    def firstMin(self, i): 
        mini = float('inf') 
        for k in range(self.total): 
            if self.graph[i][k] < mini and i != k: 
                mini = self.graph[i][k] 
        return mini
     
    def secondMin(self, i): 
        first, second = float('inf'), float('inf') 
        for j in range(self.total): 
            if i == j: 
                continue
            if self.graph[i][j] <= first: 
                second = first 
                first = self.graph[i][j] 
    
            elif(self.graph[i][j] <= second and 
                self.graph[i][j] != first): 
                second = self.graph[i][j] 
        return second 
     
    def TSPRec(self, curr_bound, curr_weight,  
                level, curr_path): 
        if level == self.total: 
            if self.graph[curr_path[level - 1]][curr_path[0]] != 0: 
                curr_res = curr_weight + self.graph[curr_path[level - 1]][curr_path[0]] 
                if curr_res < self.bestDistance:
                    self.bestOrder = curr_path[:len(curr_path)-1]
                    self.bestDistance = curr_res 
            return

        for i in range(self.total): 
            if (self.graph[curr_path[level-1]][i] != 0 and
                                self.visited[i] == False): 
                temp = curr_bound 
                curr_weight += self.graph[curr_path[level - 1]][i] 
    
                if level == 1: 
                    curr_bound -= ((self.firstMin(curr_path[level - 1]) + 
                                    self.firstMin(i)) / 2) 
                else: 
                    curr_bound -= ((self.secondMin(curr_path[level - 1]) +
                                    self.firstMin(i)) / 2) 

                if curr_bound + curr_weight < self.bestDistance: 
                    curr_path[level] = i 
                    self.visited[i] = True
                    
                    
                    self.TSPRec(curr_bound, curr_weight,  
                        level + 1, curr_path) 

                curr_weight -= self.graph[curr_path[level - 1]][i] 
                curr_bound = temp 
    
                self.visited = [False] * len(self.visited) 
                for j in range(level): 
                    if curr_path[j] != -1: 
                        self.visited[curr_path[j]] = True
    
    # This function sets up final_path 
    def find(self): 
        curr_bound = 0
        curr_path = [-1] * (self.total + 1) 
        self.visited = [False] * self.total 
     
        for i in range(self.total): 
            curr_bound += (self.firstMin(i) + 
                        self.secondMin(i)) 
     
        curr_bound = curr_bound // 2
        self.visited[0] = True
        curr_path[0] = 0
        self.TSPRec(curr_bound, 0, 1, curr_path)