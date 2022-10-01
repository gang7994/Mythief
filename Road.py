import pygame, os
from Settings import *

# 길 이미지
class Road(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(stage_road_path, "tile2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"

class Road_stage(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "tile2.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_road_path, "wTile_01.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_road_path, "tile_red_1.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_road_path, "tile_purple_0.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_road_path, "tile_electric_tile1.png")).convert_alpha()
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

#전도체
class Conductor0(pygame.sprite.Sprite): #가짜
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_11.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Conductor0"
        self.is_on = False
        
class Conductor1(pygame.sprite.Sprite): #진짜
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "electric_11.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Conductor1"
        self.is_on = False

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
        self.image = pygame.image.load(os.path.join(stage_road_path, "tile2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "eventRoad"
        self.event_code = event_code
    
class Road_Edge1(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "edge1.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile08.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_edge3.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_edge3.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_edge3.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
    
class Road_Edge2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "edge2.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile10.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_edge4.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_edge4.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_edge2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
        
class Road_Edge3(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "edge3.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile05.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_edge2.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_edge2.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_edge4.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
        
class Road_Edge4(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "edge4.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile03.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_edge1.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_edge1.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_edge1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
        
class Road_Corner1(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "rev_corner1.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_rev_C1.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_Rev_corner1.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_Rcorner1.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_Revcorner1.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
    
class Road_Corner2(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "rev_corner2.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_rev_C2.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_Rev_corner2.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_Rcorner2.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_Revcorner2.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
        
class Road_Corner3(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "rev_corner3.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_rev_C3.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_Rev_corner3.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_Rcorner3.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_Revcorner3.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"
        
class Road_Corner4(pygame.sprite.Sprite):
    def __init__(self, pos, groups, stage_num):
        super().__init__(groups)
        if stage_num == 0 or stage_num == 1:
            self.image = pygame.image.load(os.path.join(stage_road_path, "rev_corner4.png")).convert_alpha()
        elif stage_num == 2:
            self.image = pygame.image.load(os.path.join(stage_P_path, "wTile_rev_C4.png")).convert_alpha()
        elif stage_num == 3:
            self.image = pygame.image.load(os.path.join(stage_H_path, "tile_red_Rev_corner4.png")).convert_alpha()
        elif stage_num == 4:
            self.image = pygame.image.load(os.path.join(stage_D_path, "tile_purple_Rcorner4.png")).convert_alpha()
        elif stage_num == 5:
            self.image = pygame.image.load(os.path.join(stage_Z_path, "tile_electric_Revcorner4.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-3, -3)
        self.name = "Road"