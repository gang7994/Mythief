import pygame, os
from Settings import *

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
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "obstacle1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "obstacle"   # 이름 수정함 -> 파도로 위치 변경 안시킬거임
        self.is_pause = False

# 도착 이미지
class Finish(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Finish"
        self.is_pause = False

# 스테이지 입구 이미지
class Stage0(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage0"
        self.is_pause = False

class Stage1(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[1]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door_closed0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage1"
        self.is_pause = False

class Stage2(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[2]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door_closed0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage2"
        self.is_pause = False

class Stage3(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[3]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door_closed0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage3"
        self.is_pause = False

class Stage4(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[4]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door_closed0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage4"
        self.is_pause = False

class Stage5(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        if stage_clear[5]:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door.png")).convert_alpha()
        else:
            self.image = pygame.image.load(os.path.join(images_path, "wall_door_closed0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-2, -2)
        self.name = "Stage5"
        self.is_pause = False

# 길 없음 이미지
class NoneRoad(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "void_checked.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "NoneRoad"
        self.is_pause = False

#물구덩이 이미지
class WaterHole(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "wTile00.png")).convert_alpha()
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


        
