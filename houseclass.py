"""
House Class
"""
# No pygame module has its member
# pylint: disable=no-member
import pygame
import viewclass

ENTER_HOUSE = pygame.USEREVENT + 2
ENTER_BED = pygame.USEREVENT + 3
HOUSE_SIZE = viewclass.HOUSE_SIZE


class House:
    """
    Class used to sleep. When you interact with (enter) the house it means you
    sleep and a day passes.

    Attributes:
        _house_squares: String representing squares that are house squares.

    """

    WIDTH, HEIGHT = viewclass.WIDTH, viewclass.HEIGHT
    house_start_x = WIDTH - HOUSE_SIZE
    house_start_y = 0
    house_rect = pygame.Rect(
        house_start_x, house_start_y, HOUSE_SIZE, HOUSE_SIZE
    )

    bed_x = house_start_x + 3 * HOUSE_SIZE // 4
    bed_y = house_start_y + 5 * HOUSE_SIZE // 8
    bed_rect = pygame.Rect(bed_x, bed_y, HOUSE_SIZE // 4, 5 * HOUSE_SIZE // 16)

    def __init__(self):
        """
        Creates house attribute which contains house squares.
        """

        self._house = ["H", "H", "H"]  # don't think this is right

    def enter_house(self, farmer):
        """
        When the player steps on one of the house squares they "enter" the
        house, triggering the house to render around them
        """  # If we decide to implement Jun's suggestion, edit main.py
        collide = pygame.Rect.colliderect(self.house_rect, farmer.farmer_rect)
        if collide:
            pygame.event.post(pygame.event.Event(ENTER_HOUSE))
            # self._day_number = self._day_number + 1

    def enter_bed(self, farmer):
        """
        When a player touches the bed in the house, it triggers the player to
        sleep and start a new day.
        """
        collide = pygame.Rect.colliderect(self.bed_rect, farmer.farmer_rect)
        if collide:
            pygame.event.post(pygame.event.Event(ENTER_BED))
            # self._day_number = self._day_number + 1
