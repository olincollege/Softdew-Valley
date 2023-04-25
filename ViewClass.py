import pygame
import os


class View:
    FARMER_WIDTH = 50
    FARMER_HEIGHT = 100
    GROUND_SIZE = 50
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    INVENTORY_ITEM_SIZE = 40

    WHITE = (255, 255, 255)
    INVENTORY_START_WIDTH = WIDTH // 2 - GROUND_SIZE * 4
    INVENTORY_START_HEIGHT = HEIGHT - GROUND_SIZE * 2

    # FARMER SPRITES
    FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Front.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    BACK_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Back.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Right.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Facing_Left.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )

    # FARMER WATERING SPRITES
    WATER_FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Front_Water.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    WATER_BACK_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Back_Water.png")),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    WATER_RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Right_Water.png")),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )
    WATER_LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Left_Water.png")),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )

    # FARMER TILLING SPRITES
    TILL_FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Front_Till.png")),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    TILL_BACK_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Back_Till.png")),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    TILL_RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Right_Till.png")),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )
    TILL_LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Left_Till.png")),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )

    # GROUND SPRITES
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

    # INVENTORY/ITEM SPRITES
    INVENTORY_SQUARE = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Inventory_Square.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    farmer_image = FRONT_FARMER
    type_ground = FREE_GROUND

    def __init__(self, Farmer, Ground, Gamestate, Inventory):
        self.farmer = Farmer
        self.ground = Ground
        self.gamestate = Gamestate
        self.inventory = Inventory

    def farmer_direction(self):
        """
        Get the direction the farmer is facing and change the image displayed
        to match that direction
        """
        if self.gamestate.is_water and self.farmer.direction == "down":
            self.farmer_image = self.WATER_FRONT_FARMER
        elif self.gamestate.is_water and self.farmer.direction == "up":
            self.farmer_image = self.WATER_BACK_FARMER
        elif self.gamestate.is_water and self.farmer.direction == "right":
            self.farmer_image = self.WATER_RIGHT_FARMER
        elif self.gamestate.is_water and self.farmer.direction == "left":
            self.farmer_image = self.WATER_LEFT_FARMER

        elif self.gamestate.is_till and self.farmer.direction == "down":
            self.farmer_image = self.TILL_FRONT_FARMER
        elif self.gamestate.is_till and self.farmer.direction == "up":
            self.farmer_image = self.TILL_BACK_FARMER
        elif self.gamestate.is_till and self.farmer.direction == "right":
            self.farmer_image = self.TILL_RIGHT_FARMER
        elif self.gamestate.is_till and self.farmer.direction == "left":
            self.farmer_image = self.TILL_LEFT_FARMER

        elif self.farmer.direction == "down":
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

    def draw_inventory_items(self):
        for idx, item in enumerate(self.inventory.inventory):
            if not isinstance(item, str):  # item type is not a string:
                self.WIN.blit(
                    item.pg_image,
                    (
                        self.INVENTORY_START_WIDTH
                        + (idx * self.GROUND_SIZE)
                        + 5,
                        self.INVENTORY_START_HEIGHT + 5,
                    ),
                )

    def draw_window(self):
        self.WIN.fill(self.WHITE)

        # draw ground
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                self.ground_type(i, j)
                self.WIN.blit(
                    self.type_ground,
                    ((i) * self.GROUND_SIZE, (j) * self.GROUND_SIZE),
                )

        # draw farmer
        self.farmer_direction()
        if (
            self.farmer_image == self.WATER_LEFT_FARMER
            or self.farmer_image == self.TILL_LEFT_FARMER
        ):
            self.WIN.blit(
                self.farmer_image,
                (
                    self.farmer.farmer_rect.x - self.GROUND_SIZE,
                    self.farmer.farmer_rect.y,
                ),
            )
        elif (
            self.farmer_image == self.TILL_BACK_FARMER
            or self.farmer_image == self.WATER_FRONT_FARMER
        ):
            self.WIN.blit(
                self.farmer_image,
                (
                    self.farmer.farmer_rect.x,
                    self.farmer.farmer_rect.y - self.GROUND_SIZE // 2,
                ),
            )
        else:
            self.WIN.blit(
                self.farmer_image,
                (self.farmer.farmer_rect.x, self.farmer.farmer_rect.y),
            )

        # draw inventory
        for i in range(len(self.inventory.inventory)):
            self.WIN.blit(
                self.INVENTORY_SQUARE,
                (
                    self.INVENTORY_START_WIDTH + (i * self.GROUND_SIZE),
                    self.INVENTORY_START_HEIGHT,
                ),
            )
        self.draw_inventory_items()
        pygame.display.update()
        if self.gamestate.is_water or self.gamestate.is_till:
            pygame.time.delay(250)
            self.gamestate.stop_watering()
            self.gamestate.stop_tilling()
