import pygame
from model.CarregadorImagem import load_image

class Ground(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
    def __init__(self, x, y, width, height,name):
        """ Constructor function """
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a BLUE wall, of the size specified in the parameters
        self.image, self.rect = load_image('view/img/' + name + '.jpg')

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x