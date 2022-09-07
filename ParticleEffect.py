import pygame, os, random
from Settings import *

class Particle():
    def __init__(self):
        self.click_particles = []
        self.click_flag = False
        self.monster_create_particles = []
        self.monster_particle_flag = False

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0, 0, 0))
        return surf

    def click_effect(self, screen, mx, my, dt):
        while len(self.click_particles) < 50 and not self.click_flag:
            self.click_particles.append([[mx + random.randint(-20, 20), my + random.randint(-20, 20)],
                                    [random.randint(-4, 4), random.randint(-4, 4)], random.randint(5, 8)])
        if not self.click_flag:
            for i in self.click_particles:
                i[0] = [mx + random.randint(-20, 20), my + random.randint(-20, 20)]
        if self.click_flag:
            for particle in self.click_particles:
                particle[0][1] += particle[1][1] * (dt // 6)
                particle[0][0] += particle[1][0] * (dt // 6)
                particle[2] -= 0.1 * (dt // 6)
                particle[1][1] += 0.15 * (dt // 6)
                pygame.draw.circle(screen, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])],
                                   int(particle[2]))
                radius = particle[2] * 2
                if radius > 0:
                    screen.blit(self.circle_surf(radius, (20, 20, 60)),
                                (int(particle[0][0] - radius), int(particle[0][1] - radius)),
                                special_flags=pygame.BLEND_RGB_ADD)
                if particle[2] <= 0:
                    self.click_particles.remove(particle)
        if len(self.click_particles) == 0:
            self.click_flag = False

    def monster_create_effect(self, screen, pos, dt):
        while len(self.monster_create_particles) < 30 and not self.monster_particle_flag:
            self.monster_create_particles.append(
                [[pos[0] + random.randint(-10, 10), pos[1] + random.randint(0, 10)], [random.randint(0, 20) / 10 - 1, -5],
                 random.randint(10, 15)])
        if not self.monster_particle_flag:
            for i in self.monster_create_particles:
                i[0] = [pos[0] + random.randint(-10, 10), pos[1] + random.randint(0, 10)]
        if self.monster_particle_flag:
            for particle in self.monster_create_particles:
                particle[0][1] += particle[1][1]
                particle[0][0] += particle[1][0]
                particle[2] -= 0.5
                particle[1][1] += 0.15
                pygame.draw.circle(screen, (0, 0, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
                radius = particle[2] * 2
                if particle[2] <= 0:
                    self.monster_create_particles.remove(particle)
        if len(self.monster_create_particles) == 0:
            self.monster_particle_flag = False
