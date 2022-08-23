#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

new_surf = pygame.Surface((500, 500))

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

# [loc, velocity, timer]
glow = circle_surf(20, (255, 255, 255))

# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((0,0,0))
    new_surf.fill((0, 0, 0))
    pygame.draw.rect(screen, (50, 20, 120), pygame.Rect(100, 100, 200, 80))
    mx, my = pygame.mouse.get_pos()
    new_surf.blit(glow, (mx - 20, my - 20))

    screen.blit(new_surf, (0,0), special_flags=pygame.BLEND_RGB_MULT)

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)