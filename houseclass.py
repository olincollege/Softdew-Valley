"""
House Class
"""
import pygame
from ViewClass import View
from farmerclass import Farmer


class House:
    """
    Class used to sleep. When you interact with (enter) the house it means you
    sleep and a day passes.

    Attributes:
        _house_squares: String representing squares that are house squares.

    """

    ENTER_HOUSE = pygame.USEREVENT + 2
    WIDTH, HEIGHT = View.WIDTH, View.HEIGHT
    house_start_square_x = WIDTH - 250
    house_start_square_y = 200
    house_rect = pygame.Rect(
        house_start_square_x, house_start_square_y, 250, 200
    )

    def __init__(self):
        """
        Creates house attribute which contains house squares.
        """

        self._house = ["H", "H", "H"]  # don't think this is right

    def enter_house(self):
        """
        When the player steps on one of the house squares they "enter" the
        house and that triggers the player to sleep and start a new day.
        """
        print("calling")
        collide = pygame.Rect.colliderect(self.house_rect, Farmer.farmer_rect)
        if collide:
            pygame.event.post(pygame.event.Event(self.ENTER_HOUSE))
            print("They've collided")
            # self._day_number = self._day_number + 1