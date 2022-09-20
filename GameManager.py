import pygame, sys, os, time
from Settings import *
from Level import *
from Button import Button
from Button_text import Button_text
from Map import *
from ParticleEffect import Particle
from TextScene import *

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("proto")
        self.clock = pygame.time.Clock()
        self.particle = Particle()
        self.total_time = 0
        self.total_rock_count = 0
        self.total_score = 0
        self.running = True
        self.level = None
        self.use_rope = False
        self.text = TextManager(0)
        self.is_opening = False
        self.interaction_UI = pygame.image.load(os.path.join(images_path, "interaction_UI.png")).convert_alpha()
        self.item_cover = pygame.image.load(os.path.join(item_path, "item_cover.png")).convert_alpha()

    def Encyclopedia(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = self.get_font(45).render("백과사전창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button_text(image=None, pos=(1300, 0),
                                text_input="BACK", font = self.get_font(60), base_color="White", hovering_color="Red")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        running = False
            self.particle.click_effect(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1], dt)
            self.particle.mouse_cursor(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1])
            pygame.display.update()

    def Credit(self):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = self.get_titlefont(60).render("Mythief", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width / 2), 70))

            TEXT1 = self.get_font(30).render("여기에 크레딧 내용 추가", True, "White")
            TEXT1_RECT = TEXT1.get_rect(center=((screen_width / 2), 300))

            TEXT2 = self.get_font(30).render("Add credit content here", True, "White")
            TEXT2_RECT = TEXT1.get_rect(center=((screen_width / 2), 400))

            self.screen.blit(TEXT1, TEXT1_RECT)
            self.screen.blit(TEXT2, TEXT2_RECT)
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button_text(image=None, pos=(1300, 0),
                                       text_input="BACK", font=self.get_font(60), base_color="White", hovering_color="Red")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        running = False
            self.particle.click_effect(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1], dt)
            self.particle.mouse_cursor(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1])
            pygame.display.update()

    def Option(self):
        global bgm_vol, effect_vol
        running = True
        while running:
            dt = self.clock.tick(FPS)
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = self.get_font(45).render("옵션창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width / 2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()

            TEXT1 = self.get_font(30).render("BGM VOLUME", True, "White")
            TEXT1_RECT = TEXT1.get_rect(center=((screen_width / 2), 200))

            TEXT2 = self.get_font(30).render("EFFECT VOLUME", True, "White")
            TEXT2_RECT = TEXT1.get_rect(center=((screen_width / 2), 400))

            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            self.screen.blit(TEXT1, TEXT1_RECT)
            self.screen.blit(TEXT2, TEXT2_RECT)

            self.draw_volume_bar()

            BGM_UP = Button(image0=pygame.image.load(os.path.join(images_path, "up0.png")).convert_alpha(),
                            image1=pygame.image.load(os.path.join(images_path, "up1.png")).convert_alpha(),
                            pos=(956, 265), scale_x=50, scale_y=50)
            BGM_DOWN = Button(image0=pygame.image.load(os.path.join(images_path, "down0.png")).convert_alpha(),
                              image1=pygame.image.load(os.path.join(images_path, "down1.png")).convert_alpha(),
                              pos=(500, 265), scale_x=50, scale_y=50)

            EFFECT_UP = Button(image0=pygame.image.load(os.path.join(images_path, "up0.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "up1.png")).convert_alpha(),
                               pos=(956, 465), scale_x=50, scale_y=50)
            EFFECT_DOWN = Button(image0=pygame.image.load(os.path.join(images_path, "down0.png")).convert_alpha(),
                                 image1=pygame.image.load(os.path.join(images_path, "down1.png")).convert_alpha(),
                                 pos=(500, 465), scale_x=50, scale_y=50)

            OPTIONS_BACK = Button_text(image=None, pos=(1200, 0),
                                       text_input="BACK", font=self.get_font(60), base_color="White", hovering_color="Red")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            BGM_UP.changeColor(OPTIONS_MOUSE_POS)
            BGM_UP.update(self.screen)
            BGM_DOWN.changeColor(OPTIONS_MOUSE_POS)
            BGM_DOWN.update(self.screen)
            EFFECT_UP.changeColor(OPTIONS_MOUSE_POS)
            EFFECT_UP.update(self.screen)
            EFFECT_DOWN.changeColor(OPTIONS_MOUSE_POS)
            EFFECT_DOWN.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        running = False
                    if BGM_UP.checkForInput(OPTIONS_MOUSE_POS):
                        if bgm_vol != 100:
                            bgm_vol += 10
                    if BGM_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        if bgm_vol != 0:
                            bgm_vol -= 10
                    if EFFECT_UP.checkForInput(OPTIONS_MOUSE_POS):
                        if effect_vol != 100:
                            effect_vol += 10
                    if EFFECT_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        if effect_vol != 0:
                            effect_vol -= 10
            self.particle.click_effect(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1], dt)
            self.particle.mouse_cursor(self.screen, OPTIONS_MOUSE_POS[0], OPTIONS_MOUSE_POS[1])
            pygame.display.update()

    def draw_volume_bar(self):
        pygame.draw.rect(self.screen, WHITE, (528, 250, bgm_vol / 0.25, 30))
        pygame.draw.rect(self.screen, BLACK, (528, 250, 400, 30), 3)
        pygame.draw.rect(self.screen, WHITE, (528, 450, effect_vol / 0.25, 30))
        pygame.draw.rect(self.screen, BLACK, (528, 450, 400, 30), 3)

    def get_titlefont(self, size):
        return pygame.font.Font("Images/TestPix/font.ttf", size)

    def get_font(self, size):
        return pygame.font.SysFont('malgungothic', size)

    def main_menu(self):
        global rope_item, current_hp
        while True:
            dt = self.clock.tick(FPS)
            self.screen.fill(BLACK)
            bg_image = pygame.transform.scale(
                pygame.image.load(os.path.join(images_path, "mainBackGround.png")).convert_alpha(), (1456, 776))
            logo_image = pygame.transform.scale(
                pygame.image.load(os.path.join(images_path, "mainLogo.png")).convert_alpha(), (600, 200))
            self.screen.blits([(bg_image, (0, 0)), (logo_image, (428, 20))])
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            pygame.mouse.set_visible(False)

            PLAY_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_start_0.png")).convert_alpha(),
                                 image1=pygame.image.load(os.path.join(images_path, "btn_start_1.png")).convert_alpha(),
                                 pos=(728, 280), scale_x=400, scale_y=100)
            ENCYCLOPEDIA_BUTTON = Button(
                image0=pygame.image.load(os.path.join(images_path, "btn_Collection_0.png")).convert_alpha(),
                image1=pygame.image.load(os.path.join(images_path, "btn_Collection_1.png")).convert_alpha(),
                pos=(728, 390), scale_x=400, scale_y=100)
            CREDIT_BUTTON = Button(
                image0=pygame.image.load(os.path.join(images_path, "btn_credit_0.png")).convert_alpha(),
                image1=pygame.image.load(os.path.join(images_path, "btn_credit_1.png")).convert_alpha(),
                pos=(728, 500), scale_x=400, scale_y=100)
            OPTION_BUTTON = Button(
                image0=pygame.image.load(os.path.join(images_path, "btn_start_0.png")).convert_alpha(),
                image1=pygame.image.load(os.path.join(images_path, "btn_start_1.png")).convert_alpha(),
                pos=(728, 610), scale_x=400, scale_y=100)
            QUIT_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_exit_0.png")).convert_alpha(),
                                 image1=pygame.image.load(os.path.join(images_path, "btn_exit_1.png")).convert_alpha(),
                                 pos=(728, 720), scale_x=400, scale_y=100)

            for button in [PLAY_BUTTON, ENCYCLOPEDIA_BUTTON, CREDIT_BUTTON, OPTION_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            self.particle.click_effect(self.screen, MENU_MOUSE_POS[0], MENU_MOUSE_POS[1], dt)
            self.particle.mouse_cursor(self.screen, MENU_MOUSE_POS[0], MENU_MOUSE_POS[1])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.particle.click_flag = True
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            current_hp = max_hp
                            if not self.is_opening:
                                self.text.draw_text(0, self.screen)
                                self.is_opening = True
                            self.level = Level(0, 0, 0, pygame.time.get_ticks())
                            self.running = True
                            self.Run()
                            theme_inventory.clear()
                            rope_item = 2
                        if ENCYCLOPEDIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.Encyclopedia()
                        if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.Credit()
                        if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.Option()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

    def dead_surface(self, mouse_pos):
        MAINMENU = Button(image0=pygame.image.load(os.path.join(images_path, "exit_icon.png")).convert_alpha(),
                       image1=pygame.image.load(os.path.join(images_path, "exit_icon2.png")).convert_alpha(),
                       pos=(700, 550), scale_x=200, scale_y=200)
        game_font = pygame.font.Font(None, 120)
        msg = game_font.render("You are dead", True, WHITE)
        msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))
        self.screen.fill(BLACK)
        self.screen.blit(msg, msg_rect)
        MAINMENU.changeColor(mouse_pos)
        MAINMENU.update(self.screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.particle.click_flag = True
                if MAINMENU.checkForInput(mouse_pos):
                    self.running = False
        self.particle.mouse_cursor(self.screen, mouse_pos[0], mouse_pos[1])



    # 시간 재기
    def draw_time(self, elapse_time):
        font = pygame.font.Font(None, 25)
        timer = font.render("Time : {}".format(int(elapse_time)), True, WHITE)
        self.screen.blit(timer, (10, 170))

    # 걸린 시간
    def total_time_update(self, elapse_time):
        self.total_time += elapse_time
        return self.total_time
    
    # 얻은 점수 수정 필요
    def total_score_update(self, score):
        self.total_score += score
        return self.total_score

    # 점수 그리기
    def draw_score(self, total_score):
        font = pygame.font.Font(None, 25)
        score = font.render("Score : {}".format(int(total_score)), True, WHITE)
        self.screen.blit(score, (10, 205))

    # 돌 던진 횟수 그리기
    def draw_rock_count(self):
        font = pygame.font.Font(None, 25)
        score = font.render("Rock Count : {}".format(int(self.level.player.rock_count)), True, WHITE)
        self.screen.blit(score, (10, 240))

    # 체력 그리기
    def draw_hp(self):
        pygame.draw.rect(self.screen, RED, (10, 15, current_hp / (max_hp / hp_bar_length), 30))
        pygame.draw.rect(self.screen, WHITE, (10, 15, hp_bar_length, 30), 2)

    # 무기 이미지 그리기
    def draw_rock_image(self):
        self.screen.blit(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (1330, 400))
        pygame.draw.rect(self.screen, WHITE, (1325.5, 395.5, 32, 32), 2)

    def draw_frame(self):
        pygame.draw.rect(self.screen, BLACK, (0,0,1456,776), 150)
        pygame.draw.rect(self.screen, WHITE, (150, 150, 1156, 476), 1)

    # 무기 쿨타임 그리기
    def draw_rock_cool_time(self):
        if self.level.player.current_time != 0 and self.level.player.rock_time != 0:
            if self.level.player.current_time - self.level.player.rock_time <= self.level.player.rock_cool_time:
                pygame.draw.rect(self.screen,
                                 BLACK,
                                 (1325.5, 395.5, 32,
                                  32 - (self.level.player.current_time - self.level.player.rock_time) / 63))

    def item_interaction_text(self):
        if self.level.player.item_interaction:
            font = pygame.font.Font("Images/TestPix/Mabinogi_Classic_TTF.ttf", 20)
            tap_key = font.render("Tap을 누르시오", True, BLACK)
            txt_w, txt_h = tap_key.get_size()
            self.screen.blit(self.interaction_UI,(screen_width // 2 - 149 // 2, screen_height // 2 - 75))
            self.screen.blit(tap_key, (screen_width // 2 - txt_w // 2, screen_height // 2 - 65))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_TAB]:
                pygame.draw.rect(self.screen, YELLOW,
                                 (screen_width // 2 - self.level.player.item_bar_length // 2,
                                  screen_height // 2 + 30,
                                  self.level.player.current_item_gage / self.level.player.item_ratio,
                                  10))
                pygame.draw.rect(self.screen, WHITE,
                                 (screen_width // 2 - self.level.player.item_bar_length // 2,
                                  screen_height // 2 + 30,
                                  self.level.player.item_bar_length,
                                  10), 2)

    def door_interaction_text(self):
        font = pygame.font.Font("Images/TestPix/Mabinogi_Classic_TTF.ttf", 30)
        door_text = font.render("", True, WHITE)
        if self.level.player.stage0_interaction:
            door_text = font.render("Tutorial", True, WHITE)
        elif self.level.player.stage1_interaction:
            door_text = font.render("STAGE 1", True, WHITE)
        elif self.level.player.stage2_interaction:
            door_text = font.render("STAGE 2", True, WHITE)
        elif self.level.player.stage3_interaction:
            door_text = font.render("STAGE 3", True, WHITE)
        elif self.level.player.stage4_interaction:
            door_text = font.render("STAGE 4", True, WHITE)
        elif self.level.player.stage5_interaction:
            door_text = font.render("STAGE 5", True, WHITE)
        self.screen.blit(door_text, (680, 690))
            

    # 클리어 함수
    # def total_score_update(self, score): 수정시 수정 필요
    def clear(self, elapsed_time):
        game_font = pygame.font.Font(None, 120)
        msg = game_font.render(f"Your score is {self.total_score_update(self.total_time_update(elapsed_time))}", True, WHITE)
        msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2))
        self.screen.fill(BLACK)
        self.screen.blit(msg, msg_rect)
        self.running = False
    
    # 현재 스테이지 글자로 표시
    def current_stage(self):
        font = pygame.font.Font(None, 40)
        stage = self.level.stage_number
        if stage == 0: text = font.render(f"[ MAIN ]", True, WHITE)
        elif stage == 1: text = font.render(f"[ TUTORIAL ]", True, WHITE)
        elif stage == 2: text = font.render(f"[ STAGE 1 ]", True, WHITE)
        elif stage == 3: text = font.render(f"[ STAGE 2 ]", True, WHITE)
        elif stage == 4: text = font.render(f"[ STAGE 3 ]", True, WHITE)
        elif stage == 5: text = font.render(f"[ STAGE 4 ]", True, WHITE)
        elif stage == 6: text = font.render(f"[ STAGE 5]", True, WHITE)
        self.screen.blit(text, (660, 15))
        
    def show_general_inventory(self):
        for i in range(12):
            pygame.draw.circle(self.screen, GREY, (150+i*105, 100), 40)
        for i, item in enumerate(general_inventory):
            if item[0].name in ["test_general_item0", "test_general_item1", "test_general_item2", "test_general_item3", "test_general_item4", "test_general_item5"]:
                image_rect = item[0].image.get_rect(center=(150+i*105, 100))                                       
                self.screen.blit(item[0].image, image_rect)
                self.item_cover = pygame.image.load(os.path.join(item_path, "item_cover.png")).convert_alpha()
                self.item_cover = pygame.transform.scale(self.item_cover, (30,30-item[1]*5))
                self.item_cover.set_alpha(200)                                          
                self.screen.blit(self.item_cover,(135+i*105, 85))

    def show_info(self):
        font = pygame.font.Font(None, 25)
        pos = font.render(f"Player_pos: {self.level.player.rect.centerx, self.level.player.rect.centery,}", True, WHITE)
        remain_monster = font.render(f"Remaining_Monster: {self.level.remain_monster}", True, WHITE) # Show_info로 주석표기
        fps = font.render(f"FPS: {str(int(self.clock.get_fps()))}", True, WHITE)
        self.screen.blits([(pos, (10, 560)),(remain_monster, (10, 590)), (fps, (10, 620))])
        
    def show_theme_inventory(self):
        pygame.draw.circle(self.screen, GREY, (150, 710), 40)
        pygame.draw.circle(self.screen, GREY, (270, 710), 40)
        pygame.draw.circle(self.screen, GREY, (390, 710), 40)
        pygame.draw.circle(self.screen, GREY, (510, 710), 40)
        for i, item in enumerate(theme_inventory):
            if item.name == "test0_item":
                image_rect = item.image.get_rect(center=(150+i*120, 710))
                self.screen.blit(item.image, image_rect)
            elif item.name == "test1_item":
                image_rect = item.image.get_rect(center=(150+i*120, 710))
                self.screen.blit(item.image, image_rect)
            elif item.name == "test2_item":
                image_rect = item.image.get_rect(center=(150 + i * 120, 710))
                self.screen.blit(item.image, image_rect)
            i+= 120
        
    def show_item(self):
        pygame.draw.circle(self.screen, GREY, (1370, 480), 40) #기믹아이템
        pygame.draw.circle(self.screen, GREY, (1370, 600), 40) #패스권
        game_font = pygame.font.Font(None, 50)
        rope_count = game_font.render(f"{rope_item}/2", True, WHITE)
        self.screen.blit(rope_count, (1350, 580))
        self.screen.blit(pygame.transform.scale(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (50, 50)), (1345, 690))
        pygame.draw.rect(self.screen, WHITE, (1341, 690, 55, 55), 2)
        if self.level.player.current_time != 0 and self.level.player.rock_time != 0:
            if self.level.player.current_time - self.level.player.rock_time <= self.level.player.rock_cool_time:
                pygame.draw.rect(self.screen, BLACK,(1341, 690, 55, 55 - (self.level.player.current_time - self.level.player.rock_time) / 40))


    def show_dir(self):
        keys = pygame.key.get_pressed()
        if not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
            if self.level.player.last_dir == 1:
                image = pygame.image.load(os.path.join(images_path, "arr0.png")).convert_alpha()
                self.screen.blit(image, (710, 360))
            elif self.level.player.last_dir == 2:
                image = pygame.image.load(os.path.join(images_path, "arr1.png")).convert_alpha()
                self.screen.blit(image, (746, 360))
            elif self.level.player.last_dir == 3:
                image = pygame.image.load(os.path.join(images_path, "arr2.png")).convert_alpha()
                self.screen.blit(image, (715, 350))
            elif self.level.player.last_dir == 4:
                image = pygame.image.load(os.path.join(images_path, "arr3.png")).convert_alpha()
                self.screen.blit(image, (715, 400))
                
    def general_item_effect(self):
        global rope_item, max_hp, use_item0, use_item1, use_item2
        for tmp in general_inventory:
            if tmp[1] == 6:
                if tmp[0].name == "test_general_item0" and not use_item0: #로프 1개 추가
                    rope_item +=1
                    use_item0 = True
                elif tmp[0].name == "test_general_item1": #플레이어 이동 속도 증가
                    self.level.player.player_speed_x+=1
                    self.level.player.player_speed_y+=1
                    use_item1 = True
                elif tmp[0].name == "test_general_item2" and not use_item2: 
                    max_hp += 30
                    use_item2 = True
                    
    def player_hp(self):
        global current_hp
        if current_hp > 0:
            if self.level.player.is_damage5:
                current_hp -= 5
                self.level.player.is_damage5 = False
            if self.level.player.is_damage10:
                current_hp -= 10
                self.level.player.is_damage10 = False
        else:
            current_hp = 0
            self.level.player.is_dead = True
            
    # 게임 로직
    def Run(self):
        global rope_item
        # 프레임 영역
        self.start_time = pygame.time.get_ticks()
        # 메인 로직 영역
        while self.running:
            dt = self.clock.tick(FPS)
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()
            if not self.level.is_pause:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "pause1.png")).convert_alpha(), 
                                pos=(1390,35), scale_x=50, scale_y=50)
                SETTING = Button(image0=pygame.image.load(os.path.join(images_path, "setting_icon.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "setting_icon2.png")).convert_alpha(),
                               pos=(740, 380), scale_x=200, scale_y=200)
                EXIT = Button(image0=pygame.image.load(os.path.join(images_path, "exit_icon.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "exit_icon2.png")).convert_alpha(),
                               pos=(1140, 380), scale_x=300, scale_y=300)
            else:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause2.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "pause3.png")).convert_alpha(), 
                                pos=(340,380), scale_x=200, scale_y=200)
                SETTING = Button(image0=pygame.image.load(os.path.join(images_path, "setting_icon.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "setting_icon2.png")).convert_alpha(),
                               pos=(740, 380), scale_x=300, scale_y=300)
                EXIT = Button(image0=pygame.image.load(os.path.join(images_path, "exit_icon.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "exit_icon2.png")).convert_alpha(),
                               pos=(1140, 380), scale_x=300, scale_y=300)
            PAUSE.changeColor(PAUSE_MOUSE_POS)
            SETTING.changeColor(PAUSE_MOUSE_POS)
            EXIT.changeColor(PAUSE_MOUSE_POS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if PAUSE.checkForInput(PAUSE_MOUSE_POS) and not self.level.is_pause:
                        self.level.pause("T")
                    elif PAUSE.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.level.pause("F")

                    if SETTING.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.Option()
                    if EXIT.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not self.level.is_pause:
                        self.level.pause("T")
                    elif event.key == pygame.K_ESCAPE and self.level.is_pause:
                        self.level.pause("F")
                    if event.key == pygame.K_r and self.level.stage_number != 0:
                        if rope_item != 0 and not self.use_rope:
                            if(self.level.map_idx == 3 or self.level.map_idx == 7 or self.level.map_idx == 8):
                                pass
                            if (not self.level.stage_number == 1) or (self.level.stage_number == 1 and self.level.map_idx == 3):
                                rope_item -= 1
                                self.use_rope = True
                    if event.key == pygame.K_f:
                        if self.level.text is not None:
                            if self.level.text.text_idx < len(self.level.text.texts[self.level.map_idx]) - 1:
                                self.level.text.text_idx += 1
                            else:
                                self.level.text.ui_flag = False


            # 이미지 영역
            self.screen.fill(BLACK)
            self.level.run()
            self.draw_frame()
            self.draw_rock_count()
            self.show_item()
            self.player_hp()
            self.draw_hp()
            self.current_stage()
            self.show_general_inventory()
            self.general_item_effect()
            #self.draw_current_stage(self.level.map_idx)
            self.show_dir()
            self.show_info()
            self.item_interaction_text()
            self.door_interaction_text()
            self.show_theme_inventory()
            if not text_flag[self.level.stage_number + 1]:
                self.level.text.draw_ui_text(self.level.text_idx, self.screen)     # 자동으로 생성되는 텍스트(한번 봤으면 다시 못봄)
            PAUSE.update(self.screen)

            if not self.level.is_pause:
                self.tem_now_time = pygame.time.get_ticks() - self.start_time
                elapse_time = (self.tem_now_time) / 1000
            else:
                self.start_time = pygame.time.get_ticks() - self.tem_now_time
                elapse_time = (self.tem_now_time) / 1000
            self.draw_time(elapse_time)
            self.draw_score(self.total_score)
            if self.level.is_pause:
                self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
                self.popup.set_alpha(200)
                self.screen.blit(self.popup, (100, 100))
                SETTING.update(self.screen)
                EXIT.update(self.screen)
                self.particle.mouse_cursor(self.screen, PAUSE_MOUSE_POS[0], PAUSE_MOUSE_POS[1])

            if self.level.glow.dead_rad <= 0:
                self.dead_surface(PAUSE_MOUSE_POS)
            self.particle.click_effect(self.screen, PAUSE_MOUSE_POS[0], PAUSE_MOUSE_POS[1], dt)

            # 게임 클리어 영역
            x = self.level.get_player() # 캐릭터
            y = self.level.get_finish() # Finish 타일

            # 이부분 고쳐야함
            if self.use_rope:
                if self.level.map_idx < len(map[self.level.stage_number]) - 1: #다음 방이 있다면 넘어가기
                    self.level = Level(self.level.text_idx + 1, self.level.stage_number, self.level.map_idx + 1, pygame.time.get_ticks())
                elif self.level.stage_number < len(self.level.cur_map) - 1: #추후 보스맵에서는 로프권 사용 못하게 할 예정
                    self.level = Level(0, self.level.stage_number + 1, 0, pygame.time.get_ticks())
                else:
                    self.clear(int(elapse_time))
                self.use_rope = False

            if x.hitbox.colliderect(y.rect):
                if self.level.map_idx < len(map[self.level.stage_number]) - 1: #다음 방이 있다면 넘어가기
                    Level.remain_monster = 0 # Show_info
                    self.level = Level(self.level.text_idx + 1, self.level.stage_number, self.level.map_idx + 1, pygame.time.get_ticks())
                else: #다음 방이 없으면 메인 스테이지로 넘어가기
                    if self.level.stage_number == 1: #튜토리얼 스테이지 마지막 방에서 나왔을때 초기화
                        theme_inventory.clear()
                        rope_item = 2
                    elif self.level.stage_number == 6: # 마지막 스테이지 
                        self.clear(int(elapse_time))
                    stage_clear[self.level.stage_number] = True
                    text_flag[self.level.stage_number + 1] = True
                    self.level = Level(0, 0, 0, pygame.time.get_ticks())

            if self.level.stage_number == 0: #메인 스테이지 
                s0 = self.level.get_stage0() #스테이지 입구 타일
                s1 = self.level.get_stage1() 
                s2 = self.level.get_stage2()
                s3 = self.level.get_stage3()
                s4 = self.level.get_stage4()
                s5 = self.level.get_stage5()

                if x.hitbox.colliderect(s0.rect): #튜토리얼 입구로 들어 갔을때
                    self.level.stage_number = 1
                    text_flag[1] = True
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())

                if x.hitbox.colliderect(s1.rect) and stage_clear[1]: #스테이지 1 입구로 들어 갔을때
                    self.level.stage_number = 2
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())

                if x.hitbox.colliderect(s2.rect) and stage_clear[2]: #스테이지 2 입구로 들어 갔을때
                    self.level.stage_number = 3
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                
                if x.hitbox.colliderect(s3.rect) and stage_clear[3]: #스테이지 3 입구로 들어 갔을때
                    self.level.stage_number = 4
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())

                if x.hitbox.colliderect(s4.rect) and stage_clear[4]: #스테이지 4 입구로 들어 갔을때
                    self.level.stage_number = 5
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                
                if x.hitbox.colliderect(s5.rect) and stage_clear[5]: #스테이지 5 입구로 들어 갔을때
                    self.level.stage_number = 6
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())


            # 화면 업데이트
            pygame.display.update()


if __name__ == "__main__":
    game = GameManager()
    game.main_menu()