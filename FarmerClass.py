import pygame
from ViewClass import View


class Farmer:
    FARMER_WIDTH = View.FARMER_WIDTH
    FARMER_HEIGHT = View.FARMER_HEIGHT
    VEL = 5
    WIDTH, HEIGHT = View.WIDTH, View.HEIGHT
    SQUARE_SIZE = View.GROUND_SIZE
    FARMER_WIDTH, FARMER_HEIGHT = View.FARMER_WIDTH, View.FARMER_HEIGHT

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

    def update_position(self, x, y):
        self._position = (x, y)

    def update_direction(self, direction):
        self._direction = direction

    @property
    def direction(self):
        return self._direction

    @property
    def position(self):
        return self._position

    def harvest_crops(self):
        """
        Harvest fully grown crops and store them in the inventory
        """

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
