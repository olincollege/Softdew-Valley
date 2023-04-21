import pygame
import os


class Farmer:
    FARMER_WIDTH = 50
    FARMER_HEIGHT = 120
    VEL = 5
    WIDTH, HEIGHT = 900, 500

    farmer_width, farmer_height = 40, 60
    farmer_rect = pygame.Rect(100, 100, farmer_width, farmer_height)
    direction = "down"  # random direction to start
    # position is the (x, y) or (row, col) position of the farmer on the map
    position = (100 / 50, 100 / 50)

    def __init__():
        pass

    def move(self, keys):
        if keys[pygame.K_a] and self.farmer_rect.x - self.VEL > 0:  # LEFT
            self.farmer_rect.x -= self.VEL
            self.direction = "left"
        if (
            keys[pygame.K_d]
            and self.farmer_rect.x - self.VEL + self.farmer_rect.width
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
        self.position = (self.farmer_rect.x // 50, self.farmer_rect.y // 50)

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

    def till_ground(self):
        """
        If the hoe is equipped, use it to till the ground in front of the
        farmer
        """

    def water_crops(self):
        """
        If the watering can is equipped, use it to water crops in front of the
        farmer
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
