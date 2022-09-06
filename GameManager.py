import pygame, sys, os, time
from Settings import *
from Level import *
from Button import Button
from Button_text import Button_text
from Map import *
from ParticleEffect import Particle

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
        while True:
            dt = self.clock.tick(FPS)
            self.screen.fill(BLACK)
            bg_image = pygame.transform.scale(
                pygame.image.load(os.path.join(images_path, "mainBackGround.png")).convert_alpha(), (1456, 776))
            logo_image = pygame.transform.scale(
                pygame.image.load(os.path.join(images_path, "mainLogo.png")).convert_alpha(), (600, 200))
            self.screen.blits([(bg_image, (0, 0)), (logo_image, (428, 20))])
            MENU_MOUSE_POS = pygame.mouse.get_pos()

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

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.particle.click_flag = True
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.level = Level(0)
                            self.running = True
                            self.Run()
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
        pygame.draw.rect(self.screen, RED, (10, 15, self.level.player.current_hp / self.level.player.hp_ratio, 30))
        pygame.draw.rect(self.screen, WHITE, (10, 15, self.level.player.hp_bar_length, 30), 2)

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
            font = pygame.font.Font(None, 25)
            tap_key = font.render("Press Tap", True, WHITE)
            self.screen.blit(tap_key, (680, 690))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_TAB]:
                pygame.draw.rect(self.screen, YELLOW,
                                 (570, 710, self.level.player.current_item_gage / self.level.player.item_ratio, 10))
                pygame.draw.rect(self.screen, WHITE, (570, 710, self.level.player.item_bar_length, 10), 2)

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
        stage = self.level.map_idx + 1
        if stage == 4: text = font.render(f"[ EVENT ]", True, WHITE)
        elif stage == 8: text = font.render(f"[ EVENT ]", True, WHITE)
        else: text = font.render(f"[ STAGE: {stage} ]", True, WHITE)
        self.screen.blit(text, (660, 15))
        
    # 현재 스테이지 그림으로 표시
    def draw_current_stage(self, n):
        if n == 0:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage0.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==1:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage1.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==2:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage2.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==3:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage3.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==4:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage4.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==5:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage5.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==6:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage6.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==7:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage7.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==8:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage8.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
        elif n ==9:
            self.stage = pygame.transform.scale(pygame.image.load(os.path.join(images_path, "stage9.png")).convert_alpha(), (1150, 70))
            self.screen.blit(self.stage, (153, 70))
            
    def show_info(self):
        font = pygame.font.Font(None, 25)
        pos = font.render(f"Player_pos: {self.level.player.rect.centerx, self.level.player.rect.centery,}", True, WHITE)
        remain_monster = font.render(f"Remaining_Monster: {self.level.remain_monster}", True, WHITE) # Show_info로 주석표기
        fps = font.render(f"FPS: {str(int(self.clock.get_fps()))}", True, WHITE)
        self.screen.blits([(pos, (10, 560)),(remain_monster, (10, 590)), (fps, (10, 620))])
        
    def show_inventory(self):
        pygame.draw.circle(self.screen, GREY, (150, 710), 40)
        pygame.draw.circle(self.screen, GREY, (270, 710), 40)
        pygame.draw.circle(self.screen, GREY, (390, 710), 40)
        pygame.draw.circle(self.screen, GREY, (510, 710), 40)
        for i, item in enumerate(inventory):
            if item.name == "test0_item":
                image_rect = item.image.get_rect(center=(150+i*120, 710))
                self.screen.blit(item.image, image_rect)
            elif item.name == "test1_item":
                image_rect = item.image.get_rect(center=(150+i*120, 710))
                self.screen.blit(item.image, image_rect)
            i+= 120
        

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
    
    # 게임 로직
    def Run(self):
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

            # 이미지 영역
            self.screen.fill(BLACK)
            self.level.run()
            self.draw_frame()
            self.draw_rock_count()
            self.draw_rock_image()
            self.draw_rock_cool_time()
            self.draw_hp()
            self.current_stage()
            self.draw_current_stage(self.level.map_idx)
            self.show_dir()
            self.show_info()
            self.item_interaction_text()
            self.show_inventory()
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

            if self.level.glow.dead_rad <= 0:
                self.dead_surface(PAUSE_MOUSE_POS)
            self.particle.click_effect(self.screen, PAUSE_MOUSE_POS[0], PAUSE_MOUSE_POS[1], dt)

            # 게임 클리어 영역
            x = self.level.get_player()
            y = self.level.get_finish()
            if x.hitbox.colliderect(y.rect):
                if self.level.map_idx < len(map) - 1:
                    Level.remain_monster = 0 # Show_info
                    self.level = Level(self.level.map_idx + 1)
                else:
                    self.clear(int(elapse_time))

            # 화면 업데이트
            pygame.display.update()


if __name__ == "__main__":
    game = GameManager()
    game.main_menu()