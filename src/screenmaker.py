# Pygame Cheat Sheet
# This program should show you the basics of using the Pygame library.
# by Al Sweigart http://inventwithpython.com

# Download files from:
#     http://inventwithpython.com/cat.png
#     http://inventwithpython.com/bounce.wav

import pygame, sys
from pygame.locals import *
from MazeGenerator import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Cheat Sheet')

catSurfaceObj = pygame.image.load('../assets/cat.png')
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
mousex, mousey = 0, 0

fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello world!'

soundObj = pygame.mixer.Sound('../assets/bounce.wav')

m = Maze()
m.generate()

while True:
    windowSurfaceObj.fill(black)
    
    for row in m.pixels:
        for pixel in row:
            if pixel.white == True:
                windowSurfaceObj.set_at((m.pixels.index(row), row.index(pixel)), white)

    pygame.display.update()
    #fpsClock.tick(30) # pause to run the loop at 30 frames per second
    fpsClock.tick(3)