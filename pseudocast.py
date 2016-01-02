#!/usr/bin/env python

import pygame
from pygame.locals import *
pygame.init()

pygame.display.set_caption("PseudoCasting - Sam Tubb")

frame = pygame.display.set_mode((320,240))

vm = pygame.image.load("viewmodel.png")

l = pygame.image.load("lakeside.png")

pos = [25,15]

def testArray(pos,levelmap):
    level = levelmap

    posgrid = [(pos[0],pos[1]),(pos[0]+1,pos[1]),(pos[0]+2,pos[1]),(pos[0]+3,pos[1]),
    (pos[0],pos[1]-1),(pos[0]+1,pos[1]-1),(pos[0]+2,pos[1]-1),(pos[0]+3,pos[1]-1),
    (pos[0],pos[1]-2),(pos[0]+1,pos[1]-2),(pos[0]+2,pos[1]-2),(pos[0]+3,pos[1]-2),
    (pos[0],pos[1]-3),(pos[0]+1,pos[1]-3),(pos[0]+2,pos[1]-3),(pos[0]+3,pos[1]-3)]

    #(0,0)
    pygame.draw.polygon(frame, (level.get_at(posgrid[12])), [(1,47),(1,74),(136,74),(158,47)], 0)
    #(0,1)
    pygame.draw.polygon(frame, (level.get_at(posgrid[8])), [(1,76),(1,109),(107,109),(134,76)], 0)
    #(0,2)
    pygame.draw.polygon(frame, (level.get_at(posgrid[4])), [(1,111),(1,172),(55,172),(105,111)], 0)
    #(0,3)
    pygame.draw.polygon(frame, (level.get_at(posgrid[0])), [(1,174),(1,237),(53,174)], 0)

    #(1,0)
    pygame.draw.polygon(frame, (level.get_at(posgrid[13])), [(159,48),(138,74),(159,74)], 0)
    #(1,1)
    pygame.draw.polygon(frame, (level.get_at(posgrid[9])), [(136,76),(109,109),(159,109),(159,76)], 0)
    #(1,2)
    pygame.draw.polygon(frame, (level.get_at(posgrid[4])), [(107,111),(57,172),(159,172),(159,111)], 0)
    #(1,3)
    pygame.draw.polygon(frame, (level.get_at(posgrid[1])), [(55,174),(2,238),(159,238),(159,174)], 0)

    #(2,0)
    pygame.draw.polygon(frame, (level.get_at(posgrid[14])), [(161,48),(161,74),(182,74)], 0)
    #(2,1)
    pygame.draw.polygon(frame, (level.get_at(posgrid[10])), [(161,76),(161,109),(211,109),(184,76)], 0)
    #(2,2)
    pygame.draw.polygon(frame, (level.get_at(posgrid[5])), [(161,111),(161,172),(263,172),(213,111)], 0)
    #(2,3)
    pygame.draw.polygon(frame, (level.get_at(posgrid[2])), [(161,174),(161,238),(317,238),(264,174)], 0)

    #(3,0)
    pygame.draw.polygon(frame, (level.get_at(posgrid[15])), [(162,47),(184,74),(318,74),(318,47)], 0)
    #(3,1)
    pygame.draw.polygon(frame, (level.get_at(posgrid[11])), [(186,76),(213,109),(318,109),(318,76)], 0)
    #(3,2)
    pygame.draw.polygon(frame, (level.get_at(posgrid[6])), [(215,111),(265,172),(318,172),(318,111)], 0)
    #(3,3)
    pygame.draw.polygon(frame, (level.get_at(posgrid[3])), [(266,174),(318,238),(318,174)], 0)

go = True

while go:
    frame.fill((50,50,50))
    #frame.blit(vm,(0,0))
    testArray(pos,l)
    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == QUIT:
            go = False
            pygame.display.quit()
        if e.type == KEYDOWN:
            if e.key == K_UP:
                pos[1]-=1
            if e.key == K_DOWN:
                pos[1]+=1

exit()
