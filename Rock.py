import pygame, os
from Settings import *

# 벽 이미지
class Rock(pygame.sprite.Sprite):
    def __init__(self, pos, direction, border_images):
        super().__init__()
        self.image = pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.speed = 5
        self.direction = direction
        self.border_images = border_images

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
                if sprite.name == "NoneRoad":
                    self.border_images.remove(sprite)
                    sprite.image = pygame.image.load(os.path.join(images_path, "road.png")).convert_alpha()

    # 업데이트 영역
    def update(self):
        if self.direction == 1: self.rect.x += self.speed
        elif self.direction == 2: self.rect.x -= self.speed
        elif self.direction == 3: self.rect.y += self.speed
        elif self.direction == 4: self.rect.y -= self.speed
        self.collision()
