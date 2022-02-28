import pygame
import sys
import time
from pygame.locals import *

# Variables to be used
height = 700
width = 700
turn = 'x'
winner = None
tie = None
white = (255, 255, 255)
black = (0, 0, 0)

# Sets board as 3 rows of the 3
board = [[None]*3, [None]*3, [None]*3]

# Initialize pygame
pygame.init()

# Set display and game speeds
frames = 30
clock = pygame.time.Clock()
display = pygame.display.set_mode((width, height + 100), 0, 32)
pygame.display.set_caption("Pygame TicTacToe by Cormac")

# import sprites
outline = pygame.image.load("board.png")
x_sprite = pygame.image.load("X.png")
o_sprite = pygame.image.load("O.png")

# resize sprites
outline = pygame.transform.scale(outline, (width, height + 100))
x_sprite = pygame.transform.scale(x_sprite, (80, 80))
o_sprite = pygame.transform.scale(o_sprite, (80, 80))

