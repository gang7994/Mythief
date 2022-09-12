import pygame, os, random
from Settings import *
from BorderImages import Wall1, Wall2, Wall3, Wall4, Fire_Wall, Corner1, Corner2, Corner3, Corner4, NoneRoad, Finish, Obstacle, WaterHole, Stage0, Stage1, Stage2, Stage3, Stage4, Stage5
from Player import Player
from Road import Road
from Monster import LaserMonster, RushMonster
from Item import Test0Item, Test1Item, Test2Item
from Map import *
from TextScene import *
from ParticleEffect import Particle

# 레벨 클래스
class Level:
    remain_monster = 0 # Show_info
    def __init__(self, stage_num, map_idx, start_time):
        self.stage_number = stage_num
        self.map_idx = map_idx
        self.display_surface = pygame.display.get_surface()
        # image_groups
        self.images = CameraGroup()
        self.monster_images = CameraGroup()
        self.border_images = pygame.sprite.Group()
        self.item_images = pygame.sprite.Group()
        self.damage_images = pygame.sprite.Group()
        self.fire_images = []
        self.road_images = []
        # tile random_mix
        self.tile_group = []
        self.random_group = []
        self.tile_mix_flag = False
        # map_init
        self.create_map()
        self.cur_map = map[0]
        # player_glow
        self.glow = Glow(self.player.rect.topleft)
        # FPS, pause var
        self.clock = pygame.time.Clock()
        self.is_pause = False
        # elapsed time
        self.start_time = start_time
        # monster_auto_create var
        self.one_per_create = 5
        self.create_flag = False
        self.create_effects = [Glow([0,0]), Glow([0,0]), Glow([0,0]), Glow([0,0]), Glow([0,0])]


    # 맵 생성
    def create_map(self):
        if self.stage_number == 0:
            self.cur_map = map[0]
        elif self.stage_number == 1:
            self.cur_map = map[1]
        elif self.stage_number == 2:
            self.cur_map = map[2]

        for row_idx, row in enumerate(self.cur_map[self.map_idx]):
            for col_idx, col in enumerate(row):
                tile_pos_x = col_idx * tile_width_size + horizontal_margin
                tile_pos_y = row_idx * tile_height_size + vertical_margin
                if col == ".":
                    tem = NoneRoad((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.tile_group.append(tem)
                    self.random_group.append(tem)
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
                    tem = Obstacle((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.tile_group.append(tem)
                    self.random_group.append(tem)
                if col == "R" or col == "P" or col == "M" or col == "JM" or col == "I0" or col == "I1" or col == "I2":
                    tem = Road((tile_pos_x, tile_pos_y), [self.images])
                    self.tile_group.append(tem)
                    self.random_group.append(tem)
                    self.road_images.append((tile_pos_x, tile_pos_y))
                if col == "F":
                    self.finish = Finish((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "I0":
                    Test0Item((tile_pos_x + tile_width_size // 2 - 8, tile_pos_y + tile_height_size // 2 - 8), [self.images, self.item_images])
                if col == "I1":
                    Test1Item((tile_pos_x + tile_width_size // 2 - 8, tile_pos_y + tile_height_size // 2 - 8), [self.images, self.item_images])
                if col == "I2":
                    Test2Item((tile_pos_x + tile_width_size // 2 - 8, tile_pos_y + tile_height_size // 2 - 8), [self.images, self.item_images])
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
                if col == "W":
                    WaterHole((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S0":
                    self.stage0 = Stage0((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S1":
                    self.stage1 = Stage1((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S2":
                    self.stage2 = Stage2((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S3":
                    self.stage3 = Stage3((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S4":
                    self.stage4 = Stage4((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "S5":
                    self.stage5 = Stage5((tile_pos_x, tile_pos_y), [self.images, self.border_images])

        self.player = Player((player_start_pos_x, player_start_pos_y), [self.images],
                             self.border_images,
                             self.damage_images,
                             self.item_images,
                             self.images,
                             self.road_images)

    # 현재 레벨의 플레이어 반환
    def get_player(self):
        return self.player

    # 현재 레벨의 도착지 반환
    def get_finish(self):
        return self.finish

    def get_stage0(self):
        return self.stage0
    def get_stage1(self):
        return self.stage1
    def get_stage2(self):
        return self.stage2
    def get_stage3(self):
        return self.stage3
    def get_stage4(self):
        return self.stage4
    def get_stage5(self):
        return self.stage5

    def pause(self, str):
        if str == "T":
            self.is_pause = True
            for sprite in self.images:
                sprite.is_pause = True
            for sprite in self.monster_images:
                sprite.is_pause = True
            for fire in self.fire_images:
                fire.is_pause = True
        elif str == 'F':
            self.is_pause = False
            for sprite in self.images:
                sprite.is_pause = False
            for sprite in self.monster_images:
                sprite.is_pause = False
            for fire in self.fire_images:
                fire.is_pause = False

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

    def monster_auto_create(self, time, dt):
        for i in self.create_effects:
            i.get_create_effects(i.pos)
        if int(time) % 10 != 0:
            self.create_flag = False
        if int(time) % 10 == 0 and int(time) != 0 and not self.create_flag:
            self.create_flag = True
            for idx, sample in enumerate(random.sample(self.road_images, k=self.one_per_create)):
                self.create_effects[idx].monster_create_effect(self.player, sample, dt)
                LaserMonster(sample, [self.monster_images, self.damage_images],
                             self.border_images, self.damage_images, self.images)
                Level.remain_monster += 1  # Show_info

    def tile_random_mix(self, time):
        if int(time) % 5 != 0:
            self.tile_mix_flag = False
        if int(time) % 5 == 0 and int(time) != 0 and not self.tile_mix_flag:
            self.tile_mix_flag = True
            random.shuffle(self.random_group)
            for idx, tile in enumerate(self.tile_group):
                tile.rect, self.random_group[idx].rect = self.random_group[idx].rect, tile.rect
                tile.hitbox, self.random_group[idx].hitbox = self.random_group[idx].hitbox, tile.hitbox

    # 현재 레벨의 메인 게임 로직
    def run(self):
        dt = self.clock.tick(FPS)
        self.images.custom_draw(self.player, dt)
        self.monster_images.custom_draw(self.player, dt)
        self.monster_images.update()
        self.images.update()

        if not self.is_pause:
            self.get_player_distance(self.player, dt)
            self.tem_now_time = pygame.time.get_ticks() - self.start_time
            elapsed_time = (self.tem_now_time) / 1000
            if self.stage_number != 0 and self.stage_number != 1:
                self.monster_auto_create(elapsed_time, dt)
            self.tile_random_mix(elapsed_time)
        else:
            self.start_time = pygame.time.get_ticks() - self.tem_now_time

        # 어두운 맵은 따로 확인이 가능한 변수를 두는 것이 좋을듯 합니다. 이부분 수정해야겠네요
        """if self.map_idx == 2:
            self.glow.draw_player_glow()
            for fire in self.fire_images:
                fire.draw_fire_glow(self.player, dt)"""

        self.glow.draw_display_change(dt)

        if self.player.is_dead:
            self.glow.draw_dead_display_change(dt)

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
            if sprite.name == "Player":
                self.display_surface.blit(sprite.image, (offset_rect[0], offset_rect[1] - 5))
            else:
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
        # glow var
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
        # pause var
        self.is_pause = False
        # dead_display_change_animation
        self.dead_display_flag = False
        self.dead_display_surf = pygame.Surface((screen_width, screen_height))
        self.dead_circle_pause = False
        self.dead_loop_cnt = 0
        self.dead_rad = 700
        # monster_create_particle
        self.monster_create_particles = []

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

    def draw_fire_glow(self, player, dt):
        pos = []
        pos.append(self.pos[0])
        pos.append(self.pos[1])
        if not self.is_pause:
            self.fire_glow.append([pos, [random.randint(0, 20) / 10 - 1, -5], random.randint(6, 9)])
        if not self.camera_move_flag:
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
        self.camera_move((player.rect.centerx - self.half_width, player.rect.centery - self.half_height), dt)
        for particle in self.fire_glow:
            if not self.is_pause:
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

    def draw_dead_display_change(self, dt):
        if not self.dead_display_flag:
            self.dead_display_surf.fill((0, 0, 0))
            self.dead_display_surf.blit(self.circle_surf(self.dead_rad, (255, 255, 255)), (self.half_width - self.dead_rad, self.half_height - self.dead_rad))
            self.display_surface.blit(self.dead_display_surf, pygame.math.Vector2(), special_flags=pygame.BLEND_RGB_MULT)
            if not self.dead_circle_pause: self.dead_rad -= 10 * (dt // 6)
            if self.dead_rad < 100:
                self.dead_loop_cnt += 1
                self.dead_circle_pause = True
                if self.dead_loop_cnt == 1:
                    self.pause_start = pygame.time.get_ticks()
                else:
                    self.pause_end = pygame.time.get_ticks()
                    if self.pause_end - self.pause_start > 700:
                        self.dead_circle_pause = False
            if self.dead_rad <= 0: self.dead_display_flag = True

    def get_create_effects(self, pos):
        while len(self.monster_create_particles) < 30:
            self.monster_create_particles.append(
                [[pos[0] + random.randint(-10, 10), pos[1] + random.randint(0, 10)], [random.randint(0, 20) / 10 - 1, -5],
                 random.randint(10, 15)])

    def monster_create_effect(self, player, pos, dt):
        if not self.camera_move_flag:
            self.offset.x = player.rect.centerx - self.half_width
            self.offset.y = player.rect.centery - self.half_height
        self.camera_move((player.rect.centerx - self.half_width, player.rect.centery - self.half_height), dt)
        for i in self.monster_create_particles:
            i[0] = [pos[0] + random.randint(-10, 10), pos[1] + random.randint(0, 10)]
        while len(self.monster_create_particles) != 0:
            for particle in self.monster_create_particles:
                particle[0][1] += particle[1][1] * (dt // 6)
                particle[0][0] += particle[1][0] * (dt // 6)
                particle[2] -= 1 * (dt // 6)
                particle[1][1] += 0.25 * (dt // 6)
                pygame.draw.circle(self.display_surface, (255, 255, 255), [int(particle[0][0]) - self.offset.x, int(particle[0][1]) - self.offset.y], int(particle[2]))
                if particle[2] <= 0:
                    self.monster_create_particles.remove(particle)
