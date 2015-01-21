import pygame
from model.CarregadorImagem import load_image

class Saida(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)

        self.image, self.rect = load_image('view/img/saida.gif')

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update(self,robo, tela):

        colidiu = pygame.sprite.spritecollide(self,robo, False)
        if len(colidiu) > 0:
            tela.statusbar.SetBackgroundColour('#00CC00')
            tela.statusbar.SetStatusText("Parabens por chegar ao final !!!")