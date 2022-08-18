import pygame, os
from Settings import *
from BorderImages import Wall1, Wall2, Wall3, Wall4, Corner1, Corner2, Corner3, Corner4, NoneRoad, Finish, Obstacle
from Player import Player
from Road import Road
from Monster import LaserMonster, JumpMonster

# 레벨 클래스
class Level:
    remain_monster = 0 # Show_info
    def __init__(self, map_idx):
        self.map_idx = map_idx
        self.display_surface = pygame.display.get_surface()
        self.images = pygame.sprite.Group()
        self.border_images = pygame.sprite.Group()
        self.monster_images = pygame.sprite.Group()
        self.damage_images = pygame.sprite.Group()
        self.create_map()

    # 맵 생성
    def create_map(self):
        for row_idx, row in enumerate(map[self.map_idx]):
            for col_idx, col in enumerate(row):
                tile_pos_x = col_idx * tile_width_size + horizontal_margin
                tile_pos_y = row_idx * tile_height_size + vertical_margin
                if col == ".":
                    NoneRoad((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "W1":
                    Wall1((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "W2":
                    Wall2((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "W3":
                    Wall3((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "W4":
                    Wall4((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "C1":
                    Corner1((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "C2":
                    Corner2((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "C3":
                    Corner3((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "C4":
                    Corner4((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "O":
                    Obstacle((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "R" or col == "P" or col == "M" or col == "JM":
                    Road((tile_pos_x, tile_pos_y), [self.images])
                if col == "F":
                    self.finish = Finish((tile_pos_x, tile_pos_y), [self.images])
                if col == "P":
                    player_start_pos_x = tile_pos_x
                    player_start_pos_y = tile_pos_y
                if col == "M":
                    LaserMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images],
                            self.border_images, self.damage_images)
                    Level.remain_monster+=1 # Show_info
                if col == "JM":
                    JumpMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images],
                            self.border_images, self.damage_images)
                    Level.remain_monster+=1 # Show_info


        self.player = Player((player_start_pos_x, player_start_pos_y), [self.images], self.border_images, self.damage_images)

    # 현재 레벨의 플레이어 반환
    def get_player(self):
        return self.player

    # 현재 레벨의 도착지 반환
    def get_finish(self):
        return self.finish
    
    # 몬스터 레이져 그리기
    def draw_monster_laser(self, display_surface):
        for monster in self.monster_images:
            if monster.name == "laser_Monster":
                monster.lasers.draw(display_surface)

    # 플레이어 , 적 거리 계산
    def get_player_distance(self, player):
        for monster in self.monster_images:
            if monster.name == "jump_Monster":
                monster_vec = pygame.math.Vector2(monster.rect.center)
                player_vec = pygame.math.Vector2(player.rect.center)
                distance = (player_vec - monster_vec).magnitude()
                if distance <= monster.boundary:
                    if (player_vec - monster_vec)[0] != 0 or (player_vec - monster_vec)[1] != 0:
                        monster.rush((player_vec - monster_vec).normalize())
                else:
                    monster.is_rush = False

    # 현재 레벨의 메인 게임 로직
    def run(self):
        self.images.draw(self.display_surface)
        self.monster_images.draw(self.display_surface)
        self.player.rocks.draw(self.display_surface)
        self.draw_monster_laser(self.display_surface)
        self.get_player_distance(self.player)
        self.monster_images.update()
        self.images.update()