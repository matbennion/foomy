import socket

from pygame import surface
from pygame.cursors import sizer_x_strings
from board import *
import math
import pickle
import sys, pygame, random
from pygame.locals import *
import time 
import winsound
from config import * 
from grid import *
import copy


doExit = False

pygame.init()

# Set up screen
screen = pygame.display.set_mode(size)

# Make a list of all squareys
squareyTypes = [dirt(screen), water(screen)]

################################
# DIPLAY SQUAREY MENU          #
################################

def showMenu(x, y):

    gridSize = math.ceil(math.sqrt(len(squareyTypes)))

    # Draw box
    rect = pygame.Rect(x, y, (blockW + 5) * gridSize + 15, (blockH + 5) * gridSize + 15)
    pygame.draw.rect(screen, pygame.Color("grey"), rect)

    # Draw squareys
    sx = x + 10
    sy = y + 10
    for sq in squareyTypes:
        sq.drawAt(sx, sy)
        sx = sx + blockW + 5

    pygame.display.update()

    # Wait for mouse click in squareys
    loop = True
    while loop:    
        events = pygame.event.get()
    
        # Check for next click
        for ev in events:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                (clickx, clicky) = pygame.mouse.get_pos()
                loop = False

    # Work out which squarey clicked
    sx = x + 10
    sy = y + 10
    for sq in squareyTypes:
        rect = pygame.Rect(sx, sy, blockW, blockH)
        if rect.collidepoint(clickx, clicky):
            # Add clicked squarey to grid
            myGrid.addSquarey(sq, x, y)
        sx = sx + blockW + 5


################################
# CHECK KEYS                   #
################################

def checkKeys():

    global doExit

    events = pygame.event.get()

    for ev in events:

         # Check all keys
        if ev.type == pygame.KEYDOWN:

            if ev.key == pygame.K_ESCAPE:
                doExit = True

        if ev.type == pygame.QUIT:
            doExit = True

        if ev.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            showMenu(x, y) 

        if ev.type == pygame.MOUSEBUTTONUP:
             myGrid.draw()



serverIP = "192.168.1.161"
serverPort = 60001
clientIP = None
clientPort = None

myboard = board()
myboard.set("tony")


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', serverPort))
sock.setblocking(False)

rxdata = []

myGrid = grid(screen)

myGrid.draw()
pygame.display.update()    

while not doExit:
    pygame.event.pump()

    checkKeys()

    pygame.display.update()    
    time.sleep(0.1)

    pass
#    try:
#        (data, addr) = sock.recvfrom(65536)
#        rxdata = data
#    except:
#        pass

#    if len(rxdata) > 0:
#        print("Got it *-*")
    
#    sock.sendto(pickle.dumps(myboard), ("192.168.1.179", 60001))