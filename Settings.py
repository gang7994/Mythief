import os

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈
screen_width = 1056
screen_height = 576
# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# 프레임
FPS = 60
# 타일 사이즈
tile_width_size = 48
tile_height_size = 48
# 이미지 경로
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Images\\TestPix")
# 맵
map = [[list("WWWWWWWWWWWFWWWWWWWWWW"),
       list("W....................W"),
       list("W.........O..........W"),
       list("W..........O.........W"),
       list("W...........O........W"),
       list("W............O.......W"),
       list("W..............O.....W"),
       list("W....................W"),
       list("W....................W"),
       list("W.......O............W"),
       list("WP...................W"),
       list("WWWWWWWWWWWWWWWWWWWWWW")],
       [list("WWWWWWWWWWWFWWWWWWWWWW"),
       list("W....................W"),
       list("W.........O..........W"),
       list("W..........O.........W"),
       list("W....................W"),
       list("W..O.........O.......W"),
       list("W..............O.....W"),
       list("W....................W"),
       list("W....................W"),
       list("W.......O......O.....W"),
       list("WP...................W"),
       list("WWWWWWWWWWWWWWWWWWWWWW")],
       [list("WWWWWWWWWWWFWWWWWWWWWW"),
       list("W....................W"),
       list("W.........O..........W"),
       list("W..........O.........W"),
       list("W...........O........W"),
       list("W............O.......W"),
       list("W..............O.....W"),
       list("W....................W"),
       list("W....................W"),
       list("W.......O...O........W"),
       list("WP...................W"),
       list("WWWWWWWWWWWWWWWWWWWWWW")]]