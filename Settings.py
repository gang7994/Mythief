import os, pygame
pygame.init()
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
item_path = os.path.join(current_path, "Images/Item")
stage_road_path = os.path.join(current_path, "Images/Stage_Road")
stage_P_path = os.path.join(current_path, "Images/Stage1_P")
stage_H_path = os.path.join(current_path, "Images/Stage2_H")
stage_D_path = os.path.join(current_path, "Images/Stage3_D")
stage_Z_path = os.path.join(current_path, "Images/Stage4_Z")

# 인벤토리
theme_inventory = ["Them_1.png", "Them_2.png", "Them_3.png", "Them_4.png", "Them_5.png"]
general_inventory = []
# 로프(패스권)
rope_item = 100
# 스테이지 클리어 여부
stage_clear = [True, True, True, True, True, True]

# player use item
use_item0 = False
use_item1 = False
use_item2 = False
use_item3 = False
use_item4 = False
use_item5 = False
use_item6 = False
use_item7 = False
use_item8 = False
use_item9 = False
use_item10 = False

# 플레이어
current_hp = 100
max_hp = 100
hp_bar_length = 500
shield = 0

# score
stage_score = [0,0,0,0,100]
bonus = 0

#sound
sound_path = os.path.join(current_path, "Sound")
click_sound = pygame.mixer.Sound((os.path.join(sound_path, "click.wav")))
stone_break_sound = pygame.mixer.Sound((os.path.join(sound_path, "stone_break.mp3")))
item_interaction_sound = pygame.mixer.Sound("Sound/item_interaction.wav")
use_sound = pygame.mixer.Sound((os.path.join(sound_path, "throw.wav")))
damage_sound = pygame.mixer.Sound((os.path.join(sound_path, "hurt.wav")))
thunder_sound = pygame.mixer.Sound((os.path.join(sound_path, "thunder.wav")))