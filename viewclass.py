import pygame
import os
import random

pygame.font.init()

# Setting constants to be used throughout the file
FARMER_WIDTH = 45
FARMER_HEIGHT = 90
GROUND_SIZE = 50
WIDTH, HEIGHT = 1000, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
INVENTORY_ITEM_SIZE = 40
INVENTORY_FONT = pygame.font.Font("Assets/stardew_font.ttf", 16)
HOUSE_SIZE = GROUND_SIZE * 8

# Setting color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_COLOR = (0, 0, 0)
SELECTION_BOX_COLOR = (244, 88, 66)

# Setting inventory position values
INVENTORY_START_WIDTH = WIDTH // 2 - GROUND_SIZE * 4
INVENTORY_START_HEIGHT = HEIGHT - GROUND_SIZE * 2


def pygameify_image(subfolder, image_name, width_scale, height_scale):
    """
    Transforms and loads an image from a joined image pathway

    ARGS:
        subfolder: a string representing the name of a subfolder of the Assets
        folder
        image_name: a string representing the name of the desired image file
        width_scale: a float or int representing how much an image should be
        scaled horizontally
        height_scale: a float or int representing how much an image should be
        scaled vertically
    """
    return pygame.transform.scale(
        pygame.image.load(os.path.join("Assets", subfolder, image_name)),
        (width_scale, height_scale),
    ).convert_alpha()


# FARMER SPRITES
FRONT_FARMER = pygameify_image(
    "idle_farmer", "facing_down.png", FARMER_WIDTH, FARMER_HEIGHT
)

BACK_FARMER = pygameify_image(
    "idle_farmer", "facing_up.png", FARMER_WIDTH, FARMER_HEIGHT
)

RIGHT_FARMER = pygameify_image(
    "idle_farmer", "facing_right.png", FARMER_WIDTH, FARMER_HEIGHT
)

LEFT_FARMER = pygameify_image(
    "idle_farmer", "facing_left.png", FARMER_WIDTH, FARMER_HEIGHT
)

# FARMER WATERING SPRITES
WATER_FRONT_FARMER = pygameify_image(
    "watering_farmer", "Front_Water.png", FARMER_WIDTH, FARMER_HEIGHT
)

WATER_BACK_FARMER = pygameify_image(
    "watering_farmer", "Back_Water.png", FARMER_WIDTH, FARMER_HEIGHT * 1.25
)

WATER_RIGHT_FARMER = pygameify_image(
    "watering_farmer", "Right_Water.png", 2 * FARMER_WIDTH, FARMER_HEIGHT
)  # x2 width to make room for tool

WATER_LEFT_FARMER = pygameify_image(
    "watering_farmer", "Left_Water.png", 2 * FARMER_WIDTH, FARMER_HEIGHT
)  # x2 width to make room for tool

