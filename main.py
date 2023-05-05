"""
Runs the main game loop
"""
# No pygame module has its member
# pylint: disable=no-member
# A pygame game loop by nature requires a branch for every action
# pylint: disable=too-many-branches
# pylint: disable=too-many-nested-blocks
import pygame
import audio
import houseclass
from viewclass import View
from plants import Plants

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
        - entering the store

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
            # Take keyboard inptus
            if event.type == pygame.KEYDOWN:
                # If question mark is hit display or hide controls menu
                if (
                    pygame.key.get_pressed()[pygame.K_SLASH]
                    and pygame.key.get_mods() & pygame.KMOD_SHIFT
                ):
                    control_screen = not control_screen
                # if space is hit perform item action
                if event.key == pygame.K_SPACE:
                    model.action()
                # if number key is hit, equip that inventory item
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        control.select_inventory(num=i - 1)
                # if h key is hit, perform harvest action
                if event.key == pygame.K_h:
                    model.harvest_crop()
                # if e is hit, enter or exit the store
                if event.key == pygame.K_e:
                    if model.in_store:
                        model.leave_store()
                    else:
                        model.enter_store()
            # If user interacts with bed, make a day pass
            if event.type == houseclass.ENTER_BED:
                model.day_passes()
                display.day_change()
                pygame.time.delay(300)
            # Handles mouse clicking
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # check if the inventory has been clicked
                control.click_inventory(mouse_pos)
                # check if the store menu has been clicked
                store_item = control.click_store(mouse_pos, model.stand)
                model.buy_item(store_item)
        keys_pressed = pygame.key.get_pressed()
        # move the farmer
        control.move_farmer(keys_pressed)
        model.house.enter_bed(model.farmer)
        # draw window
        display.draw_window(control_screen)

    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
