import pygame, os, random
from Settings import *
from BorderImages import Wall1, Wall2, Wall3, Wall4, Fire_Wall, Corner1, Corner2, Corner3,\
                         Corner4, NoneRoad, Finish, Finish2, Finish3, Finish4, Obstacle, WaterHole, Stage0, Stage1,\
                         Stage2, Stage3, Stage4, Stage5, Wave, Flood, Pillar0, Pillar1,Pillar2, Thunder, \
                         CrossWire, DownLeftWire, DownRightWire, HorizontalDownWire, HorizontalUpWire, \
                         UpLeftWire, UpRightWire, VerticalLeftWire, VerticalRightWire, VerticalWire, HorizontalWire
from Player import Player
from Road import Road, Road_Horizontal, Road_Vertical, AlcoholRoad, EventTile, Conductor0, Conductor1,\
    Stage1_Edge1, Stage1_Edge2, Stage1_Edge3, Stage1_Edge4, Stage1_Corner1, Stage1_Corner2, Stage1_Corner3, Stage1_Corner4
from Monster import LaserMonster, RushMonster, Cerberus, FishMonster, Satiros
from Item import Test0Item, Test1Item, Test2Item, GeneralItem0, GeneralItem1, GeneralItem2,\
     GeneralItem3, GeneralItem4, GeneralItem5, GeneralItem6, GeneralItem7, GeneralItem8, GeneralItem9,\
     GeneralItem10, GeneralItem, HadesHelmet
from Map import *
from TextScene import *
from ParticleEffect import Particle

