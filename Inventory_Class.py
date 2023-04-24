"""
Inventory_Class
"""


class Inventory:
    """
    Class that creates the inventory for the game.

    Attributes:
        _inventory: list of strings representing the current state of the
        inventory
        empty_slot: a String that represents an empty inventory slot
    """

    empty_slot = " "

    def __init__(self, watering_can, hoe, seeds):
        """
        Initializes _inventory attribute so that it starts as a list of empty
        strings to represent the initial state of the inventory being empty
        """
        self._inventory = [self.empty_slot for i in range(8)]
        self._inventory[0] = watering_can
        self._inventory[1] = hoe
        self._inventory[2] = seeds

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
