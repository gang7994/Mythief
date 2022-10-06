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
        pygame.display.set_caption("Mythief")
        self.clock = pygame.time.Clock()
        self.particle = Particle()
        self.total_time = 0
        self.total_rock_count = 0
        self.running = True
        self.level = None
        self.use_rope = False
        self.text = TextManager(0)
        self.is_opening = False
        self.interaction_UI = pygame.image.load(os.path.join(images_path, "interaction_UI.png")).convert_alpha()
        self.item_cover = pygame.image.load(os.path.join(item_path, "item_cover.png")).convert_alpha()
        self.finish = False

    def Option(self):  # 옵션창
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
                                       text_input="BACK", font=self.get_font(60), base_color="White",
                                       hovering_color="Red")

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
                pygame.mixer.Channel(0).stop()
                pygame.mixer.Channel(2).stop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.sound_click()
                        running = False
                    if BGM_UP.checkForInput(OPTIONS_MOUSE_POS):
                        self.sound_click()
                        if bgm_vol != 100:
                            bgm_vol += 10
                    if BGM_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        self.sound_click()
                        if bgm_vol != 0:
                            bgm_vol -= 10
                    if EFFECT_UP.checkForInput(OPTIONS_MOUSE_POS):
                        self.sound_click()
                        if effect_vol != 100:
                            effect_vol += 10
                    if EFFECT_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        self.sound_click()
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

    def get_font(self, size):
        return pygame.font.SysFont('malgungothic', size)

    def main_menu(self):
        global rope_item, current_hp, max_hp, half_hp_count, stage_clear
        while True:
            dt = self.clock.tick(FPS)
            if not pygame.mixer.Channel(0).get_busy():
                bgm_sound.set_volume(bgm_vol / 200)
                pygame.mixer.Channel(0).play(bgm_sound)
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
                                 pos=(728, 340), scale_x=400, scale_y=100)
            OPTION_BUTTON = Button(
                image0=pygame.image.load(os.path.join(images_path, "btn_option0.png")).convert_alpha(),
                image1=pygame.image.load(os.path.join(images_path, "btn_option1.png")).convert_alpha(),
                pos=(728, 480), scale_x=400, scale_y=100)
            QUIT_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_exit_0.png")).convert_alpha(),
                                 image1=pygame.image.load(os.path.join(images_path, "btn_exit_1.png")).convert_alpha(),
                                 pos=(728, 620), scale_x=400, scale_y=100)

            for button in [PLAY_BUTTON, OPTION_BUTTON, QUIT_BUTTON]:
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
                            self.sound_click()
                            if not self.is_opening:
                                self.text.draw_text(0, self.screen)
                                self.is_opening = True
                            self.level = Level(0, 0, 0, pygame.time.get_ticks())
                            self.running = True
                            self.Run()
                            # 초기화
                            half_hp_count = 0
                            max_hp = 100
                            current_hp = max_hp
                            general_inventory.clear()
                            rope_item = 2
                            for i in range(1, 6):
                                stage_clear[i] = False
                            stage_clear[0] = True
                            for i in range(5):
                                theme_clear[i] = False
                            print(stage_clear)
                            self.general_item_effect_clear()

                        if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.sound_click()
                            self.Option()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.sound_click()
                            time.sleep(0.1)
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.particle.click_flag = True
                if MAINMENU.checkForInput(mouse_pos):
                    self.sound_click()
                    self.running = False
        self.particle.mouse_cursor(self.screen, mouse_pos[0], mouse_pos[1])

    # 체력 그리기
    def draw_hp(self):
        pygame.draw.rect(self.screen, RED, (10, 15, current_hp / (max_hp / hp_bar_length), 30))
        pygame.draw.rect(self.screen, WHITE, (10, 15, hp_bar_length, 30), 2)

    # 무기 이미지 그리기
    def draw_rock_image(self):
        self.screen.blit(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (1330, 400))
        pygame.draw.rect(self.screen, WHITE, (1325.5, 395.5, 32, 32), 2)

    def draw_frame(self):
        pygame.draw.rect(self.screen, BLACK, (0, 0, 1456, 776), 150)
        pygame.draw.rect(self.screen, WHITE, (150, 150, 1156, 476), 1)

    def item_interaction_text(self):
        if self.level.player.item_interaction:
            font = pygame.font.Font(os.path.join(font_path, resource_path("Font\Mabinogi.ttf")), 20)
            tap_key = font.render("Tab을 누르시오", True, BLACK)
            txt_w, txt_h = tap_key.get_size()
            self.screen.blit(self.interaction_UI, (screen_width // 2 - 149 // 2, screen_height // 2 - 75))
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
        font = pygame.font.Font(os.path.join(font_path, resource_path("Font\Mabinogi.ttf")), 30)
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
    def clear(self):
        running = True
        while running:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.mixer.Channel(1).get_busy(): pygame.mixer.Channel(1).stop()
            item_score = 0
            time_score = 0
            hp_score = half_hp_count * 200
            for i in general_inventory:  # 테마 유물 아이템 개당 700점
                if i[1] >= 6: item_score += 700
            if 1400 - time_record > 0:
                time_score = int(1400 - time_record) * 25

            MAINMENU = Button(image0=pygame.image.load(os.path.join(images_path, "exit_icon.png")).convert_alpha(),
                              image1=pygame.image.load(os.path.join(images_path, "exit_icon2.png")).convert_alpha(),
                              pos=(1200, 650), scale_x=200, scale_y=200)
            title_font = pygame.font.Font(os.path.join(font_path, resource_path("Font\Mabinogi.ttf")), 100)
            game_font = pygame.font.Font(os.path.join(font_path, resource_path("Font\Mabinogi.ttf")), 70)

            total = time_score + 15000 + bonus + item_score + hp_score
            msg0 = title_font.render(f"[ Your Score ]", True, WHITE)
            msg0_rect = msg0.get_rect(center=(screen_width / 2, screen_height / 2 - 290))
            msg1 = game_font.render(f"클리어 타임 : {time_score}", True, WHITE)
            msg1_rect = msg1.get_rect(center=(screen_width / 2, screen_height / 2 - 190))
            msg2 = game_font.render(f"테마유물 : 15000", True, WHITE)  # 테마유물 점수
            msg2_rect = msg2.get_rect(center=(screen_width / 2, screen_height / 2 - 90))
            msg3 = game_font.render(f"보너스 : {bonus}", True, WHITE)  # 추가 점수 오브젝트
            msg3_rect = msg3.get_rect(center=(screen_width / 2, screen_height / 2 + 10))
            msg4 = game_font.render(f"일반유물 : {item_score}", True, WHITE)  # 유물 개수
            msg4_rect = msg4.get_rect(center=(screen_width / 2, screen_height / 2 + 110))
            msg5 = game_font.render(f"체력 : {hp_score}", True, WHITE)  # 유물 개수
            msg5_rect = msg5.get_rect(center=(screen_width / 2, screen_height / 2 + 210))

            msg = game_font.render(f"TOTAL : {total}", True, WHITE)  # 총합
            msg_rect = msg.get_rect(center=(screen_width / 2, screen_height / 2 + 310))
            self.screen.fill(BLACK)
            self.screen.blits(
                [(msg0, msg0_rect), (msg1, msg1_rect), (msg2, msg2_rect), (msg3, msg3_rect), (msg4, msg4_rect),
                 (msg5, msg5_rect), (msg, msg_rect)])
            MAINMENU.changeColor(mouse_pos)
            MAINMENU.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.particle.click_flag = True
                    if MAINMENU.checkForInput(mouse_pos):
                        self.sound_click()
                        if total >= 32600:
                            self.text.draw_text(7, self.screen)  # happy end
                        elif total >= 24100:
                            self.text.draw_text(8, self.screen)  # normal end
                        else:
                            self.text.draw_text(9, self.screen)  # bad end
                        running = False
            self.particle.mouse_cursor(self.screen, mouse_pos[0], mouse_pos[1])
            pygame.display.update()
        self.running = False

    # 현재 스테이지 글자로 표시
    def current_stage(self):
        font = pygame.font.Font(None, 40)
        stage = self.level.stage_number
        map_num = self.level.map_idx + 1
        if stage == 0:
            text = font.render(f"[ MAIN ]", True, WHITE)
        elif stage == 1:
            text = font.render(f"[ TUTORIAL ]", True, WHITE)
        elif stage == 2:
            text = font.render(f"[ STAGE 1 - {map_num}]", True, WHITE)
        elif stage == 3:
            text = font.render(f"[ STAGE 2 - {map_num}]", True, WHITE)
        elif stage == 4:
            text = font.render(f"[ STAGE 3 - {map_num}]", True, WHITE)
        elif stage == 5:
            text = font.render(f"[ STAGE 4 - {map_num}]", True, WHITE)
        elif stage == 6:
            text = font.render(f"[ STAGE 5 - {map_num}]", True, WHITE)
        self.screen.blit(text, (640, 15))

    def show_general_inventory(self):
        for i in range(12):
            pygame.draw.circle(self.screen, GREY, (150 + i * 105, 100), 40)
        for i, item in enumerate(general_inventory):
            if item[0].name == "general_item0":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item0.png")).convert_alpha()
            elif item[0].name == "general_item1":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item1.png")).convert_alpha()
            elif item[0].name == "general_item2":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item2.png")).convert_alpha()
            elif item[0].name == "general_item3":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item3.png")).convert_alpha()
            elif item[0].name == "general_item4":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item4.png")).convert_alpha()
            elif item[0].name == "general_item5":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item5.png")).convert_alpha()
            elif item[0].name == "general_item6":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item6.png")).convert_alpha()
            elif item[0].name == "general_item7":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item7.png")).convert_alpha()
            elif item[0].name == "general_item8":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item8.png")).convert_alpha()
            elif item[0].name == "general_item9":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item9.png")).convert_alpha()
            elif item[0].name == "general_item10":
                item[0].image = pygame.image.load(os.path.join(item_path, "general_item10.png")).convert_alpha()
            image_rect = item[0].image.get_rect(center=(150 + i * 105, 100))
            self.screen.blit(item[0].image, image_rect)
            self.item_cover = pygame.image.load(os.path.join(item_path, "item_cover.png")).convert_alpha()
            if item[1] == -1:
                self.item_cover = pygame.transform.scale(self.item_cover, (45, 45))
            elif item[1] == 7:
                self.item_cover = pygame.transform.scale(self.item_cover, (45, 45))
            else:
                self.item_cover = pygame.transform.scale(self.item_cover, (45, 45 - item[1] * 7.5))
            self.item_cover.set_alpha(200)
            self.screen.blit(self.item_cover, (130 + i * 105, 78))

    def show_theme_inventory(self):
        pygame.draw.circle(self.screen, GREY, (45, 710), 40)
        pygame.draw.circle(self.screen, GREY, (165, 710), 40)
        pygame.draw.circle(self.screen, GREY, (285, 710), 40)
        pygame.draw.circle(self.screen, GREY, (405, 710), 40)
        pygame.draw.circle(self.screen, GREY, (525, 710), 40)
        for i, item in enumerate(theme_inventory):
            if item == "Them_1.png" and theme_clear[0]:
                image = pygame.image.load(os.path.join(item_path, "Them_1.png")).convert_alpha()
                image_rect = image.get_rect(center=(45 + i * 120, 710))
                self.screen.blit(image, image_rect)
            elif item == "Them_2.png" and theme_clear[1]:
                image = pygame.image.load(os.path.join(item_path, "Them_2.png")).convert_alpha()
                image_rect = image.get_rect(center=(45 + i * 120, 710))
                self.screen.blit(image, image_rect)
            elif item == "Them_3.png" and theme_clear[2]:
                image = pygame.image.load(os.path.join(item_path, "Them_3.png")).convert_alpha()
                image_rect = image.get_rect(center=(45 + i * 120, 710))
                self.screen.blit(image, image_rect)
            elif item == "Them_4.png" and theme_clear[3]:
                image = pygame.image.load(os.path.join(item_path, "Them_4.png")).convert_alpha()
                image_rect = image.get_rect(center=(45 + i * 120, 710))
                self.screen.blit(image, image_rect)
            elif item == "Them_5.png" and theme_clear[4]:
                image = pygame.image.load(os.path.join(item_path, "Them_5.png")).convert_alpha()
                image_rect = image.get_rect(center=(45 + i * 120, 710))
                self.screen.blit(image, image_rect)

    def show_item(self):
        game_font = pygame.font.Font(None, 30)
        pygame.draw.circle(self.screen, GREY, (1370, 480), 40)  # 기믹아이템
        pygame.draw.circle(self.screen, GREY, (1370, 600), 40)  # 패스권
        if self.level.player.is_hadesHelmet:
            item = pygame.image.load(os.path.join(item_path, "hadesHelmet.png")).convert_alpha()
            item_rect = item.get_rect(center=(1370, 480))
            self.screen.blit(item, item_rect)
        elif self.level.stage_number == 5:
            rod = pygame.image.load(os.path.join(item_path, "rod_0.png")).convert_alpha()
            rod_rect = rod.get_rect(center=(1370, 470))
            rod_count = game_font.render(f"{5 - self.level.player.rod_num}/5", True, WHITE)
            self.screen.blits([(rod, rod_rect), (rod_count, (1355, 490))])
        image = pygame.image.load(os.path.join(item_path, "general_item0.png")).convert_alpha()
        image_rect = image.get_rect(center=(1370, 590))

        rope_count = game_font.render(f"{rope_item}/2", True, WHITE)
        self.screen.blits([(image, image_rect), (rope_count, (1355, 610))])
        self.screen.blit(
            pygame.transform.scale(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (50, 50)),
            (1345, 690))
        pygame.draw.rect(self.screen, WHITE, (1341, 690, 55, 55), 2)
        if self.level.player.current_time != 0 and self.level.player.rock_time != 0:
            if self.level.player.current_time - self.level.player.rock_time <= self.level.player.rock_cool_time:
                pygame.draw.rect(self.screen, BLACK, (1341, 690, 55, 55 - (
                            self.level.player.current_time - self.level.player.rock_time) / (
                                                                  self.level.player.rock_cool_time / 55)))

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
        global rope_item, max_hp, shield, bonus, use_item0, use_item1, use_item2, use_item3, use_item4, use_item5, use_item6, use_item7, use_item8, use_item9, use_item10
        for tmp in general_inventory:

            if tmp[1] == 6:
                if tmp[0].name == "general_item0" and not use_item0:  # 로프 1개 추가
                    rope_item += 1
                    use_item0 = True
                elif tmp[0].name == "general_item1":  # 플레이어 이동 속도 증가
                    self.level.player.player_speed_x += 1
                    self.level.player.player_speed_y += 1
                    use_item1 = True
                elif tmp[0].name == "general_item2" and not use_item2:  # 최대 체력 증가
                    max_hp += 30
                    use_item2 = True
                elif tmp[0].name == "general_item3" and not use_item3:  # 스테이지 마다 2회방어
                    shield = 2
                    use_item3 = True
                elif tmp[0].name == "general_item4" and not use_item4:  # 로프 1개 감소
                    if rope_item > 0:
                        rope_item -= 1
                    use_item4 = True
                elif tmp[0].name == "general_item5" and not use_item5:  # 고대주화
                    bonus += 1000
                    use_item5 = True
                elif tmp[0].name == "general_item6":  # 회중시계
                    try:
                        for tmp in self.level.monsterlist:
                            tmp.monster_speed -= 1
                    except AttributeError as e:
                        pass
                    use_item6 = True
                elif tmp[0].name == "general_item7":  # 평평한 돌
                    self.level.player.rock_item_effect = True
                    use_item7 = True
                elif tmp[0].name == "general_item8":  # 이상한 석상
                    self.level.player.is_effect0 = True
                    use_item8 = True
                elif tmp[0].name == "general_item9":  # 미믹 [비활성화 토의필요]
                    self.level.player.ignore_item = True
                    use_item9 = True
                elif tmp[0].name == "general_item10":  # 대나무 낚싯대
                    self.level.player.is_effect1 = True
                    use_item10 = True

    def general_item_effect_clear(self):
        global rope_item, max_hp, shield, bonus, use_item0, use_item1, use_item2, use_item3, use_item4, use_item5, use_item6, use_item7, use_item8, use_item9, use_item10
        if use_item0:
            rope_item = 2
            use_item0 = False
        if use_item1:
            use_item1 = False
        if use_item2:
            max_hp = 100
            use_item2 = False
        if use_item3:
            shield = 0
            use_item3 = False
        if use_item4:
            rope_item = 2
            use_item4 = False
        if use_item5:
            bonus = 0
            use_item5 = False
        if use_item6:
            use_item6 = False
        if use_item7:
            self.level.player.rock_item_effect = False
            use_item7 = False
        if use_item8:
            self.level.player.is_effect0 = False
            use_item8 = False
        if use_item9:
            self.level.player.ignore_item = False
            use_item9 = False
        if use_item10:
            self.level.player.is_effect1 = False
            use_item10 = False

    def player_hp(self):
        global current_hp, shield
        if current_hp > 0:
            if self.level.player.is_damage2 and shield == 0:
                current_hp -= 2
                self.level.player.is_damage2 = False
            if self.level.player.is_damage5 and shield == 0:
                current_hp -= 5
                self.level.player.is_damage5 = False
            if self.level.player.is_damage10 and shield == 0:
                current_hp -= 10
                self.level.player.is_damage10 = False
            if self.level.player.is_damage30 and shield == 0:
                current_hp -= 30
                self.level.player.is_damage30 = False
            elif (
                    self.level.player.is_damage2 or self.level.player.is_damage5 or self.level.player.is_damage10 or self.level.player.is_damage30) and shield != 0:
                shield -= 1
                self.level.player.is_damage2 = False
                self.level.player.is_damage5 = False
                self.level.player.is_damage10 = False
                self.level.player.is_damage30 = False
        else:
            current_hp = 0
            self.level.player.is_dead = True

    def player_hp_recovery(self):
        global current_hp
        if current_hp + 10 > max_hp:
            current_hp = max_hp
        else:
            current_hp += 10

    def player_event_hp_get(self):
        global current_hp, max_hp
        if self.level.player.player_get_hp:
            if current_hp + 50 > max_hp:
                current_hp = max_hp
            else:
                current_hp += 50
            self.level.player.player_get_hp = False

    def player_event_hp_loss(self):
        global current_hp, max_hp
        if self.level.player.player_loss_hp:
            if current_hp - 30 <= 0:
                current_hp = 1
            else:
                current_hp -= 30
            self.level.player.player_loss_hp = False

    def player_event_max_hp(self):
        global current_hp, max_hp
        if self.level.player.player_loss_max_hp:
            max_hp -= 30
            current_hp = max_hp
            self.level.player.player_loss_max_hp = False

        if self.level.player.player_get_max_hp:
            max_hp += 30
            if current_hp - 20 > 0:
                current_hp -= 20
            else:
                current_hp = 1
            self.level.player.player_get_max_hp = False

    def get_bonus_score(self):
        global bonus
        if self.level.player.bonus_flag:
            bonus += 200
            self.level.player.bonus_flag = False

    def sound_click(self):
        click_sound.set_volume(effect_vol / 100)
        click_sound.play()

    def sound_setting(self):
        self.level.player.effect_vol = effect_vol
        self.level.effect_vol = effect_vol

    # 게임 로직
    def Run(self):
        global rope_item, shield, max_hp, current_hp, half_hp_count, time_record
        # 프레임 영역
        self.start_time = pygame.time.get_ticks()
        # 메인 로직 영역
        while self.running:
            if not pygame.mixer.Channel(0).get_busy():
                bgm_sound.set_volume(bgm_vol / 200)
                pygame.mixer.Channel(0).play(bgm_sound)
            dt = self.clock.tick(FPS)
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()
            if not self.level.is_pause:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause0.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "pause1.png")).convert_alpha(),
                               pos=(1390, 35), scale_x=50, scale_y=50)
                SETTING = Button(
                    image0=pygame.image.load(os.path.join(images_path, "setting_icon.png")).convert_alpha(),
                    image1=pygame.image.load(os.path.join(images_path, "setting_icon2.png")).convert_alpha(),
                    pos=(740, 380), scale_x=200, scale_y=200)
                EXIT = Button(image0=pygame.image.load(os.path.join(images_path, "exit_icon.png")).convert_alpha(),
                              image1=pygame.image.load(os.path.join(images_path, "exit_icon2.png")).convert_alpha(),
                              pos=(1140, 380), scale_x=300, scale_y=300)
            else:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause2.png")).convert_alpha(),
                               image1=pygame.image.load(os.path.join(images_path, "pause3.png")).convert_alpha(),
                               pos=(340, 380), scale_x=200, scale_y=200)
                SETTING = Button(
                    image0=pygame.image.load(os.path.join(images_path, "setting_icon.png")).convert_alpha(),
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
                        self.sound_click()
                        self.level.pause("T")
                    elif PAUSE.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.sound_click()
                        self.level.pause("F")
                    if SETTING.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.sound_click()
                        self.Option()
                    if EXIT.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
                        self.sound_click()
                        self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not self.level.is_pause:
                        self.level.pause("T")
                    elif event.key == pygame.K_ESCAPE and self.level.is_pause:
                        self.level.pause("F")
                    if event.key == pygame.K_r and self.level.stage_number != 0:
                        if rope_item != 0 and not self.use_rope:
                            if self.level.stage_number == 0:
                                pass
                            elif self.level.stage_number == 1:
                                if self.level.map_idx == 3:
                                    use_sound.set_volume(effect_vol / 100)
                                    use_sound.play()
                                    rope_item -= 1
                                    self.use_rope = True
                            elif self.level.stage_number == 2 or self.level.stage_number == 5:
                                if not (self.level.map_idx == 3 or self.level.map_idx == 7 or self.level.map_idx == 8):
                                    use_sound.set_volume(effect_vol / 100)
                                    use_sound.play()
                                    rope_item -= 1
                                    self.use_rope = True
                            elif self.level.stage_number == 3 or self.level.stage_number == 4:
                                if not (self.level.map_idx == 3 or self.level.map_idx == 7 or self.level.map_idx == 8):
                                    use_sound.set_volume(effect_vol / 100)
                                    use_sound.play()
                                    rope_item -= 1
                                    self.use_rope = True

                    if event.key == pygame.K_f:
                        if not text_flag[self.level.stage_number + 1]:
                            if len(self.level.text.texts[self.level.map_idx]) != 0:
                                if self.level.text.text_idx < len(self.level.text.texts[self.level.map_idx]) - 1:
                                    self.level.text.text_idx += 1
                                else:
                                    self.level.text.ui_flag = False
                        if self.level.player.event_handler:
                            if self.level.text.event_text_idx < len(self.level.text.event_texts) - 1:
                                self.level.text.event_text_idx += 1
                            else:
                                self.level.player.event_handler = False
                                self.level.text.event_text_idx = 0

            # 이미지 영역
            self.screen.fill(BLACK)
            self.level.run()
            self.draw_frame()  # 게임화면에서 테투리를 그리는 함수
            self.show_item()  # 오른쪽 하단의 기믹아이템, 로프(패스권), 돌 쿨타임을 화면에 보여주는 함수
            self.player_hp()  # 캐릭터의 체력을 계산해주는 함수
            self.draw_hp()  # 캐릭터의 체력을 화면에 보여주는 함수
            self.current_stage()  # 현재 캐릭터가 있는 스테이지와 맵의 번호를 보여주는 함수
            self.show_general_inventory()  # 획득한 일반 유물 아이템을 보여주는 함수
            self.general_item_effect()  # 획득한 일반 유물 아이템 조각 6개가 모이면 각 효과에 맞게 실행시켜주는 함수
            self.show_dir()  # 캐릭터가 보고 있는 방향을 화살표로 알려주는 함수f
            self.item_interaction_text()  # 아이템 근처에 갔을 경우 상호작용 할 수 있는 함수
            self.door_interaction_text()  # 스테이지 입구 문 근처에 갔을 경우 스테이지 명을 보여주는 함수
            self.show_theme_inventory()  # 테마 유물 아이템을 보여주는 인벤토리
            self.sound_setting()  # 조절한 소리 값으로 모든 소리크기 변수를 바꿔주는 함수
            # player_get_event
            self.player_event_hp_loss()  # 이벤트 맵의 결과에 따라 캐릭터 체력 30을 잃게 만드는 함수
            self.player_event_hp_get()  # 이벤트 맵의 결과에 따라 캐릭터 체력 50을 회복하게 만드는 함수
            self.player_event_max_hp()  # 이벤트 맵의 결과에 따라 캐릭터 최대 체력이 변경되게 하는 함수
            # player_bonus
            self.get_bonus_score()  # 보너스 아이템을 먹었을 때 보너스 점수 100을 더하는 함수

            if not text_flag[self.level.stage_number + 1] and len(
                    self.level.text.texts[self.level.map_idx]):  # 해당스테이지와 맵에 맞는 텍스트를 보여줌
                self.level.text.draw_ui_text(self.level.text_idx, self.screen)  # 자동으로 생성되는 텍스트(한번 봤으면 다시 못봄)
            if self.level.player.event_handler:
                if self.level.player.event_code is not None:
                    self.level.text.draw_event_text(self.screen, self.level.player.event_code)
            PAUSE.update(self.screen)

            if not self.level.is_pause:
                self.tem_now_time = pygame.time.get_ticks() - self.start_time
                elapse_time = (self.tem_now_time) / 1000

            else:
                self.start_time = pygame.time.get_ticks() - self.tem_now_time
                elapse_time = (self.tem_now_time) / 1000

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

            if self.level.stage_number == 0 and self.finish:
                self.level.finish.image = pygame.image.load(os.path.join(images_path, "wall_door1.png")).convert_alpha()
                self.level.finish.name = "Finish"

            # 게임 클리어 영역
            x = self.level.get_player()  # 캐릭터
            y = self.level.get_finish()  # Finish 타일

            if self.use_rope:
                if self.level.map_idx < len(map[self.level.stage_number]) - 1:  # 다음 방이 있다면 넘어가기
                    if max_hp / 2 <= current_hp and not (
                            self.level.map_idx == 3 or self.level.map_idx == 7): half_hp_count += 1
                    time_record += (pygame.time.get_ticks() - self.level.start_time) / 1000
                    self.level = Level(self.level.text_idx + 1, self.level.stage_number, self.level.map_idx + 1,
                                       pygame.time.get_ticks())
                    self.player_hp_recovery()
                self.use_rope = False
            if x.hitbox.colliderect(y.rect):
                if not self.finish:
                    time_record += (pygame.time.get_ticks() - self.level.start_time) / 1000
                if self.level.map_idx < len(map[self.level.stage_number]) - 1:  # 다음 방이 있다면 넘어가기
                    self.level.remain_monster = 0
                    if max_hp / 2 <= current_hp and not (
                            self.level.map_idx == 3 or self.level.map_idx == 7): half_hp_count += 1
                    self.level = Level(self.level.text_idx + 1, self.level.stage_number, self.level.map_idx + 1,
                                       pygame.time.get_ticks())
                    self.player_hp_recovery()
                else:  # 다음 방이 없으면 메인 스테이지로 넘어가기
                    if self.level.stage_number == 1:  # 튜토리얼 스테이지 마지막 방에서 나왔을때 초기화
                        general_inventory.clear()
                        rope_item = 2
                        max_hp = 100
                        current_hp = max_hp
                        time_record = 0

                    if self.level.stage_number == 5:  # 마지막 스테이지
                        self.finish = True
                        theme_clear[self.level.stage_number - 1] = True
                    if self.level.stage_number == 0 and self.finish:
                        self.clear()
                        self.text.draw_credit_text(10, self.screen)
                    else:
                        stage_clear[self.level.stage_number] = True
                        theme_clear[self.level.stage_number - 1] = True
                        stage_clear[self.level.stage_number - 1] = False

                        text_flag[self.level.stage_number + 1] = True
                        if max_hp / 2 <= current_hp and not (
                                self.level.map_idx == 3 or self.level.map_idx == 7): half_hp_count += 1
                        self.level = Level(0, 0, 0, pygame.time.get_ticks())
                        self.player_hp_recovery()
            if self.level.stage_number == 0:  # 메인 스테이지
                s0 = self.level.get_stage0()  # 스테이지 입구 타일
                s1 = self.level.get_stage1()
                s2 = self.level.get_stage2()
                s3 = self.level.get_stage3()
                s4 = self.level.get_stage4()
                if x.hitbox.colliderect(s0.rect) and stage_clear[0]:  # 튜토리얼 입구로 들어 갔을때
                    self.level.stage_number = 1
                    self.text.draw_text(1, self.screen)
                    text_flag[1] = True
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                if x.hitbox.colliderect(s1.rect) and stage_clear[1]:  # 스테이지 1 입구로 들어 갔을때
                    self.level.stage_number = 2
                    self.text.draw_text(2, self.screen)
                    if use_item3:
                        shield = 2
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                if x.hitbox.colliderect(s2.rect) and stage_clear[2]:  # 스테이지 2 입구로 들어 갔을때
                    self.level.stage_number = 3
                    self.text.draw_text(3, self.screen)
                    if use_item3:
                        shield = 2
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                if x.hitbox.colliderect(s3.rect) and stage_clear[3]:  # 스테이지 3 입구로 들어 갔을때
                    self.level.stage_number = 4
                    self.text.draw_text(4, self.screen)
                    if use_item3:
                        shield = 2
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
                if x.hitbox.colliderect(s4.rect) and stage_clear[4]:  # 스테이지 4 입구로 들어 갔을때
                    self.level.stage_number = 5
                    self.text.draw_text(5, self.screen)
                    if use_item3:
                        shield = 2
                    self.level = Level(0, self.level.stage_number, 0, pygame.time.get_ticks())
            # 화면 업데이트
            pygame.display.update()


if __name__ == "__main__":
    game = GameManager()
    game.main_menu()