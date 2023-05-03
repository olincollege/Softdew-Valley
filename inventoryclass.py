"""
Class that keeps track of the player's inventory
"""
from audio import play_sound


class Inventory:
    """
    Class that creates the inventory for the game.

    Attributes:
        empty_slot: a String that represents an empty inventory slot
        inventory: a list that holds different instances from the Equipment
        class for each item in the inventory
    """

    empty_slot = " "

    def __init__(self, watering_can, hoe, parsnipseeds, cauliflowerseeds):
        """
        Initializes _inventory attribute so that it starts as a list of empty
        strings to represent the initial state of the inventory being empty
        Adds items that the player starts with
        """
        self._inventory = [self.empty_slot for i in range(8)]
        self._inventory[0] = watering_can
        self._inventory[1] = hoe
        self._inventory[2] = parsnipseeds
        self._inventory[3] = cauliflowerseeds

    def equip_item(self, slot):
        """
        Equip the item in the specified inventory slot

        Args:
            slot: An int representing the slot of the item being equipped
        """
        item = self._inventory[slot]
        if not isinstance(item, str):
            item.equip()
            play_sound("inventory_swap")

    def get_equipped_item(self):
        """
        Return the equipped item in the inventory
        If nothing is equipped return None
        """
        for item in self.inventory:
            if not isinstance(item, str):
                if item.equipped:
                    return item
        return None

    def get_equipped_item_slot(self):
        """
        Return the slot of the equipped item in the inventory
        If nothing is equipped return None
        """
        for idx, item in enumerate(self.inventory):
            if not isinstance(item, str):
                if item.equipped:
                    return idx
        return None

    def get_item(self, slot):
        """
        Get an item at the specified inventory slot

        Args:
            slot: int representing an inventory slot
        """
        return self.inventory[slot]

    def add_item(self, slot, item):
        """
        Function used to add an item to the player's inventory.

        Args:
            slot: integer representing what slot of the inventory to put the
            item in
            item: An instance of the Equipment class representing the item to
            put in the specified inventory spot
        """
        self._inventory[slot] = item

    def first_empty_slot(self):
        """
        Returns the index of the first empty slot in the inventory
        If the inventory is full, returns none
        """
        for idx, item in enumerate(self._inventory):
            if isinstance(item, str):
                return idx
        return None

    @property
    def inventory(self):
        """
        Return the value of the inventory attribute (a list of Equipment
        instances)
        """
        return self._inventory
