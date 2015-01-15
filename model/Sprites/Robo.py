import pygame

from model.CarregadorImagem import load_image

#modelo
class Robo(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('view/img/zombie.png')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 100
        self.rect.midright = [550,450];
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

    def temColisaoCima(self, grupowalls, negacao):
        temColisao = False;

        self.rect[1] -= self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[1] += self.speed

        if negacao == '!':
            return not temColisao

        return temColisao


    def temColisaoEsquerda(self, grupowalls, negacao):
        temColisao = False;
        self.rect[0] -= self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[0] += self.speed

        if negacao == '!':
            return not temColisao

        return temColisao

    def temColisaoDireita(self, grupowalls, negacao):
        temColisao = False;
        self.rect[0] += self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[0] -= self.speed

        if negacao == '!':
            return not temColisao

        return temColisao

    def temColisaoBaixo(self, grupowalls, negacao):
        temColisao = False;
        self.rect[1] += self.speed

        possivelcolisao = pygame.sprite.spritecollide(self, grupowalls, False)
        for wall in possivelcolisao:
            temColisao = True

        self.rect[1] -= self.speed

        if negacao == '!':
            return not temColisao

        return temColisao

    def move(self):
        self.movepos[1] = self.movepos[1] - (self.speed) # para cima

    def moveback(self):
        self.movepos[1] = self.movepos[1] + (self.speed) # para tras

    def moveleft(self):
        self.movepos[0] = self.movepos[1] - (self.speed) # para esquerda

    def moveright(self):
        self.movepos[0] = self.movepos[0] + (self.speed) # para direita