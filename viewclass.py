"""
Handles all in-game views/displays
"""
import os
import random
import pygame

import constants

pygame.font.init()

# Setting constants to be used throughout the file
FARMER_WIDTH = constants.FARMER_WIDTH
FARMER_HEIGHT = constants.FARMER_HEIGHT
GROUND_SIZE = constants.GROUND_SIZE
WIDTH, HEIGHT = constants.WIDTH, constants.HEIGHT
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
INVENTORY_ITEM_SIZE = constants.INVENTORY_ITEM_SIZE
INVENTORY_FONT = pygame.font.Font("Assets/stardew_font.ttf", 16)
WALLET_FONT = pygame.font.Font("Assets/stardew_font.ttf", 24)
HOUSE_SIZE = constants.HOUSE_SIZE
SHIPPING_BIN_WIDTH, SHIPPING_BIN_HEIGHT = (
    constants.SHIPPING_BIN_WIDTH,
    constants.SHIPPING_BIN_HEIGHT,
)
CONTROL_WIDTH = constants.CONTROL_WIDTH
CONTROL_HEIGHT = constants.CONTROL_HEIGHT

COIN_SIZE = constants.COIN_SIZE
STAND_WIDTH, STAND_HEIGHT = constants.STAND_WIDTH, constants.STAND_HEIGHT
STAND_START_WIDTH = constants.STAND_START_WIDTH
STAND_START_HEIGHT = constants.STAND_START_HEIGHT

STORE_RECT_WIDTH, STORE_RECT_HEIGHT = (
    constants.STORE_RECT_WIDTH,
    constants.STORE_RECT_HEIGHT,
)
STORE_RECT_START_WIDTH = constants.STORE_RECT_START_WIDTH
STORE_RECT_START_HEIGHT = constants.STORE_RECT_START_HEIGHT
STORE_RECT_PADDING = constants.STORE_RECT_PADDING
# Setting color values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_COLOR = (0, 0, 0)
SELECTION_BOX_COLOR = (244, 88, 66)

# Setting inventory position values
INVENTORY_START_WIDTH = constants.INVENTORY_START_WIDTH
INVENTORY_START_HEIGHT = constants.INVENTORY_START_HEIGHT

# Setting shipping bin starting positions
BIN_START_W, BIN_START_H = constants.BIN_START_W, constants.BIN_START_H


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


