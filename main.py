import pygame

import audio
from ViewClass import View
from Model import Model
from Controller import Controller

FPS = 60


def main():
    """Run the game by creating instances"""
    pygame.init()
    model = Model()
    display = View(model.farmer, model.ground, model.gamestate, model.inventory)
    control = Controller(model.farmer, model.inventory)
    clock = pygame.time.Clock()
    game_running = True
    audio.play_music()
    pygame.display.set_caption("Super Swag Stardew")
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == audio.MUSIC_END:
                audio.play_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    control.perform_action()
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        control.select_inventory(num=i - 1)
                if event.key == pygame.K_h:
                    model.gamestate.harvest_crop(model.inventory)
                # should be triggered by house interaction event
                if event.key == pygame.K_p:
                    model.day_passes()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                control.click_inventory(mouse_pos)

        keys_pressed = pygame.key.get_pressed()
        control.move_farmer(keys_pressed)
        display.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
