import pygame, os
from Settings import *
from Rock import Rock


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, border_images, damage_images, images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "sprite_0.png")).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-15)
        self.name = "Player"
        self.character_width = self.rect.size[0]
        self.character_height = self.rect.size[1]
        self.current_hp = 100
        self.max_hp = 100
        self.hp_bar_length = 500
        self.hp_ratio = self.max_hp / self.hp_bar_length
        self.dir = pygame.math.Vector2()
        self.move_order = [0]
        self.is_horizon = False
        self.player_speed_x = 0
        self.player_speed_y = 0
        self.border_images = border_images
        self.damage_images = damage_images
        self.images = images
        self.rock_cool_time = 3000
        self.is_rock_ready = True
        self.rock_count = 0
        self.current_time = 0
        self.rock_time = 0
        self.undamaged_time = 1000    # 무적시간 1초
        self.is_damaged = False      # 데미지 상태인지
        self.last_x_dir = 1
        self.last_dir = 2
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
        self.test_item_on = False

        
    def walk_animation(self):
        if self.walk_count > 5:
            self.walk_count = 0
        self.walk_current_time = pygame.time.get_ticks()
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
        if self.idle_count == 0:
            self.image = pygame.image.load(os.path.join(images_path, "sprite_idle0.png")).convert_alpha()
        elif self.idle_count == 1:
            self.image = pygame.image.load(os.path.join(images_path, "sprite_idle1.png")).convert_alpha()
        elif self.idle_count == 2:
            self.image = pygame.image.load(os.path.join(images_path, "sprite_idle2.png")).convert_alpha()
        if self.last_x_dir == -1: self.image = pygame.transform.flip(self.image, True, False)
        if self.is_damaged: self.image.set_alpha(200)
    
    def throw_animation(self):
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
    def get_damaged(self, attack):
        self.is_damaged = True
        if self.current_hp > 0:
            self.current_hp -= attack
        if self.current_hp <= 0:
            self.current_hp = 0
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
        if (keys[pygame.K_SPACE] and self.is_rock_ready):
            self.throw_rock()
            self.is_rock_ready = False
            self.rock_time = pygame.time.get_ticks()
            self.throw_animation()

    # 무기 발사 함수
    def throw_rock(self):
        self.rock_count += 1
        if self.last_dir == 2:
            self.images.add(Rock((self.rect.x, self.rect.y + 7.5), 1, self.border_images))
        elif self.last_dir == 1:
            self.images.add(Rock((self.rect.x, self.rect.y + 7.5), 2, self.border_images))
        elif self.last_dir == 4:
            self.images.add(Rock(self.rect.center, 3, self.border_images))
        elif self.last_dir == 3:
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



    # 충돌 함수
    def collision(self, direction):
        if direction == "horizontal":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if self.dir.x > 0:
                        self.hitbox.right = sprite.rect.left
                    elif self.dir.x < 0:
                        self.hitbox.left = sprite.rect.right
        if direction == "vertical":
            for sprite in self.border_images:
                if sprite.rect.colliderect(self.hitbox):
                    if self.dir.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    elif self.dir.y < 0:
                        self.hitbox.top = sprite.rect.bottom

    # 데미지를 주는 충돌을 따로 만듦
    def damage_collision(self):
        for sprite in self.damage_images:
            if sprite.rect.colliderect(self.hitbox):
                if sprite.name == "laser_Monster" and not self.is_damaged:
                    self.get_damaged(10)
                if sprite.name == "monster_laser" and not self.is_damaged:
                    self.get_damaged(5)
                    sprite.kill()
                if sprite.name == "rush_Monster" and not self.is_damaged:
                    self.get_damaged(10)


    # 업데이트 영역 -> 무적 시간 함수 추가
    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_pause:
            self.un_damaged_time()
            self.add_rock()
            self.re_load_rock()
            self.damage_collision()
            self.move(self.player_speed_x, self.player_speed_y, dt)
            self.walk_delay()
            self.idle()
            self.idle_delay()
        