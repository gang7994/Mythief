import os

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈
horizontal_margin = 200    
vertical_margin = 100
screen_width = 1056 + horizontal_margin * 2
screen_height = 576 + vertical_margin * 2


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
# 맵 -> 적들이 길 위에서만 움직이게 변경
map = [[list("WWWWWWWWWWWFWWWWWWWWWW"),
       list("W....................W"),
       list("W.........O..........W"),
       list("W..........O.....RRR.W"),
       list("W...........O....RMR.W"),
       list("W....RRR.....O...RRR.W"),
       list("W....RMR.......O.....W"),
       list("W....RRR.............W"),
       list("W...............MR...W"),
       list("W.......O.......RR...W"),
       list("WP...................W"),
       list("WWWWWWWWWWWWWWWWWWWWWW")],
       [list("WWWWWWWWWWWFWWWWWWWWWW"),
       list("W....................W"),
       list("W.........O..........W"),
       list("W..........O....RRR..W"),
       list("W...............RMR..W"),
       list("W..O....RR...O..RRR..W"),
       list("W.......MR.....O.....W"),
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
       list("W...............RRR..W"),
       list("W...............RMR..W"),
       list("W.......O...O...RRR..W"),
       list("WP...................W"),
       list("WWWWWWWWWWWWWWWWWWWWWW")]]