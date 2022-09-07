#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random, math

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

def circle_surf(radius, color):
    surf = pygame.Surface((radius * 2, radius * 2))
    pygame.draw.circle(surf, color, (radius, radius), radius)
    surf.set_colorkey((0, 0, 0))
    return surf

# [loc, velocity, timer]
particles = []
boom_particles = []
click_particles = []
monster_create_particles = []
boom_color = [120, 200, 255]
boom_flag = False
click_flag = False
monster_particle_flag = False

game_display_flag = False
new_surf = pygame.Surface((500, 500))
rad = 0
circle_pause = False
loop_cnt = 0
# Loop ------------------------------------------------------- #
while True:

    # Background --------------------------------------------- #
    screen.fill((20,20,60))
    mx, my = pygame.mouse.get_pos()

# -------------------------------------------- display change --------------------------------------------#
    if not game_display_flag:
        new_surf.fill((0,0,0))
        new_surf.blit(circle_surf(rad, (255,255,255)), (mx - rad, my - rad))
        screen.blit(new_surf, pygame.math.Vector2(), special_flags=BLEND_RGB_MULT)
        if not circle_pause: rad += 10
        if rad > 100:
            loop_cnt += 1
            circle_pause = True
            if loop_cnt == 1:
                pause_start = pygame.time.get_ticks()
            else:
                pause_end = pygame.time.get_ticks()
                if pause_end - pause_start > 300:
                    circle_pause = False
        if rad > 700: game_display_flag = True


# ------------------------------------------ fire effect ---------------------------------------------------------#
    """particles.append([[mx, my], [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 11)])
    for particle in particles:
        particle[0][1] += particle[1][1]
        particle[2] -= 0.5
        particle[1][1] += 0.15
        pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        radius = particle[2] * 2
        screen.blit(circle_surf(radius, (20, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)), special_flags=BLEND_RGB_ADD)
        if particle[2] <= 0:
            particles.remove(particle)"""

# ---------------------------------- boom effect ------------------------------------------- #
    while len(boom_particles) < 50 and not boom_flag:
        boom_particles.append([[mx + random.randint(-50, 50), my + random.randint(-50, 50)], [random.randint(-10, 10), random.randint(-10, 10)], random.randint(3, 40)])
    if not boom_flag:
        for i in boom_particles:
            i[0] = [mx + random.randint(-50, 50), my + random.randint(-50, 50)]
    if boom_flag:
        for particle in boom_particles:
            particle[0][1] += particle[1][1]
            particle[0][0] += particle[1][0]
            particle[2] -= 1
            particle[1][1] += 0.15
            idx = random.randint(0, 2)
            pygame.draw.circle(screen, (boom_color[idx], boom_color[idx], boom_color[idx]), [int(particle[0][0]), int(particle[0][1])],
                               int(particle[2]))
            radius = particle[2] * 2
            if particle[2] <= 0:
                boom_particles.remove(particle)
    if len(boom_particles) == 0:
        boom_flag = False
    # ------------------------------------- click effect ---------------------------------------------------
    """while len(click_particles) < 50 and not click_flag:
        click_particles.append([[mx + random.randint(-20, 20), my + random.randint(-20, 20)], [random.randint(-4, 4), random.randint(-4, 4)], random.randint(5, 8)])
    if not click_flag:
        for i in click_particles:
            i[0] = [mx + random.randint(-20, 20), my + random.randint(-20, 20)]
    if click_flag:
        for particle in click_particles:
            particle[0][1] += particle[1][1]
            particle[0][0] += particle[1][0]
            particle[2] -= 0.2
            particle[1][1] += 0.15
            pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            radius = particle[2] * 2
            screen.blit(circle_surf(radius, (20, 20, 60)), (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                        special_flags=BLEND_RGB_ADD)
            if particle[2] <= 0:
                click_particles.remove(particle)
    if len(click_particles) == 0:
        click_flag = False"""

    # ------------------------------------- monster create effect ---------------------------------------------------

    while len(monster_create_particles) < 30 and not monster_particle_flag:
        monster_create_particles.append([[mx + random.randint(-10, 10), my + random.randint(0, 10)], [random.randint(0, 20) / 10 - 1, -5], random.randint(10, 15)])
    if not monster_particle_flag:
        for i in monster_create_particles:
            i[0] = [mx + random.randint(-10, 10), my + random.randint(0, 10)]
    if monster_particle_flag:
        for particle in monster_create_particles:
            particle[0][1] += particle[1][1]
            particle[0][0] += particle[1][0]
            particle[2] -= 0.5
            particle[1][1] += 0.15
            pygame.draw.circle(screen, (0, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            radius = particle[2] * 2
            if particle[2] <= 0:
                monster_create_particles.remove(particle)
    if len(monster_create_particles) == 0:
        monster_particle_flag = False


    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            boom_flag = True
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            click_flag = True
            monster_particle_flag = True

    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)