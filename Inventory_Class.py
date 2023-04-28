"""
Inventory_Class
"""
from ViewClass import View
import pygame

mixer_works = pygame.mixer.get_init()


class Inventory:
    """
    Class that creates the inventory for the game.

    Attributes:
        _inventory: list of strings representing the current state of the
        inventory
        empty_slot: a String that represents an empty inventory slot
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
        """
        item = self._inventory[slot]
        if not isinstance(item, str):
            item.equip()
            if mixer_works is not None:
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound("Assets/sound_bites/inventory_swap.wav")
                )

    def get_equipped_item(self):
        """Return the equipped item of inventory"""
        for item in self.inventory:
            if not isinstance(item, str):
                if item.equipped:
                    return item

    def get_equipped_item_slot(self):
        """Return the slot of the equipped item"""
        for idx, item in enumerate(self.inventory):
            if not isinstance(item, str):
                if item.equipped:
                    return idx

    def get_item(self, slot):
        """Get an item at the specified inventory slot"""
        return self.inventory[slot]

    def add_item(self, slot, item):
        """
        Function used to add an item to the player's inventory.

        Args:
            slot: integer representing what slot of the inventory to put the
            item in
            item: ?class? representing the item to put in the specified
            inventory spot
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

    def __repr__(self):
        """for debugging purposes"""
        return f"{self._inventory}"

    def control_inventory(self, mouse_pos=None, num=None):
        """click the thing and do the thing"""
        current_item = self.get_equipped_item()
        if current_item is not None:
            current_item.unequip()
        slot = num
        if mouse_pos is not None:
            mouse_posx = mouse_pos[0]
            for i in range(8):
                if mouse_posx > View.INVENTORY_START_WIDTH + (
                    i * View.GROUND_SIZE
                ) and mouse_posx < View.INVENTORY_START_WIDTH + (
                    (i + 1) * View.GROUND_SIZE
                ):
                    slot = i

        self.equip_item(slot)

    @property
    def inventory(self):
        return self._inventory
