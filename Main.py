from lib2to3.pgen2.token import OP
import pygame, sys
from Button import Button
from Settings import *
import GameManager

class Encyclopedia:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Enc")
    def Encyclopedia(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_font(45).render("백과사전창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button(image=None, pos=(1300, 0), 
                                text_input="BACK", font = get_font(60), base_color="White", hovering_color="Red")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
            pygame.display.update()

class Credit:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Cre")
    def Credit(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_font(45).render("크레딧창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.popup = pygame.transform.scale(self.popup, (800, 650))
            self.screen.blit(self.popup, (328, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button(image=None, pos=(1300, 0), 
                                text_input="BACK", font=get_font(60), base_color="White", hovering_color="Red")
            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
            pygame.display.update()
            
class Option:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Cre")
    def Option(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_font(45).render("옵션창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button(image=None, pos=(1300, 0), 
                                text_input="BACK", font=get_font(60), base_color="White", hovering_color="Red")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
            pygame.display.update()


pygame.init()
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")
Enc = Encyclopedia()
Cre = Credit()
Opt = Option()

def get_titlefont(size): 
    return pygame.font.Font("Images/TestPix/font.ttf", size)

def get_font(size): 
    return pygame.font.SysFont('malgungothic', size)

def Play():
    game = GameManager.GameManager()
    game.Run()

def main_menu():
    SCREEN.fill(BLACK)
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_titlefont(100).render("Mythief", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(topleft=(80, 80))

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(images_path, "Button.png")).convert_alpha(), pos=(80, 200), 
                            text_input="게임시작", font=get_font(60), base_color="Black", hovering_color="White")
        ENCYCLOPEDIA_BUTTON = Button(image=pygame.image.load(os.path.join(images_path, "Button.png")).convert_alpha(), pos=(80, 310), 
                            text_input="백과사전", font=get_font(60), base_color="Black", hovering_color="White")
        CREDIT_BUTTON = Button(image=pygame.image.load(os.path.join(images_path, "Button.png")).convert_alpha(), pos=(80, 420), 
                            text_input="크레딧", font=get_font(60), base_color="Black", hovering_color="White")
        OPTION_BUTTON = Button(image=pygame.image.load(os.path.join(images_path, "Button.png")).convert_alpha(), pos=(80, 530), 
                            text_input="설정", font=get_font(60), base_color="Black", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(images_path, "Button.png")).convert_alpha(), pos=(80, 640), 
                            text_input="종료", font=get_font(60), base_color="Black", hovering_color="White")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, ENCYCLOPEDIA_BUTTON, CREDIT_BUTTON, OPTION_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Play()
                    if ENCYCLOPEDIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Enc.Encyclopedia()
                    if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Cre.Credit()
                    if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                        Opt.Option()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

        pygame.display.update()

main_menu()