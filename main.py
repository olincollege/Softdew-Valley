"""
Runs the main game loop
"""
# No pygame module has its member
# pylint: disable=no-member
# A pygame game loop by nature requires a branch for every action
# pylint: disable=too-many-branches
import pygame
import audio
import houseclass
from viewclass import View

# import model
from model import Model
from controller import Controller


FPS = 60


def main():
    """
    Runs game at 60 FPS by initializing overall game instances
    (Model, View, and Controller instances)

    Includes logic for button controls:
        - general action key (space)
        - number keys
        - mouse clicks for inventory slots
        - the harvesting key (h)
        - day passing key (p)gi

    Passes keys pressed to farmer movement in control
    Quits the game and calls draw_window in View class
    """  # edit day passing when house is done
    pygame.init()
    model = Model()
    display = View(model)
    control = Controller(model.farmer, model.inventory)
    clock = pygame.time.Clock()
    game_running = True
    audio.play_music()
    pygame.display.set_caption("Super Swag Stardew")
    control_screen = False
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == audio.MUSIC_END:
                audio.play_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("you hit ?")
                    control_screen = not control_screen
                    print(control_screen)
                if event.key == pygame.K_SPACE:
                    model.action()
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        control.select_inventory(num=i - 1)
                if event.key == pygame.K_h:
                    model.harvest_crop()
                # should be triggered by house interaction event
                # brought back for testing purposes (DELETE LATER)
                if event.key == pygame.K_p:
                    model.day_passes()
            if event.type == houseclass.ENTER_HOUSE:
                pass
            if event.type == houseclass.ENTER_BED:
                model.day_passes()
                display.day_change()
                pygame.time.delay(300)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                control.click_inventory(mouse_pos)
        keys_pressed = pygame.key.get_pressed()
        control.move_farmer(keys_pressed)
        model.house.enter_bed(model.farmer)
        display.draw_window(control_screen)

    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
