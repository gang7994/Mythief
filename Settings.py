import os

# 게임 세팅 - 시험해보기 주석

# 화면 사이즈
screen_width = 1000
screen_height = 800
# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# 프레임
FPS = 60
# 타일 사이즈
tile_width_size = 100
tile_height_size = 80
# 이미지 경로
current_path = os.path.dirname(__file__)
images_path = os.path.join(current_path, "Images\\TestPix")
# 맵
map = [[list("WWWWF.WWWW"),
       list(".W........"),
       list(".W....W..."),
       list("W.....W..."),
       list(".........."),
       list(".W.W......"),
       list(".W....W..."),
       list("....W....."),
       list("....W....."),
       list("P...W.....")],
       [list("WWWWF.WWWW"),
       list(".........."),
       list("......W..."),
       list("......W..."),
       list(".........."),
       list("...W......"),
       list("......W..."),
       list("....WWWWW."),
       list("....W....."),
       list("P...W.....")],
       [list("WWWWW.WWWW"),
        list(".P...W.W.."),
        list("......W..."),
        list("......W..."),
        list(".........F"),
        list("...W......"),
        list("......W..."),
        list(".W..WWWWW."),
        list("....W....."),
        list("WWWWW.....")]]