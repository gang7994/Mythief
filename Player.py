import random
import pygame, os
from Settings import *
from Rock import Rock
from TextGroup import *
from Item import ThunderRod, GeneralItem0, GeneralItem1, GeneralItem2, GeneralItem3, GeneralItem4, \
                 GeneralItem5, GeneralItem6, GeneralItem7, GeneralItem8, GeneralItem9, GeneralItem10


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, damage_images, item_images, door_images, images, stage_number, map_idx):
        super().__init__(groups)
        pygame.init()
        self.image = pygame.image.load(os.path.join(images_path, "sprite_idle0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.hitbox.top += 5
        self.rod_put_box = self.hitbox.inflate(-21, -25)
        self.name = "Player"
        self.character_width = self.rect.size[0]
        self.character_height = self.rect.size[1]
        self.stage_num = stage_number
        self.map_num = map_idx
        self.ignore_item = False
        self.item_name_list = ["general_item0", "general_item1", "general_item2",
                               "general_item3", "general_item4", "general_item5",
                               "general_item6", "general_item7", "general_item8",
                               "general_item9", "general_item10"]
        # player hp var
        self.is_dead = False
        # player move var
        self.dir = pygame.math.Vector2()
        self.last_x_dir = 1
        self.last_dir = 2
        self.move_order = [0]
        self.is_horizon = False
        self.player_speed_x = 0
        self.player_speed_y = 0
        # images group
        self.border_images = border_images
        self.damage_images = damage_images
        self.item_images = item_images
        self.door_images = door_images
        self.images = images
        # player rock var
        self.rock_cool_time = 1000
        self.is_rock_ready = True
        self.rock_count = 0
        self.current_time = 0
        self.rock_time = 0
        self.rock_item_effect = False
        # damage var
        self.undamaged_time = 1000    # 무적시간 1초
        self.is_damaged = False      # 데미지 상태인지
        self.is_damage2 = False
        self.is_damage5 = False
        self.is_damage10 = False
        self.is_damage30 = False
        # walk animation variable 
        self.walk_count = 0
        self.walk_time = 0
        self.walk_current_time = 0
        self.step_cooltime = 100
        self.is_walk = True
        # idle animation variable
        self.idle_count = 0
        self.idle_time = 0
        self.idle_current_time = 0
        self.idle_cooltime = 100
        self.is_idle = True
        self.is_move_x = False
        self.is_move_y = False
        # throw animation variable
        self.throw = []
        # pause var
        self.clock = pygame.time.Clock()
        self.is_pause = False
        # item interaction flag
        self.item_interaction = False
        self.current_item_gage = 0
        self.max_item_gage = 100
        self.item_bar_length = 300
        self.item_ratio = self.max_item_gage / self.item_bar_length
        # event item handler var
        self.event_handler = False
        self.event_code = None
        self.get_event_item = False
        # is wave?
        self.is_tile_mix = False
        self.player_in_wave = False
        self.is_road = True
        # stage door interaction flag
        self.stage0_interaction = False
        self.stage1_interaction = False
        self.stage2_interaction = False
        self.stage3_interaction = False
        self.stage4_interaction = False
        self.stage5_interaction = False
        # player_drunken
        self.is_player_drunken = False
        self.drunken_time = 3000
        self.drunken_start_time = 0
        # is player cerberus
        self.is_player_cerberus = True
        self.is_hadesHelmet = False
        # is thunder
        self.is_thunder = False
        self.is_rod_ready = True
        self.rod_put_cool_time = 300
        self.rod_position = []
        self.rod_num = 0
        self.rod_start_time = pygame.time.get_ticks()
        self.rod_current_time = pygame.time.get_ticks()
        # is dark
        self.is_dark = False
        # item effect
        self.is_first0 = True # 이상한 석상
        self.is_first1 = True #대나무 낚싯대
        self.is_effect0 = False #이상한 석상
        self.is_effect1 = False #대나무 낚싯대
        # sound var
        self.effect_vol = 0


    def walk_animation(self):
        if self.walk_count > 5:
            self.walk_count = 0
        self.walk_current_time = pygame.time.get_ticks()
        if self.is_player_drunken:
            if self.walk_count == 0:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken0.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 1:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken1.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 2:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken2.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 3:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken3.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 4:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken4.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 5:
                self.image = pygame.image.load(os.path.join(images_path, "runb_drunken5.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
        else:
            if self.walk_count == 0:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_0.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 1:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_1.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 2:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_2.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 3:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_3.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 4:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_4.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
            elif self.walk_count == 5:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_5.png")).convert_alpha()
                if self.is_damaged: self.image.set_alpha(200)
        
    def idle_animation(self):
        if self.idle_count > 2:
            self.idle_count = 0
        self.idle_current_time = pygame.time.get_ticks()
        if self.is_player_drunken:
            if self.idle_count == 0:
                self.image = pygame.image.load(os.path.join(images_path, "idle_drunken0.png")).convert_alpha()
            elif self.idle_count == 1:
                self.image = pygame.image.load(os.path.join(images_path, "idle_drunken0.png")).convert_alpha()
            elif self.idle_count == 2:
                self.image = pygame.image.load(os.path.join(images_path, "idle_drunken1.png")).convert_alpha()
        else:
            if self.idle_count == 0:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_idle0.png")).convert_alpha()
            elif self.idle_count == 1:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_idle1.png")).convert_alpha()
            elif self.idle_count == 2:
                self.image = pygame.image.load(os.path.join(images_path, "sprite_idle2.png")).convert_alpha()
        if self.last_x_dir == -1: self.image = pygame.transform.flip(self.image, True, False)
        if self.is_damaged: self.image.set_alpha(200)
    
    def throw_animation(self):
        if self.is_player_drunken:
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken0.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken1.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken2.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken3.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken4.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "throw_drunken5.png")).convert_alpha())
        else:
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw0.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw1.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw2.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw3.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw4.png")).convert_alpha())
            self.throw.append(pygame.image.load(os.path.join(images_path, "sprite_throw5.png")).convert_alpha())
        for i in self.throw:
            self.image = i
            if self.last_x_dir == -1:
                self.image = pygame.transform.flip(self.image, True, False)
                
    def walk_delay(self):
        if not self.is_walk:
            self.walk_current_time = pygame.time.get_ticks()
            if self.walk_current_time - self.walk_time > self.step_cooltime:
                self.is_walk = True
    
    def idle_delay(self):
        if not self.is_idle:
            self.idle_current_time = pygame.time.get_ticks()
            if self.idle_current_time - self.idle_time > self.idle_cooltime:
                self.is_idle = True
    
    def idle(self):
        if not self.is_move_x and not self.is_move_y:
            if self.is_idle:
                self.idle_time = pygame.time.get_ticks()
                self.idle_count+=1
                self.is_idle = False
                self.idle_animation()
    
    # 피해 함수 (무적 시간 추가) -> 무적시 투명도 올림
    def get_damaged(self):
        self.is_damaged = True
        self.damaged_start = pygame.time.get_ticks()
        self.image.set_alpha(200)

    # 수평 이동 입력
    def get_horizontal(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.is_move_x = True
            self.dir.x = -1
            self.last_x_dir = -1
            self.last_dir = 1
            self.player_speed_x = 2
            if self.is_player_drunken:
                self.player_speed_x = 1
            if self.is_walk:
                self.walk_time = pygame.time.get_ticks()
                self.walk_count+=1
                self.is_walk = False
                self.walk_animation()
                self.image = pygame.transform.flip(self.image, True, False)
        elif keys[pygame.K_RIGHT]:
            self.is_move_x = True
            self.dir.x = 1
            self.last_x_dir = 1
            self.last_dir = 2
            self.player_speed_x = 2
            if self.is_player_drunken:
                self.player_speed_x = 1
            if self.is_walk:
                self.walk_time = pygame.time.get_ticks()
                self.walk_count+=1
                self.is_walk = False
                self.walk_animation()
        else:
            self.dir.x = 0
            self.is_move_x = False
            self.player_speed_x = 0

        return self.dir.x

    # 수직 이동 입력
    def get_vertical(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.is_move_y = True
            self.dir.y = -1
            self.last_dir = 3
            self.player_speed_y = 2
            if self.is_player_drunken:
                self.player_speed_y = 1
            if self.is_walk:
                self.walk_time = pygame.time.get_ticks()
                self.walk_count+=1
                self.is_walk = False
                self.walk_animation()
                if self.last_x_dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
        elif keys[pygame.K_DOWN]:
            self.is_move_y = True
            self.dir.y = 1
            self.last_dir = 4
            self.player_speed_y = 2
            if self.is_player_drunken:
                self.player_speed_y = 1
            if self.is_walk:
                self.walk_time = pygame.time.get_ticks()
                self.walk_count+=1
                self.is_walk = False
                self.walk_animation()
                if self.last_x_dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
        else:
            self.dir.y = 0
            self.is_move_y = False
            self.player_speed_y = 0
        return self.dir.y

    # 이동 함수
    # 나중에 쉽게 수정할 수 있다면 하는 편이 좋을듯
    def move(self, speed_x, speed_y, dt):
        x = self.get_horizontal()
        y = self.get_vertical()
        # 이동 순서(쯔꾸르 이동)
        if x != 0:
            if len(self.move_order) != 3 and "x" not in self.move_order:
                self.move_order.append("x")
        if y != 0:
            if len(self.move_order) != 3 and "y" not in self.move_order:
                self.move_order.append("y")
        if self.move_order[-1] == "x": self.is_horizon = True
        if self.move_order[-1] == "y": self.is_horizon = False
        if x == 0 or y == 0:
            self.is_horizon = x != 0
        if x == 0 and y == 0: self.move_order = [0]
        # 이동 로직 + 충돌방지
        if self.is_horizon:
            self.hitbox.left += x * speed_x * (dt // 6)
            self.collision("horizontal")
        else:
            self.hitbox.top += y * speed_y * (dt // 6)
            self.collision("vertical")
        self.rect.centerx = self.hitbox.centerx
        self.rect.centery = self.hitbox.centery - 5
        self.rod_put_box.center = self.hitbox.center

    # 무기 입력 확인 함수
    def add_rock(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] and self.is_rock_ready):
            use_sound.set_volume(self.effect_vol/100)
            use_sound.play()
            self.throw_rock()
            self.is_rock_ready = False
            self.rock_time = pygame.time.get_ticks()
            self.throw_animation()

    # 무기 발사 함수
    def throw_rock(self):
        if(self.rock_item_effect and self.rock_count==0):
            effect = True
        else:
            effect = False
        self.rock_count += 1
        if self.is_player_drunken:
            dir = random.randint(1, 4)
        else:
            dir = self.last_dir
        if dir == 2:
            self.images.add(Rock(self.rect.center, 1, self.border_images, effect, self.stage_num, self.effect_vol))
        elif dir == 1:
            self.images.add(Rock(self.rect.center, 2, self.border_images, effect, self.stage_num, self.effect_vol))
        elif dir == 4:
            self.images.add(Rock(self.rect.center, 3, self.border_images, effect, self.stage_num, self.effect_vol))
        elif dir:
            self.images.add(Rock(self.rect.center, 4, self.border_images, effect, self.stage_num, self.effect_vol))

    # 재장전 함수
    def re_load_rock(self):
        if not self.is_rock_ready:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.rock_time > self.rock_cool_time:
                self.is_rock_ready = True

    # 무적 시간 함수 -> 무적 해제 후엔 원래 이미지
    def un_damaged_time(self):
        if self.is_damaged:
            current_time = pygame.time.get_ticks()
            if current_time - self.damaged_start > self.undamaged_time:
                self.is_damaged = False
                self.image.set_alpha(255)
                

    def player_drunken(self):
        self.is_player_drunken = True
        self.drunken_start_time = pygame.time.get_ticks()

    def drunken_cool_time(self):
        if self.is_player_drunken:
            current_time = pygame.time.get_ticks()
            if current_time - self.drunken_start_time > self.drunken_time:
                self.is_player_drunken = False
                self.player_speed_x = 2
                self.player_speed_y = 2

    def remove_item_effect(self, name):
        global rope_item, max_hp, shield, bonus, use_item0, use_item1, use_item2, use_item3, use_item4, use_item5, use_item6, use_item7, use_item8, use_item9, use_item10
        if name == "general_item0":
            rope_item -= 1
            use_item0 = False
        elif name == "general_item1":
            self.player_speed_x-=1
            self.player_speed_y-=1
            use_item1 = False
        elif name == "general_item2":
            max_hp -= 30
            use_item2 = False
        elif name == "general_item3":
            shield = 0
            use_item3 = False
        elif name == "general_item4":
            rope_item += 1
            use_item4 = False
        elif name == "general_item5":
            if bonus >= 100:
                bonus -= 100
            use_item5 = False
        elif name == "general_item6":         # 이거 로직 변경 필요해보임
            use_item6 = False
        elif name == "general_item7":
            self.rock_item_effect = False
            use_item7 = False
        elif name == "general_item8":
            self.is_effect0 = False
            use_item8 = False
        elif name == "general_item9":         # 잘 모르겠음
            self.ignore_item = False
            use_item9 = False
            pass
        elif name == "general_item10":
            self.is_effect1 = False
            use_item10 = False

    def remove_item(self):
        tmp = []
        for idx, item in enumerate(general_inventory):
            if item[0].is_get:
                tmp.append(idx)
        if len(tmp) != 0:
            idx = random.choice(tmp)
            general_inventory[idx][0].is_get = False
            self.remove_item_effect(general_inventory[idx][0].name)
            general_inventory.pop(idx)
            return True
        return False

    def get_item(self):
        while True:
            tmp = random.choice(self.item_name_list)
            flag = False
            for item in general_inventory:
                if item[0].name == tmp and item[1] < 6:
                    item[1] = 6
                    item[0].is_get = True
                    return
                elif item[0].name == tmp and item[1] == 6:
                    flag = True
            if not flag:
                if tmp == "general_item0":
                    a = GeneralItem0((0,0),[self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item1":
                    a = GeneralItem1((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item2":
                    a = GeneralItem2((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item3":
                    a = GeneralItem3((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item4":
                    a = GeneralItem4((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item5":
                    a = GeneralItem5((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item6":
                    a = GeneralItem6((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item7":
                    a = GeneralItem7((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item8":
                    a = GeneralItem8((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item9":
                    a = GeneralItem9((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                elif tmp == "general_item10":
                    a = GeneralItem10((0, 0), [self.images, self.item_images])
                    a.is_get = True
                    general_inventory.append([a, 6])
                    a.kill()
                return

    def event_item_effects(self, event_char):    # 이벤트 유물 효과 필요 -> hp관련 수정 필요
        global current_hp, max_hp
        if event_char == "A":
            flag = self.remove_item()
            if flag:
                if current_hp + 50 > max_hp:
                    current_hp = max_hp
                else:
                    current_hp += 50
        elif event_char == "B":
            flag = self.remove_item()
            if flag:
                self.get_item()
        elif event_char == "C":
            if current_hp - 30 <= 0:
                pass
            else:
                current_hp -= 30
                self.get_item()
        elif event_char == "D":
            tmp = []
            for idx, item in enumerate(general_inventory):
                if item.is_get:
                    tmp.append(idx)
            if len(tmp) >= 2:
                self.remove_item()
                self.remove_item()
                current_hp = max_hp
        elif event_char == "E":
            self.remove_item()
        elif event_char == "F":
            max_hp -= 20
            current_hp = max_hp
        elif event_char == "G":
            max_hp += 20
            if current_hp - 20 > 0:
                current_hp -= 20
            else:
                current_hp = 1
        elif event_char == "H":
            self.get_item()
        elif event_char == "I":
            pass

    # 충돌 함수
    def collision(self, direction):
        self.is_road = True
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.name != "Finish" and \
                   sprite.name != "Stage0" and \
                   sprite.name != "Stage1" and \
                   sprite.name != "Stage2" and \
                   sprite.name != "Stage3" and \
                   sprite.name != "Stage4" and \
                   sprite.name != "Stage5" and \
                   sprite.name != "Pillar_0" and \
                   sprite.name != "Pillar_1":
                    if sprite.rect.colliderect(self.hitbox):
                        self.is_road = False
                        if not self.is_road and self.is_first0:
                            self.start0 = pygame.time.get_ticks()
                        if sprite.name == "alcoholRoad":
                            self.player_drunken()
                        elif not self.is_dark and not self.is_thunder and not self.is_tile_mix or sprite.name == "Wall" or sprite.name == "obstacle":
                            if self.dir.x > 0:
                                self.hitbox.right = sprite.rect.left
                            elif self.dir.x < 0:
                                self.hitbox.left = sprite.rect.right
                        elif self.is_tile_mix and not self.is_damaged:
                            current_time0 = pygame.time.get_ticks()
                            if current_time0 - self.start0 < 5000 and self.is_effect0:
                                damage_sound.set_volume(self.effect_vol/100)
                                damage_sound.play()
                                self.get_damaged()
                                self.is_first0 = False
                            else :
                                damage_sound.set_volume(self.effect_vol/100)
                                damage_sound.play()
                                self.get_damaged()
                                self.is_damage10 = True
                                self.is_first0 = True
                        elif self.is_thunder and not self.is_damaged:
                            damage_sound.set_volume(self.effect_vol/100)
                            damage_sound.play()
                            self.get_damaged()
                            self.is_damage10 = True
                        elif self.is_dark and not self.is_damaged:
                            damage_sound.set_volume(self.effect_vol/100)
                            damage_sound.play()
                            self.get_damaged()
                            self.is_damage10 = True
                if sprite.name == "Pillar_0" or sprite.name == "Pillar_1":
                    if sprite.rect.colliderect(self.hitbox):
                        self.is_player_cerberus = False
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.name != "Finish" and \
                   sprite.name != "Stage0" and \
                   sprite.name != "Stage1" and \
                   sprite.name != "Stage2" and \
                   sprite.name != "Stage3" and \
                   sprite.name != "Stage4" and \
                   sprite.name != "Stage5" and \
                   sprite.name != "Pillar_0" and \
                   sprite.name != "Pillar_1":
                    if sprite.rect.colliderect(self.hitbox):
                        self.is_road = False
                        if not self.is_road and self.is_first0:
                            self.start1 = pygame.time.get_ticks()
                        if sprite.name == "alcoholRoad":
                            self.player_drunken()
                        elif not self.is_dark and not self.is_thunder and not self.is_tile_mix or sprite.name == "Wall" or sprite.name == "obstacle":
                            if self.dir.y > 0:
                                self.hitbox.bottom = sprite.rect.top
                            elif self.dir.y < 0:
                                self.hitbox.top = sprite.rect.bottom
                        elif self.is_tile_mix and not self.is_damaged:
                            current_time1 = pygame.time.get_ticks()
                            if current_time1 - self.start1 < 5000 and self.is_effect0:
                                damage_sound.set_volume(self.effect_vol/100)
                                damage_sound.play()
                                self.get_damaged()
                                self.is_first0 = False
                            else :
                                damage_sound.set_volume(self.effect_vol/100)
                                damage_sound.play()
                                self.get_damaged()
                                self.is_damage10 = True
                                self.is_first0 = True
                        elif self.is_thunder and not self.is_damaged:
                            damage_sound.set_volume(self.effect_vol/100)
                            damage_sound.play()
                            self.get_damaged()
                            self.is_damage10 = True
                        elif self.is_dark and not self.is_damaged:
                            damage_sound.set_volume(self.effect_vol/100)
                            damage_sound.play()
                            self.get_damaged()
                            self.is_damage10 = True
                if sprite.name == "Pillar_0" or sprite.name == "Pillar_1":
                    if sprite.rect.colliderect(self.hitbox):
                        self.is_player_cerberus = False
        if self.is_road:
            self.is_tile_mix = False
            self.is_thunder = False

    # 데미지를 주는 충돌을 따로 만듦
    def damage_collision(self):
        for sprite in self.damage_images:
            if sprite.hitbox.colliderect(self.hitbox):
                if sprite.name == "laser_Monster" and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage2 = True
                if sprite.name == "monster_laser" and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage2 = True
                    sprite.kill()
                if sprite.name == "rush_Monster" and not self.is_damaged:           # 데미지 2~3
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage2 = True
                if sprite.name == "thunder" and sprite.animation_idx == 9 and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.is_thunder = True
                    self.get_damaged()
                    self.is_damage10 = True
                if sprite.name == "Fish" and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage5 = True
                    sprite.image = pygame.image.load(os.path.join(images_path, "monster_fish_animation_atk.png")).convert_alpha()
                if sprite.name == "satiros" and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage5 = True
                if sprite.name == "cerberus" and self.is_player_cerberus and not self.is_damaged:
                    damage_sound.set_volume(self.effect_vol/100)
                    damage_sound.play()
                    self.get_damaged()
                    self.is_damage30 = True



    def get_item_interaction(self):
        for item in self.item_images:
            if self.get_event_item and item.name in ["event_item1", "event_item2", "event_item3"]:
                item.kill()
            if item.name in ["event_item1",
                             "event_item2",
                             "event_item3",
                             "general_item",
                             "general_item0",
                             "general_item1",
                             "general_item2",
                             "general_item3",
                             "general_item4",
                             "general_item5",
                             "general_item6",
                             "general_item7",
                             "general_item8",
                             "general_item9",
                             "general_item10",
                             "hadesHelmet"]:
                item_vec = pygame.math.Vector2(item.rect.center)
                player_vec = pygame.math.Vector2(self.rect.center)
                distance = (player_vec - item_vec).magnitude()
                if distance <= item.boundary:
                    self.item_interaction = True
                    item.is_interaction = True
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_TAB]:
                        item.item_gage += 1
                        self.current_item_gage = item.item_gage
                        if item.item_gage == 100:
                            self.item_interaction = False
                            item.is_interaction = False
                            self.current_item_gage = 0
                            item_interaction_sound.set_volume(self.effect_vol/100)
                            item_interaction_sound.play()
                            if item.name in ["event_item1", "event_item2", "event_item3"]:
                                self.event_item_effects(item.event)
                                self.get_event_item = True
                            elif item.name == "hadesHelmet":
                                self.is_hadesHelmet = True
                                self.is_player_cerberus = False
                            else:
                                self.is_full = False
                                if item.name == "general_item":
                                    while 1:
                                        item.name = random.choice(["general_item0","general_item1","general_item2","general_item3","general_item4",\
                                            "general_item5", "general_item6", "general_item7", "general_item8", "general_item9", "general_item10"])
                                        for i in general_inventory:
                                            if (i[0].name == item.name):
                                                if i[1] == 6: self.is_full = True; break
                                                else: self.is_full = False;
                                        if not self.is_full: break
                                is_fill = True
                                for tmp in general_inventory:
                                    if tmp[0].name == item.name:
                                        if tmp[1] < 6:
                                            tmp[1] += 1
                                            if tmp[1] == 6:
                                                tmp[0].is_get = True
                                        is_fill = False
                                if is_fill:
                                    general_inventory.append([item, 1])
                                
                            item.kill()
                    elif not keys[pygame.K_TAB]:
                        item.item_gage = 0
                        self.current_item_gage = item.item_gage
                elif distance > item.boundary:
                    if item.is_interaction:
                        self.current_item_gage = 0
                        item.item_gage = 0
                        self.item_interaction = False
                        item.is_interaction = False

    def rod_put(self):
        for sprite in self.images:
            if sprite.name == "Road" or sprite.name == "Conductor0" or sprite.name == "Conductor1" or sprite.name in ["ElectricRoad00","ElectricRoad01","ElectricRoad02","ElectricRoad03","ElectricRoad04","ElectricRoad05","ElectricRoad06","ElectricRoad07","ElectricRoad08","ElectricRoad09","ElectricRoad10"]:
                if sprite.rect.colliderect(self.rod_put_box) and not self.item_interaction:
                    if self.is_rod_ready:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_q]:
                            if self.stage_num == 5 and self.rod_num != 5 and not(self.map_num == 3 or self.map_num == 7):
                                ThunderRod((sprite.rect.left, sprite.rect.top), [self.images])
                                self.rod_start_time = pygame.time.get_ticks()
                                self.is_rod_ready = False
                                if self.rod_num < 5:
                                    self.rod_num += 1
                                self.rod_position.append((sprite.rect.left, sprite.rect.top - 96))

    def rod_cool_time(self):
        if not self.is_rod_ready:
            self.rod_current_time = pygame.time.get_ticks()
            if self.rod_current_time - self.rod_start_time > self.rod_put_cool_time:
                self.is_rod_ready = True


    def get_door_interaction(self):
        for door in self.door_images:
            item_vec = pygame.math.Vector2(door.rect.center)
            player_vec = pygame.math.Vector2(self.rect.center)
            distance = (player_vec - item_vec).magnitude()
            if door.name == "Stage0":
                if distance <= 50: self.stage0_interaction = True
                else: self.stage0_interaction = False
            elif door.name == "Stage1":
                if distance <= 50: self.stage1_interaction = True
                else: self.stage1_interaction = False
            elif door.name == "Stage2":
                if distance <= 50: self.stage2_interaction = True
                else: self.stage2_interaction = False
            elif door.name == "Stage3":
                if distance <= 50: self.stage3_interaction = True
                else: self.stage3_interaction = False
            elif door.name == "Stage4":
                if distance <= 50: self.stage4_interaction = True
                else: self.stage4_interaction = False
            elif door.name == "Stage5":
                if distance <= 50: self.stage5_interaction = True
                else: self.stage5_interaction = False

    def eventTrigger(self):
        global random_event_item_text, event_texts
        for event in self.images:
            if event.rect.colliderect(self.hitbox) and not self.event_handler:
                if event.name == "eventRoad":
                    if event.event_code == "000":
                        self.event_code = "000"
                    self.event_handler = True


    # 업데이트 영역 -> 무적 시간 함수 추가
    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_pause:
            self.get_item_interaction()
            self.get_door_interaction()
            self.un_damaged_time()
            self.drunken_cool_time()
            self.eventTrigger()
            self.rod_put()
            self.rod_cool_time()
            if not self.is_dead:
                self.add_rock()
                self.re_load_rock()
                self.damage_collision()
                self.move(self.player_speed_x, self.player_speed_y, dt)
            self.walk_delay()
            self.idle()
            self.idle_delay()