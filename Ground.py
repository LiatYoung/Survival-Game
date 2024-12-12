import pygame

# set up a vector 
vec = pygame.math.Vector2

# Create Ground class
class Ground(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, name):
        """
        Parameters
        ----------
        width: 
        
        height:
        
        x, y: int
            Starting position from which to draw the image.
            
        name: string
            Name of the image file to load (including the directory if necesary).
        """
        
        # Get the image file
        self.image = pygame.image.load(name)

        # the vector previously set up allows us to access both the width and the height at once.
        self.size = vec(width, height)
        # store x and y position
        self.pos = vec(x, y)

    def render(self, display):
        """
        display:
            
        """

        # Call the function to draw the image file 
        display.blit(self.image, self.pos)