import pygame
from elements.button import Button
from pages.index import Index
from pages.game import Game
from pages.about import About
from pages.levels import Levels
from pages.win import Win

pygame.init()
running = True

index_page = Index()
index_page.makeCurrentScreen()
index_page.mount()

game_page = Game()
about_page = About()
levels_page = Levels()
win_page = Win()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_page.handle_events(event)

    return_index = index_page.screenUpdate()
    if(return_index == 1):
        game_page.makeCurrentScreen()
        game_page.mount(1)
    elif(return_index == 2):
        about_page.makeCurrentScreen()
        about_page.mount()
    elif(return_index == 3):
        levels_page.makeCurrentScreen()
        levels_page.mount()

    return_about = about_page.screenUpdate()
    if(return_about == 1):
        index_page.makeCurrentScreen()
        index_page.mount()

    
    return_levels = levels_page.screenUpdate()
    if(return_levels == -1):
        index_page.makeCurrentScreen()
        index_page.mount()
    elif(return_levels > 0):
        game_page.makeCurrentScreen()
        game_page.mount(start_level=return_levels)

    return_game = game_page.screenUpdate()
    if(return_game == 1):
        win_page.makeCurrentScreen()
        win_page.mount()
    

    return_win = win_page.screenUpdate()
    if(return_win == 1):
        index_page.makeCurrentScreen()
        index_page.mount()
        
    pygame.display.update()
       
pygame.quit()
    



