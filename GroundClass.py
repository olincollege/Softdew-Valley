from ViewClass import View

WIDTH, HEIGHT = View.WIDTH, View.HEIGHT
SQUARE_SIZE = View.GROUND_SIZE


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

    num_rows = WIDTH // SQUARE_SIZE
    num_cols = HEIGHT // SQUARE_SIZE
    land = []

    def __init__(self):
        self.land = [
            [self._free_land for i in range(self.num_cols)]
            for j in range(self.num_rows)
        ]

    def get_square(self, row, col):
        """
        Returns a square in the land attribute
        """
        return self.land[row][col]

    def is_watered(self, square):
        """
        Returns a bool that says whether a square is watered
        """
        return self._watered_land in square

    def is_tilled(self, square):
        """
        Returns a bool that says whether a square is tilled
        """
        return self._tilled_land in square

    def has_crop(self, square):
        """
        Returns a bool that says whether a square has a crop on it
        """
        return self._crop_land in square

    def water_square(self, row, col):
        """
        Update land to have a watered square at the row/col
        """
        if not self.is_watered(self.land[row][col]):
            self.land[row][col] += self._watered_land

    def unwater_squares(self):
        """
        Update watered crop land to revert the square back to tilled
        """
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                if "C" in self.land[j][i]:
                    self.land[j][i] = self.land[j][i].replace("W", "T")

    def til_square(self, row, col):
        """
        Update land to have a tilled square at the row/col
        """
        self.land[row][col] = self._tilled_land

    def plant_crop(self, row, col):
        """
        Update land to have a crop at the row/col
        """
        if not self.has_crop(self.land[row][col]):
            self.land[row][col] += self._crop_land
