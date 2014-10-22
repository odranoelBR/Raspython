import pygame

from model.CarregadorImagem import load_image

#modelo
class Robo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.angulo = 0
        self.image, self.rect = load_image('view/img/Normal_Zombie.gif')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 50
        self.rect.midright = [550,475];
        self.movepos = [0,0]

    def posicaoinicial(self):
        self.rect.midright = [550,475];

    def update(self,grupowalls):

        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        self.movepos = [0,0]

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:

            if not self.emfrente and self.angulo == 0:
                self.rect.bottom = wall.rect.top # bloqueia dar re olhando para frente
            elif not self.emfrente and (self.angulo == 90  or self.angulo == -270):
                self.rect.right = wall.rect.left # bloqueia dar re olhando para direita
            elif not self.emfrente and (self.angulo == 270  or self.angulo == -90):
                self.rect.left = wall.rect.right # bloqueia dar re olhando para esquerda
            elif not self.emfrente and (self.angulo == 180  or self.angulo == -180):
                self.rect.top = wall.rect.bottom # bloqueia dar re olhando para baixo
            elif self.angulo == 0:
                self.rect.top = wall.rect.bottom # bloqueia para cima
            elif self.angulo == 90  or self.angulo == -270:
                self.rect.left = wall.rect.right # bloqueia para esquerda
            elif self.angulo == 270 or  self.angulo == -90:
                self.rect.right = wall.rect.left # bloqueia para direita


    def move(self):
        self.movepos[1] = self.movepos[1] - (self.speed) # para cima

    def moveback(self):
        self.movepos[1] = self.movepos[1] + (self.speed) # para tras

    def moveleft(self):
        self.movepos[0] = self.movepos[1] - (self.speed) # para esquerda

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed) # para direita