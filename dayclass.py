"""
Updates the in-game day
"""


class Day:
    """
    Class that keeps track of how many days have passed based on when you've
    slept.

    Attributes:
        day_number = integer representing the number of the day that the game
        is on.
    """

    def __init__(self):
        """
        Create an initial day to be day 1 when you start the game
        """
        self._day_number = 1

    def add_day(self):
        """
        When the player goes to sleep add a day to day_number
        """
        self._day_number += 1

    def fetch_day(self):
        """
        Returns a copy of the private day_number attribute
        """
        return self._day_number

    def update_game_state(self):
        """
        Updates all the tiles when the player goes to sleep
        """
