import pygame
from elements.button import Button
from pages.index import Index
from pages.game import Game

pygame.init()
running = True

index_page = Index()
index_page.makeCurrentScreen()
index_page.mount()

game_page = Game()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_page.handle_events(event)

    if(index_page.screenUpdate()):
        game_page.makeCurrentScreen()
        game_page.mount()
    
    game_page.screenUpdate()

    pygame.display.update()
       
pygame.quit()
    



