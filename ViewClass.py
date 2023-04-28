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
    RED = (255, 0, 0)

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
    FREE_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ground", "free_ground.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    TILLED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ground", "tilled_ground.jpg")),
        (GROUND_SIZE, GROUND_SIZE),
    )

    WATERED_GROUND = pygame.transform.scale(
        pygame.image.load(os.path.join("Assets/ground", "watered_ground.jpg")),
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
    type_ground = FREE_GROUND
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
            else "till" if self.gamestate.is_till else False
        )

        self.farmer_image = direction_map[(self.farmer.direction, tile_value)]

        # if self.gamestate.is_water and self.farmer.direction == "down":
        #     self.farmer_image = self.WATER_FRONT_FARMER
        # elif self.gamestate.is_water and self.farmer.direction == "up":
        #     self.farmer_image = self.WATER_BACK_FARMER
        # elif self.gamestate.is_water and self.farmer.direction == "right":
        #     self.farmer_image = self.WATER_RIGHT_FARMER
        # elif self.gamestate.is_water and self.farmer.direction == "left":
        #     self.farmer_image = self.WATER_LEFT_FARMER

        # elif self.gamestate.is_till and self.farmer.direction == "down":
        #     self.farmer_image = self.TILL_FRONT_FARMER
        # elif self.gamestate.is_till and self.farmer.direction == "up":
        #     self.farmer_image = self.TILL_BACK_FARMER
        # elif self.gamestate.is_till and self.farmer.direction == "right":
        #     self.farmer_image = self.TILL_RIGHT_FARMER
        # elif self.gamestate.is_till and self.farmer.direction == "left":
        #     self.farmer_image = self.TILL_LEFT_FARMER

        # elif self.farmer.direction == "down":
        #     self.farmer_image = self.FRONT_FARMER
        # elif self.farmer.direction == "up":
        #     self.farmer_image = self.BACK_FARMER
        # elif self.farmer.direction == "left":
        #     self.farmer_image = self.LEFT_FARMER
        # elif self.farmer.direction == "right":
        #     self.farmer_image = self.RIGHT_FARMER

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
            self.type_ground = self.FREE_GROUND

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
            pygame.draw.rect(self.WIN, self.RED, rect, 2, border_radius=1)

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
