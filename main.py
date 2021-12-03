import pygame
from pygame.locals import *
import sys
import random

pygame.init() #start game

'''Variables to be used throughout the entire game.
These dictate the window size. Not sure if it can scale with the screen size'''

vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
ACC = 0.3
FRIC = -0.10
FPS = 60
FPS_CLOCK = pygame.time.Clock()
COUNT = 0
