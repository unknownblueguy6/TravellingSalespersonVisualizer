import random
import sys
import pygame
from pygame.locals import *

############################################ 
WIDTH  = 300
HEIGHT = 300
FONT_HEIGHT = 20

WINDOW_WIDTH  = WIDTH * 4
WINDOW_HEIGHT = (HEIGHT + FONT_HEIGHT + FONT_HEIGHT) * 2
WINDOW_X = 10
WINDOW_Y = 10

CITY_SIZE = 250
DIVIDER_OFFSET = 2.5

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
#############################################

def calcPathDistance(points, order):
    dist = 0
    for i in range(len(order)):
        cityA = points[order[i % len(order)]]
        cityB = points[order[(i+1) % len(order)]]
        d = (cityA - cityB).length()
        dist += d
    return dist

def makeGraphFromCityList(cities):
    n = len(cities)
    graph = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        cityA = cities[i]
        for j in range(i, n):
            if i == j:
                graph[i][j] = 0
            else:
                cityB = cities[j]

                d = (cityA - cityB).length()
                graph[i][j] = graph[j][i] = d 
    return graph

def makeCities(totalCities):
    cities = []
    r = CITY_SIZE // totalCities
    for i in range(totalCities):
        cities.append(pygame.math.Vector2(random.randrange(r, WIDTH-r), random.randrange(r, HEIGHT-r)))
    return cities

def displace(cities, x, y):
    new = []
    displaceVector = pygame.math.Vector2(x, y)
    for c in cities:
        new.append(c + displaceVector)
    return new