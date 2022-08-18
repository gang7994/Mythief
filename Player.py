import pygame, os
from Settings import *
from Rock import Rock

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, damage_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "pix.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.character_width = self.rect.size[0]
        self.character_height = self.rect.size[1]
        self.current_hp = 100
        self.max_hp = 100
        self.hp_bar_length = 300
        self.hp_ratio = self.max_hp / self.hp_bar_length
        self.dir = pygame.math.Vector2()
        self.move_order = [0]
        self.is_horizon = False
        self.player_speed = 2
        self.border_images = border_images
        self.damage_images = damage_images
        self.rocks = pygame.sprite.Group()
        self.rock_cool_time = 700
        self.is_rock_ready = True
        self.rock_count = 0
        self.current_time = 0
        self.rock_time = 0
        self.undamaged_time = 1000    # 무적시간 1초
        self.is_damaged = False      # 데미지 상태인지

    # 피해 함수 (무적 시간 추가) -> 무적시 투명도 올림
    def get_damaged(self, attack):
        self.is_damaged = True
        if self.current_hp > 0:
            self.current_hp -= attack
        if self.current_hp <= 0:
            self.current_hp = 0
        self.damaged_start = pygame.time.get_ticks()
        self.image = pygame.image.load(os.path.join(images_path, "damaged_pix.png")).convert_alpha()
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
            self.dir.x = -1
        elif keys[pygame.K_RIGHT]:
            self.dir.x = 1
        else:
            self.dir.x = 0
        return self.dir.x

    # 수직 이동 입력
    def get_vertical(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.dir.y = -1
        elif keys[pygame.K_DOWN]:
            self.dir.y = 1
        else:
            self.dir.y = 0
        return self.dir.y

    # 이동 함수
    # 나중에 쉽게 수정할 수 있다면 하는 편이 좋을듯
    def move(self, speed):
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
            self.rect.left += x * speed
            self.collision("horizontal")
        else:
            self.rect.top += y * speed
            self.collision("vertical")
        # 화면 밖 안나가게
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.left > screen_width - self.rect.size[0]:
            self.rect.left = screen_width - self.rect.size[0]
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.top > screen_height - self.rect.size[1]:
            self.rect.top = screen_height - self.rect.size[1]

    # 무기 입력 확인 함수
    def add_rock(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_rock_ready:
            self.throw_rock()
            self.is_rock_ready = False
            self.rock_time = pygame.time.get_ticks()

    # 무기 발사 함수
    def throw_rock(self):
        self.rock_count += 1
        if self.dir.x == 1:
            self.rocks.add(Rock(self.rect.center, 1, self.border_images))
        elif self.dir.x == -1:
            self.rocks.add(Rock(self.rect.center, 2, self.border_images))
        elif self.dir.y == 1:
            self.rocks.add(Rock(self.rect.center, 3, self.border_images))
        elif self.dir.y == -1:
            self.rocks.add(Rock(self.rect.center, 4, self.border_images))

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
                self.image = pygame.image.load(os.path.join(images_path, "pix.png")).convert_alpha()
                self.image.set_alpha(255)



    # 충돌 함수 -> 적 충돌시 hp감소 추가(방향에 대한 매개변수로 인해 적 충돌에 버그가 좀 있음, 적 충돌을 따로 만들어야할 수도 있음)
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

    # 데미지를 주는 충돌을 따로 만듦
    def damage_collision(self):
        for sprite in self.damage_images:
            if sprite.rect.colliderect(self.rect):
                if sprite.name == "laser_Monster" and not self.is_damaged:
                    self.get_damaged(10)
                if sprite.name == "monster_laser" and not self.is_damaged:
                    self.get_damaged(5)
                    sprite.kill()
                if sprite.name == "jump_Monster" and not self.is_damaged:
                    self.get_damaged(10)


    # 업데이트 영역 -> 무적 시간 함수 추가
    def update(self):
        self.un_damaged_time()
        self.add_rock()
        self.re_load_rock()
        self.rocks.update()
        self.damage_collision()
        self.move(self.player_speed)