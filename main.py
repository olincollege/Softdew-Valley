import pygame
from FarmerClass import Farmer
from ViewClass import View

FPS = 60


def main():
    farmer = Farmer
    display_farmer = View(farmer)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        farmer.move(farmer, keys_pressed)
        display_farmer.draw_window()
    pygame.quit()


# makes sure main is run when the file is run directly
if __name__ == "__main__":
    main()
