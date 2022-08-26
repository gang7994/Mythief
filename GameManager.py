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
        self.is_pause = False
        self.level = Level(0)

    # 시간 재기
    def draw_time(self, elapse_time):
        font = pygame.font.Font(None, 40)
        timer = font.render("Time : {}".format(int(elapse_time)), True, WHITE)
        self.screen.blit(timer, (10, 10))

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
        font = pygame.font.Font(None, 40)
        score = font.render("Score : {}".format(int(total_score)), True, WHITE)
        self.screen.blit(score, (10, 45))

    # 돌 던진 횟수 그리기
    def draw_rock_count(self):
        font = pygame.font.Font(None, 40)
        score = font.render("Rock Count : {}".format(int(self.level.player.rock_count)), True, WHITE)
        self.screen.blit(score, (10, 80))

    # 체력 그리기
    def draw_hp(self):
        pygame.draw.rect(self.screen, RED, (10, 115, self.level.player.current_hp / self.level.player.hp_ratio, 15))
        pygame.draw.rect(self.screen, WHITE, (10, 115, self.level.player.hp_bar_length, 15), 2)

    # 무기 이미지 그리기
    def draw_rock_image(self):
        self.screen.blit(pygame.image.load(os.path.join(images_path, "rock.png")).convert_alpha(), (10, 150))
        pygame.draw.rect(self.screen, WHITE, (5.5, 145.5, 32, 32), 2)

    # 무기 쿨타임 그리기
    def draw_rock_cool_time(self):
        if self.level.player.current_time != 0 and self.level.player.rock_time != 0:
            if self.level.player.current_time - self.level.player.rock_time <= self.level.player.rock_cool_time:
                pygame.draw.rect(self.screen,
                                 BLACK,
                                 (5.5, 145.5, 32,
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

    def pause(self):
        print("stop")
        self.is_pause = True
        return self.is_pause
    
    def show_info(self):
        font = pygame.font.Font(None, 20)
        pos = font.render(f"Player_pos: {self.level.player.rect.centerx, self.level.player.rect.centery,}", True, WHITE)
        remain_monster = font.render(f"Remaining_Monster: {self.level.remain_monster}", True, WHITE) # Show_info로 주석표기
        self.screen.blit(pos, (10, 700))
        self.screen.blit(remain_monster, (10, 710))
    
    # 게임 로직
    def Run(self):
        # 프레임 영역
        start_time = pygame.time.get_ticks()
        # 메인 로직 영역
        while self.running:
            self.clock.tick(FPS)
            PAUSE_MOUSE_POS = pygame.mouse.get_pos()
            PAUSE = Button(image0=pygame.image.load(os.path.join(images_path, "pause0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "pause1.png")).convert_alpha(), 
                                pos=(1390,50), scale_x=50, scale_y=50)
            PAUSE.changeColor(PAUSE_MOUSE_POS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if PAUSE.checkForInput(PAUSE_MOUSE_POS) and not self.is_pause:
                        self.pause()
                    elif PAUSE.checkForInput(PAUSE_MOUSE_POS) and self.is_pause:
                        self.is_pause = False
    
            # 이미지 영역
            self.screen.fill(BLACK)
            self.level.run()
            self.draw_rock_count()
            self.draw_rock_image()
            self.draw_rock_cool_time()
            self.draw_hp()
            PAUSE.update(self.screen)
            self.show_info()
            elapse_time = (pygame.time.get_ticks() - start_time) / 1000
            self.draw_time(elapse_time)
            self.draw_score(self.total_score)
            if self.is_pause:
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