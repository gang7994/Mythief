import pygame, os, sys
from Settings import *
from TextGroup import *

class TextManager:
    def __init__(self, texts_key):
        self.display_surface = pygame.display.get_surface()
        self.texts = texts[texts_key]
        self.event_texts = None
        self.max_idx = len(self.texts) - 1
        self.text_speed = text_speed
        self.scene_font = pygame.font.Font("Images/TestPix/Mabinogi_Classic_TTF.ttf", 25)
        self.ui_font = pygame.font.Font("Images/TestPix/Mabinogi_Classic_TTF.ttf", 20)
        self.text_ui = pygame.image.load(os.path.join(images_path, "text_UI.png")).convert_alpha()
        self.ui_flag = True
        self.event_ui_flag = True
        self.text_idx = 0
        self.event_text_idx = 0
        self.event_item_list = ["rotatingEXP_0.png", "rotatingEXP2_0.png", "rotatingEXP3_0.png"]
        self.event_item_image = None
        self.clock = pygame.time.Clock()

    def draw_text(self, idx, screen):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            screen.fill(BLACK)
            support = self.scene_font.render("F를 눌러 다음", True, WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        if self.text_idx < len(self.texts[idx]) - 1:
                            self.text_idx += 1
                        else:
                            running = False
            text = self.scene_font.render(self.texts[idx][self.text_idx], True, WHITE)
            screen.blit(text, (300, 600))
            screen.blit(support, (1200, 700))
            pygame.display.update()

    def draw_ui_text(self, idx, screen):
        if self.ui_flag:
            text = self.ui_font.render(self.texts[idx][self.text_idx], True, BLACK)
            support = self.ui_font.render("F를 눌러 다음", True, BLACK)
            screen.blit(self.text_ui, (570, 635))
            screen.blit(text, (585, 685))
            screen.blit(support,(1180, 725))

    def draw_event_text(self, screen, code):
        self.event_texts = event_texts[code]
        if self.event_ui_flag:
            text = self.ui_font.render(self.event_texts[self.event_text_idx], True, BLACK)
            support = self.ui_font.render("F를 눌러 다음", True, BLACK)
            screen.blit(self.text_ui, (570, 635))
            screen.blit(text, (585, 685))
            screen.blit(support,(1180, 725))
            if code == "000":
                self.event_item_image = pygame.image.load(os.path.join(item_path, self.event_item_list[self.event_text_idx])).convert_alpha()
                screen.blit(self.event_item_image, (575, 665))


