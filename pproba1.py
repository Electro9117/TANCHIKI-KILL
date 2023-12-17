from time import sleep
import pygame
import pygame_menu
import main

 
pygame.init()
surface = pygame.display.set_mode((700, 800))
 
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)

def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)

def start_the_game2():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 20)

 
def level_menu():
    mainmenu._open(level)
 
# кнопки не функцианируют 
mainmenu = pygame_menu.Menu('Welcome', 700, 800, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username')
mainmenu.add.button('Play', main)
mainmenu.add.button('Multiplay', start_the_game2)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)
# ----------------------------------------------------------
level = pygame_menu.Menu('Select a Difficulty', 630, 630, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
 
loading = pygame_menu.Menu('Loading the Game...', 700, 800, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id = "1", default=0, width = 200, )
 
arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 
update_loading = pygame.USEREVENT + 0
 
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 0)
        if event.type == pygame.QUIT:
            exit()
 
    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if (mainmenu.get_current().get_selected_widget()):
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())
 
    pygame.display.update()
