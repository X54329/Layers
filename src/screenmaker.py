#Chapter 12 from http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound&lang=en#section_12
import pygame
import time
 
# Define some colors
white=[255,255,255]
black=[0,0,0]
 
# Call this function so the Pygame library can initialize itself
print ('Initializing pygame')
pygame.init()
print ('Initialized')

# Create an 800x600 sized screen
print ('Starting the screen')
screen = pygame.display.set_mode([600, 389])
print ('Screen set')

# Set positions of graphics
background_position=[0,0]
print ('Loading the loading screen')
loading_image = pygame.image.load("../res/img/img.png").convert()
print ('Loaded')

 
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
print ('blitting')
screen.blit(loading_image, background_position)
print ('blat')
print ('updating')
pygame.display.flip()
print ('updated')

# This sets the name of the window
pygame.display.set_caption('background images')

 
### Fill the screen with a black background
##background.fill(black)
 

## (haven't done sounds yet)
### Before the loop, load the sounds:
##click_sound = pygame.mixer.Sound("click.wav")
 
# Load and set up graphics.
print ('Loading stuff')
#player_image = pygame.image.load("../res/img").convert()
player_image.set_colorkey(white)
print ('Loaded')

clock = pygame.time.Clock()

print ('Showing Animation')

screen.blit(animation_image, background_position)
pygame.display.flip()
time.sleep(4)

print ('Animation Shown')

 
done = False
print ('Starting Main Loop')
while done==False:
    clock.tick(30)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
##        if event.type == pygame.MOUSEBUTTONDOWN:
##            click_sound.play() 
             
    # Copy image to screen:
    screen.blit(background_image, background_position)
 
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
##    player_position = pygame.mouse.get_pos()
##    x=player_position[0]
##    y=player_position[1]
     
    # Copy image to screen:
    screen.blit(player_image, [300,280])
     
    pygame.display.flip()

print ('Exiting')
pygame.quit ()
