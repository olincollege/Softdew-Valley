"""
File contains class and related methods for the farmer (player character)
"""
import pygame
import viewclass

# Sizing values come from viewclass file
FARMER_WIDTH = viewclass.FARMER_WIDTH
FARMER_HEIGHT = viewclass.FARMER_HEIGHT
VEL = 5
WIDTH, HEIGHT = viewclass.WIDTH, viewclass.HEIGHT
SQUARE_SIZE = viewclass.GROUND_SIZE
FARMER_WIDTH, FARMER_HEIGHT = (
    viewclass.FARMER_WIDTH,
    viewclass.FARMER_HEIGHT,
)


class Farmer:
    """
    Class representing the farmer playable character

    Attributes:
        direction: a String representing which direction the farmer is facing
        position: A tuple representing the map position of the farmer (row, col)
    """

    def __init__(self):
        self.start_square_x = 2
        self.start_square_y = 2
        self.farmer_rect = pygame.Rect(
            self.start_square_x * SQUARE_SIZE,
            self.start_square_y * SQUARE_SIZE,
            FARMER_WIDTH,
            FARMER_HEIGHT,
        )
        self._direction = "down"  # random direction to start
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)

    def set_position(self, x_val, y_val):
        """
        Set the row, col position of the farmer on the map

        Args:
            x_val: an int representing the row of the map the farmer is on
            y_val: an int representing the column of the map the farmer is on
        """
        self._position = (x_val, y_val)

    def set_direction(self, direction):
        """
        Set the direction the farmer is facing

        Args:
            direction: A String representing the direction the farmer is facing
        """
        self._direction = direction

    def redraw_farmer(self):
        self.farmer_rect = pygame.Rect(
            self.start_square_x * SQUARE_SIZE,
            self.start_square_y * SQUARE_SIZE,
            FARMER_WIDTH,
            FARMER_HEIGHT,
        )  # it would be cool if the farmer respawned next to the bed instead
        self._direction = "down"  # random direction to start
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)

    @property
    def direction(self):
        """
        Return the value of the direction attribute (string)
        """
        return self._direction

    @property
    def position(self):
        """
        Return the value of the position attribute (tuple containing two ints
        """
        return self._position

    # DELETE BEFORE SUBMISSION IF NOT USED
    def add_funds(self, amount):
        """
        Add amount funds to the wallet attribute
        """

    def spend_funds(self, amount):
        """
        Subtract amount funds from the wallet attribute
        Return True if that transaction is successful, return False if the
        farmer does not have enough money and do not subtract funds
        """
