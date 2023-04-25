import pygame
from FarmerClass import Farmer
from ViewClass import View
from GroundClass import Ground
from GameState import GameState
from EquipmentClass import Equipment, WateringCan, Hoe, Seeds
from Inventory_Class import Inventory
from plants import Plants

FPS = 60


def main():
    farmer = Farmer
    ground = Ground()
    gamestate = GameState(farmer, ground)
    plants = Plants
    watering_can = WateringCan(0, gamestate)
    hoe = Hoe(1, gamestate)
    seeds = Seeds(2, gamestate)
    inventory = Inventory(watering_can, hoe, seeds)
    display_farmer = View(farmer, ground, gamestate, plants, inventory)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    gamestate.plant_seed()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    equipped_item = inventory.get_equipped_item()
                    if equipped_item is not None:
                        # the action function is different for each item
                        equipped_item.action()
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
                if event.key == pygame.K_SPACE:
                    equipped_item = inventory.get_equipped_item()
                    print(equipped_item)
                    if isinstance(equipped_item, WateringCan):
                        gamestate.water_ground()
                    if isinstance(equipped_item, Hoe):
                        gamestate.till_ground()
        keys_pressed = pygame.key.get_pressed()
        farmer.move(farmer, keys_pressed)
        display_farmer.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
