import pygame
from ViewClass import View


class Farmer:
    FARMER_WIDTH = View.FARMER_WIDTH
    FARMER_HEIGHT = View.FARMER_HEIGHT
    VEL = 5
    WIDTH, HEIGHT = View.WIDTH, View.HEIGHT
    SQUARE_SIZE = View.GROUND_SIZE

    FARMER_WIDTH, FARMER_HEIGHT = View.FARMER_WIDTH, View.FARMER_HEIGHT
    start_square_x = 2
    start_square_y = 2
    farmer_rect = pygame.Rect(
        start_square_x * SQUARE_SIZE,
        start_square_y * SQUARE_SIZE,
        FARMER_WIDTH,
        FARMER_HEIGHT,
    )
    direction = "down"  # random direction to start
    # position is the (x, y) or (row, col) position of the farmer on the map
    position = (start_square_x, start_square_y)

    def __init__(self):
        # self.start_square_x = 2
        # self.start_square_y = 2
        # self.farmer_rect = pygame.Rect(
        #     self.start_square_x * self.SQUARE_SIZE,
        #     self.start_square_y * self.SQUARE_SIZE,
        #     self.FARMER_WIDTH,
        #     self.FARMER_HEIGHT,
        # )
        # self._direction = "down"  # random direction to start
        # # position is the (x, y) or (row, col) position of the farmer on the map
        # self._position = (self.start_square_x, self.start_square_y)
        pass

    def move(self, keys):
        if keys[pygame.K_a] and self.farmer_rect.x - self.VEL > 0:  # LEFT
            self.farmer_rect.x -= self.VEL
            self.direction = "left"
        if (
            keys[pygame.K_d]
            and self.farmer_rect.x - self.VEL + self.farmer_rect.width + 10
            < self.WIDTH
        ):  # RIGHT
            self.farmer_rect.x += self.VEL
            self.direction = "right"
        if keys[pygame.K_w] and self.farmer_rect.y - self.VEL > 0:  # UP
            self.farmer_rect.y -= self.VEL
            self.direction = "up"
        if (
            keys[pygame.K_s]
            and self.farmer_rect.y + self.VEL + self.farmer_rect.height
            < self.HEIGHT
        ):  # DOWN
            self.farmer_rect.y += self.VEL
            self.direction = "down"
        self.position = (
            (self.farmer_rect.x + self.FARMER_WIDTH // 2) // self.SQUARE_SIZE,
            (self.farmer_rect.y + self.FARMER_HEIGHT // 2) // self.SQUARE_SIZE,
        )

    @property
    def direction(self):
        return self.direction

    @property
    def position(self):
        return self.position

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
