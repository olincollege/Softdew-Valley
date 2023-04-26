"""
House Class
"""
import Day_Class

class House:
    """
    Class used to sleep. When you interact with (enter) the house it means you
    sleep and a day passes.

    Attributes:
        _house_squares: String representing squares that are house squares.

    """

    def __init__(self):
        """
        Creates house attribute which contains house squares.
        """

        self._house = ["H","H","H"] #don't think this is right 

    def enter_house(self):
        """
        When the player steps on one of the house squares they "enter" the
        house and that triggers the player to sleep and start a new day.
        """
        if #current_square = self._house  ??not sure 
            self._day_number = self._day_number + 1
