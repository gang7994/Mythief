import pygame, os
import random
from Settings import *
from MonsterLaser import MonsterLaser


class LaserMonster(pygame.sprite.Sprite):
    # 몬스터 이미지 임시로 변경
    def __init__(self, pos, groups, border_images, damage_images, images):
        super().__init__(groups)
        # 이미지 + 히트박스 영역
        self.image = pygame.image.load(os.path.join(images_path, "monster.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)
        # 몬스터 이름
        self.name = "laser_Monster"
        # 몬스터 움직임 변수
        self.dir = pygame.math.Vector2()
        self.monster_speed = 1
        self.is_moving = False
        self.monster_order_wait_time = 1000
        self.monster_move = [[1,0], [0,1], [0,0], [-1,0], [0,-1]]
        # 몬스터 충돌 정보
        self.border_images = border_images
        self.damage_images = damage_images
        self.images = images
        # 레이져 몬스터 공격 변수
        self.laser_cool_time = random.randint(1, 5) * 1000
        self.is_laser_ready = True
        self.current_time = 0
        self.laser_time = 0
        # FPS + 일시정지 변수
        self.clock = pygame.time.Clock()
        self.is_pause = False
        
    # 적 움직임 랜덤으로 얻기
    def move_order(self):
        if not self.is_moving:
            self.is_moving = True
            move_idx = random.randint(0, 4)
            self.dir.x = self.monster_move[move_idx][0]
            self.dir.y = self.monster_move[move_idx][1]
            self.monster_move_start = pygame.time.get_ticks()
    
    # 첫 이동 입력 이후 1초간 그 움직임 사용
    def move_wait(self):
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            if current_time - self.monster_move_start > self.monster_order_wait_time:
                self.is_moving = False

    # 입력받은 움직임으로 이동 + 충돌 적용
    def move(self, speed, dt):
        if self.is_moving:
            self.hitbox.left += self.dir.x * speed * (dt // 6)
            self.collision("horizontal")
            self.hitbox.top += self.dir.y * speed * (dt // 6)
            self.collision("vertical")
            self.rect.center = self.hitbox.center
        
    # 몬스터 충돌
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.x > 0:
                            self.hitbox.right = sprite.rect.left
                        elif self.dir.x < 0:
                            self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        elif self.dir.y < 0:
                            self.hitbox.top = sprite.rect.bottom

    # 몬스터 레이져 추가 함수 -> 레이져 발사 쿨타임을 랜덤으로 정하기
    def add_laser(self):
        if self.is_laser_ready:
            self.laser_cool_time = random.randint(1, 5) * 1000
            self.throw_laser()
            self.is_laser_ready = False
            self.laser_time = pygame.time.get_ticks()

    # 몬스터 레이져 발사 함수
    def throw_laser(self):
        if self.dir.x == 1:
            self.images.add(MonsterLaser(self.rect.center, 1, [self.damage_images], self.border_images))
        elif self.dir.x == -1:
            self.images.add(MonsterLaser(self.rect.center, 2, [self.damage_images], self.border_images))
        elif self.dir.y == 1:
            self.images.add(MonsterLaser(self.rect.center, 3, [self.damage_images], self.border_images))
        elif self.dir.y == -1:
            self.images.add(MonsterLaser(self.rect.center, 4, [self.damage_images], self.border_images))

    # 재장전 함수
    def re_load_laser(self):
        if not self.is_laser_ready:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.laser_time > self.laser_cool_time:
                self.is_laser_ready = True

    # 몬스터 로직 업데이트
    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_pause:
            self.move_order()
            if self.monster_speed <= 0: self.monster_speed = 1
            self.move(self.monster_speed, dt)
            self.move_wait()
            self.add_laser()
            self.re_load_laser()

class RushMonster(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "monster.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, 0)
        self.name = "rush_Monster"
        self.dir = pygame.math.Vector2()
        self.border_images = border_images
        self.monster_speed = 1
        self.is_moving = False
        self.monster_order_wait_time = 1000
        self.monster_move = [[1, 0], [0, 1], [0, 0], [-1, 0], [0, -1]]
        self.boundary = 150
        self.is_rush = False
        self.clock = pygame.time.Clock()
        self.is_pause = False

    # 적 움직임 랜덤으로 얻기
    def move_order(self):
        if not self.is_moving:
            self.is_moving = True
            move_idx = random.randint(0, 4)
            self.dir.x = self.monster_move[move_idx][0]
            self.dir.y = self.monster_move[move_idx][1]
            self.monster_move_start = pygame.time.get_ticks()

    # 첫 이동 입력 이후 1초간 그 움직임 사용
    def move_wait(self):
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            if current_time - self.monster_move_start > self.monster_order_wait_time:
                self.is_moving = False

    # 입력받은 움직임으로 이동
    def move(self, speed, dt):
        if self.is_moving:
            self.hitbox.left += self.dir.x * speed * (dt // 6)
            self.collision("horizontal")
            self.hitbox.top += self.dir.y * speed * (dt // 6)
            self.collision("vertical")
            self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.x > 0:
                            self.hitbox.right = sprite.rect.left
                        elif self.dir.x < 0:
                            self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        elif self.dir.y < 0:
                            self.hitbox.top = sprite.rect.bottom


    def rush(self, direction, dt):
        self.is_rush = True
        self.hitbox.left += direction[0] * self.monster_speed * (dt // 6)
        self.dir.x = direction[0]
        if self.dir.x != 0:
            self.last_x_dir = self.dir.x
        self.collision("horizontal")
        if not direction[0]:
            self.hitbox.top += direction[1] * self.monster_speed * (dt // 6)
            self.dir.y = direction[1]
            self.collision("vertical")
        self.rect.center = self.hitbox.center


    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_rush and not self.is_pause:
            self.move_order()
            if self.monster_speed <= 0: self.monster_speed = 1
            self.move(self.monster_speed, dt)
            self.move_wait()

class FishMonster(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images):
        super().__init__(groups)
        self.animation_array = ["monster_fish_animation_walk0.png",
                                "monster_fish_animation_walk1.png",
                                "monster_fish_animation_walk2.png",
                                "monster_fish_animation_walk3.png",
                                "monster_fish_animation_walk4.png",
                                "monster_fish_animation_walk5.png"]
        self.image = pygame.image.load(os.path.join(images_path, "monster_fish_animation_idle.png")).convert_alpha()
        self.image_origin = pygame.image.load(os.path.join(images_path, "monster_fish_animation_idle.png")).convert_alpha()
        self.image_flip = pygame.transform.flip(self.image_origin, True, False)
        self.animation_frame = 100
        self.animation_idx = 0
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_current_time = pygame.time.get_ticks()
        self.is_walk = False

        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10) # 16, 32 픽셀
        self.hitbox.y += 5
        self.name = "Fish"
        self.dir = pygame.math.Vector2()
        self.border_images = border_images
        self.monster_speed = 1
        self.is_moving = False
        self.monster_order_wait_time = 1000
        self.monster_move = [[1, 0], [0, 1], [0, 0], [-1, 0], [0, -1]]
        self.last_x_dir = -1
        self.boundary = 175
        self.is_rush = False
        self.clock = pygame.time.Clock()
        self.is_pause = False

        # 적 움직임 랜덤으로 얻기

    def idle(self):
        if self.last_x_dir == 1:
            self.image = self.image_origin
        elif self.last_x_dir == -1:
            self.image = self.image_flip

    def walk(self):
        if self.is_walk:
            self.animation_current_time = pygame.time.get_ticks()
            if self.animation_current_time - self.animation_start_time > self.animation_frame:
                self.image = pygame.image.load(
                    os.path.join(images_path, self.animation_array[self.animation_idx])).convert_alpha()
                self.animation_idx += 1
                self.animation_idx %= 6
                if self.last_x_dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                self.animation_start_time = self.animation_current_time

    def animation(self):
        if not (self.dir.x == 0 and self.dir.y == 0):
            self.is_walk = True
            self.walk()
        elif self.dir.x == 0 and self.dir.y == 0:
            self.is_walk = False
            self.idle()

    def move_order(self):
        if not self.is_moving:
            self.is_moving = True
            move_idx = random.randint(0, 4)
            self.dir.x = self.monster_move[move_idx][0]
            self.dir.y = self.monster_move[move_idx][1]
            if self.dir.x != 0:
                self.last_x_dir = self.dir.x
            self.monster_move_start = pygame.time.get_ticks()

        # 첫 이동 입력 이후 1초간 그 움직임 사용

    def move_wait(self):
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            if current_time - self.monster_move_start > self.monster_order_wait_time:
                self.is_moving = False

        # 입력받은 움직임으로 이동

    def move(self, speed, dt):
        if self.is_moving:
            self.hitbox.left += self.dir.x * speed * (dt // 6)
            self.collision("horizontal")
            self.hitbox.top += self.dir.y * speed * (dt // 6)
            self.collision("vertical")
            self.rect.centerx = self.hitbox.centerx
            self.rect.centery = self.hitbox.centery - 5

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.x > 0:
                            self.hitbox.right = sprite.rect.left
                        elif self.dir.x < 0:
                            self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        elif self.dir.y < 0:
                            self.hitbox.top = sprite.rect.bottom

    def rush(self, direction, dt):
        self.is_rush = True
        self.hitbox.left += direction[0] * self.monster_speed * (dt // 6)
        self.dir.x = direction[0]
        if self.dir.x != 0:
            self.last_x_dir = self.dir.x
        self.collision("horizontal")
        if not direction[0]:
            self.hitbox.top += direction[1] * self.monster_speed * (dt // 6)
            self.dir.y = direction[1]
            self.collision("vertical")
        self.rect.centerx = self.hitbox.centerx
        self.rect.centery = self.hitbox.centery - 5

    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_rush and not self.is_pause:
            self.move_order()
            self.move(self.monster_speed, dt)
            self.move_wait()

        self.animation()

class Satiros(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, max_distance):
        super().__init__(groups)
        self.animation_array = ["sa_running_0.png",
                                "sa_running_1.png",
                                "sa_running_2.png",
                                "sa_running_3.png",
                                "sa_running_4.png",
                                "sa_running_5.png"]
        self.image = pygame.image.load(os.path.join(images_path, "sa_idle_0.png")).convert_alpha()
        self.image_origin = pygame.image.load(os.path.join(images_path, "sa_idle_0.png")).convert_alpha()
        self.image_flip = pygame.transform.flip(self.image_origin, True, False)
        self.animation_frame = 100
        self.animation_idx = 0
        self.animation_start_time = pygame.time.get_ticks()
        self.animation_current_time = pygame.time.get_ticks()
        self.is_walk = False
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10) # 16, 32 픽셀
        self.hitbox.y += 5
        self.pos = pos
        self.name = "satiros"
        self.dir = pygame.math.Vector2()
        self.dir.y = 1
        self.border_images = border_images
        self.monster_speed = 1
        self.max_distance = max_distance
        self.is_moving = False
        self.last_x_dir = -1
        self.clock = pygame.time.Clock()
        self.is_pause = False

        # 적 움직임 랜덤으로 얻기

    def idle(self):
        if self.last_x_dir == 1:
            self.image = self.image_origin
        elif self.last_x_dir == -1:
            self.image = self.image_flip

    def walk(self):
        if self.is_walk:
            self.animation_current_time = pygame.time.get_ticks()
            if self.animation_current_time - self.animation_start_time > self.animation_frame:
                self.image = pygame.image.load(
                    os.path.join(images_path, self.animation_array[self.animation_idx])).convert_alpha()
                self.animation_idx += 1
                self.animation_idx %= 6
                if self.last_x_dir == -1:
                    self.image = pygame.transform.flip(self.image, True, False)
                self.animation_start_time = self.animation_current_time

    def animation(self):
        if not (self.dir.x == 0 and self.dir.y == 0):
            self.is_walk = True
            self.walk()
        elif self.dir.x == 0 and self.dir.y == 0:
            self.is_walk = False
            self.idle()

        # 입력받은 움직임으로 이동

    def move(self, speed, dt):
        self.hitbox.left += self.dir.x * speed * (dt // 6)
        self.collision("horizontal")
        self.hitbox.top += self.dir.y * speed * (dt // 6)
        self.collision("vertical")
        self.rect.centerx = self.hitbox.centerx
        self.rect.centery = self.hitbox.centery - 5

    def dir_change(self):
        if self.dir.y == 1:
            if abs(self.rect.y - self.pos[1]) >= self.max_distance:
                self.dir.y *= -1
        else:
            if self.rect.y <= self.pos[1]:
                self.dir.y *= -1



    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.x > 0:
                            self.hitbox.right = sprite.rect.left
                        elif self.dir.x < 0:
                            self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        elif self.dir.y < 0:
                            self.hitbox.top = sprite.rect.bottom

    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_pause:
            self.dir_change()
            self.move(self.monster_speed, dt)
            self.animation()

class Cerberus(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, images, move_flag):
        super().__init__(groups)
        # animation, image
        self.idle_animation_array = ["CR_idleAnim_0.png", "CR_idleAnim_1.png"]
        self.atk_animation_array = ["CR_atkAnim_0.png", "CR_atkAnim_1.png", "CR_atkAnim_2.png", "CR_atkAnim_3.png"]
        self.image = pygame.image.load(os.path.join(images_path, "cerberus.png")).convert_alpha()
        self.image_origin = pygame.image.load(os.path.join(images_path, "cerberus.png")).convert_alpha()
        self.image_flip = pygame.transform.flip(self.image_origin, True, False)
        self.animation_frame = 100
        self.idle_animation_idx = 0
        self.idle_animation_start_time = pygame.time.get_ticks()
        self.idle_animation_current_time = pygame.time.get_ticks()
        self.is_attack = False
        self.atk_animation_idx = 0
        self.atk_animation_start_time = pygame.time.get_ticks()
        self.atk_animation_current_time = pygame.time.get_ticks()
        # hitbox
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-30, -72)
        self.hitbox.y += 36
        # name
        self.name = "cerberus"
        # move var
        self.dir = pygame.math.Vector2()
        self.monster_speed = 1
        self.is_moving = False
        self.move_flag = move_flag
        self.monster_order_wait_time = 1000
        self.monster_move = [[1, 0], [0, 1], [0, 0], [-1, 0], [0, -1]]
        self.last_x_dir = -1
        self.boundary = 2000
        self.is_rush = False
        # collision var
        self.border_images = border_images
        self.images = images
        # clock
        self.clock = pygame.time.Clock()
        self.is_pause = False

        # 적 움직임 랜덤으로 얻기

    def idle(self):
        self.idle_animation_current_time = pygame.time.get_ticks()
        if self.idle_animation_current_time - self.idle_animation_start_time > self.animation_frame:
            self.image = pygame.image.load(
                os.path.join(images_path, self.idle_animation_array[self.idle_animation_idx])).convert_alpha()
            self.idle_animation_idx += 1
            self.idle_animation_idx %= 2
            if self.last_x_dir == 1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.idle_animation_start_time = self.idle_animation_current_time

    def Atk(self):
        self.atk_animation_current_time = pygame.time.get_ticks()
        if self.atk_animation_current_time - self.atk_animation_start_time > self.animation_frame:
            self.image = pygame.image.load(
                os.path.join(images_path, self.atk_animation_array[self.atk_animation_idx])).convert_alpha()
            self.atk_animation_idx += 1
            self.atk_animation_idx %= 4
            if self.last_x_dir == 1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.atk_animation_start_time = self.atk_animation_current_time

    def animation(self):
        if not (self.dir.x == 0 and self.dir.y == 0) and not self.is_attack:
            self.idle()
        if self.is_attack:
            self.Atk()

    def move_order(self):
        if not self.is_moving:
            self.is_moving = True
            move_idx = random.randint(0, 4)
            self.dir.x = self.monster_move[move_idx][0]
            if self.dir.x != 0:
                self.last_x_dir = self.dir.x
            self.dir.y = self.monster_move[move_idx][1]
            self.monster_move_start = pygame.time.get_ticks()

        # 첫 이동 입력 이후 1초간 그 움직임 사용

    def move_wait(self):
        if self.is_moving:
            current_time = pygame.time.get_ticks()
            if current_time - self.monster_move_start > self.monster_order_wait_time:
                self.is_moving = False

        # 입력받은 움직임으로 이동

    def move(self, speed, dt):
        if self.is_moving:
            self.hitbox.left += self.dir.x * speed * (dt // 5)
            self.collision("horizontal")
            self.hitbox.top += self.dir.y * speed * (dt // 5)
            self.collision("vertical")
            self.rect.centerx = self.hitbox.centerx
            self.rect.centery = self.hitbox.centery - 36

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.x > 0:
                            self.hitbox.right = sprite.rect.left
                        elif self.dir.x < 0:
                            self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if sprite.name != "NoneRoad" and \
                       sprite.name != "alcoholRoad" and \
                       sprite.name != "Pillar_0" and \
                       sprite.name != "Pillar_1":
                        if self.dir.y > 0:
                            self.hitbox.bottom = sprite.rect.top
                        elif self.dir.y < 0:
                            self.hitbox.top = sprite.rect.bottom

    def player_collision(self):
        for sprite in self.images:
            if sprite.name == "Player":
                if sprite.hitbox.colliderect(self.hitbox):
                    self.is_attack = True
                else:
                    self.is_attack = False

    def rush(self, direction, dt):
        if self.move_flag:
            self.is_rush = True
            self.hitbox.left += direction[0] * self.monster_speed * (dt // 5)
            self.dir.x = direction[0]
            if self.dir.x != 0:
                self.last_x_dir = self.dir.x
            self.collision("horizontal")
            if direction[0] == 0:
                self.hitbox.top += direction[1] * self.monster_speed * (dt // 5)
                self.dir.y = direction[1]
                self.collision("vertical")
            self.rect.centerx = self.hitbox.centerx
            self.rect.centery = self.hitbox.centery - 36
        else:
            self.dir.x = direction[0]
            self.dir.y = direction[1]
            if self.dir.x != 0:
                self.last_x_dir = self.dir.x

    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_rush and not self.is_pause:
            if self.move_flag:
                self.move_order()
                self.move(self.monster_speed, dt)
        self.animation()
        self.player_collision()



        
        
