import pygame, os
from Settings import *

# 벽 이미지
class Rock(pygame.sprite.Sprite):
    def __init__(self, pos, direction, border_images):
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
                    if self.is_on_alcohol:
                        sprite.image = pygame.image.load(os.path.join(images_path, "purple_tile_1.png")).convert_alpha()
                        sprite.name = "alcoholRoad"
                    else:
                        self.border_images.remove(sprite)
                        sprite.image = pygame.image.load(os.path.join(images_path, "re_bridge.png")).convert_alpha()
                elif sprite.name != "WaterHole" and sprite.name != "alcoholRoad":
                    self.kill()

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
