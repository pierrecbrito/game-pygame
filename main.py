import pygame
from elements.button import Button
from pages.index import Index
from pages.game import Game
from pages.about import About

pygame.init()
running = True

index_page = Index()
index_page.makeCurrentScreen()
index_page.mount()

game_page = Game()

about_page = About()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_page.handle_events(event)

    return_index = index_page.screenUpdate()
    if(return_index == 1):
        game_page.makeCurrentScreen()
        game_page.mount()
    elif(return_index == 2):
        about_page.makeCurrentScreen()
        about_page.mount()

    return_about = about_page.screenUpdate()
    if(return_about == 1):
        index_page.makeCurrentScreen()
        index_page.mount()

    game_page.screenUpdate()

    pygame.display.update()
       
pygame.quit()
    



