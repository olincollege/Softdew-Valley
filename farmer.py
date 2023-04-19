class Farmer:
    """
    DOCSTRING
    """

    def __init__(self):
        pass

    def move(self):
        """
        Take wasd keyboard input from the user to move the farmer
        """
        # maybe move to control class?

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

    def wallet(self):
        """
        Keeps track of how much money the farmer has as an int
        """


class ViewFarmer:
    """
    DOCSTRING
    """

    def __init__(self, sprite_path):
        """
        Load sprite to represent farmer
        """


class WateringCan:
    """
    DOCSTRING
    """

    def __init__(self):
        pass

    def water(self):
        """
        Water space in front (display)
        """

    def is_equipped(self):
        """
        Returns a boolean stating whether the watering can is equipped or not
        """


class Hoe:
    """
    DOCSTRING
    """

    def __init__(self):
        pass

    def till(self):
        """
        Till the space in front (display)
        """

    def is_equipped(self):
        """
        Returns a boolean stating whether the hoe is equipped or not
        """


class Ground:
    """
    DOCSTRING
    """

    _free_land = ""
    _tilled_land = "T"
    _crop_land = "C"
    _watered_land = "W"

    def __init__(self):
        self.land = [
            [
                self._free_land,
                self._free_land,
                self._free_land,
                self._free_land,
            ],
            [
                self._free_land,
                self._free_land,
                self._free_land,
                self._free_land,
            ],
        ]  # etc.

    def get_square(self, row, col):
        """DOCSTRING"""
        return self.land[row][col]

    def is_watered(self, square):
        """
        Returns a bool that says whether a square is watered
        """
        if self._watered_land in square:
            return True
        return False

    def is_tilled(self, square):
        """
        Returns a bool that says whether a square is tilled
        """

    def has_crop(self, square):
        """
        Returns a bool that says whether a square has a crop on it
        """

    def water_square(self, row, col):
        """
        Update land to have a watered square at the row/col
        """
        self.land[row][col] += self._watered_land

    def til_square(self, row, col):
        """
        Update land to have a tilled square at the row/col
        """

    def plant_crop(self, row, col):
        """
        Update land to have a crop at the row/col
        """
