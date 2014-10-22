import pygame

from model.CarregadorImagem import load_image

#modelo
class Robo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('view/img/Normal_Zombie.gif')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 50
        self.rect.midright = [550,475];
        self.movepos = [0,0]

    def posicaoinicial(self):
        self.rect.midright = [550,475];

    def update(self,grupowalls):

        oldpos = self.rect
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        self.movepos = [0,0]

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            self.rect = oldpos


    def move(self):
        self.movepos[1] = self.movepos[1] - (self.speed) # para cima

    def moveback(self):
        self.movepos[1] = self.movepos[1] + (self.speed) # para tras

    def moveleft(self):
        self.movepos[0] = self.movepos[1] - (self.speed) # para esquerda

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed) # para direita