import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode([700,600]
pygame.display.set_caption("Block + Jump")
clock = pygame.time.Clock()

while True:
screen.fill([255,255,255])

player = pygame.draw.rect(screen, (0,0,0), [100,100,40,80]

gedrueckt = pygame.key.get_pressed()
