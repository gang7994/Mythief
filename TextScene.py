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
        self.clock = pygame.time.Clock()

    def draw_text(self, idx, screen):
        running = True
        text_idx = 0
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
                        if text_idx < len(self.texts[idx]) - 1:
                            text_idx += 1
                        else:
                            running = False
            score = self.font.render(self.texts[idx][text_idx], True, WHITE)
            screen.blit(score, (300, 600))
            screen.blit(support, (1200, 700))
            pygame.display.update()
