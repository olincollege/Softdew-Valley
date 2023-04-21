import pygame
import os
from FarmerClass import Farmer
from GroundClass import Ground


class View:
    FARMER_WIDTH = 50
    FARMER_HEIGHT = 120
    GROUND_SIZE = 50

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

    FREE_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "free_ground.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    TILLED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "tilled_ground.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    WATERED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "watered_ground.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    WIDTH, HEIGHT = 900, 500

    WIN = pygame.display.set_mode((WIDTH, HEIGHT))

    WHITE = (255, 255, 255)

    farmer_image = FRONT_FARMER
    type_ground = FREE_GROUND

    def __init__(self, Farmer, Ground):
        self.farmer = Farmer
        self.ground = Ground

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

    def ground_type(self, row, col):
        # IGNORING PLANTS FOR NOW
        if self.ground.is_watered(self.ground.get_square(row, col)):
            self.type_ground = self.WATERED_GROUND
        elif self.ground.is_tilled(self.ground.get_square(row, col)):
            self.type_ground = self.TILLED_GROUND
        else:
            self.type_ground = self.FREE_GROUND

    def draw_window(self):
        self.WIN.fill(self.WHITE)

        # draw ground
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                self.ground_type(i, j)
                self.WIN.blit(self.type_ground, ((i) * 50, (j) * 50))

        # draw farmer
        self.farmer_direction()
        self.WIN.blit(
            self.farmer_image,
            (self.farmer.farmer_rect.x, self.farmer.farmer_rect.y),
        )

        pygame.display.update()
