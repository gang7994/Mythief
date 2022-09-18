import pygame, os
from Settings import *

class Test0Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test0_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test0_item"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

    def update(self):
        pass

class Test1Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test1_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test1_item"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class Test2Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test2_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test2_item"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

    def update(self):
        pass
    

class GeneralItem0(pygame.sprite.Sprite): # 로프권 1개 추가
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item0"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item1"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item2"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item3.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item3"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item4.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item4"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "test_general_item5.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "test_general_item5"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False