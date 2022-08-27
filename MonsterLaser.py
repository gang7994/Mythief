import pygame, os
from Settings import *

# 레이져 이미지
class MonsterLaser(pygame.sprite.Sprite):
    def __init__(self, pos, direction, groups, border_images):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join(images_path, "monster_laser.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.name = "monster_laser"
        self.speed = 5
        self.direction = direction
        self.border_images = border_images
        self.clock = pygame.time.Clock()

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
            if sprite.rect.colliderect(self.rect):
                if sprite.name == "Wall":
                    self.kill()

    # 업데이트 영역
    def update(self):
        dt = self.clock.tick(FPS)
        if self.direction == 1: self.rect.x += self.speed * (dt // 6)
        elif self.direction == 2: self.rect.x -= self.speed * (dt // 6)
        elif self.direction == 3: self.rect.y += self.speed * (dt // 6)
        elif self.direction == 4: self.rect.y -= self.speed * (dt // 6)
        self.collision()
