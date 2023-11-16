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

#def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None)
button1 = ImageButton(WIDTH/2-504, 200, 252, 74, "Нажми", "image1_1.jpg", "image1_2.jpg", "sound_1.mp3")
button2 = ImageButton(WIDTH/2-504, 325, 252, 74, "На", "image1_1.jpg", "image1_2.jpg", "insta.mp3")
button3 = ImageButton(WIDTH/2-504, 450, 252, 74, "Меня", "image1_1.jpg", "image1_2.jpg", "putana.mp3")
button4 = ImageButton (WIDTH/2-504, 600, 252, 74, "на последок)", "image1_1.jpg", "image1_2.jpg", "shaman.mp3")

def main_menu():
    # Создание кнопки
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(main_background, (0, 0))

        font = pygame.font.Font(None, 72)
        text_surface = font.render("Menu test", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(WIDTH/2, 100))
        screen.blit(text_surface, text_rect)

        for event in pygame. event.get():
            if event.type == pygame.QUIT:
                running =False
                pygame.quit()
                sys.exit()

            for but in [button1, button2, button3, button4]:
                but.handle_event(event)

        for but in [button1, button2, button3, button4]:
            but.check_hover(pygame.mouse.get_pos())
            but.draw(screen)
            
        pygame.display.flip()


main_menu()