# 레벨 클래스
class Level:
    remain_monster = 0 # Show_info
    def __init__(self, idx, stage_num, map_idx, start_time):
        self.stage_number = stage_num
        self.map_idx = map_idx
        self.display_surface = pygame.display.get_surface()
        # image_groups
        self.images = CameraGroup()
        self.monster_images = CameraGroup()
        self.pillar_images = CameraGroup()
        self.border_images = pygame.sprite.Group()
        self.item_images = pygame.sprite.Group()
        self.door_images = pygame.sprite.Group()
        self.damage_images = pygame.sprite.Group()
        self.fire_images = []
        self.monster_respawn_position = []
        # flood var
        self.flooding_tile = []
        self.flood = []
        self.flooding_time = 10
        self.flooding_flag = False
        self.alpha = 50
        self.flood_cnt = 0
        # tile random_mix
        self.wave_start_position = []
        self.wave = []
        self.wave_flag = False
        self.wave_cool_time = True
        self.wave_cnt = 0
        self.tile_group = []
        self.random_group = []
        #monster list
        self.monsterlist = []
        # thunder random var
        self.thunder_start_position = []
        self.thunder_flag = False
        self.thunder_cool_time = True
        # conductor var
        self.conductor1 = None
        # map_init
        self.cur_map = map[0]
        self.event_item_list = []
        self.create_map()
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
        # text var
        self.text = TextManager(self.stage_number + 1)
        self.text_idx = idx
        
 

    # 맵 생성
    def create_map(self):
        global random_event_item_text, event_texts

        if self.stage_number == 0: #메인
            self.cur_map = map[0]
        elif self.stage_number == 1: #튜토리얼
            self.cur_map = map[1]
        elif self.stage_number == 2:
            self.cur_map = map[2];
        elif self.stage_number == 3:
            self.cur_map = map[3]
        elif self.stage_number == 4:
            self.cur_map = map[4]
        elif self.stage_number == 5:
            self.cur_map = map[5]
        elif self.stage_number == 6:
            self.cur_map = map[6]

        for row_idx, row in enumerate(self.cur_map[self.map_idx]):
            for col_idx, col in enumerate(row):
                tile_pos_x = col_idx * tile_width_size + horizontal_margin
                tile_pos_y = row_idx * tile_height_size + vertical_margin
                if col == "." or col == "WA" or col == "CR" or col == "PL0" or col == "PL1" or col == "PL2" or col == "FM" or col == "FCR":   # 파도 실험중
                    NoneRoad((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                    self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    if col == "WA":
                        self.wave_start_position.append((tile_pos_x, tile_pos_y))


                if col == "─":
                    HorizontalWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "│":
                    VerticalWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┌":
                    DownRightWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┐":
                    DownLeftWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┘":
                    UpLeftWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "└":
                    UpRightWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "├":
                    VerticalRightWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┬":
                    HorizontalDownWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┤":
                    VerticalLeftWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┴":
                    HorizontalUpWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "┼":
                    CrossWire((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "CD0":                                              #Thunder 관련 코드 필요. Thunder가 Conductor를 때리면 이미지 변경(electric_11_on.png) 그 동안 문 열림
                    Conductor0((tile_pos_x, tile_pos_y), [self.images])
                if col == "CD1":                                              #Thunder 관련 코드 필요. Thunder가 Conductor를 때리면 이미지 변경(electric_11_on.png) 그 동안 문 열림
                    self.conductor1 = Conductor1((tile_pos_x, tile_pos_y), [self.images])

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
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                if self.cur_map == map[0] or self.cur_map == map[1] or self.cur_map == map[2]:
                    if col == "RE1":
                        Stage1_Edge1((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RE2":
                        Stage1_Edge2((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RE3":
                        Stage1_Edge3((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RE4":
                        Stage1_Edge4((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RC1":
                        Stage1_Corner1((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RC2":
                        Stage1_Corner2((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RC3":
                        Stage1_Corner3((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                    elif col =="RC4":
                        Stage1_Corner4((tile_pos_x, tile_pos_y), [self.images])
                        self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                        self.flooding_tile.append((tile_pos_x, tile_pos_y))
                        self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                        

                if col == "R" or col == "P" or col == "M" or col == "RM" or col == "I0" or col == "I1" or col == "I2" or \
                    col == "GI" or col == "GI0" or col == "GI1" or col == "GI2" or col == "GI3" or col == "GI4" or col == "GI5"  or \
                    col == "GI6" or col == "GI7" or col == "GI8"  or col == "GI9"  or col == "GI10" or col == "H":
                    Road((tile_pos_x, tile_pos_y), [self.images])
                    self.monster_respawn_position.append((tile_pos_x, tile_pos_y))
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                    self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                if col == "E000R":
                    EventTile((tile_pos_x, tile_pos_y), [self.images], "000")
                    random_event_item_text = random.sample(event_list, k=3)
                    event_texts["000"] = [event_item_text[random_event_item_text[0]],
                                          event_item_text[random_event_item_text[1]],
                                          event_item_text[random_event_item_text[2]]]
                if col == "AR":
                    AlcoholRoad((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                if col == "PL0":
                    Pillar0((tile_pos_x, tile_pos_y), [self.pillar_images, self.border_images])
                if col == "PL1":
                    Pillar1((tile_pos_x, tile_pos_y), [self.pillar_images, self.border_images])
                if col == "PL2":
                    Pillar2((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                
                if col == "F":
                    self.finish = Finish((tile_pos_x, tile_pos_y), [self.images, self.border_images], self.stage_number, self.map_idx)
                if col == "F2":
                    self.finish = Finish2((tile_pos_x, tile_pos_y), [self.images, self.border_images], self.stage_number, self.map_idx)
                if col == "F3":
                    self.finish = Finish3((tile_pos_x, tile_pos_y), [self.images, self.border_images], self.stage_number, self.map_idx)
                if col == "F4":
                    self.finish = Finish4((tile_pos_x, tile_pos_y), [self.images, self.border_images], self.stage_number, self.map_idx)
                
                if col == "I0":
                    self.event_item_list.append(Test0Item((tile_pos_x, tile_pos_y), [self.images, self.item_images]))
                if col == "I1":
                    self.event_item_list.append(Test1Item((tile_pos_x, tile_pos_y), [self.images, self.item_images]))
                if col == "I2":
                    self.event_item_list.append(Test2Item((tile_pos_x, tile_pos_y), [self.images, self.item_images]))
                if col == "GI0":
                    GeneralItem0((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI1":
                    GeneralItem1((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI2":
                    GeneralItem2((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI3":
                    GeneralItem3((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI4":
                    GeneralItem4((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI5":
                    GeneralItem5((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI6":
                    GeneralItem6((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI7":
                    GeneralItem7((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI8":
                    GeneralItem8((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI9":
                    GeneralItem9((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI10":
                    GeneralItem10((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "GI":
                    GeneralItem((tile_pos_x + tile_width_size // 2 - 20, tile_pos_y + tile_height_size // 2 - 20), [self.images, self.item_images])
                if col == "H":
                    HadesHelmet((tile_pos_x, tile_pos_y), [self.images, self.item_images])
                if col == "P":
                    player_start_pos_x = tile_pos_x
                    player_start_pos_y = tile_pos_y
                if col == "M":
                    self.monster = LaserMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images],
                            self.border_images, self.damage_images, self.images)
                    self.monsterlist.append(self.monster)
                    Level.remain_monster+=1 # Show_info
                if col == "RM":
                    self.monster = RushMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images],
                            self.border_images)
                    self.monsterlist.append(self.monster)
                    Level.remain_monster+=1 # Show_info
                if col == "FM":
                    FishMonster((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images], self.border_images)
                if "SM" in col:
                    Satiros((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images], self.border_images, int(col[2:]))
                if col == "CR":
                    Cerberus((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images], self.border_images, True)
                    Level.remain_monster+=1 # Show_info
                if col == "FCR":
                    Cerberus((tile_pos_x, tile_pos_y), [self.monster_images, self.damage_images], self.border_images, False)
                    Level.remain_monster+=1 # Show_info
                if col == "W1g":
                    Fire_Wall((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.fire_images.append(Glow([tile_pos_x, tile_pos_y]))
                if col == "W":
                    WaterHole((tile_pos_x, tile_pos_y), [self.images, self.border_images])
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                if col == "S0":
                    self.stage0 = Stage0((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "S1":
                    self.stage1 = Stage1((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "S2":
                    self.stage2 = Stage2((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "S3":
                    self.stage3 = Stage3((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "S4":
                    self.stage4 = Stage4((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "S5":
                    self.stage5 = Stage5((tile_pos_x, tile_pos_y), [self.images, self.border_images, self.door_images])
                if col == "RH":
                    Road_Horizontal((tile_pos_x, tile_pos_y), [self.images])
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                    self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))
                if col == "RV":
                    Road_Vertical((tile_pos_x, tile_pos_y), [self.images])
                    self.flooding_tile.append((tile_pos_x, tile_pos_y))
                    self.thunder_start_position.append((tile_pos_x, tile_pos_y - 96))

                
                


        self.player = Player((player_start_pos_x, player_start_pos_y), [self.images],
                             self.border_images,
                             self.damage_images,
                             self.item_images,
                             self.door_images,
                             self.images)

        if len(self.event_item_list) != 0:
            for idx, item in enumerate(self.event_item_list):
                item.event = random_event_item_text[idx]

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
            self.glow.is_pause = True
        elif str == 'F':
            self.is_pause = False
            for sprite in self.images:
                sprite.is_pause = False
            for sprite in self.monster_images:
                sprite.is_pause = False
            for fire in self.fire_images:
                fire.is_pause = False
            self.glow.is_pause = False

    # 플레이어 , 적 거리 계산
    def get_player_distance(self, player, dt):
        for monster in self.monster_images:
            if monster.name == "rush_Monster" or monster.name == "cerberus" or monster.name == "Fish":
                monster_vec = pygame.math.Vector2(monster.rect.center)
                player_vec = pygame.math.Vector2(player.rect.center)
                distance = (player_vec - monster_vec).magnitude()
                if (player_vec - monster_vec)[0] > -3 and (player_vec - monster_vec)[0] < 3:
                    dir_x = 0
                elif (player_vec - monster_vec)[0] < 0:
                    dir_x = -1
                elif (player_vec - monster_vec)[0] > 0:
                    dir_x = 1

                if (player_vec - monster_vec)[1] > -3 and (player_vec - monster_vec)[1] < 3:
                    dir_y = 0
                elif (player_vec - monster_vec)[1] < 0:
                    dir_y = -1
                elif (player_vec - monster_vec)[1] > 0:
                    dir_y = 1
                if monster.name == "cerberus":
                    if distance <= monster.boundary and self.player.is_player_cerberus:
                        monster.rush((dir_x, dir_y), dt)
                    else:
                        monster.is_rush = False
                else:
                    if distance <= monster.boundary:
                        monster.rush((dir_x, dir_y), dt)
                    else:
                        monster.is_rush = False

    def monster_auto_create(self, time, dt):
        if int(time) % 15 != 0:
            self.create_flag = False
        if int(time) % 15 == 0 and int(time) != 0 and not self.create_flag:
            self.create_flag = True
            for idx, sample in enumerate(random.sample(self.monster_respawn_position, k=self.one_per_create)):
                if idx % 2 == 0:
                    monster = LaserMonster(sample, [self.monster_images, self.damage_images],
                                self.border_images, self.damage_images, self.images)
                    self.monsterlist.append(monster)
                elif idx % 2 != 0:
                    monster = RushMonster(sample, [self.monster_images, self.damage_images],
                                self.border_images)
                    self.monsterlist.append(monster)
                Level.remain_monster += 1  # Show_info

    def tile_random_mix(self):
        random.shuffle(self.random_group)
        for idx, tile in enumerate(self.tile_group):
            tile.rect, self.random_group[idx].rect = self.random_group[idx].rect, tile.rect
            tile.hitbox, self.random_group[idx].hitbox = self.random_group[idx].hitbox, tile.hitbox

    def create_wave(self, time, wave_idx):
        if int(time) % 3 != 0:
            self.wave_flag = False
        if int(time) % 3 == 0 and int(time) != 0 and not self.wave_flag and not self.wave_cool_time:
            self.wave.append(Wave((self.wave_start_position[wave_idx][0], self.wave_start_position[wave_idx][1] + self.wave_cnt), [self.images]))
            self.wave_cnt += 48
            self.wave_flag = True
            self.wave_collision(self.wave[-1].rect)
            if len(self.wave) == 0:
                self.tile_random_mix()
                while True:
                    self.choice = random.choice(self.tile_group)
                    if self.choice.name == "Road": break
                self.wave_cool_time = True
                if self.player.player_in_wave:
                    self.player.is_tile_mix = True
                    if self.player.is_effect1 and self.player.is_first1:
                        self.player.hitbox.left = self.choice.hitbox[0]
                        self.player.hitbox.top = self.choice.hitbox[1]
                        self.player.is_first1 = False
                
                self.tile_group.clear()
                self.random_group.clear()


    def wave_collision(self, wave_rect):
        for sprite in self.images:
            if sprite.rect.colliderect(wave_rect):
                if sprite.name == "Wall":
                    for i in self.wave:
                        self.images.remove(i)
                    self.wave.clear()
                if sprite.name == "Road" or sprite.name == "NoneRoad" or sprite.name == "WaterHole":
                    
                    self.tile_group.append(sprite)
                    self.random_group.append(sprite)

                    
    def wave_player_collision_check(self):
        self.player.player_in_wave = False
        for wave in self.wave:
            if wave.rect.colliderect(self.player.hitbox):
                self.player.player_in_wave = True

    def flooding(self, time):
        if int(time) % 3 != 0:
            self.flooding_flag = False
        if int(time) % 3 == 0 and int(time) != 0 and not self.flooding_flag:
            self.flooding_flag = True
            if self.flood_cnt == 0:
                for pos in self.flooding_tile:
                    self.flood.append(Flood(pos, [self.images]))
            elif self.flood_cnt < 16:
                for sprite in self.flood:
                    sprite.image.set_alpha(self.alpha)
            else:
                self.player.is_dead = True
            self.alpha += 256//16
            self.flood_cnt += 1
            
    def random_thunder(self, time):
        if int(time) % 3 != 0:
            self.thunder_flag = False
        if int(time) % 3 == 0 and int(time) != 0 and not self.thunder_flag:
            self.thunder_flag = True
            for thunder in random.sample(self.thunder_start_position, k=5-self.player.rod_num):
                Thunder(thunder, [self.monster_images, self.damage_images], self.images, self.border_images)
            if len(self.player.rod_position) > 0:
                for i in self.player.rod_position:
                    Thunder(i, [self.monster_images, self.damage_images], self.images, self.border_images)

    # 현재 레벨의 메인 게임 로직
    def run(self):
        dt = self.clock.tick(FPS)
        
        if not self.player.is_hadesHelmet:
            self.player.is_player_cerberus = True # 케르베로스 트리거
        self.images.custom_draw(self.player, dt)
        self.monster_images.custom_draw(self.player, dt)
        self.pillar_images.custom_draw(self.player, dt)
        self.monster_images.update()
        self.images.update()

        if self.player.get_event_item:
            self.finish.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
            self.finish.name = "Finish"

        if not self.is_pause:
            self.get_player_distance(self.player, dt)
            self.tem_now_time = pygame.time.get_ticks() - self.start_time
            self.elapsed_time = (self.tem_now_time) / 1000

            if self.stage_number == 5 and (self.map_idx in [0,1,2,4,5,6,8]): # 번개 알고리즘 + 전도체 블록 알고리즘
                self.random_thunder(self.elapsed_time)
                if self.conductor1 is not None:
                    if self.conductor1.is_on and self.finish.name == "ClosedFinish":
                        self.finish.name = "Finish"
                        self.finish.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()

            if self.stage_number != 0 and self.stage_number != 1:
                self.monster_auto_create(self.elapsed_time, dt)

            if self.stage_number == 2 and len(self.wave_start_position) != 0:
                if self.wave_cool_time:
                    self.wave_idx = random.randint(0, len(self.wave_start_position) - 1)
                    self.wave_cool_time = False
                    self.wave_cnt = 0
                self.wave_player_collision_check()
                self.create_wave(self.elapsed_time * 10, self.wave_idx)
            elif self.stage_number == 2 and (self.map_idx == 2 or self.map_idx == 4 or self.map_idx == 8):
                self.flooding(self.elapsed_time)

        else:
            self.start_time = pygame.time.get_ticks() - self.tem_now_time

        if self.stage_number == 3 and (self.map_idx == 1 or self.map_idx == 3 or self.map_idx == 6):
            self.glow.wait_bright()
            self.glow.wait_dark()
            self.glow.draw_before_glow()
            self.glow.draw_player_glow()
            self.player.is_dark = True


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
        for i in [[10, 50],[50,40],[100,30],[200,20],[255,10]]:
            self.player_glow.append([self.circle_surf(i[1],(i[0],i[0],i[0])), i[1]])
        self.is_player_glow = False
        self.is_before_glow = False
        self.bright_start = pygame.time.get_ticks()
        self.dark_start = pygame.time.get_ticks()
        self.bright_time = 1000
        self.dark_time = 5000
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
        if self.is_player_glow:
            self.new_surf.fill(BLACK)
            for glow in self.player_glow:
                self.new_surf.blit(glow[0], (self.half_width - glow[1], self.half_height - glow[1]))
            self.display_surface.blit(self.new_surf, pygame.math.Vector2(), special_flags=pygame.BLEND_RGB_MULT)

    def draw_before_glow(self):
        if self.is_before_glow:
            self.new_surf.fill(BLACK)
            for glow in self.player_glow:
                self.new_surf.blit(glow[0], (self.half_width - glow[1], self.half_height - glow[1]))
            self.display_surface.blit(self.new_surf, pygame.math.Vector2(), special_flags=pygame.BLEND_RGB_MULT)

    def wait_bright(self):
        if not self.is_pause:
            if not self.is_player_glow:
                self.tem_now_time = pygame.time.get_ticks() - self.bright_start
                if self.tem_now_time > 700:
                    if self.is_before_glow:
                        self.is_before_glow = False
                    elif not self.is_before_glow:
                        self.is_before_glow = True
                if self.tem_now_time > self.bright_time:
                    self.is_before_glow = False
                    self.is_player_glow = True
                    self.dark_start = pygame.time.get_ticks()
        else:
            self.bright_start = pygame.time.get_ticks() - self.tem_now_time

    def wait_dark(self):
        if not self.is_pause:
            if self.is_player_glow:
                self.tem_now_time = pygame.time.get_ticks() - self.dark_start
                if self.tem_now_time > self.dark_time:
                    self.is_player_glow = False
                    self.bright_start = pygame.time.get_ticks()
        else:
            self.dark_start = pygame.time.get_ticks() - self.tem_now_time

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
