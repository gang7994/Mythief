import pygame, os
from Settings import *

class Test0Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.animation_array = ["rotatingEXP_0.png",
                          "rotatingEXP_1.png",
                          "rotatingEXP_2.png",
                          "rotatingEXP_3.png",
                          "rotatingEXP_4.png",
                          "rotatingEXP_5.png",
                          "rotatingEXP_6.png",
                          "rotatingEXP_7.png"]
        self.image = pygame.image.load(os.path.join(item_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "event_item1"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.animation_idx = 0
        self.animation_frame = 200
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.effect_idx = 0
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame:
            self.animation_idx += 1
            self.animation_idx %= 8
            self.image = pygame.image.load(os.path.join(item_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time

    def update(self):
        self.animation()

class Test1Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.animation_array = ["rotatingEXP2_0.png",
                          "rotatingEXP2_1.png",
                          "rotatingEXP2_2.png",
                          "rotatingEXP2_3.png",
                          "rotatingEXP2_4.png",
                          "rotatingEXP2_5.png",
                          "rotatingEXP2_6.png",
                          "rotatingEXP2_7.png"]
        self.image = pygame.image.load(os.path.join(item_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "event_item2"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.animation_idx = 0
        self.animation_frame = 200
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.effect_idx = 0
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame:
            self.animation_idx += 1
            self.animation_idx %= 8
            self.image = pygame.image.load(os.path.join(item_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time

    def update(self):
        self.animation()

class Test2Item(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.animation_array = ["rotatingEXP3_0.png",
                                "rotatingEXP3_1.png",
                                "rotatingEXP3_2.png",
                                "rotatingEXP3_3.png",
                                "rotatingEXP3_4.png",
                                "rotatingEXP3_5.png",
                                "rotatingEXP3_6.png",
                                "rotatingEXP3_7.png"]
        self.image = pygame.image.load(os.path.join(item_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "event_item3"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.animation_idx = 0
        self.animation_frame = 200
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.effect_idx = 0
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame:
            self.animation_idx += 1
            self.animation_idx %= 8
            self.image = pygame.image.load(os.path.join(item_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time

    def update(self):
        self.animation()
    

class GeneralItem0(pygame.sprite.Sprite): # 패스권 1개 추가
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item0"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem1(pygame.sprite.Sprite): # 이동속도 증가
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item1"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem2(pygame.sprite.Sprite): #최대 체력 증가
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item2"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem3(pygame.sprite.Sprite): #스테이지마다 플레이어가 받는 피해를 최대 2회까지 방어
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item3"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem4(pygame.sprite.Sprite): #패스권 1개 감소
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item4"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem5(pygame.sprite.Sprite): #고대 주화
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item5"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem6(pygame.sprite.Sprite): # 회중시계
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item6"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
        
class GeneralItem7(pygame.sprite.Sprite): # 평평한 돌
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item7"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem8(pygame.sprite.Sprite): #이상한 석상
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item8"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem9(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item9"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem10(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item10"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class GeneralItem(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "general_item.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "general_item"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False

class ThunderRod(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.animation_array = ["rod_0.png", "rod_1.png", "rod_2.png", "rod_3.png", "rod_4.png", "rod_5.png"]
        self.image = pygame.image.load(os.path.join(item_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "thunderRod"
        self.animation_idx = 0
        self.animation_frame = 100
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame:
            self.animation_idx += 1
            self.animation_idx %= 6
            self.image = pygame.image.load(os.path.join(item_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time

    def update(self):
        if not self.is_pause:
            self.animation()

class HadesHelmet(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(item_path, "hadesHelmet.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "hadesHelmet"
        self.boundary = 50
        self.is_get = False
        self.is_interaction = False
        self.item_gage = 0
        self.is_pause = False
