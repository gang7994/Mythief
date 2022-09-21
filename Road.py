import pygame, os
from Settings import *

# 길 이미지
class Road(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "tile_N.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class Road_Horizontal(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "re_tile_horiz.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class Road_Vertical(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "re_tile_vert.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class AlcoholRoad(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "purple_tile_0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "alcoholRoad"

class EventTile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, event_code):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "tile_N.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "eventRoad"
        self.event_code = event_code
