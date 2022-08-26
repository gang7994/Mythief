from lib2to3.pgen2.token import OP
import pygame, sys
from Button import Button
from Button_text import Button_text
from Settings import *
import GameManager

class Encyclopedia:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Collection")
    def Encyclopedia(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_font(45).render("백과사전창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button_text(image=None, pos=(1300, 0), 
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
        pygame.display.set_caption("Credit")
    def Credit(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_titlefont(60).render("Mythief", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 70))
            
            TEXT1 = get_font(30).render("여기에 크레딧 내용 추가", True, "White")
            TEXT1_RECT = TEXT1.get_rect(center=((screen_width/2), 300))
            
            TEXT2 = get_font(30).render("Add credit content here", True, "White")
            TEXT2_RECT = TEXT1.get_rect(center=((screen_width/2), 400))
            '''
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()
            self.popup = pygame.transform.scale(self.popup, (800, 650))
            self.screen.blit(self.popup, (328, 100))
            '''
            self.screen.blit(TEXT1, TEXT1_RECT)
            self.screen.blit(TEXT2, TEXT2_RECT)
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            OPTIONS_BACK = Button_text(image=None, pos=(1300, 0), 
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
        global bgm_vol, effect_vol
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            self.screen.fill("Black")
            OPTIONS_TEXT = get_font(45).render("옵션창", True, "White")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=((screen_width/2), 30))
            self.popup = pygame.image.load(os.path.join(images_path, "popup.png")).convert_alpha()

            TEXT1 = get_font(30).render("BGM VOLUME", True, "White")
            TEXT1_RECT = TEXT1.get_rect(center=((screen_width/2), 200))
            
            TEXT2 = get_font(30).render("EFFECT VOLUME", True, "White")
            TEXT2_RECT = TEXT1.get_rect(center=((screen_width/2), 400))
            
            self.screen.blit(self.popup, (100, 100))
            self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
            self.screen.blit(TEXT1, TEXT1_RECT)
            self.screen.blit(TEXT2, TEXT2_RECT)

            self.draw_volume_bar()
            
            BGM_UP = Button(image0=pygame.image.load(os.path.join(images_path, "up0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "up1.png")).convert_alpha(), 
                                pos=(956,265), scale_x=50, scale_y=50)
            BGM_DOWN = Button(image0=pygame.image.load(os.path.join(images_path, "down0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "down1.png")).convert_alpha(), 
                                pos=(500,265), scale_x=50, scale_y=50)
            
            EFFECT_UP = Button(image0=pygame.image.load(os.path.join(images_path, "up0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "up1.png")).convert_alpha(), 
                                pos=(956,465), scale_x=50, scale_y=50)
            EFFECT_DOWN = Button(image0=pygame.image.load(os.path.join(images_path, "down0.png")).convert_alpha(), 
                                image1=pygame.image.load(os.path.join(images_path, "down1.png")).convert_alpha(), 
                                pos=(500,465), scale_x=50, scale_y=50)
            
            OPTIONS_BACK = Button_text(image=None, pos=(1200, 0), 
                                text_input="BACK", font=get_font(60), base_color="White", hovering_color="Red")

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()
                    if BGM_UP.checkForInput(OPTIONS_MOUSE_POS):
                        if bgm_vol != 100:
                            bgm_vol += 10
                    if BGM_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        if bgm_vol !=0:
                            bgm_vol -= 10
                    if EFFECT_UP.checkForInput(OPTIONS_MOUSE_POS):
                        if effect_vol != 100:
                            effect_vol += 10
                    if EFFECT_DOWN.checkForInput(OPTIONS_MOUSE_POS):
                        if effect_vol !=0:
                            effect_vol -= 10
            pygame.display.update()
            
    def draw_volume_bar(self):
        pygame.draw.rect(self.screen, WHITE, (528, 250, bgm_vol/0.25, 30))
        pygame.draw.rect(self.screen, BLACK, (528, 250, 400, 30), 3)
        pygame.draw.rect(self.screen, WHITE, (528, 450, effect_vol/0.25, 30))
        pygame.draw.rect(self.screen, BLACK, (528, 450, 400, 30), 3)



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
        MENU_RECT = MENU_TEXT.get_rect(center=(728, 120))

        PLAY_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_start_0.png")).convert_alpha(), 
                            image1=pygame.image.load(os.path.join(images_path, "btn_start_1.png")).convert_alpha(), 
                            pos=(728, 250), scale_x=400, scale_y=100)
        ENCYCLOPEDIA_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_Collection_0.png")).convert_alpha(), 
                            image1=pygame.image.load(os.path.join(images_path, "btn_Collection_1.png")).convert_alpha(), 
                            pos=(728, 360), scale_x=400, scale_y=100)
        CREDIT_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_credit_0.png")).convert_alpha(), 
                            image1=pygame.image.load(os.path.join(images_path, "btn_credit_1.png")).convert_alpha(), 
                            pos=(728, 470), scale_x=400, scale_y=100)
        OPTION_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_start_0.png")).convert_alpha(), 
                            image1=pygame.image.load(os.path.join(images_path, "btn_start_1.png")).convert_alpha(), 
                            pos=(728, 580), scale_x=400, scale_y=100)
        QUIT_BUTTON = Button(image0=pygame.image.load(os.path.join(images_path, "btn_exit_0.png")).convert_alpha(), 
                            image1=pygame.image.load(os.path.join(images_path, "btn_exit_1.png")).convert_alpha(), 
                            pos=(728, 690), scale_x=400, scale_y=100)
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