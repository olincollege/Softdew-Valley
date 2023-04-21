"""
Inventory_Class
"""
import farmer


class Inventory:
    """
    Class that creates the inventory for the game.

    Attributes:
        _inventory: list of strings representing the current state of the
        inventory
        empty_slot: a String that represents an empty inventory slot
    """

    empty_slot = " "

    def __init__(self):
        """
        Initializes _inventory attribute so that it starts as a list of empty
        strings to represent the initial state of the inventory being empty
        """

        _inventory = [self.empty_slot for i in range(8)]  # list of 8 items
        _inventory[0] = farmer.WateringCan()
        _inventory[1] = farmer.Hoe()
        _inventory[2] = farmer.Seeds()

    def equip_item(self, slot):
        """
        Equip the item in the specified inventory slot
        """
        pass

    def add_item(self, slot, item):
        """
        Function used to add an item to the player's inventory.

        Args:
            slot: integer representing what slot of the inventory to put the
            item in
            item: ?class? representing the item to put in the specified
            inventory spot
        """
        pass

    def __repr__(self):
        """
        Determines how the inventory game should be displayed given the current
        state of the player's inventory.

        Returns: A string representing the current state of the player's
        inventory
        """
        pass
