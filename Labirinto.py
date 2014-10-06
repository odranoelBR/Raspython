import pygame, random
from pygame.locals import *

class Labirinto:
    def __init__(self, camadaLabirinto):
        self.mazeArray = []
        self.state = 'idle'
        self.camada = camadaLabirinto
        self.camada.fill((0, 0, 0, 0)) # fill it with black translucent
        for y in xrange(10):
            pygame.draw.line(self.camada, (0,0,0,255), (0, y*50), (550, y*50))
            for x in xrange(11):
                self.mazeArray.append(0x0000)
                if ( y == 0 ):
                    pygame.draw.line(self.camada, (0, 0, 0, 255), (x*50, 0), (x*50, 500))

        self.totalCells = 110
        self.currentCell = random.randint(0, self.totalCells-1)
        self.visitedCells = 1
        self.cellStack = []
        self.compass = [(-1,0),(0,1),(1,0),(0,-1)]
        self.wallList = []
        self.currentCell = random.randint(0, self.totalCells-1)
        c = self.currentCell
        mz = self.mazeArray[c]
        self.mazeArray[c] |= 0x00F0 # now its part of the maze
        self.wallList.append((c,0))
        self.wallList.append((c,1))
        self.wallList.append((c,2))
        self.wallList.append((c,3)) # fill the walls
        self.visitedCells = 1
        self.cellStack = []
        self.compass = [(-1,0),(0,1),(1,0),(0,-1)]

    def update(self):
        if self.state == 'idle':
			#if self.visitedCells >= self.totalCells:
			if len(self.wallList) <= 0:
				self.currentCell = 0 # set current to top-left
				self.cellStack = []
				self.state = 's'
				return
			moved = False
			while(len(self.wallList) > 0):# and moved == False):
				# pick a random wall
				wi = random.randint(0, len(self.wallList)-1)
				self.currentCell = self.wallList[wi][0]
				x = self.currentCell % 10
				y = self.currentCell / 11
				dir = self.wallList[wi][1]
				nx = x + self.compass[dir][0]
				ny = y + self.compass[dir][1]
				nidx = ny*10+nx
				dx = x*50
				dy = y*50
				direction = 1 << dir # make it perty
				if ((nx >= 0) and (ny >= 0) and (nx < 11) and (ny < 10)):
					if (self.mazeArray[nidx] & 0x00F0) == 0:
						if direction & 1:
							self.mazeArray[nidx] |= (4)
							pygame.draw.line(self.camada, (0,0,0,0), (dx,dy+1),(dx,dy+7))
						elif direction & 2:
							self.mazeArray[nidx] |= (8)
							pygame.draw.line(self.camada, (0,0,0,0), (dx+1,dy+8),(dx+7,dy+8))
						elif direction & 4:
							self.mazeArray[nidx] |= (1)
							pygame.draw.line(self.camada, (0,0,0,0), (dx+8,dy+1),(dx+8,dy+7))
						elif direction & 8:
							self.mazeArray[nidx] |= (2)
							pygame.draw.line(self.camada, (0,0,0,0), (dx+10,dy),(dx+70,dy))
						self.mazeArray[self.currentCell] |= direction
						self.mazeArray[(ny*11+nx)] |= 0x00F0 # mark it as part of the maze
						# add its walls to the list
						self.wallList.append((ny*80+nx,0))
						self.wallList.append((ny*80+nx,1))
						self.wallList.append((ny*80+nx,2))
						self.wallList.append((ny*80+nx,3))
						moved = True
				self.wallList.remove(self.wallList[wi])

    def draw(self, screen):
        screen.blit(self.camada, (0, 0))
        screen.blit(self.camada, (0, 0))