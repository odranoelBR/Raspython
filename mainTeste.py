import pygame
import sys
from robo import Robo
from pygame.locals import *

screen = pygame.display.set_mode((640, 480))
pygame.init()

background = pygame.Surface(screen.get_size())
robo = Robo()

playersprites = pygame.sprite.RenderPlain((robo))
clock = pygame.time.Clock()
while 1:
    # Make sure game doesn't run at more than 60 frames per second
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                robo.moveup()
            if event.key == K_DOWN:
                robo.movedown()
            if event.key == K_LEFT:
                robo.moveleft()
            if event.key == K_RIGHT:
                robo.moveright()

        elif event.type == KEYUP:
            if event.key == K_UP or event.key == K_DOWN     \
                    or event.key == K_LEFT or event.key == K_RIGHT:
                robo.movepos = [0,0]


    screen.blit(background, robo)
    playersprites.update()
    playersprites.draw(screen)
    pygame.display.flip()

