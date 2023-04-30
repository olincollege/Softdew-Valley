import pygame
import os
import random

pygame.font.init()


class View:
    # initialize global variables
    # global FARMER_WIDTH, FARMER_HEIGHT, GROUND_SIZE, WIDTH, HEIGHT
    # global INVENTORY_ITEM_SIZE, INVENTORY_FONT
    FARMER_WIDTH = 50
    FARMER_HEIGHT = 100
    GROUND_SIZE = 50
    WIDTH, HEIGHT = 900, 500
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    INVENTORY_ITEM_SIZE = 40
    INVENTORY_FONT = pygame.font.SysFont("comicsans", 40)

    WHITE = (255, 255, 255)
    RED = (255, 30, 0)
    SELECTION_BOX_COLOR = (244, 88, 66)

    INVENTORY_START_WIDTH = WIDTH // 2 - GROUND_SIZE * 4
    INVENTORY_START_HEIGHT = HEIGHT - GROUND_SIZE * 2

    # FARMER SPRITES
    FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/idle_farmer", "facing_down.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    BACK_FARMER = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/idle_farmer", "facing_up.png")),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/idle_farmer", "facing_right.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/idle_farmer", "facing_left.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )

    # FARMER WATERING SPRITES
    WATER_FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/watering_farmer", "Front_Water.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT),
    )
    WATER_BACK_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/watering_farmer", "Back_Water.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    WATER_RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/watering_farmer", "Right_Water.png")
        ),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )
    WATER_LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/watering_farmer", "Left_Water.png")
        ),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )

    # FARMER TILLING SPRITES
    TILL_FRONT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/tilling_farmer", "Front_Till.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    TILL_BACK_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/tilling_farmer", "Back_Till.png")
        ),
        (FARMER_WIDTH, FARMER_HEIGHT * 1.25),
    )
    TILL_RIGHT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/tilling_farmer", "Right_Till.png")
        ),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )
    TILL_LEFT_FARMER = pygame.transform.scale(
        pygame.image.load(
            os.path.join("Assets/tilling_farmer", "Left_Till.png")
        ),
        (2 * FARMER_WIDTH, FARMER_HEIGHT),  # x2 width to make room for tool
    )

    # GROUND SPRITES
    def randomize_free_ground(WIDTH, HEIGHT, GROUND_SIZE):
        """
        Randomizes the free ground image to bring the spice of variety into the
        farm

        Args:
            WIDTH: int value representing the game's pixel width
            HEIGHT: int value representing the game's pixel height
            GROUND_SIZE: int value representing each tile's pixel height/width

        Returns:
            FREE_GROUND_MAP: a two-dimensional list that is width of game in
            tiles by height of game in tiles in dimension and consists only of
            randomized pygame image pathways
        """
        FREE_GROUND_MAP = [
            [None] * (HEIGHT // GROUND_SIZE)
            for _ in range(WIDTH // GROUND_SIZE)
        ]
        # Define the corresponding probabilities for each ground file
        probabilities = [0.82, 0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.02]
        for i in range(WIDTH // GROUND_SIZE):
            for j in range(HEIGHT // GROUND_SIZE):
                FREE_GROUND_MAP[i][j] = pygame.transform.scale(
                    pygame.image.load(
                        os.path.join(
                            "Assets/ground/free_ground_versions",
                            f"free_ground{random.choices(range(9), probabilities)[0]}.png",
                        )
                    ),
                    (GROUND_SIZE, GROUND_SIZE),
                )
        return FREE_GROUND_MAP

    FREE_GROUND_MAP = randomize_free_ground(WIDTH, HEIGHT, GROUND_SIZE)

    TILLED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ground", "tilled_ground.png")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    WATERED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ground", "watered_ground.png")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    # INVENTORY/ITEM SPRITES
    INVENTORY_SQUARE = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "Inventory_Square.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    # HOUSE SPRITE
    HOUSE_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", "house_ground.PNG")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    # farmer_image = FRONT_FARMER
    type_ground = pygame.image.load(
        os.path.join("Assets/ground/free_ground_versions", "free_ground0.png")
    )
    plant_image = None

    def __init__(self, Farmer, Ground, Gamestate, Inventory):
        self.farmer = Farmer
        self.ground = Ground
        self.gamestate = Gamestate
        self.inventory = Inventory

    def farmer_direction(self):
        """
        Get the direction the farmer is facing and change the image displayed
        to match that direction
        Also match the farmer action
        """
        if self.farmer.direction not in ["up", "down", "left", "right"]:
            self.farmer.direction = "down"

        direction_map = {
            ("down", "water"): self.WATER_FRONT_FARMER,
            ("up", "water"): self.WATER_BACK_FARMER,
            ("right", "water"): self.WATER_RIGHT_FARMER,
            ("left", "water"): self.WATER_LEFT_FARMER,
            ("down", False): self.FRONT_FARMER,
            ("up", False): self.BACK_FARMER,
            ("right", False): self.RIGHT_FARMER,
            ("left", False): self.LEFT_FARMER,
            ("down", "till"): self.TILL_FRONT_FARMER,
            ("up", "till"): self.TILL_BACK_FARMER,
            ("right", "till"): self.TILL_RIGHT_FARMER,
            ("left", "till"): self.TILL_LEFT_FARMER,
        }

        tile_value = (
            "water"
            if self.gamestate.is_water
            else "till"
            if self.gamestate.is_till
            else False
        )

        self.farmer_image = direction_map[(self.farmer.direction, tile_value)]

    def ground_type(self, row, col):
        """
        Get the type of square from the Ground class adn display the matching
        square image
        """
        if self.ground.is_watered(self.ground.get_square(row, col)):
            self.type_ground = self.WATERED_GROUND
        elif self.ground.is_tilled(self.ground.get_square(row, col)):
            self.type_ground = self.TILLED_GROUND
        else:
            self.type_ground = self.FREE_GROUND_MAP[row][col]

    def draw_inventory_items(self):
        """
        Draw items into the inventory
        """
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
                if item.num_item is not None:
                    pass  # draw number of item
                    num_text = str(item.num_item)
                    draw_text = self.INVENTORY_FONT.render(
                        num_text, 1, self.RED
                    )
                    self.WIN.blit(
                        draw_text,
                        (
                            (
                                self.INVENTORY_START_WIDTH
                                + (idx * self.GROUND_SIZE)
                                + self.INVENTORY_ITEM_SIZE
                                - 5
                            ),
                            (
                                self.INVENTORY_START_HEIGHT
                                + self.INVENTORY_ITEM_SIZE
                                - 5
                            ),
                        ),
                    )

    def draw_equipped_square(self):
        """
        Draw a rectangle around the equipped inventory slot
        """
        equipped_slot = self.inventory.get_equipped_item_slot()
        if equipped_slot is not None:
            y_pos = self.INVENTORY_START_HEIGHT
            x_pos = (
                self.INVENTORY_START_WIDTH + equipped_slot * self.GROUND_SIZE
            )
            rect = pygame.Rect(x_pos, y_pos, self.GROUND_SIZE, self.GROUND_SIZE)
            pygame.draw.rect(
                self.WIN, self.SELECTION_BOX_COLOR, rect, 3, border_radius=1
            )

    def draw_window(self):
        self.WIN.fill(self.WHITE)

        # draw ground and plants
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                self.ground_type(i, j)
                # self.plant_appearance(i, j)
                self.WIN.blit(
                    self.type_ground,
                    ((i) * self.GROUND_SIZE, (j) * self.GROUND_SIZE),
                )
                if self.ground.has_crop(self.ground.get_square(i, j)):
                    plant = self.ground.get_square(i, j)
                    if self.ground.has_crop(self.ground.get_square(i, j)):
                        plant_index = plant.growth_stage
                        self.plant_image = pygame.image.load(
                            os.path.join(
                                f"Assets/{plant.species}",
                                f"{plant.species}{plant_index}.png",
                            )
                        )
                    self.WIN.blit(
                        self.plant_image,
                        ((i) * self.GROUND_SIZE, (j) * self.GROUND_SIZE),
                    )
        # draw house
        num_house_rows = 5
        num_house_cols = 4
        for k in range(num_house_rows):  # change so not hard coded number
            for j in range(num_house_cols):
                self.WIN.blit(self.HOUSE_GROUND, (self.WIDTH - 50 * k, 50 * j))

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
        self.draw_equipped_square()
        pygame.display.update()
        if self.gamestate.is_water or self.gamestate.is_till:
            pygame.time.delay(250)
            self.gamestate.stop_watering()
            self.gamestate.stop_tilling()
