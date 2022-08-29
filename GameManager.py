import pygame, sys, os, time
from Settings import *
from Level import *
from Button import Button

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("proto")
        self.clock = pygame.time.Clock()
        self.total_time = 0
        self.total_rock_count = 0
        self.total_score = 0
        self.running = True
        self.level = Level(0)

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
        self.screen.blit(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (10, 270))
        pygame.draw.rect(self.screen, WHITE, (5.5, 265.5, 32, 32), 2)

    def draw_frame(self):
        pygame.draw.rect(self.screen, BLACK, (0,0,1456,776), 150)
        pygame.draw.rect(self.screen, WHITE, (150, 150, 1156, 476), 1)

    # 무기 쿨타임 그리기
    def draw_rock_cool_time(self):
        if self.level.player.current_time != 0 and self.level.player.rock_time != 0:
            if self.level.player.current_time - self.level.player.rock_time <= self.level.player.rock_cool_time:
                pygame.draw.rect(self.screen,
                                 BLACK,
                                 (5.5, 265.5, 32,
                                  32 - (self.level.player.current_time - self.level.player.rock_time) / 22))

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
        self.screen.blits([(pos, (10, 660)),(remain_monster, (10, 690)), (fps, (10, 720))])

    # 게임 로직
    def Run(self):
        # 프레임 영역
        self.start_time = pygame.time.get_ticks()
        # 메인 로직 영역
        while self.running:
            self.clock.tick(FPS)
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()
            if not self.level.is_pause:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "pause1.png")).convert_alpha(), 
                                pos=(1390,35), scale_x=50, scale_y=50)
            else:
                PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause2.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "pause3.png")).convert_alpha(), 
                                pos=(1390,35), scale_x=50, scale_y=50)
            PAUSE.changeColor(PAUSE_MOUSE_POS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if PAUSE.checkForInput(PAUSE_MOUSE_POS) and not self.level.is_pause:
                        self.level.pause("T")
                    elif PAUSE.checkForInput(PAUSE_MOUSE_POS) and self.level.is_pause:
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
            self.show_info()
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
                
            # 게임 클리어 영역
            x = self.level.get_player()
            y = self.level.get_finish()
            if x.rect.colliderect(y.rect):
                if self.level.map_idx < len(map) - 1:
                    Level.remain_monster = 0 # Show_info
                    self.level = Level(self.level.map_idx + 1)
                else:
                    self.clear(int(elapse_time))

            # 화면 업데이트
            pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = GameManager()
    game.Run()