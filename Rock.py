import pygame, os
from Settings import *

# 벽 이미지
class Rock(pygame.sprite.Sprite):
    def __init__(self, pos, direction, border_images, itemeffect):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = "Rock"
        self.hitbox = self.rect.inflate(-20, -20)
        self.speed = 5
        self.direction = direction
        self.border_images = border_images
        self.clock = pygame.time.Clock()
        self.is_pause = False
        self.is_on_alcohol = False
        self.itemeffect = itemeffect

    # 영역 밖에서 오브젝트 삭제
    def destroy(self):
        if self.direction == 1:
            if self.rect.x > screen_width: self.kill()
        elif self.direction == 2:
            if self.rect.x < 0: self.kill()
        elif self.direction == 3:
            if self.rect.y > screen_height: self.kill()
        elif self.direction == 4:
            if self.rect.y < 0: self.kill()

    # 충돌 함수
    def collision(self):
        for sprite in self.border_images:
            if sprite.hitbox.colliderect(self.hitbox):
                if sprite.name == "alcoholRoad":
                    self.is_on_alcohol = True
                if sprite.name == "NoneRoad":
                    if self.is_on_alcohol and not self.itemeffect:
                        sprite.image = pygame.image.load(os.path.join(images_path, "purple_tile_1.png")).convert_alpha()
                        sprite.name = "alcoholRoad"
                    else:
                        self.border_images.remove(sprite)
                        sprite.image = pygame.image.load(os.path.join(images_path, "re_bridge.png")).convert_alpha()
                        sprite.name = "Road"
                elif sprite.name == "NoneRoad1":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "wTile_Bridge.png")).convert_alpha()
                    sprite.name = "Road"
                elif sprite.name != "WaterHole" and sprite.name != "alcoholRoad" and not sprite.name in ["Electric00","Electric01","Electric02","Electric03","Electric04","Electric05","Electric06","Electric07","Electric08","Electric09","Electric10"]:
                    self.kill()
                if sprite.name == "Electric00":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_00_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad00"
                if sprite.name == "Electric01":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_01_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad01"
                if sprite.name == "Electric02":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_02_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad02"
                if sprite.name == "Electric03":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_03_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad03"
                if sprite.name == "Electric04":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_04_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad04"
                if sprite.name == "Electric05":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_05_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad05"
                if sprite.name == "Electric06":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_06_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad06"
                if sprite.name == "Electric07":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_07_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad07"
                if sprite.name == "Electric08":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_08_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad08"
                if sprite.name == "Electric09":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_09_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad09"
                if sprite.name == "Electric10":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "electric_10_bridge.png")).convert_alpha()
                    sprite.name = "ElectricRoad10"

    # 업데이트 영역
    def update(self):
        dt = self.clock.tick(FPS)
        if not self.is_pause:
            if self.direction == 1: self.hitbox.x += self.speed * (dt // 6)
            elif self.direction == 2: self.hitbox.x -= self.speed * (dt // 6)
            elif self.direction == 3: self.hitbox.y += self.speed * (dt // 6)
            elif self.direction == 4: self.hitbox.y -= self.speed * (dt // 6)
            self.rect.center = self.hitbox.center
            self.collision()
