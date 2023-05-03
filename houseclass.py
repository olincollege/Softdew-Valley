"""
House Class
"""
import pygame
import viewclass
from farmerclass import Farmer

ENTER_HOUSE = pygame.USEREVENT + 2
ENTER_BED = pygame.USEREVENT + 3 # put in main.py as an event
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

    # HOUSE WALLS
    # left_wall = pygame.Rect(
    #     house_start_x, house_start_y, HOUSE_SIZE // 16, HOUSE_SIZE
    # )
    # right_wall = pygame.Rect(
    #     house_start_x + 15 * HOUSE_SIZE // 16, house_start_y, 
    #     HOUSE_SIZE // 16, HOUSE_SIZE
    # )
    # top_wall = pygame.Rect(
    #     house_start_x, house_start_y, HOUSE_SIZE, HOUSE_SIZE // 16
    # )
    # bottom_wall_left = pygame.Rect(
    #     house_start_x, house_start_y - HOUSE_SIZE // 16, 
    #     # FILL IN, HOUSE_SIZE // 16
    # )
    # bottom_wall_right = pygame.Rect(
    #     # FILL IN, house_start_y - HOUSE_SIZE // 16,
    #     # FILL IN, HOUSE_SIZE // 16
    # )
    # door = pygame.Rect(
    #     # FILL IN, house_start_y - HOUSE_SIZE // 16,
    #     # FILL IN, HOUSE_SIZE // 16
    # )

    bed_x = house_start_x + 6 * HOUSE_SIZE // 8
    bed_y = house_start_y + 5 * HOUSE_SIZE // 8
    # WIDTH - 5 * HOUSE_SIZE // 16, 5 * HOUSE_SIZE // 8
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
        """ # If we decide to implement Jun's suggestion, edit main.py
        collide = pygame.Rect.colliderect(self.house_rect, farmer.farmer_rect)
        if collide:
            pygame.event.post(pygame.event.Event(ENTER_HOUSE))
            print("They've collided")
            # self._day_number = self._day_number + 1

    def enter_bed(self, farmer):
        """
        When a player touches the bed in the house, it triggers the player to
        sleep and start a new day.
        """
        collide = pygame.Rect.colliderect(self.bed_rect, farmer.farmer_rect)
        if collide:
            pygame.event.post(pygame.event.Event(ENTER_BED))
            print("They've collided")
            # self._day_number = self._day_number + 1

        