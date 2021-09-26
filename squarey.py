import sys, pygame
import random
import time
from config import * 
from pygame import surface

class squarey:
    def __init__(self, surface, x = None, y = None):
        self.surface = surface
        self.x = x
        self.y = y
            
    def draw(self):
        rect = pygame.Rect(blockW * self.x, blockH * self.y, blockW, blockH)
        pygame.draw.rect(self.surface, pygame.Color("white"), rect)
        pygame.draw.rect(self.surface, pygame.Color("light grey"), rect, 1)

    def drawAt(self, x, y):
        rect = pygame.Rect(x, y, blockW, blockH)
        pygame.draw.rect(self.surface, pygame.Color("white"), rect)
        pygame.draw.rect(self.surface, pygame.Color("light grey"), rect, 1)

######################################################################################
######################################################################################

class dirt(squarey):
    def __init__(self, surface, x = None, y = None):
        super().__init__(surface, x, y)
        image = pygame.image.load("dirt.jpg")
        self.scaledImage = pygame.transform.smoothscale(image, (blockW, blockH))

    def draw(self):
        self.surface.blit(self.scaledImage, (blockW * self.x, blockH * self.y))

    def drawAt(self, x, y):
        self.surface.blit(self.scaledImage, (x, y))

######################################################################################
######################################################################################

class water(squarey):
    def __init__(self, surface, x = None, y = None):
        super().__init__(surface, x, y)
        image = pygame.image.load("water.jpg")
        self.scaledImage = pygame.transform.smoothscale(image, (blockW, blockH))

    def draw(self):
        self.surface.blit(self.scaledImage, (blockW * self.x, blockH * self.y))

    def drawAt(self, x, y):
        self.surface.blit(self.scaledImage, (x, y))