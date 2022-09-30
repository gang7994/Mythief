import pygame, os
from Settings import *
"""
stage number :
0 : main
1 : tutorial
2 : poseidon
3 : hades
4 : dionysus
5 : zeus
"""

# 벽 이미지
class Wall1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2,-2)
        self.name = "Wall"
        self.is_pause = False
        
class Wall2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Wall3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall3.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Wall4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall4.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False

class Wall_Wreck(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "W_tile_wall_0.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_wall1.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_wall1.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_wall1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False

class Wall_Plant(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "W_tile_wall_1.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_wall2.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_wall2.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_wall2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False

class Fire_Wall(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "fire2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False

class Fire_torch(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "fire.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Corner1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "corner0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
    
class Corner2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "corner1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Corner3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "corner2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Corner4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "corner3.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wall"
        self.is_pause = False
        
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(images_path, "obstacle1.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_obs.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_obs.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_obs.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_obs.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "obstacle"   # 이름 수정함 -> 파도로 위치 변경 안시킬거임
        self.is_pause = False

# 도착 이미지
class Finish(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num, map_idx):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        self.name = "Finish"
        if stage_num == 5 and (map_idx in [3,4,5,6,7,8]):
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num == 1 and map_idx == 4:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num in [2,3,4] and (map_idx + 1) % 4 == 0:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
            self.name = "ClosedFinish"

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.is_pause = False

class Finish2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num, map_idx):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door2.png")).convert_alpha()
        self.name = "Finish"
        if stage_num == 5 and (map_idx in [3,4,5,6,7,8]):
            self.image = pygame.image.load(os.path.join(images_path, "wall_door2_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num == 1 and map_idx == 4:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door2_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num in [2,3,4] and (map_idx + 1) % 4 == 0:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door2_closed.png")).convert_alpha()
            self.name = "ClosedFinish"

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.is_pause = False

class Finish3(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num, map_idx):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door3.png")).convert_alpha()
        self.name = "Finish"
        if stage_num == 5 and (map_idx in [3,4,5,6,7,8]):
            self.image = pygame.image.load(os.path.join(images_path, "wall_door3_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num == 1 and map_idx == 4:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door3_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num in [2,3,4] and (map_idx + 1) % 4 == 0:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door3_closed.png")).convert_alpha()
            self.name = "ClosedFinish"

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.is_pause = False

class Finish4(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num, map_idx):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door4.png")).convert_alpha()
        self.name = "Finish"
        if stage_num == 5 and (map_idx in [3,4,5,6,7,8]):
            self.image = pygame.image.load(os.path.join(images_path, "wall_door4_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num == 1 and map_idx == 4:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door4_closed.png")).convert_alpha()
            self.name = "ClosedFinish"
        elif stage_num in [2,3,4] and (map_idx + 1) % 4 == 0:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door4_closed.png")).convert_alpha()
            self.name = "ClosedFinish"

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.is_pause = False

# 스테이지 입구 이미지
class Stage0(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage0"
        self.is_pause = False

class Stage1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[1]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage1"
        self.is_pause = False

class Stage2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[2]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage2"
        self.is_pause = False

class Stage3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[3]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage3"
        self.is_pause = False

class Stage4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[4]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage4"
        self.is_pause = False

class Stage5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[5]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door1_closed.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage5"
        self.is_pause = False

# 길 없음 이미지
class NoneRoad(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(images_path, "void_checked.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_Void.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_void.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_void.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_void.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "NoneRoad"
        self.is_pause = False

# 제우스 전선
class HorizontalWire(pygame.sprite.Sprite): #─
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_00.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric00"
        self.is_pause = False

class VerticalWire(pygame.sprite.Sprite): #│
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_01.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric01"
        self.is_pause = False

class CrossWire(pygame.sprite.Sprite): #┼
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_02.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric02"
        self.is_pause = False

class VerticalLeftWire(pygame.sprite.Sprite): #┤
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_03.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric03"
        self.is_pause = False

class HorizontalDownWire(pygame.sprite.Sprite): #┬
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_04.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric04"
        self.is_pause = False
        
class VerticalRightWire(pygame.sprite.Sprite): #├
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_05.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric05"
        self.is_pause = False

class HorizontalUpWire(pygame.sprite.Sprite): #┴
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_06.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric06"
        self.is_pause = False

class UpLeftWire(pygame.sprite.Sprite): #┘
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_07.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric07"
        self.is_pause = False

class DownLeftWire(pygame.sprite.Sprite): #┐
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_08.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric08"
        self.is_pause = False
        
class DownRightWire(pygame.sprite.Sprite): #┌
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_09.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric09"
        self.is_pause = False

class UpRightWire(pygame.sprite.Sprite): #└
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_10.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Electric10"
        self.is_pause = False

#물구덩이 이미지
class WaterHole(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(stage_P_path, "wTile00.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "WaterHole"
        self.is_pause = False

class Pillar0(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "pillar0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-48, -48)
        self.name = "Pillar_0"
        self.is_pause = False

class Pillar1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "pillar1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-48, -48)
        self.name = "Pillar_1"
        self.is_pause = False

class Pillar2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "pillar2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Pillar_2"
        self.is_pause = False

class Wave(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.animation_array = ["waveAnim_0.png", "waveAnim_1.png", "waveAnim_2.png", "waveAnim_3.png"]
        self.image = pygame.image.load(os.path.join(images_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Wave"
        self.animation_idx = 0
        self.animation_frame = 100
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame and self.animation_idx < 3:
            self.animation_idx += 1
            self.image = pygame.image.load(os.path.join(images_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time

    def update(self):
        self.animation()

class Flood(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "flood.png")).convert_alpha()
        self.image.set_alpha(50)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Flood"
        self.is_pause = False

class Thunder(pygame.sprite.Sprite):
    def __init__(self, pos, groups, images, border_images):
        super().__init__(groups)
        self.animation_array = ["lighting0.png",
                                "lighting1.png",
                                "lighting0.png",
                                "lighting1.png",
                                "lighting0.png",
                                "lighting1.png",
                                "lighting2.png",
                                "lighting3.png",
                                "lighting4.png",
                                "lighting5.png",
                                "lighting5.png"]
        self.image = pygame.image.load(os.path.join(images_path, self.animation_array[0])).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -96)
        self.hitbox.top += 48
        self.images = images
        self.border_images = border_images
        self.name = "thunder"
        self.animation_idx = 0
        self.animation_frame = 100
        self.start_time = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.is_pause = False

    def animation(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time > self.animation_frame:
            self.animation_idx += 1
            self.image = pygame.image.load(os.path.join(images_path, self.animation_array[self.animation_idx])).convert_alpha()
            self.start_time = self.current_time
        if self.animation_idx == 10:
            self.kill()

    def collision(self):
        for sprite in self.images:
            if sprite.name == "Road":
                if sprite.rect.colliderect(self.hitbox):
                    self.border_images.add(sprite)
                    sprite.name = "NoneRoad"
                    sprite.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_void.png")).convert_alpha()
                    sprite.hitbox = sprite.rect.inflate(-3, -3)
            elif sprite.name == "Conductor0" or sprite.name == "Conductor1":
                if sprite.rect.colliderect(self.hitbox):
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_11_on.png")).convert_alpha()
                    sprite.is_on = True
            elif sprite.name in ["ElectricRoad00","ElectricRoad01","ElectricRoad02","ElectricRoad03","ElectricRoad04","ElectricRoad05","ElectricRoad06","ElectricRoad07","ElectricRoad08","ElectricRoad09","ElectricRoad10"]:
                if sprite.rect.colliderect(self.hitbox):
                    self.border_images.add(sprite)
                    if sprite.name == "ElectricRoad00":
                        sprite.name = "Electric00"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_00.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad01":
                        sprite.name = "Electric01"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_01.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad02":
                        sprite.name = "Electric02"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_02.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad03":
                        sprite.name = "Electric03"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_03.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad04":
                        sprite.name = "Electric04"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_04.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad05":
                        sprite.name = "Electric05"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_05.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad06":
                        sprite.name = "Electric06"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_06.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad07":
                        sprite.name = "Electric07"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_07.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad08":
                        sprite.name = "Electric08"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_08.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad09":
                        sprite.name = "Electric09"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_09.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)
                    elif sprite.name == "ElectricRoad10":
                        sprite.name = "Electric10"
                        sprite.image = pygame.image.load(os.path.join(images_path, "electric_10.png")).convert_alpha()
                        sprite.hitbox = sprite.rect.inflate(-3, -3)

                        
    def update(self):
        if not self.is_pause:
            self.animation()
            if self.animation_idx == 9:
                self.collision()