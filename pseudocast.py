#!/usr/bin/env python

import pygame
from pygame.locals import *
pygame.init()

pygame.display.set_caption("PseudoCasting - Sam Tubb")

frame = pygame.display.set_mode((320,240))

vm = pygame.image.load("viewmodel.png")

def testArray():
    #(0,0)
    pygame.draw.polygon(frame, (0,200,0), [(1,47),(1,74),(136,74),(158,47)], 0)
    #(0,1)
    pygame.draw.polygon(frame, (0,200,0), [(1,76),(1,109),(107,109),(134,76)], 0)


go = True

while go:
    frame.fill((50,50,50))
    frame.blit(vm,(0,0))
    testArray()
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == QUIT:
            go = False
            pygame.display.quit()



exit()
