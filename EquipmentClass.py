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