# CONTROL SCREEN
CONTROL_SCREEN = pygameify_image(
    "", "controls_screen.png", CONTROL_WIDTH, CONTROL_HEIGHT
)

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
def randomize_free_ground():
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
    free_ground_map = [
        [None] * (HEIGHT // GROUND_SIZE) for _ in range(WIDTH // GROUND_SIZE)
    ]
    # Define the corresponding probabilities for each ground file
    probabilities = [0.82, 0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.02]
    for i in range(WIDTH // GROUND_SIZE):
        for j in range(HEIGHT // GROUND_SIZE):
            free_ground_map[i][j] = pygameify_image(
                "ground/free_ground_versions",
                f"free_ground{random.choices(range(9), probabilities)[0]}.png",
                GROUND_SIZE,
                GROUND_SIZE,
            )
    return free_ground_map


ground_map = randomize_free_ground()

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

# SHIPPING BIN SPRITES
CLOSED_SHIPPING_BIN = pygameify_image(
    "", "Closed_Shipping_Bin.png", SHIPPING_BIN_WIDTH, SHIPPING_BIN_HEIGHT
)
OPEN_SHIPPING_BIN = pygameify_image(
    "", "Open_Shipping_Bin.png", SHIPPING_BIN_WIDTH, SHIPPING_BIN_HEIGHT
)

# COIN IMAGE
COIN = pygameify_image("", "olin_coin.png", COIN_SIZE, COIN_SIZE)

# SHOP IMAGE
STAND = pygameify_image("stand", "shop.png", STAND_WIDTH, STAND_HEIGHT)

PARSNIP_RECT = pygameify_image(
    "stand", "parsniprectangle.png", STORE_RECT_WIDTH, STORE_RECT_HEIGHT
)
CAULIFLOWER_RECT = pygameify_image(
    "stand", "cauliflowerrectangle.png", STORE_RECT_WIDTH, STORE_RECT_HEIGHT
)
POTATO_RECT = pygameify_image(
    "stand", "potatorectangle.png", STORE_RECT_WIDTH, STORE_RECT_HEIGHT
)

STORE_ITEMS = [PARSNIP_RECT, CAULIFLOWER_RECT, POTATO_RECT]


class View:  # pylint: disable=too-many-instance-attributes
    """
    Class that handles displaying the game

    Attributes:
        farmer: the Farmer instance being displayed
        ground: the Ground instance being displayed
        inventory: the inventory of the player being displayed
        farmer_image: the sprite of the farmer being displayed
        type_ground: the image of the ground square being displayed
        plant_image: the sprite of the plant being displayed
    """

    def __init__(self, model):
        self.model = model
        self.farmer = self.model.farmer
        self.ground = self.model.ground
        self.inventory = self.model.inventory
        self.stand = self.model.stand
        self.farmer_image = None
        self.type_ground = None
        self.plant_image = None

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
            if self.model.is_water
            else "till"
            if self.model.is_till
            else False
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
            self.type_ground = ground_map[row][col]

    def draw_stand(self):
        """
        Draw stand sprite at stand position
        """
        WIN.blit(STAND, (STAND_START_WIDTH, STAND_START_HEIGHT))

    def draw_stand_items(self):
        """
        Draw rectangles for each item in the shop
        """
        for idx, _ in enumerate(self.stand.stock_list):
            # blit rectangle at idx * whatever for height
            WIN.blit(
                STORE_ITEMS[idx],
                (
                    STORE_RECT_START_WIDTH,
                    STORE_RECT_START_HEIGHT + STORE_RECT_HEIGHT * idx,
                ),
            )

    def draw_inventory_items(self):
        """
        Draw items into the inventory
        """
        for idx, item in enumerate(self.inventory.inventory):
            paddingx = 3
            paddingy = 5
            if not isinstance(item, str):  # item type is not a string:
                WIN.blit(
                    item.pg_image,
                    (
                        INVENTORY_START_WIDTH + (idx * GROUND_SIZE) + paddingx,
                        INVENTORY_START_HEIGHT + paddingy,
                    ),
                )
                if item.num_item is not None:
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

    def draw_wallet(self):
        """
        Display the farmer wallet
        """
        wallet_text = str(self.farmer.wallet)
        draw_text = WALLET_FONT.render(wallet_text, 1, FONT_COLOR)
        text_height = draw_text.get_height()
        coin_padding = 10
        text_padding = 50
        padding = 13
        WIN.blit(draw_text, (text_padding, HEIGHT - text_height - padding))
        WIN.blit(COIN, (padding, HEIGHT - coin_padding - COIN_SIZE))

    def draw_shipping_bin(self):
        """
        Draw the shipping bin at the shipping bin position
        If the farmer is close enough to the shipping bin, make the shipping
        bin open
        """
        if (
            self.farmer.position[0] <= constants.SHIPPING_BIN_SQUARES
            and self.farmer.position[1] <= constants.SHIPPING_BIN_SQUARES
        ):
            bin_sprite = OPEN_SHIPPING_BIN
        else:
            bin_sprite = CLOSED_SHIPPING_BIN

        # draw shipping bin
        WIN.blit(bin_sprite, (BIN_START_W, BIN_START_H))

    def draw_selling_crop(self):
        """
        Draw an image of the crop being sold over the shipping bin when it
        is being sold
        """
        crop = self.model.display_crop
        padding = 20
        if crop is not None:
            WIN.blit(
                crop.pg_image,
                (
                    BIN_START_W + SHIPPING_BIN_WIDTH // 2 - padding,
                    BIN_START_H + padding,
                ),
            )
            pygame.display.update()
            pygame.time.delay(250)
            self.model.stop_selling()

    def draw_ground_plants(self):
        """
        Draw the ground and the plants in the window
        """
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                self.ground_type(i, j)
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

    def draw_farmer(self):
        """
        Draw the farmer
        The farmer sprite changes depending on the direction the farmer is
        facing and the action they are performing
        """
        self.farmer_direction()
        if self.farmer_image in (WATER_LEFT_FARMER, TILL_LEFT_FARMER):
            WIN.blit(
                self.farmer_image,
                (
                    self.farmer.farmer_rect.x - GROUND_SIZE,
                    self.farmer.farmer_rect.y,
                ),
            )
        elif self.farmer_image in (TILL_BACK_FARMER, WATER_FRONT_FARMER):
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

    def draw_window(self, control_screen):
        """
        Draws the entire pygame window every time it is called
        (ground, plants, house, farmer, inventory, and inventory text)

        Args:
            control_screen: A boolean that determines whether the control
            screen graphic should be blitted or not
        """
        WIN.fill(WHITE)

        # draw ground and plants
        self.draw_ground_plants()

        # draw house
        WIN.blit(HOUSE_SPRITE, (WIDTH - HOUSE_SIZE, 0))

        # draw shipping bin
        self.draw_shipping_bin()

        # draw stand
        self.draw_stand()

        # draw farmer
        self.draw_farmer()

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
        self.draw_wallet()
        # draw crop when sold
        if self.model.selling_crop:
            self.draw_selling_crop()
            pygame.time.delay(250)
        # draw control screen
        if control_screen:
            WIN.blit(
                CONTROL_SCREEN,
                (
                    WIDTH // 2 - CONTROL_WIDTH // 2,
                    HEIGHT // 2 - CONTROL_HEIGHT // 2,
                ),
            )
        if self.model.in_store:
            self.draw_stand_items()
        pygame.display.update()

        if self.model.is_water or self.model.is_till or self.model.selling_crop:
            pygame.time.delay(250)
            self.model.stop_watering()
            self.model.stop_tilling()
            self.model.stop_selling()

    def day_change(self):
        """
        Fill the screen with black when a day passes
        """
        WIN.fill(BLACK)

        pygame.display.update()
