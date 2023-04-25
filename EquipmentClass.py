import pygame
import os
from ViewClass import View

INVENTORY_ITEM_SIZE = View.INVENTORY_ITEM_SIZE


class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Attributes:
        inventory_slot: an int that represents the inventory location
        equipped: a boolean that shows whether the item is equipped or not
    """

    def __init__(self, slot):
        self._equipped = False
        self._inventory_slot = slot
        self._pg_image = None

    def update_inventory_slot(self, new_slot):
        """
        Update the inventory_slot attribute if the item is moved
        """
        self._inventory_slot = new_slot

    def update_image(self, link):
        self._pg_image = pygame.transform.scale(
            pygame.image.load(link),
            (INVENTORY_ITEM_SIZE, INVENTORY_ITEM_SIZE),
        )

    @property
    def equipped(self):
        return self._equipped

    @property
    def inventory_slot(self):
        return self._inventory_slot

    @property
    def pg_image(self):
        return self._pg_image


class WateringCan(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__()
        self.update_inventory_slot(slot)
        self.update_image(os.path.join("Assets", "Watering_Can.png"))


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__()
        self.update_inventory_slot(slot)
        self.update_image(os.path.join("Assets", "Axe.png"))


class Seeds(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__()
        self.update_inventory_slot(slot)
        self.update_image(os.path.join("Assets", "Parsnip_Seeds.png"))
