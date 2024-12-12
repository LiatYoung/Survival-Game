import pygame

# import library to create keys
from pygame.locals import *

# create vector object to store position 
vec = pygame.math.Vector2

# Create Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        """
        x, y: int
            Starting position of the player.
        """

        # Position of the player
        # pos means position
        self.pos = vec(x, y)

        # Create new variables to allow for player movement
        # acc means acceleration
        # initialise x and y components of the acceleration to 0
        self.acc = vec(0, 0)

        # set acceleration to a constant
        self.ACC = .65

        # set friction to a constant
        # friction causes player to not immediately move at full speed
        # and not immediately stop but instead grind to a halt
        self.FRIC = -0.1

        # vel means velocity
        # initialise x and y components of velocity to 0
        self.vel = vec(0, 0)

        # Get the image file
        self.image = pygame.image.load("images/player_top_back_view1.png")
        self.image = pygame.transform.scale(self.image, (156, 163))

    # Create a movement function
    def move(self):
        # x and y component needs to be 0 every time move function is called
        self.acc = vec(0, 0)

        # pygame.key.get_pressed() returns a list of all the keys pressed in the game
        keys = pygame.key.get_pressed()
        
        # if left key is pressed
        if keys[K_LEFT]:
            # move player position to the left by 1 pixel
            self.acc.x = -self.ACC
            self.image = pygame.image.load("images/player_top_left_side_walking1.png")
            self.image = pygame.transform.scale(self.image, (156, 163))

            # top right corner is (0,0) and bottom right corner is max width & height

        # if right key is pressed
        if keys[K_RIGHT]:
            self.acc.x = self.ACC
            self.image = pygame.image.load("images/player_top_right_side_walking1.png")
            self.image = pygame.transform.scale(self.image, (156, 163))
        
        # if up key is pressed
        if keys[K_UP]:
            self.acc.y = -self.ACC
            self.image = pygame.image.load("images/player_top_back_walking1.png")
            self.image = pygame.transform.scale(self.image, (156, 163))

        # if down key is pressed
        if keys[K_DOWN]:
            self.acc.y = self.ACC
            self.image = pygame.image.load("images/player_top_front_walking1.png")
            self.image = pygame.transform.scale(self.image, (156, 163))


        # multiply friction by velocity and that this to x component of acceleration
        # as speed of velocity increases, friction increases
        self.acc.x += self.vel.x * self.FRIC

        self.acc.y += self.vel.y * self.FRIC

        # add acceleration into velocity
        self.vel += self.acc

        # increase position
        self.pos += self.vel + 0.5 * self.acc

    def render(self, display):
        display.blit(self.image, self.pos)