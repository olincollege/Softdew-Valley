import pygame

import music
from FarmerClass import Farmer
from ViewClass import View
from GroundClass import Ground
from GameState import GameState
from EquipmentClass import (
    WateringCan,
    Hoe,
    Seed,
    ParsnipSeeds,
    CauliflowerSeeds,
    Crop,
    Parsnip_Crop,
    Cauliflower_Crop,
)
from Inventory_Class import Inventory
from plants import Plants

FPS = 60


def main():
    farmer = Farmer  # should probably make this an instance?
    ground = Ground()
    gamestate = GameState(farmer, ground)
    watering_can = WateringCan(gamestate)
    hoe = Hoe(gamestate)
    parsnipseeds = ParsnipSeeds(gamestate)
    cauliflowerseeds = CauliflowerSeeds(gamestate)
    inventory = Inventory(watering_can, hoe, parsnipseeds, cauliflowerseeds)
    display_farmer = View(farmer, ground, gamestate, inventory)
    clock = pygame.time.Clock()
    game_running = True
    pygame.init()
    mixer_works = pygame.mixer.get_init()  # None if the mixer doesn't work
    if mixer_works is not None:
        music.play_music()
    pygame.display.set_caption("Super Swag Stardew")
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == music.MUSIC_END:
                if mixer_works is not None:
                    music.play_music()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    equipped_item = inventory.get_equipped_item()
                    if equipped_item is not None:
                        # the action function is different for each item
                        equipped_item.action()
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        inventory.control_inventory(num=i - 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    gamestate.harvest_crop(inventory)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (
                    mouse_pos[0] > View.INVENTORY_START_WIDTH
                    and mouse_pos[0] < View.INVENTORY_START_WIDTH + 7 * 50
                ):
                    if (
                        mouse_pos[1] > View.INVENTORY_START_HEIGHT
                        and mouse_pos[1]
                        < View.INVENTORY_START_HEIGHT + View.GROUND_SIZE
                    ):
                        inventory.control_inventory(mouse_pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    # print("you hit p")
                    rows = ground.num_rows
                    cols = ground.num_cols
                    for j in range(cols):
                        for i in range(rows):
                            if isinstance(ground.land[i][j], Plants):
                                ground.land[i][j].grow()
                    ground.unwater_squares()

        keys_pressed = pygame.key.get_pressed()
        farmer.move(farmer, keys_pressed)
        display_farmer.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
