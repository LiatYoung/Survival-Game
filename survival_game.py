# First need to download pygame using bash command with:
# pip install pygame

import pygame
from pygame.locals import *
import sys

# import ground file
# from Ground import Ground

from Player import Player

# Begin Pygame
pygame.init()

display_width = 2500
display_height = 1400
FPS = 80
clock = pygame.time.Clock()

# create the screen for the game
display = pygame.display.set_mode((display_width, display_height))

# Set the name to appear on the pygame windows
pygame.display.set_caption("Survival Game")

# set background
background = pygame.image.load("images/Top down view of a field of grass.png")


# Create the ground
#ground = Ground(width, height, x, y, "directory,filename")


# Create the player
player = Player(1000, 500)


# Create an infinite loop since games run infinitely until you close them
# This is where all the main game code will be
while True:
    # create an event loop
    # event.get() returns a list of all events currently occuring in pygame
    for event in pygame.event.get():
        # create the ability to exit the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # for mouse events
        if event.type == MOUSEBUTTONDOWN:
            pass
        
        # for keyboard events
        if event.type == KEYDOWN:
            pass
    
    # Allow movement of the player
    player.move()

    # blit draws whatever passed into it to a set of specified coordinates
    # here, it begins drawing from the (0,0) coordinates which is the top left of the image while the bottom right is the (display_width, display_height)
    # Render background first because in pygame things tend to stack ontop of each other.
    display.blit(background, (0,0))

    #ground.render(display)
    player.render(display)

    # Update the entire window based on all the above code in the while loop
    # the changes will only show until this pygame.display.update() function is called
    pygame.display.update()
    # limit the while loop from running infinitely times a ssecond
    # FPS is the number of times the while loop will be executing   
    clock.tick(FPS)