import pygame, os

from model.RoboControllerApi import RoboControllerApi
from model.CarregadorImagem import load_image

#modelo
class Robo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('view/img/zombie.png')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 100
        self.rect.midright = [400,50];
        self.movepos = [0,0]
        self.roboControllerApi = RoboControllerApi()

    def posicaoinicial(self):
        self.rect.midright = [400,50];

    def update(self,grupowalls):

        oldpos = self.rect
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        self.movepos = [0,0]

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            self.rect = oldpos

    def temColisaoCima(self, grupowalls):
        temColisao = False;

        self.rect[1] -= self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[1] += self.speed

        return temColisao


    def temColisaoEsquerda(self, grupowalls):
        temColisao = False;
        self.rect[0] -= self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[0] += self.speed

        return temColisao

    def temColisaoDireita(self, grupowalls):
        temColisao = False;
        self.rect[0] += self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[0] -= self.speed


        return temColisao

    def temColisaoBaixo(self, grupowalls):
        temColisao = False;
        self.rect[1] += self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[1] -= self.speed

        return temColisao

    def moveFront(self):
        if os.environ.get('conexaoRobo') == 'True':
            self.roboControllerApi.moveFront()
        self.movepos[1] = self.movepos[1] - (self.speed) # para cima

    def moveBack(self):
        if os.environ.get('conexaoRobo') == 'True':
            self.roboControllerApi.moveBack()
        self.movepos[1] = self.movepos[1] + (self.speed) # para tras

    def moveLeft(self):
        if os.environ.get('conexaoRobo') == 'True':
            self.roboControllerApi.moveLeft()
            self.roboControllerApi.moveFront()

        self.movepos[0] = self.movepos[1] - (self.speed) # para esquerda

    def moveRight(self):
        if os.environ.get('conexaoRobo') == 'True':
            self.roboControllerApi.moveRight()
            self.roboControllerApi.moveFront()

        self.movepos[0] = self.movepos[0] + (self.speed) # para direita