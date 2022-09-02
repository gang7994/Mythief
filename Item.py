import pygame, os
from Settings import *

class TestItem(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "test_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.boundary = 100
        self.is_interaction = False
        self.is_get = False
        self.item_gage = 0
        self.name = "test_item"
        self.is_pause = False

    def get_item(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_TAB]:
            self.item_gage += 1
            if self.item_gage == 100:
                self.is_get = True
                self.kill()
        elif not keys[pygame.K_TAB]:
            self.item_gage = 0

    def update(self):
        print(self.item_gage)
        if self.is_interaction:
            self.get_item()

