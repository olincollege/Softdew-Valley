import pygame
import audio
import houseclass
from viewclass import View
import model
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
        - day passing key (p)

    Passes keys pressed to farmer movement in control
    Quits the game and calls draw_window in View class
    """  # edit day passing when house is done
    pygame.init()
    # model = Model()
    display = View(
        model.farmer,
        model.ground,
        model.gamestate,
        model.inventory,
    )
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
                # brought back for testing purposes (DELETE LATER)
                if event.key == pygame.K_p:
                    model.day_passes()
            if event.type == houseclass.ENTER_HOUSE:
                print("you went inside")
            if event.type == houseclass.HIT_WALL:
                print("that was a wall")
                # prevent farmer position from increasing towards wall?
            if event.type == houseclass.ENTER_BED:
                model.day_passes()
                display.day_change()
                pygame.time.delay(300)

        keys_pressed = pygame.key.get_pressed()
        control.move_farmer(keys_pressed)
        model.house.enter_bed(model.farmer)
        model.house.enter_bed(
            model.farmer
        )  # I now realize the dictionary is totally useless
        model.house.hit_wall(model.farmer)
        display.draw_window()

    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
