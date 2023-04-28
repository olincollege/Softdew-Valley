import pygame

import audio
from ViewClass import View
from Model import Model

FPS = 60


def main():
    pygame.init()
    model = Model()
    display = View(model.farmer, model.ground, model.gamestate, model.inventory)
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
                    model.perform_action()
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        model.inventory.control_inventory(num=i - 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    model.gamestate.harvest_crop(model.inventory)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                model.update_equipped_inventory(mouse_pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    model.day_passes()

        keys_pressed = pygame.key.get_pressed()
        model.farmer.move(model.farmer, keys_pressed)
        display.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
