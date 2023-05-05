"""
File contains class and related methods for the farmer (player character)
"""
import pygame
import constants

# Sizing values come from viewclass file
FARMER_WIDTH = constants.FARMER_WIDTH
FARMER_HEIGHT = constants.FARMER_HEIGHT
WIDTH, HEIGHT = constants.WIDTH, constants.HEIGHT
SQUARE_SIZE = constants.GROUND_SIZE
FARMER_WIDTH, FARMER_HEIGHT = (
    constants.FARMER_WIDTH,
    constants.FARMER_HEIGHT,
)


class Farmer:
    """
    Class representing the farmer playable character

    Attributes:
        start_square_x: an int representing the x square the farmer starts on
        start_square_y: an int representing the y square the farmer starts on
        farmer_rect: a pygame rectangle that represents the farmer
        direction: a String representing which direction the farmer is facing
        position: A tuple representing the map position of the farmer (row, col)
        wallet: An int representing how much money the farmer has
        vel: An int representing the speed of the farmer
    """

    def __init__(self):
        self.start_square_x = 16
        self.start_square_y = 8
        self.farmer_rect = pygame.Rect(
            self.start_square_x * SQUARE_SIZE,
            self.start_square_y * SQUARE_SIZE,
            FARMER_WIDTH,
            FARMER_HEIGHT,
        )
        self._direction = "down"  # random direction to start
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)
        self.wallet = 0
        self.vel = 5

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

    def respawn_farmer(self):
        """
        Resets the farmer to starting position and direction when a day passes
        """
        self.farmer_rect = pygame.Rect(
            self.start_square_x * SQUARE_SIZE,
            self.start_square_y * SQUARE_SIZE,
            FARMER_WIDTH,
            FARMER_HEIGHT,
        )
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)
        self._direction = "down"

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

        Args:
            amount: an int representing the amount of money added to the wallet
        """
        self.wallet += amount

    def spend_funds(self, amount):
        """
        Subtract amount funds to the wallet attribute

        Args:
            amount: an int representing the amount of money subtracted from the
            wallet

        Returns:
            Returns True if the wallet has enough money to subtract from, false
            otherwise
        """
        if self.wallet - amount >= 0:
            self.wallet -= amount
            return True
        return False
