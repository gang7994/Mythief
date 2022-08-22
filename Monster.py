import pygame, os
import random
from Settings import *
from MonsterLaser import MonsterLaser


class LaserMonster(pygame.sprite.Sprite):
    # 몬스터 이미지 임시로 변경
    def __init__(self, pos, groups, border_images, damage_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "monster.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "laser_Monster"
        self.dir = pygame.math.Vector2()
        self.border_images = border_images
        self.damage_images = damage_images
        self.monster_speed = 1
        self.is_moving = False
        self.monster_order_wait_time = 1000
        self.monster_move = [[1,0], [0,1], [0,0], [-1,0], [0,-1]]
        self.lasers = pygame.sprite.Group()
        self.laser_cool_time = random.randint(1, 5) * 1000
        self.is_laser_ready = True
        self.current_time = 0
        self.laser_time = 0
        
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
    def move(self, speed):
        if self.is_moving:
            self.rect.left += self.dir.x * speed
            self.collision("horizontal")
            self.rect.top += self.dir.y * speed
            self.collision("vertical")
        
    # 몬스터 충돌 (여기에 플레이어 충돌을 만들까 고민중)
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.rect):
                    if self.dir.x > 0:
                        self.rect.right = sprite.rect.left
                    elif self.dir.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.rect):
                    if self.dir.y > 0:
                        self.rect.bottom = sprite.rect.top
                    elif self.dir.y < 0:
                        self.rect.top = sprite.rect.bottom

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
            self.lasers.add(MonsterLaser(self.rect.center, 1, [self.damage_images], self.border_images))
        elif self.dir.x == -1:
            self.lasers.add(MonsterLaser(self.rect.center, 2, [self.damage_images], self.border_images))
        elif self.dir.y == 1:
            self.lasers.add(MonsterLaser(self.rect.center, 3, [self.damage_images], self.border_images))
        elif self.dir.y == -1:
            self.lasers.add(MonsterLaser(self.rect.center, 4, [self.damage_images], self.border_images))

    # 재장전 함수
    def re_load_laser(self):
        if not self.is_laser_ready:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.laser_time > self.laser_cool_time:
                self.is_laser_ready = True

    # 몬스터 로직 업데이트
    def update(self):
        self.move_order()
        self.move(self.monster_speed)
        self.move_wait()
        self.add_laser()
        self.re_load_laser()
        self.lasers.update()

class RushMonster(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, damage_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "monster.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.name = "rush_Monster"
        self.dir = pygame.math.Vector2()
        self.border_images = border_images
        self.damage_images = damage_images
        self.monster_speed = 1
        self.is_moving = False
        self.monster_order_wait_time = 1000
        self.monster_move = [[1, 0], [0, 1], [0, 0], [-1, 0], [0, -1]]
        self.boundary = 150
        self.is_rush = False

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
    def move(self, speed):
        if self.is_moving:
            self.rect.left += self.dir.x * speed
            self.collision("horizontal")
            self.rect.top += self.dir.y * speed
            self.collision("vertical")

    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.rect):
                    if self.dir.x > 0:
                        self.rect.right = sprite.rect.left
                    elif self.dir.x < 0:
                        self.rect.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.rect):
                    if self.dir.y > 0:
                        self.rect.bottom = sprite.rect.top
                    elif self.dir.y < 0:
                        self.rect.top = sprite.rect.bottom

    # 돌진 함수 - 버그 있음
    def rush(self, direction):
        self.is_rush = True
        self.rect.left += direction[0] * self.monster_speed
        self.dir.x = direction[0]
        if not direction[0]:
            self.rect.top += direction[1] * self.monster_speed
            self.dir.y = direction[1]


    def update(self):
        if not self.is_rush:
            self.move_order()
            self.move(self.monster_speed)
            self.move_wait()



        
        
