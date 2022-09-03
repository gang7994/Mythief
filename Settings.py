import os

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈
import pygame

horizontal_margin = 200
vertical_margin = 100
screen_width = 1056 + horizontal_margin * 2
screen_height = 576 + vertical_margin * 2

bgm_vol = 100
effect_vol = 100
vol_ratio = 0.25

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
# 프레임
FPS = 60
# 타일 사이즈
tile_width_size = 48
tile_height_size = 48
# 이미지 경로
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Images\\TestPix")