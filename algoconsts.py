from algorithms import ga, bfs, bnb, ls, mst, dp
from utils import *


ALGO_INFO = [
    {
        'displacement' : (0, FONT_HEIGHT),
        'name' : 'Genetic Algorithm',
        'sim' : ga.GASolver,
        'depends' : -1,
        'namecoords' : (0,0),
        'lengthcoords' : (0, HEIGHT+FONT_HEIGHT),
    },

    {
        'displacement' : (WIDTH, FONT_HEIGHT),
        'name' : 'Brute Force',
        'sim' : bfs.BruteForceSolver,
        'depends' : -1,
        'namecoords' : (WIDTH, 0),
        'lengthcoords' : (WIDTH, HEIGHT+FONT_HEIGHT),
    }, 

    {
        'displacement' : (0, HEIGHT + 3 * FONT_HEIGHT),
        'name' : 'Branch and Bound',
        'sim' : bnb.BranchAndBoundSolver,
        'depends' : -1,
        'namecoords'   :(0, HEIGHT+FONT_HEIGHT*2                   ),
        'lengthcoords' :(0, HEIGHT+FONT_HEIGHT*2+HEIGHT+FONT_HEIGHT),      
    },

    {
        'displacement' : (WIDTH, HEIGHT + 3 * FONT_HEIGHT),
        'name' : 'Approximation using MST',
        'sim' : mst.ApproxMSTSolver,
        'depends' : -1,
        'namecoords'   : (WIDTH, HEIGHT+FONT_HEIGHT*2                   ),
        'lengthcoords' : (WIDTH, HEIGHT+FONT_HEIGHT*2+HEIGHT+FONT_HEIGHT)
    },

    {
        'displacement' : (3 * WIDTH, FONT_HEIGHT),
        'name' : 'Dynamic Programming',
        'sim' : dp.DPSolver,
        'depends' : -1,
        'namecoords'   : (3*WIDTH, 0                   ),
        'lengthcoords' : (3*WIDTH, HEIGHT+FONT_HEIGHT  ),  
    },

    {
        'displacement' : (2 * WIDTH, FONT_HEIGHT),
        'name' : 'Local Search on MST Solution, degree 2',
        'sim' : ls.LocalSearchSolver,
        'depends' : 3,
        'namecoords'   : (2*WIDTH, 0                 ),
        'lengthcoords' : (2*WIDTH, HEIGHT+FONT_HEIGHT),
    },

    {
        'displacement' : (2 * WIDTH, HEIGHT + 3 * FONT_HEIGHT),
        'name' : 'Local Search on MST Solution, degree 3',
        'sim' : ls.LocalSearchSolver,
        'depends' : 3,
        'namecoords'   : (2*WIDTH, HEIGHT+FONT_HEIGHT*2                   ),
        'lengthcoords' : (2*WIDTH, HEIGHT+FONT_HEIGHT*2+HEIGHT+FONT_HEIGHT),  
    },

    {
        'displacement' : (3 * WIDTH, HEIGHT + 3 * FONT_HEIGHT),
        'name' : 'Genetic Algorithm on MST Solution',
        'sim' : ga.GASolver,
        'depends' : 3,
        'namecoords'   : (3*WIDTH, HEIGHT+FONT_HEIGHT*2                   ),
        'lengthcoords' : (3*WIDTH, HEIGHT+FONT_HEIGHT*2+HEIGHT+FONT_HEIGHT),  
    },
]

DIVIDERS = [
    (0, HEIGHT + FONT_HEIGHT*2, WINDOW_WIDTH, HEIGHT + FONT_HEIGHT*2),
    (WIDTH, 0, WIDTH, WINDOW_HEIGHT),
    (2*WIDTH, 0, 2*WIDTH, WINDOW_HEIGHT),
    (3*WIDTH, 0, 3*WIDTH, WINDOW_HEIGHT)
]