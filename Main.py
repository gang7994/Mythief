import pygame, sys
from Button import Button
from Settings import *
import GameManager
pygame.init()

SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

def get_titlefont(size): 
    return pygame.font.Font("Images/TestPix/font.ttf", size)

def get_font(size): 
    return pygame.font.SysFont('malgungothic', size)

def Play():
    game = GameManager.GameManager()
    game.Run()

def Encyclopedia():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("백과사전창", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def Credit():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("크레딧창", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()
    
def Option():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("옵션창", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()

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
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Play()
                if ENCYCLOPEDIA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Encyclopedia()
                if CREDIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Credit()
                if OPTION_BUTTON.checkForInput(MENU_MOUSE_POS):
                    Option()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()