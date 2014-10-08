import pygame

from model.CarregadorImagem import load_image

#modelo
class Robo(pygame.sprite.Sprite):
    def __init__(self):
        self.angulo = 0
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('view/img/robot.png')
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.speed = 50
        self.reinit()

    def reinit(self):
        self.movepos = [275,225]
        self.rect.midright = self.area.center

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.area.contains(newpos):
            self.rect = newpos
        self.movepos = [0,0]

    def move(self):
        if(self.angulo == 0 ):
            self.movepos[1] = self.movepos[1] - (self.speed) # para cima
        elif(self.angulo == 90  or self.angulo == -270):
            self.movepos[0] = self.movepos[1] - (self.speed) # para esquerda
        elif(self.angulo == 180 or self.angulo == -180):
            self.movepos[1] = self.movepos[1] + (self.speed) # para tras
        elif(self.angulo == 270 or  self.angulo == -90):
            self.movepos[0] = self.movepos[0] + (self.speed) # para direita

    def moveleft(self):
        self.angulo += 90
        self.rotacionar(90)

    def moveright(self):
        self.angulo -= 90
        self.rotacionar(-90)


    def rotacionar(self,angulo):

        if(self.angulo == 360 or self.angulo == -360):
            self.angulo = 0

        """rotate an image while keeping its center and size"""
        orig_rect = self.image.get_rect()
        rot_image = pygame.transform.rotate(self.image, angulo)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        self.image =  rot_image