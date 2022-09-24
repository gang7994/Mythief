import random

import pygame, os
from Settings import *
from Rock import Rock
from TextGroup import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, damage_images, item_images, door_images, images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "sprite_0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.name = "Player"
        self.character_width = self.rect.size[0]
        self.character_height = self.rect.size[1]
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
        self.rock_cool_time = 2000
        self.is_rock_ready = True
        self.rock_count = 0
        self.current_time = 0
        self.rock_time = 0
        # damage var
        self.undamaged_time = 1000    # 무적시간 1초
        self.is_damaged = False      # 데미지 상태인지
        self.is_damage5 = False
        self.is_damage10 = False
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

    # 회복 함수
    def get_hp(self, heal):
        if self.current_hp < self.max_hp:
            self.current_hp += heal
        if self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp


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
        self.rect.center = self.hitbox.center

    # 무기 입력 확인 함수
    def add_rock(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] and self.is_rock_ready):
            self.throw_rock()
            self.is_rock_ready = False
            self.rock_time = pygame.time.get_ticks()
            self.throw_animation()

    # 무기 발사 함수
    def throw_rock(self):
        self.rock_count += 1
        if self.is_player_drunken:
            dir = random.randint(1, 4)
        else:
            dir = self.last_dir

        if dir == 2:
            self.images.add(Rock((self.rect.x, self.rect.y + 7.5), 1, self.border_images))
        elif dir == 1:
            self.images.add(Rock((self.rect.x, self.rect.y + 7.5), 2, self.border_images))
        elif dir == 4:
            self.images.add(Rock(self.rect.center, 3, self.border_images))
        elif dir:
            self.images.add(Rock(self.rect.center, 4, self.border_images))

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
                        if sprite.name == "alcoholRoad":
                            self.player_drunken()
                        elif not self.is_tile_mix or sprite.name == "Wall" or sprite.name == "obstacle":
                            if self.dir.x > 0:
                                self.hitbox.right = sprite.rect.left
                            elif self.dir.x < 0:
                                self.hitbox.left = sprite.rect.right
                        elif self.is_tile_mix and not self.is_damaged:
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
                        if sprite.name == "alcoholRoad":
                            self.player_drunken()
                        elif not self.is_tile_mix or sprite.name == "Wall" or sprite.name == "obstacle":
                            if self.dir.y > 0:
                                self.hitbox.bottom = sprite.rect.top
                            elif self.dir.y < 0:
                                self.hitbox.top = sprite.rect.bottom
                        elif self.is_tile_mix and not self.is_damaged:
                            self.get_damaged()
                            self.is_damage10 = True
                if sprite.name == "Pillar_0" or sprite.name == "Pillar_1":
                    if sprite.rect.colliderect(self.hitbox):
                        self.is_player_cerberus = False
        if self.is_road:
            self.is_tile_mix = False

    # 데미지를 주는 충돌을 따로 만듦
    def damage_collision(self):
        for sprite in self.damage_images:
            if sprite.rect.colliderect(self.hitbox):
                if sprite.name == "laser_Monster" and not self.is_damaged:
                    self.get_damaged()
                    self.is_damage10 = True
                if sprite.name == "monster_laser" and not self.is_damaged:
                    self.get_damaged()
                    self.is_damage5 = True
                    sprite.kill()
                if sprite.name == "rush_Monster" and not self.is_damaged:
                    self.get_damaged()
                    self.is_damage10 = True

    def get_item_interaction(self):
        for item in self.item_images:
            if item.name in ["event_item1",
                             "event_item2",
                             "event_item3",
                             "test_general_item0",
                             "test_general_item1",
                             "test_general_item2",
                             "test_general_item3",
                             "test_general_item4",
                             "test_general_item5"]:
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
                            item.is_get = True
                            self.item_interaction = False
                            item.is_interaction = False
                            self.current_item_gage = 0
                            if item.name in ["event_item1", "event_item2", "event_item3"]:
                                theme_inventory.append(item)
                            else:
                                is_fill = True
                                for tmp in general_inventory:
                                    if tmp[0].name == item.name:
                                        if tmp[1] < 6: tmp[1] += 1
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
            if not self.is_dead:
                self.add_rock()
                self.re_load_rock()
                self.damage_collision()
                self.move(self.player_speed_x, self.player_speed_y, dt)
            self.walk_delay()
            self.idle()
            self.idle_delay()
        