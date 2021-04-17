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
    r = int((12 / len(cities)) * 10)
    for i in range(len(order)):
        cityA = cities[order[i % len(order)]]
        cityB = cities[order[(i+1) % len(order)]]
        pygame.draw.circle(surface, RED, (int(cityA.x), int(cityA.y)), r)
        pygame.draw.aaline(surface, WHITE, cityA, cityB, 2)
        # drawTextCenter(surface, str(cities.index(cityA)), font, int(cityA.x), int(cityA.y))

def drawDividers(surface):
    pygame.draw.aaline(surface, WHITE, (0, HEIGHT + FONT_HEIGHT*2), (WINDOW_WIDTH, HEIGHT + FONT_HEIGHT*2))
    pygame.draw.aaline(surface, WHITE, (WIDTH, 0), (WIDTH, WINDOW_HEIGHT))
    pygame.draw.aaline(surface, WHITE, (2*WIDTH, 0), (2*WIDTH, WINDOW_HEIGHT))