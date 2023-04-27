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

    def __init__(self, slot, gamestate):
        self._equipped = False
        self._inventory_slot = slot
        self._pg_image = None
        self._gamestate = gamestate

    def update_inventory_slot(self, new_slot):
        """
        Update the inventory_slot attribute if the item is moved

        Args:
            new_slot: An int representing the slot the item is being moved to
        """
        self._inventory_slot = new_slot

    def update_image(self, link):
        """
        Generate the image for an item

        Args:
            link: A string representing the location of the item image
        """
        self._pg_image = pygame.transform.scale(
            pygame.image.load(link),
            (INVENTORY_ITEM_SIZE, INVENTORY_ITEM_SIZE),
        )

    def equip(self):
        """
        Equip an item
        """
        self._equipped = True

    def unequip(self):
        """
        Unequip an item
        """
        self._equipped = False

    def action(self):
        """
        Perform the action of an item
        """
        pass

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

    def __init__(self, slot, gamestate):
        super(Equipment, self).__init__()
        self._equipped = False
        self.update_inventory_slot(slot)
        self.update_image(os.path.join("Assets/equipment", "watering_can.png"))
        self._gamestate = gamestate

    def action(self):
        """
        Water the ground
        """
        self._gamestate.water_ground()


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot, gamestate):
        super(Equipment, self).__init__()
        self._equipped = False
        self.update_inventory_slot(slot)
        self.update_image(os.path.join("Assets/equipment", "hoe.png"))
        self._gamestate = gamestate

    def action(self):
        """
        Till the ground
        """
        self._gamestate.till_ground()


class Seed(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot, gamestate, seed_type):
        super(Equipment, self).__init__()
        self._equipped = False
        self.seed_type = seed_type
        self.update_inventory_slot(slot)
        self.update_image(
            os.path.join("Assets/seeds", f"{seed_type}_seeds.png")
        )
        self._gamestate = gamestate

    def action(self):
        """
        Plant a seed
        """
        self._gamestate.harvest_crop()
        self._gamestate.plant_seed()


class ParsnipSeeds(Seed):
    """Class respresenting parsnip seeds"""

    def __init__(self, slot, gamestate):
        super().__init__(slot, gamestate, "parsnip")


class CauliflowerSeeds(Seed):
    """Class representing cauliflower seeds"""

    def __init__(self, slot, gamestate):
        super().__init__(slot, gamestate, "cauliflower")
