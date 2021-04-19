import pygame
from pygame.locals import *
from utils import *

def checkEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

def drawTextCenter(surface, text, font, x, y):
    textobj = font.render(text, 1, RED)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def drawTextTopLeft(surface, text, color, font, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def drawPath(surface, cities, order):
    if len(order) != len(cities):
        return
    r = CITY_SIZE // len(cities)
    r = max(MIN_CITY_SIZE, r)
    order = order[order.index(0):] + order[:order.index(0)]
    for i in range(len(order)):
        cityA = cities[order[i % len(order)]]
        cityB = cities[order[(i+1) % len(order)]]
        if i == 0:
            pygame.draw.circle(surface, BLUE, (int(cityA.x), int(cityA.y)), r)
        else:
            pygame.draw.circle(surface, RED, (int(cityA.x), int(cityA.y)), r)
        pygame.draw.aaline(surface, WHITE, cityA, cityB, 2)
        # drawTextCenter(surface, str(cities.index(cityA)), font, int(cityA.x), int(cityA.y))

def drawDividers(surface, DIVIDERS):
    for x1, y1, x2, y2 in DIVIDERS:
        pygame.draw.aaline(surface, WHITE, (x1 - DIVIDER_OFFSET, y1), (x2 - DIVIDER_OFFSET, y2))