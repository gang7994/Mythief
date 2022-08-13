import pygame, os
from Settings import *

# 벽 이미지
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "Wall"
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "obstacle1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "Wall"

# 도착 이미지
class Finish(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "Finish"

# 길 없음 이미지
class NoneRoad(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "void_checked.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "NoneRoad"

