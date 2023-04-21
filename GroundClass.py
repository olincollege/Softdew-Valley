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
    num_rows = 18  # depends on width and square size, make dynamic later
    num_cols = 10  # depends on width and square size, make dynamic later
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
        return square == self._watered_land

    def is_tilled(self, square):
        """
        Returns a bool that says whether a square is tilled
        """
        return square == self._tilled_land

    def has_crop(self, square):
        """
        Returns a bool that says whether a square has a crop on it
        """

    def water_square(self, row, col):
        """
        Update land to have a watered square at the row/col
        """
        self.land[row][col] = self._watered_land

    def til_square(self, row, col):
        """
        Update land to have a tilled square at the row/col
        """
        self.land[row][col] = self._tilled_land

    def plant_crop(self, row, col):
        """
        Update land to have a crop at the row/col
        """

    # @property
    # def land(self):
    #     return self.land

    # @property
    # def num_rows(self):
    #     return self.num_rows

    # @property
    # def num_cols(self):
    #     return self.num_cols
