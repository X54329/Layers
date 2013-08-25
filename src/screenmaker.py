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

rightImg = pygame.image.load('../assets/Right.jpg')
leftImg = pygame.image.load('../assets/Left.jpg')
upImg = pygame.image.load('../assets/Up.jpg')
downImg = pygame.image.load('../assets/Down.jpg')
rightUpImg = pygame.image.load('../assets/RightUp.jpg')
rightLeftImg = pygame.image.load('../assets/RightLeft.jpg')
rightDownImg = pygame.image.load('../assets/RightDown.jpg')
upLeftImg = pygame.image.load('../assets/UpLeft.jpg')
upDownImg = pygame.image.load('../assets/UpDown.jpg')
leftDownImg = pygame.image.load('../assets/Leftdown.jpg')
rightUpLeftImg = pygame.image.load('../assets/RightUpLeft.jpg')
upLeftDownImg = pygame.image.load('../assets/UpLeftDown.jpg')
rightLeftDownImg = pygame.image.load('../assets/RightLeftDown.jpg')
rightUpDownImg = pygame.image.load('../assets/RightUpDown.jpg')
allImg = pygame.image.load('../assets/Undiscovered.jpg')


fontObj = pygame.font.Font('freesansbold.ttf', 32)
msg = 'Hello world!'

soundObj = pygame.mixer.Sound('../assets/bounce.wav')

m = Maze()
m.generate()

while True:
    windowSurfaceObj.fill(black)
    
    for row in m.pixels:
        for pixel in row:
            sides = pixel.get_sides_open()
	    if sides[0]:
                if sides[1]:
                    if sides[2]:
                        if sides[3]:
                	    windowSurfaceObj.blit(allImg, (m.pixels.index(row)*20, row.index(pixel)*20))
			else:
			    windowSurfaceObj.blit(rightUpLeftImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		    elif sides[3]:
			windowSurfaceObj.blit(rightUpDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		    else:
			windowSurfaceObj.blit(rightUpImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		elif sides[2]:
		    if sides[3]:
			windowSurfaceObj.blit(rightLeftDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		    else:
			windowSurfaceObj.blit(rightLeftImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		elif sides[3]:
		    windowSurfaceObj.blit(rightDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		else:
		    windowSurfaceObj.blit(rightImg, (m.pixels.index(row)*20, row.index(pixel)*20))
	    elif sides[1]:
		if sides[2]:
		    if sides[3]:
			windowSurfaceObj.blit(upLeftDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		    else:
			windowSurfaceObj.blit(upLeftImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		elif sides[3]:
		    windowSurfaceObj.blit(upDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		else:
		    windowSurfaceObj.blit(upImg, (m.pixels.index(row)*20, row.index(pixel)*20))
	    elif sides[2]:
		if sides[3]:
		    windowSurfaceObj.blit(leftDownImg, (m.pixels.index(row)*20, row.index(pixel)*20))
		else:
		    windowSurfaceObj.blit(leftImg, (m.pixels.index(row)*20, row.index(pixel)*20))
	    elif sides[3]:
		windowSurfaceObj.blit(downImg, (m.pixels.index(row)*20, row.index(pixel)*20))


    pygame.display.update()
    #fpsClock.tick(30) # pause to run the loop at 30 frames per second
    fpsClock.tick(3)
