import pygame
import sys
from menu import ImageButton

# Инициализация pygame
pygame.init()

# Параметры экрана
WIDTH, HEIGHT = 1200, 750

screen = pygame.display.set_mode ((WIDTH, HEIGHT))
pygame.display.set_caption("Menu test")
main_background = pygame.image.load("background.jpg")

#Загрузка и установка курсора
cursor = pygame.image.load("cursor.jpg")
pygame.mouse.set_visible(False)  #Скрываем стандартный курсор

def main_menu():
    # Создание кнопки
    #def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None)
    button1 = ImageButton(WIDTH/2-504, 200, 252, 74, "Одиночная игра", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")
    button2 = ImageButton(WIDTH/2-504, 325, 252, 74, "Настройки", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")
    button3 = ImageButton(WIDTH/2-504, 450, 252, 74, "Выйти", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Menu test", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == button1:
                print('Кнопка "Новая игра" была нажата!')
                new_game()

            if event.type == pygame.USEREVENT and event.button == button2:
                print('Кнопка "Настройки" была нажата!')
                settings_menu()

            if event.type == pygame.USEREVENT and event.button == button3:
                running = False
                pygame.quit()
                sys.exit()

            for but in [button1, button2, button3]:
                but.handle_event(event)

        for but in [button1, button2, button3]:
            but.check_hover(pygame.mouse.get_pos())
            but.draw(screen)

        #Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()

#экран настроек с кнопками и выходом назад
def settings_menu():
    set_but1 = ImageButton(WIDTH/2-504, 200, 252, 74, "Аудио", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")
    set_but2 = ImageButton(WIDTH/2-504, 325, 252, 74, "Видео", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")
    set_but3 = ImageButton(WIDTH/2-504, 450, 252, 74, "Назад", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")


    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))
    
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Settings", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running =False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #Возврат в меню
                if event.key ==  pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button ==  set_but3:
                running = False

            for but in [set_but1, set_but2, set_but3]:
                but.handle_event(event)

        for but in [set_but1, set_but2, set_but3]:
            but.check_hover(pygame.mouse.get_pos())
            but.draw(screen)

        #Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()

def new_game():
    back_but = ImageButton (WIDTH/2-504, 600, 252, 74, "Назад", "image1_1.jpg", "image1_2.jpg", "zvuk.mp3")

    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Welcome", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame. event.get():
            if event.type == pygame.QUIT:
                running =False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #Возврат в меню
                if event.key ==  pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button ==  back_but:
                running = False

            for but in [back_but]:
                but.handle_event(event)

        for but in [back_but]:
            but.check_hover(pygame.mouse.get_pos())
            but.draw(screen)

        #Отображение курсора в текущей позиции мыши
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-2, y-2))

        pygame.display.flip()

main_menu()
