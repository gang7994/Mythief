import pygame, os
from Settings import *

# 레이져 이미지
class MonsterLaser(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups, border_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "monster_laser.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate(0, 0)
        self.name = "monster_laser"
        self.speed = 5
        self.direction = direction
        self.border_images = border_images
        self.clock = pygame.time.Clock()
        self.is_pause = False

    # 영역 밖에서 오브젝트 삭제
    def destroy(self):
        if self.direction == 1:
            if self.hitbox.x > screen_width: self.kill()
        elif self.direction == 2:
            if self.hitbox.x < 0: self.kill()
        elif self.direction == 3:
            if self.hitbox.y > screen_height: self.kill()
        elif self.direction == 4:
            if self.hitbox.y < 0: self.kill()

    # 충돌 함수
    def collision(self):
        for sprite in self.border_images:
            if sprite.rect.colliderect(self.rect):
                if sprite.name == "Wall" or sprite.name == "obstacle":
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
