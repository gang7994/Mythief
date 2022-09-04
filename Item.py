import pygame, os
from Settings import *

class TestItem(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "test0_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_item"
        self.boundary = 50
        self.is_get = False
        self.item_gage = 0
        self.is_pause = False

    def update(self):
        print(self.item_gage)

