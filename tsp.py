import os, sys
import threading
import pygame
from pygame.locals import *

import gfx
from algoconsts import *

if(len(sys.argv) == 2):
    totalCities = int(sys.argv[1])
else:
    totalCities = 20

def simLoop():
    for i in range(len(ALGO_INFO)):
        if ALGO_INFO[i]['depends'] == -1:
            threads[i].start()

    while True:
        gfx.checkEvents()

        for i in range(len(ALGO_INFO)):
            if i < len(sims):
                gfx.drawTextTopLeft(surface, ALGO_INFO[i]['name'], GREEN, font, *ALGO_INFO[i]['namecoords'])
                gfx.drawPath(surface, listOfCitiesList[i], sims[i].bestOrder)
                gfx.drawTextTopLeft(surface, "Path Length : " + str(sims[i].bestDistance), RED, font, *ALGO_INFO[i]['lengthcoords'])
            elif len(sims[ALGO_INFO[i]['depends']].bestOrder) != 0:
                for j in range(len(ALGO_INFO)):
                    if ALGO_INFO[j]['depends'] != -1:
                        if ALGO_INFO[j]['sim'] == ls.LocalSearchSolver:
                            sims.append(ALGO_INFO[j]['sim'](listOfCitiesList[j], sims[ALGO_INFO[j]['depends']].bestOrder[:], int(ALGO_INFO[j]['name'][-1])))
                        else:
                            sims.append(ALGO_INFO[j]['sim'](listOfCitiesList[j], sims[ALGO_INFO[j]['depends']].bestOrder[:]))
                        threads.append(threading.Thread(target = sims[j].find))
                        threads[j].daemon = True
                        threads[j].start()
        
        gfx.drawDividers(surface, DIVIDERS)

        pygame.display.update()
        surface.fill(BLACK)

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (WINDOW_X,WINDOW_Y)
pygame.init()
sys.setrecursionlimit(10**9)
surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Travelling Salesperson Visualizer')
font = pygame.font.SysFont('Ubuntu', FONT_HEIGHT)
cities = makeCities(totalCities)

listOfCitiesList = []
sims = []
threads = []

for i in range(len(ALGO_INFO)):
    listOfCitiesList.append(displace(cities, *ALGO_INFO[i]['displacement']))

for i in range(len(ALGO_INFO)):
    if ALGO_INFO[i]['depends'] == -1:
        sims.append(ALGO_INFO[i]['sim'](listOfCitiesList[i]))
        threads.append(threading.Thread(target = sims[i].find))
        threads[i].daemon = True

simLoop()