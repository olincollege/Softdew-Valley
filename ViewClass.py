import pygame
import os
from FarmerClass import Farmer


class View:
    FARMER_WIDTH = 35
    FARMER_HEIGHT = 70

    FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Front.jpg")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    BACK_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Back.jpg")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Right.jpg")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Left.jpg")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )

    WIDTH, HEIGHT = 900, 500

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    WHITE = (255, 255, 255)

    farmer_image = FRONT_FARMER

    def __init__(self, Farmer):
        self.farmer = Farmer

    def farmer_direction(self):
        """
        Get the direction the farmer is facing and change the image displayed
        to match that direction
        """
        if self.farmer.direction == "down":
            self.farmer_image = self.FRONT_FARMER
        elif self.farmer.direction == "up":
            self.farmer_image = self.BACK_FARMER
        elif self.farmer.direction == "left":
            self.farmer_image = self.LEFT_FARMER
        elif self.farmer.direction == "right":
            self.farmer_image = self.RIGHT_FARMER

    def draw_window(self):
        self.WIN.fill(self.WHITE)

        # draw farmer
        self.farmer_direction()
        self.WIN.blit(
            self.farmer_image,
            (self.farmer.farmer_rect.x, self.farmer.farmer_rect.y),
        )
        pygame.display.update()
