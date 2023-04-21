
class Ground:
    """
    A class that represents the map of the game

    Attributes:
        free_land: A string representing a free space of land
        tilled_land: A string representing a tilled space of land
        crop_land: A string representing a space of land that has a crop on it
        watered_land: A string representing a space of land that is watered
        land: a nested list that represents all the spaces of land on the map
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
        """
        Returns a square in the land attribute
        """
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
