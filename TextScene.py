import pygame, os, sys
from Settings import *
from TextGroup import *

class TextManager:
    def __init__(self, texts_key):
        self.display_surface = pygame.display.get_surface()
        self.texts = texts[texts_key]
        self.max_idx = len(self.texts) - 1
        self.text_speed = text_speed
        self.font = pygame.font.Font("Images/TestPix/Mabinogi_Classic_TTF.ttf", 25)
        self.text_ui = pygame.image.load(os.path.join(images_path, "text_UI.png")).convert_alpha()
        self.ui_flag = True
        self.text_idx = 0
        self.clock = pygame.time.Clock()

    def draw_text(self, idx, screen):
        running = True
        while running:
            dt = self.clock.tick(FPS)
            screen.fill(BLACK)
            support = self.font.render("F를 눌러 다음", True, WHITE)
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
            text = self.font.render(self.texts[idx][self.text_idx], True, WHITE)
            screen.blit(text, (300, 600))
            screen.blit(support, (1200, 700))
            pygame.display.update()

    def draw_ui_text(self, idx, screen):
        if self.ui_flag:
            text = self.font.render(self.texts[idx][self.text_idx], True, BLACK)
            screen.blit(self.text_ui, (153, 425))
            screen.blit(text, (170, 510))

