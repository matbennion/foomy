# Define a class to hold an animated sprite
import sys, pygame
import random
import time
from config import * 
from pygame import surface
from squarey import *
 
class grid:

    # Define attributes for objects
    def __init__(self, surface):

        self.board = [[squarey(surface, j, i) for j in range(numBlockX)] for i in range(numBlockY)]

        self.board[6][10] = dirt(surface, 10, 6)
        self.board[7][10] = water(surface, 10, 7)

        # Use to calculate animation times
        self.lastTime = 0
        self.isFirst = True

        # Save a copy of the surface to draw later
        self.surface = surface


    ####################################################################
    # DRAWS GRID AND ALL OBJECTS IN IT                                 #
    ####################################################################

    def draw(self):

        if self.isFirst:
            dt = 0
            self.isFirst = False
        else:
            dt = time.time() - self.lastTime

        # Store the time of this call ready for next time called
        self.lastTime = time.time()

        self.surface.fill((0,0,0))
        for row in self.board:
            for sq in row:
                sq.draw()


    ####################################################################
    # ADD NEW SQUAREY TO GRID                                          #
    ####################################################################

    def addSquarey(self, sq, x, y):

        sq.x = int(x / blockW)
        sq.y = int(y / blockH)
        self.board[int(y / blockH)][int(x / blockW)] = sq


