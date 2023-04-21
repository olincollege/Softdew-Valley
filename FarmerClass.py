import pygame
import os


class Farmer:
    FARMER_WIDTH = 35
    FARMER_HEIGHT = 70
    VEL = 5
    WIDTH, HEIGHT = 900, 500

    farmer_width, farmer_height = 40, 60
    farmer_rect = pygame.Rect(40, 40, farmer_width, farmer_height)
    direction = "up"

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

    @property
    def direction(self):
        return self.direction

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

    def get_position(self):
        """
        Return the row and column of the square the farmer is currently
        occupying
        """
