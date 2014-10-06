import pygame
from image import load_image

class Bloco(pygame.sprite.Sprite):
    def __init__(self, posicaoInicial):
        self.angulo = 0
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('bloco.png')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 20
        self.movepos = posicaoInicial
        self.reinit()

    def reinit(self):
        self.rect.midright = self.area.center

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        self.movepos = [0,0]