# FARMER TILLING SPRITES
TILL_FRONT_FARMER = pygameify_image(
    "tilling_farmer", "Front_Till.png", FARMER_WIDTH, FARMER_HEIGHT * 1.25
)
TILL_BACK_FARMER = pygameify_image(
    "tilling_farmer", "Back_Till.png", FARMER_WIDTH, FARMER_HEIGHT * 1.25
)
TILL_RIGHT_FARMER = pygameify_image(
    "tilling_farmer", "Right_Till.png", 2 * FARMER_WIDTH, FARMER_HEIGHT
)  # x2 width to make room for tool
TILL_LEFT_FARMER = pygameify_image(
    "tilling_farmer", "Left_Till.png", 2 * FARMER_WIDTH, FARMER_HEIGHT
)  # x2 width to make room for tool


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
        [None] * (HEIGHT // GROUND_SIZE) for _ in range(WIDTH // GROUND_SIZE)
    ]
    # Define the corresponding probabilities for each ground file
    probabilities = [0.82, 0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.02]
    for i in range(WIDTH // GROUND_SIZE):
        for j in range(HEIGHT // GROUND_SIZE):
            FREE_GROUND_MAP[i][j] = pygameify_image(
                "ground/free_ground_versions",
                f"free_ground{random.choices(range(9), probabilities)[0]}.png",
                GROUND_SIZE,
                GROUND_SIZE,
            )
    return FREE_GROUND_MAP


FREE_GROUND_MAP = randomize_free_ground(WIDTH, HEIGHT, GROUND_SIZE)

TILLED_GROUND = pygameify_image(
    "ground", "tilled_ground.png", GROUND_SIZE, GROUND_SIZE
)

WATERED_GROUND = pygameify_image(
    "ground", "watered_ground.png", GROUND_SIZE, GROUND_SIZE
)

# INVENTORY/ITEM SPRITES
INVENTORY_SQUARE = pygameify_image(
    "", "Inventory_Square.jpg", GROUND_SIZE, GROUND_SIZE
)

# HOUSE SPRITE
HOUSE_SPRITE = pygameify_image("", "olin_farmhouse.png", HOUSE_SIZE, HOUSE_SIZE)


class View:
    """
    Class that handles displaying the game

    Attributes:
        FARMER_WIDTH: An int representing the width of the farmer in pixels
        FARMER_HEIGHT: An int representing the height of the farmer in pixels
        GROUND_SIZE: An int representing the width/height of a ground square
            in pixels
        WIDTH: An int representing the width of the window in pixels
        HEIGHT An int representing the height of the window in pixels
        WIN: A pygame object that is the window the game is played on
        INVENTORY_ITEM_SIZE: An int representing the width/height of an item in
            the inventory in pixels
        INVENTORY_FONT: The font of the numbers displayed in the inventory

        WHITE: A tuple representing the RGB values for white
        RED: A tuple representing the RGB values for red
        SELECTION_BOX_COLOR: A tuple representing the RGB values for the color
            of the box drawn around an equipped item in the inventory


    """

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
            ("down", "water"): WATER_FRONT_FARMER,
            ("up", "water"): WATER_BACK_FARMER,
            ("right", "water"): WATER_RIGHT_FARMER,
            ("left", "water"): WATER_LEFT_FARMER,
            ("down", False): FRONT_FARMER,
            ("up", False): BACK_FARMER,
            ("right", False): RIGHT_FARMER,
            ("left", False): LEFT_FARMER,
            ("down", "till"): TILL_FRONT_FARMER,
            ("up", "till"): TILL_BACK_FARMER,
            ("right", "till"): TILL_RIGHT_FARMER,
            ("left", "till"): TILL_LEFT_FARMER,
        }

        tile_value = (
            "water"
            if self.gamestate.is_water
            else "till" if self.gamestate.is_till else False
        )

        self.farmer_image = direction_map[(self.farmer.direction, tile_value)]

    def ground_type(self, row, col):
        """
        Get the type of square from the Ground class and display the matching
        square image

        ARGS:
            row: the int row index of a game tile
            col: the int column index of a game tile
        """
        if self.ground.is_watered(self.ground.get_square(row, col)):
            self.type_ground = WATERED_GROUND
        elif self.ground.is_tilled(self.ground.get_square(row, col)):
            self.type_ground = TILLED_GROUND
        else:
            self.type_ground = FREE_GROUND_MAP[row][col]

    def draw_inventory_items(self):
        """
        Draw items into the inventory
        """
        for idx, item in enumerate(self.inventory.inventory):
            if not isinstance(item, str):  # item type is not a string:
                WIN.blit(
                    item.pg_image,
                    (
                        INVENTORY_START_WIDTH + (idx * GROUND_SIZE) + 5,
                        INVENTORY_START_HEIGHT + 5,
                    ),
                )
                if item.num_item is not None:
                    pass  # draw number of item
                    num_text = str(item.num_item)
                    draw_text = INVENTORY_FONT.render(num_text, 1, FONT_COLOR)
                    WIN.blit(
                        draw_text,
                        (
                            (
                                INVENTORY_START_WIDTH
                                + (idx * GROUND_SIZE)
                                + INVENTORY_ITEM_SIZE
                                - 3
                            ),
                            (INVENTORY_START_HEIGHT + INVENTORY_ITEM_SIZE - 7),
                        ),
                    )

    def draw_equipped_square(self):
        """
        Draw a rectangle around the equipped inventory slot
        """
        equipped_slot = self.inventory.get_equipped_item_slot()
        if equipped_slot is not None:
            y_pos = INVENTORY_START_HEIGHT
            x_pos = INVENTORY_START_WIDTH + equipped_slot * GROUND_SIZE
            rect = pygame.Rect(x_pos, y_pos, GROUND_SIZE, GROUND_SIZE)
            pygame.draw.rect(WIN, SELECTION_BOX_COLOR, rect, 3, border_radius=1)

    def draw_window(self):
        """
        Draws the entire pygame window every time it is called
        (ground, plants, house, farmer, inventory, and inventory text)
        """
        WIN.fill(WHITE)

        # draw ground and plants
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                self.ground_type(i, j)
                # self.plant_appearance(i, j)
                WIN.blit(
                    self.type_ground,
                    ((i) * GROUND_SIZE, (j) * GROUND_SIZE),
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
                    WIN.blit(
                        self.plant_image,
                        ((i) * GROUND_SIZE, (j) * GROUND_SIZE),
                    )
        # draw house
        WIN.blit(HOUSE_SPRITE, (WIDTH - HOUSE_SIZE, 0))

        # draw farmer
        self.farmer_direction()
        if (
            self.farmer_image == WATER_LEFT_FARMER
            or self.farmer_image == TILL_LEFT_FARMER
        ):
            WIN.blit(
                self.farmer_image,
                (
                    self.farmer.farmer_rect.x - GROUND_SIZE,
                    self.farmer.farmer_rect.y,
                ),
            )
        elif (
            self.farmer_image == TILL_BACK_FARMER
            or self.farmer_image == WATER_FRONT_FARMER
        ):
            WIN.blit(
                self.farmer_image,
                (
                    self.farmer.farmer_rect.x,
                    self.farmer.farmer_rect.y - GROUND_SIZE // 2,
                ),
            )
        else:
            WIN.blit(
                self.farmer_image,
                (self.farmer.farmer_rect.x, self.farmer.farmer_rect.y),
            )

        # draw inventory
        for i in range(len(self.inventory.inventory)):
            WIN.blit(
                INVENTORY_SQUARE,
                (
                    INVENTORY_START_WIDTH + (i * GROUND_SIZE),
                    INVENTORY_START_HEIGHT,
                ),
            )
        self.draw_inventory_items()
        self.draw_equipped_square()
        pygame.display.update()
        if self.gamestate.is_water or self.gamestate.is_till:
            pygame.time.delay(250)
            self.gamestate.stop_watering()
            self.gamestate.stop_tilling()

    def day_change(self):
        WIN.fill(BLACK)

        pygame.display.update()
        # print("called day change")