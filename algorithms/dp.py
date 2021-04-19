from utils import *

class DPSolver:
    def __init__(self, cities): 
        self.cities = cities
        self.total = len(cities)
        self.bestOrder = []
        self.bestDistance = float('inf')
        self.graph = makeGraphFromCityList(cities)
        self.setOfAllPoints = set(range(self.total))
        self.memo = {(tuple([i]), i): tuple([0, None]) for i in range(self.total)}
        self.queue = [(tuple([i]), i) for i in range(self.total)] 
    
    def find(self):
        while self.queue:
            prevVisited, prevLastPoint = self.queue.pop(0)
            prevDist, _ = self.memo[(prevVisited, prevLastPoint)]

            toVisit = self.setOfAllPoints.difference(set(prevVisited))
            for newLastPoint in toVisit:
                newVisited = tuple(sorted(list(prevVisited) + [newLastPoint]))
                newDist = prevDist + self.graph[prevLastPoint][newLastPoint]

                if (newVisited, newLastPoint) not in self.memo:
                    self.memo[(newVisited, newLastPoint)] = (newDist, prevLastPoint)
                    self.queue += [(newVisited, newLastPoint)]
                else:
                    if newDist < self.memo[(newVisited, newLastPoint)][0]:
                        self.memo[(newVisited, newLastPoint)] = (newDist, prevLastPoint)
                
        self.bestOrder, self.bestDistance = self.retraceOptimalPath()
    
    def retraceOptimalPath(self):
        pointsToRetrace = tuple(range(self.total))

        fullPathMemo = dict((k, v) for k, v in self.memo.items() if k[0] == pointsToRetrace)
        pathKey = min(fullPathMemo.keys(), key=lambda x: fullPathMemo[x][0])

        lastPoint = pathKey[1]
        optimalCost, nextToLastPoint = self.memo[pathKey]

        optimalPath = [lastPoint]
        pointsToRetrace = tuple(sorted(set(pointsToRetrace).difference({lastPoint})))

        while nextToLastPoint is not None:
            lastPoint = nextToLastPoint
            pathKey = (pointsToRetrace, lastPoint)
            _, nextToLastPoint = self.memo[pathKey]

            optimalPath = [lastPoint] + optimalPath
            pointsToRetrace = tuple(sorted(set(pointsToRetrace).difference({lastPoint})))

        return optimalPath, optimalCost