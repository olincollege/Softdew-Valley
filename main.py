import pygame
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
)
from Inventory_Class import Inventory
from plants import Plants

FPS = 60


def main():
    farmer = Farmer
    ground = Ground()
    gamestate = GameState(farmer, ground)
    watering_can = WateringCan(0, gamestate)
    hoe = Hoe(1, gamestate)
    parsnipseeds = ParsnipSeeds(2, gamestate)
    cauliflowerseeds = CauliflowerSeeds(3, gamestate)
    inventory = Inventory(watering_can, hoe, parsnipseeds, cauliflowerseeds)
    display_farmer = View(farmer, ground, gamestate, inventory)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    equipped_item = inventory.get_equipped_item()
                    if equipped_item is not None:
                        # the action function is different for each item
                        equipped_item.action()
                for i in range(1, 9):
                    if event.key == getattr(pygame, f"K_{i}"):
                        inventory.control_inventory(num=i - 1)
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
                    print("you hit p")
                    rows = ground.num_rows
                    cols = ground.num_cols
                    for j in range(cols):
                        for i in range(rows):
                            if isinstance(ground.land[i][j], Plants):
                                ground.land[i][j].grow()
                    ground.unwater_squares()
                if event.key == pygame.K_SPACE:
                    equipped_item = inventory.get_equipped_item()
                    print(equipped_item)
                    if isinstance(equipped_item, WateringCan):
                        gamestate.water_ground()
                    if isinstance(equipped_item, Hoe):
                        gamestate.till_ground()
                    if isinstance(equipped_item, Seed):
                        print(equipped_item.seed_type)
                        gamestate.plant_seed(equipped_item.seed_type)

        keys_pressed = pygame.key.get_pressed()
        farmer.move(farmer, keys_pressed)
        display_farmer.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
