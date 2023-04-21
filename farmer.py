class Farmer:
    """
    A class that represents the player's farmer character

    Attributes:
        wallet: an int representing how much currency a player has
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

    def add_funds(self, amount):
        """
        Add amount funds to the wallet attribute
        """

    def spend_funds(self, amount):
        """
        Subtract amount funds from the wallet attribute
        Return True if that transaction is successful, return False if the
        farmer does not have enough money and do not subtract funds
        """

    def get_position(self):
        """
        Return the row and column of the square the farmer is currently
        occupying
        """

    def get_direction(self):
        """
        Return the direction that the farmer is facing
        """


class ViewFarmer:
    """
    Class that displays the farmer sprite
    """

    def __init__(self, sprite_path):
        """
        Load sprite to represent farmer
        """


# should do a parent class item/equipment class and have these inherit from
# that because they are pretty similar
class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self):
        pass

    def is_equipped(self):
        """
        Returns a boolean stating whether the item is equipped or not
        """

    def update_inventory_slot(self):
        """
        Update the inventory_slot attribute if the item is moved
        """


class WateringCan(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self):
        pass

    def water(self):
        """
        Water space in the direction the farmer is facing
        """


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self):
        pass

    def till(self):
        """
        Till the space in the direction the farmer is facing
        """


class Seeds(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self):
        pass

    def plant(self):
        """
        Plant the seed in the space in the direction the farmer is facing
        """


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
