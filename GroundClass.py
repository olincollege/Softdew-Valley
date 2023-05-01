import ViewClass
from plants import Plants
from audio import play_sound

WIDTH, HEIGHT = ViewClass.WIDTH, ViewClass.HEIGHT
SQUARE_SIZE = ViewClass.GROUND_SIZE


class Ground:
    """
    A class that represents the map of the game

    Attributes:
        free_land: A string representing a free space of land
        tilled_land: A string representing a tilled space of land
        watered_land: A string representing a space of land that is watered
        land: a nested list that represents all the spaces of land on the map
    """

    _free_land = ""
    _tilled_land = "T"
    _watered_land = "W"

    num_rows = WIDTH // SQUARE_SIZE
    num_cols = HEIGHT // SQUARE_SIZE

    def __init__(self):
        self.land = [
            [self._free_land for j in range(self.num_cols)]
            for i in range(self.num_rows)
        ]

    def day_passes(self):
        """
        Grows any watered plants and sets them back to unwatered when called
        """
        rows = self.num_rows
        cols = self.num_cols
        for j in range(cols):
            for i in range(rows):
                if isinstance(self.land[i][j], Plants):
                    self.land[i][j].grow()
        self.unwater_squares()

    def get_square(self, row, col):
        """
        Returns a square in the land attribute

        ARGS:
            row: an int representing the row index of the square in the array
            self.land
            col: an int representing the column index of the square in the
            array self.land
        """
        return self.land[row][col]

    def is_watered(self, square):
        """
        Returns a bool that says whether a square is watered

        ARGS:
            square: a string or instance of the class Plant representing the
            state of a particular tile of the game
            ("T" is tilled, "W" watered, a plant is an Plant instance)
        """
        if isinstance(square, str):
            return self._watered_land in square
        return square.water

    def is_tilled(self, square):
        """
        Returns a bool that says whether a square is tilled

        ARGS:
            square: a string or instance of the class Plant representing the
            state of a particular tile of the game
            ("T" is tilled, "W" watered, a plant is an Plant instance)
        """
        if isinstance(square, str):
            return self._tilled_land in square
        return True

    def has_crop(self, square):
        """
        Returns a bool that says whether a square has a crop on it

        ARGS:
            square: a string or instance of the class Plant representing the
            state of a particular tile of the game
            ("T" is tilled, "W" watered, a plant is an Plant instance)
        """
        return not isinstance(square, str)

    def water_square(self, row, col):
        """
        Update land to have a watered square at the row/col

        ARGS:
            row: an int representing the row index of the square in the array
            self.land being watered
            col: an int representing the column index of the square in the
            array self.land being watered
        """
        if isinstance(self.land[row][col], str):
            if not self.is_watered(self.land[row][col]):
                self.land[row][col] += self._watered_land
        else:
            self.land[row][col].plant_water()

    def unwater_squares(self):
        """
        Update watered crop land to revert the square back to tilled
        """
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if isinstance(self.land[i][j], Plants):
                    self.land[i][j].water = False

    def till_square(self, row, col):
        """
        Update land to have a tilled square at the row/col

        ARGS:
            row: an int representing the row index of the square in the array
            self.land being tilled
            col: an int representing the column index of the square in the
            array self.land being tilled
        """
        self.land[row][col] = self._tilled_land

    def plant_crop(self, row, col, plant):
        """
        Update land to have a crop at the row/col

        ARGS:
            row: an int representing the row index of the square in the array
            self.land being planted on
            col: an int representing the column index of the square in the
            array self.land being planted on
            plant: an instance of the class Plant representing an individual
            plant
        """
        self.land[row][col] = plant

    def harvest(self, row, col):
        """
        Convert a planted square back to its watered or tilled state and play
        a harvesting sound

        ARGS:
            row: an int representing the row index of the square in the array
            self.land being harvested
            col: an int representing the column index of the square in the
            array self.land being harvested
        """
        play_sound("harvest", 3)
        if self.land[row][col].water:
            self.land[row][col] = "W"
        else:
            self.till_square(row, col)

        if isinstance(self.land[row][col], type):
            print("uh oh, harvest in groundclass says this square is a class")
        if isinstance(self.land[row][col], Plants):
            print("for some reason, this square is still a plant.")
