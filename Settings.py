import os, pygame

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈

horizontal_margin = 200
vertical_margin = 100
screen_width = 1056 + horizontal_margin * 2
screen_height = 576 + vertical_margin * 2

bgm_vol = 100
effect_vol = 100
vol_ratio = 0.25

# 텍스트 속도
text_speed = 1

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)
# 프레임
FPS = 60
# 타일 사이즈
tile_width_size = 48
tile_height_size = 48
# 이미지 경로
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Images/TestPix")

# 인벤토리
inventory = []
# 로프(패스권)
rope_item = 2
# 스테이지 클리어 여부
stage_clear = [True, False, False, False, False, False]
