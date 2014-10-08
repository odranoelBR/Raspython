import pygame


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
    def __init__(self, x, y, width, height):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill([0,200,255])
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x