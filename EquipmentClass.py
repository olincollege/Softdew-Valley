import pygame
import os
from ViewClass import View
import random

INVENTORY_ITEM_SIZE = View.INVENTORY_ITEM_SIZE

# LOOK INTO WHETHER WE SHOULD ACTUALLY BE ASSIGNING SLOT HERE
class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Attributes:
        inventory_slot: an int that represents the inventory location
        equipped: a boolean that shows whether the item is equipped or not
    """

    def __init__(self, gamestate=None):
        self._equipped = False
        # self._inventory_slot = slot
        self._pg_image = None
        self._gamestate = gamestate

    # def update_inventory_slot(self, new_slot):
    #     """
    #     Update the inventory_slot attribute if the item is moved

    #     Args:
    #         new_slot: An int representing the slot the item is being moved to
    #     """
    #     self._inventory_slot = new_slot

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

    # @property
    # def inventory_slot(self):
    #     return self._inventory_slot

    @property
    def pg_image(self):
        return self._pg_image


class WateringCan(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, gamestate):
        super().__init__(gamestate)
        self.update_image(os.path.join("Assets/equipment", "watering_can.png"))

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

    def __init__(self, gamestate):
        super().__init__(gamestate)
        self.update_image(os.path.join("Assets/equipment", "hoe.png"))

    def action(self):
        """
        Till the ground
        """
        self._gamestate.till_ground()
        pygame.mixer.Sound.play(
            pygame.mixer.Sound(
                os.path.join("Assets/sound_bites/hoeing_sound.wav")
            )
        )


class Seed(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, gamestate, seed_type):
        super().__init__(gamestate)
        self.seed_type = seed_type
        self.update_image(
            os.path.join("Assets/seeds", f"{seed_type}_seeds.png")
        )

    def action(self):
        """
        Plant a seed
        """
        # self._gamestate.harvest_crop()
        self._gamestate.plant_seed(self.seed_type)


class ParsnipSeeds(Seed):
    """Class representing parsnip seeds"""

    def __init__(self, gamestate):
        super().__init__(gamestate, "parsnip")


class CauliflowerSeeds(Seed):
    """Class representing cauliflower seeds"""

    def __init__(self, gamestate):
        super().__init__(gamestate, "cauliflower")


class Crop(Equipment):
    """
    Class representing the different crops a player can hold in their inventory
    """

    def __init__(self, crop_type, price):
        super().__init__()
        self.update_image(os.path.join("Assets/crops", f"{crop_type}.png"))
        self.price = price


class Parsnip_Crop(Crop):
    """Class representing sellable parsnip inventory item"""

    def __init__(self):
        super().__init__("parsnip", 35)


class Cauliflower_Crop(Crop):
    """Class representing sellable parsnip inventory item"""

    def __init__(self):
        super().__init__("cauliflower", 175)
