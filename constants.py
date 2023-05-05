"""Holds constant size and position values of the game"""

# Setting constants to be used throughout the file
FARMER_WIDTH = 45
FARMER_HEIGHT = 90
GROUND_SIZE = 50
WIDTH, HEIGHT = 1000, 600
INVENTORY_ITEM_SIZE = 40
HOUSE_SIZE = GROUND_SIZE * 8
SHIPPING_BIN_WIDTH, SHIPPING_BIN_HEIGHT = 102, 114
SHIPPING_BIN_SQUARES = 2

# Setting inventory position values
INVENTORY_START_WIDTH = WIDTH // 2 - GROUND_SIZE * 4
INVENTORY_START_HEIGHT = HEIGHT - GROUND_SIZE * 2

# Setting shipping bin starting positions
BIN_START_W, BIN_START_H = 20, 10

# Setting the size of control screen
CONTROL_WIDTH, CONTROL_HEIGHT = 768, 435

# Setting the size of coin image
COIN_SIZE = 30

STAND_START_WIDTH = GROUND_SIZE * 5
STAND_START_HEIGHT = 10
STAND_WIDTH, STAND_HEIGHT = 150, 150
STAND_INTERACTION_SQUARES_X = [
    4,
    5,
    6,
    7,
    8,
    9,
]  # cols you can interact with stand
STAND_INTERACTION_SQUARES_Y = [
    0,
    1,
    2,
    3,
    4,
]  # rows you can interact with stand

# Store retangles
STORE_RECT_WIDTH, STORE_RECT_HEIGHT = 800, 100
STORE_RECT_START_WIDTH = (WIDTH - STORE_RECT_WIDTH) // 2
STORE_RECT_START_HEIGHT = 20
STORE_RECT_PADDING = 50
