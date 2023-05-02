import pygame
import viewclass


class Farmer:
    FARMER_WIDTH = viewclass.FARMER_WIDTH
    FARMER_HEIGHT = viewclass.FARMER_HEIGHT
    VEL = 5
    WIDTH, HEIGHT = viewclass.WIDTH, viewclass.HEIGHT
    SQUARE_SIZE = viewclass.GROUND_SIZE
    FARMER_WIDTH, FARMER_HEIGHT = (
        viewclass.FARMER_WIDTH,
        viewclass.FARMER_HEIGHT,
    )

    def __init__(self):
        self.start_square_x = 2
        self.start_square_y = 2
        self.farmer_rect = pygame.Rect(
            self.start_square_x * self.SQUARE_SIZE,
            self.start_square_y * self.SQUARE_SIZE,
            self.FARMER_WIDTH,
            self.FARMER_HEIGHT,
        )
        self._direction = "down"  # random direction to start
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)

    def set_position(self, x, y):
        self._position = (x, y)

    def set_direction(self, direction):
        self._direction = direction

    def redraw_farmer(self):
        self.farmer_rect = pygame.Rect(
            self.start_square_x * self.SQUARE_SIZE,
            self.start_square_y * self.SQUARE_SIZE,
            self.FARMER_WIDTH,
            self.FARMER_HEIGHT,
        )
        self._direction = "down"  # random direction to start
        # position is the (x, y) or (row, col) position of the farmer on the map
        self._position = (self.start_square_x, self.start_square_y)

    @property
    def direction(self):
        return self._direction

    @property
    def position(self):
        return self._position

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
