import pygame
from FarmerClass import Farmer
from ViewClass import View
from GroundClass import Ground
from GameState import GameState

FPS = 60


def main():
    farmer = Farmer
    ground = Ground()
    gamestate = GameState(farmer, ground)
    display_farmer = View(farmer, ground, gamestate)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # FOR NOW: if the space key is hit, till the space in front
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gamestate.till_ground()
            # FOR NOW: if the q key is hit, water the space in front
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gamestate.water_ground()

        keys_pressed = pygame.key.get_pressed()
        farmer.move(farmer, keys_pressed)
        display_farmer.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
