import pygame, os, random
from Settings import *
from BorderImages import Wall1, Wall2, Wall3, Wall4, Fire_Wall, Corner1, Corner2, Corner3, Corner4, NoneRoad, Finish, Obstacle
from Player import Player
from Road import Road
from Monster import LaserMonster, RushMonster

# 레벨 클래스
class Level:
    remain_monster = 0 # Show_info
    def __init__(self, map_idx):
        self.map_idx = map_idx
        self.images = CameraGroup()
        self.border_images = pygame.sprite.Group()
        self.monster_images = CameraGroup()
        self.damage_images = pygame.sprite.Group()
        self.fire_images = []
        self.create_map()
        self.glow = Glow(self.player.rect.topleft)
        self.clock = pygame.time.Clock()
        self.is_pause = False

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
                            self.border_images, self.damage_images, self.images)
                    Level.remain_monster+=1 # Show_info
                if col == "JM":
                    RushMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images],
                            self.border_images, self.damage_images)
                    Level.remain_monster+=1 # Show_info
                if col == "W1g":
                    Fire_Wall((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.fire_images.append(Glow([tile_pos_x, tile_pos_y]))


        self.player = Player((player_start_pos_x, player_start_pos_y), [self.images],
                             self.border_images,
                             self.damage_images,
                             self.images)

    # 현재 레벨의 플레이어 반환
    def get_player(self):
        return self.player

    # 현재 레벨의 도착지 반환
    def get_finish(self):
        return self.finish

    def pause(self, str):
        if str == "T":
            self.is_pause = True
            for sprite in self.images:
                sprite.is_pause = True
            for sprite in self.monster_images:
                sprite.is_pause = True
        elif str == 'F':
            self.is_pause = False
            for sprite in self.images:
                sprite.is_pause = False
            for sprite in self.monster_images:
                sprite.is_pause = False

    # 플레이어 , 적 거리 계산
    def get_player_distance(self, player, dt):
        for monster in self.monster_images:
            if monster.name == "rush_Monster":
                monster_vec = pygame.math.Vector2(monster.rect.center)
                player_vec = pygame.math.Vector2(player.rect.center)
                distance = (player_vec - monster_vec).magnitude()
                if (player_vec - monster_vec)[0] < 0:
                    dir_x = -1
                elif (player_vec - monster_vec)[0] == 0:
                    dir_x = 0
                elif (player_vec - monster_vec)[0] > 0:
                    dir_x = 1
                if (player_vec - monster_vec)[1] < 0:
                    dir_y = -1
                elif (player_vec - monster_vec)[1] == 0:
                    dir_y = 0
                elif (player_vec - monster_vec)[1] > 0:
                    dir_y = 1
                if distance <= monster.boundary:
                    monster.rush((dir_x, dir_y), dt)
                else:
                    monster.is_rush = False

    # 현재 레벨의 메인 게임 로직
    def run(self):
        dt = self.clock.tick(FPS)
        self.images.custom_draw(self.player, dt)
        self.monster_images.custom_draw(self.player, dt)
        if not self.is_pause:
            self.get_player_distance(self.player, dt)
        self.monster_images.update()
        self.images.update()
        if self.map_idx == 2:
            self.glow.draw_player_glow()
            for fire in self.fire_images:
                fire.draw_fire_glow(self.player, dt)
        self.glow.draw_display_change(dt)

# 카메라 클래스
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        self.camera_move_flag = False

    # 카메라 드로우
    def custom_draw(self, player, dt):
        if not self.camera_move_flag:
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
        self.camera_move((player.rect.centerx - self.half_width, player.rect.centery - self.half_height), dt)
        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)

    # 카메라 이동
    def camera_move(self, pos, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            self.camera_move_flag = True
            if keys[pygame.K_w]:
                self.offset.y -= 2 * (dt // 6)
                if self.offset.y < pos[1] - 200: self.offset.y = pos[1] - 200
            if keys[pygame.K_a]:
                self.offset.x -= 2 * (dt // 6)
                if self.offset.x < pos[0] - 200: self.offset.x = pos[0] - 200
            if keys[pygame.K_s]:
                self.offset.y += 2 * (dt // 6)
                if self.offset.y > pos[1] + 200: self.offset.y = pos[1] + 200
            if keys[pygame.K_d]:
                self.offset.x += 2 * (dt // 6)
                if self.offset.x > pos[0] + 200: self.offset.x = pos[0] + 200
        else:
            self.camera_move_flag = False

class Glow:
    def __init__(self, pos):
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.new_surf = pygame.Surface((screen_width, screen_height))
        self.camera_move_flag = False
        self.player_glow = []
        self.fire_glow = []
        self.pos = pos
        for i in [[10, 300],[50,200],[100,100],[200,50],[255,10]]:
            self.player_glow.append([self.circle_surf(i[1],(i[0],i[0],i[0])), i[1]])
        # display_change_animation
        self.game_display_flag = False
        self.display_anim_surf = pygame.Surface((screen_width, screen_height))
        self.circle_pause = False
        self.loop_cnt = 0
        self.rad = 0




    def camera_move(self, pos, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
            self.camera_move_flag = True
            if keys[pygame.K_w]:
                self.offset.y -= 2 * (dt // 6)
                if self.offset.y < pos[1] - 200: self.offset.y = pos[1] - 200
            if keys[pygame.K_a]:
                self.offset.x -= 2 * (dt // 6)
                if self.offset.x < pos[0] - 200: self.offset.x = pos[0] - 200
            if keys[pygame.K_s]:
                self.offset.y += 2 * (dt // 6)
                if self.offset.y > pos[1] + 200: self.offset.y = pos[1] + 200
            if keys[pygame.K_d]:
                self.offset.x += 2 * (dt // 6)
                if self.offset.x > pos[0] + 200: self.offset.x = pos[0] + 200
        else:
            self.camera_move_flag = False

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
        surf.set_colorkey((0, 0, 0))
        return surf

    def draw_player_glow(self):
        self.new_surf.fill(BLACK)
        for glow in self.player_glow:
            self.new_surf.blit(glow[0], (self.half_width - glow[1], self.half_height - glow[1]))
        self.display_surface.blit(self.new_surf, pygame.math.Vector2(), special_flags=pygame.BLEND_RGB_MULT)
    
    # 버그 존재 - 고쳐야함
    def draw_fire_glow(self, player, dt):
        pos = []
        pos.append(self.pos[0])
        pos.append(self.pos[1])
        self.fire_glow.append([pos, [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 9)])
        if not self.camera_move_flag:
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
        self.camera_move((player.rect.centerx - self.half_width, player.rect.centery - self.half_height), dt)
        for particle in self.fire_glow:
            particle[0][1] += particle[1][1]
            particle[2] -= 0.5
            particle[1][1] += 0.15
            pygame.draw.circle(self.display_surface,
                               (255, 255, 255),
                               [int(particle[0][0]) - self.offset.x + 24, int(particle[0][1]) - self.offset.y + 24],
                               int(particle[2]))
            radius = particle[2] * 2
            self.display_surface.blit(self.circle_surf(radius, (20, 20, 60)),
                                      (int(particle[0][0] - radius) - self.offset.x + 24, int(particle[0][1] - radius) - self.offset.y + 24),
                                      special_flags=pygame.BLEND_RGB_ADD)
            if particle[2] <= 0:
                self.fire_glow.remove(particle)

    def draw_display_change(self, dt):
        if not self.game_display_flag:
            self.display_anim_surf.fill((0, 0, 0))
            self.display_anim_surf.blit(self.circle_surf(self.rad, (255, 255, 255)), (self.half_width - self.rad, self.half_height - self.rad))
            self.display_surface.blit(self.display_anim_surf, pygame.math.Vector2(), special_flags=pygame.BLEND_RGB_MULT)
            if not self.circle_pause: self.rad += 10 * (dt // 6)
            if self.rad > 100:
                self.loop_cnt += 1
                self.circle_pause = True
                if self.loop_cnt == 1:
                    self.pause_start = pygame.time.get_ticks()
                else:
                    self.pause_end = pygame.time.get_ticks()
                    if self.pause_end - self.pause_start > 300:
                        self.circle_pause = False
            if self.rad > 700: self.game_display_flag = True