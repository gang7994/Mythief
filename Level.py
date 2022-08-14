import pygame, os
from Settings import *
from BorderImages import Wall, NoneRoad, Finish, Obstacle
from Player import Player
from Road import Road
from Monster import Monster

# 레벨 클래스
class Level:
    def __init__(self, map_idx):
        self.map_idx = map_idx
        self.display_surface = pygame.display.get_surface()
        self.images = pygame.sprite.Group()
        self.border_images = pygame.sprite.Group()
        self.create_map()

    # 맵 생성
    def create_map(self):
        for row_idx, row in enumerate(map[self.map_idx]):
            for col_idx, col in enumerate(row):
                tile_pos_x = col_idx * tile_width_size
                tile_pos_y = row_idx * tile_height_size
                if col == ".":
                    NoneRoad((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "W":
                    Wall((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "O":
                    Obstacle((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "R" or col == "P" or col == "M":
                    Road((tile_pos_x, tile_pos_y), [self.images])
                if col == "F":
                    self.finish = Finish((tile_pos_x, tile_pos_y), [self.images])
                if col == "P":
                    player_start_pos_x = tile_pos_x
                    player_start_pos_y = tile_pos_y
                if col == "M":
                    monster_start_pos_x = tile_pos_x
                    monster_start_pos_y = tile_pos_y

        self.player = Player((player_start_pos_x, player_start_pos_y), [self.images], self.border_images)
        self.monster = Monster((monster_start_pos_x, monster_start_pos_y), [self.images, self.border_images], self.border_images)

    # 현재 레벨의 플레이어 반환
    def get_player(self):
        return self.player

    # 현재 레벨의 도착지 반환
    def get_finish(self):
        return self.finish

    # 현재 레벨의 메인 게임 로직
    def run(self):
        self.images.draw(self.display_surface)
        self.player.rocks.draw(self.display_surface)
        self.monster.monster_update()
        self.images.update()