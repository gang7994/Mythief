import pygame, os
import random
from Settings import *


class Monster(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "pix.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "Monster"
        self.border_images = border_images
        self.monster_speed = 10
        self.m_dir_x = 1
        self.initpos_x = self.rect.centerx
        
    def move(self):
        self.m_dir_x = random.randint(0,2)
        
        
        
    def collision(self):
        for sprite in self.border_images:
            if sprite.rect.colliderect(self.rect):
                if sprite.name == "Wall":
                    pass
                if sprite.name == "NoneRoad":
                    pass

        
        
