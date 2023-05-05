"""
Holds all the different classes of items that can go in the inventory
"""
import os
import pygame
import constants

INVENTORY_ITEM_SIZE = constants.INVENTORY_ITEM_SIZE


class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Instance Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        num_item: an int representing the number of items of that instance
            (ex. holding ten parsnips)
    """

    def __init__(self):
        """
        Initialize Equipped to be false, and pg_image and num_item to be none.
        """
        self._equipped = False
        self._pg_image = None
        self._num_item = None

    def update_image(self, subfolder, image_name):
        """
        Generate the pygame image for an item

        Args:
            subfolder: A string representing the name of the subfolder of Assets
            that the image is in
            image_name: A string representing the name of the item image in the
            Assets/{subfolder} folder
        """
        self._pg_image = pygame.transform.scale(
            pygame.image.load(
                os.path.join(f"Assets", f"{subfolder}", f"{image_name}")
            ),
            (INVENTORY_ITEM_SIZE, INVENTORY_ITEM_SIZE),
        ).convert_alpha()

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

    def decrease_item(self, num):
        """
        Reduce num_item by num amount
        """
        self._num_item -= num

    def add_item(self):
        """
        Adds one item to num_item
        """
        self._num_item += 1

    @property
    def equipped(self):
        """
        Returns the value of the equipped attribute (boolean)
        """
        return self._equipped

    @property
    def pg_image(self):
        """
        Returns the value of the pg_image attribute (pygame image)
        """
        return self._pg_image

    @property
    def num_item(self):
        """
        Returns the value of the num_item attribute (int)
        """
        return self._num_item


class WateringCan(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
    """

    def __init__(self):
        """Initialize watering can"""
        super().__init__()
        self.update_image("equipment", "watering_can.png")


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
    """

    def __init__(self):
        """Initialize hoe"""
        super().__init__()
        self.update_image("equipment", "hoe.png")


class Seed(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        seed_type: a string representing what kind of plant is being planted
            by the seed
        num_item: An int representing how many seeds the user has
    """

    def __init__(self, seed_type):
        """Initialize seed"""
        super().__init__()
        self.seed_type = seed_type
        self.update_image("seeds", f"{seed_type}_seeds.png")
        self._num_item = 1


class ParsnipSeeds(Seed):
    """
    A subclass of the Seeds class which represents parsnip seeds

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        seed_type: a string representing what kind of plant is being planted
            by the seed
        num_item: An int representing how many seeds the user has
    """

    def __init__(self):
        """
        Initialize parsnip seed
        """
        super().__init__("parsnip")


class CauliflowerSeeds(Seed):
    """
    A subclass of the Seeds class which represents cauliflower seeds

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        seed_type: a string representing what kind of plant is being planted
            by the seed
        num_item: An int representing how many seeds the user has
    """

    def __init__(self):
        """
        Initialize cauliflower
        """
        super().__init__("cauliflower")


class PotatoSeeds(Seed):
    """
    A subclass of the Seeds class which represents potato seeds

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        seed_type: a string representing what kind of plant is being planted
            by the seed
        num_item: An int representing how many seeds the user has
    """

    def __init__(self):
        super().__init__("potato")


class Crop(Equipment):
    """
    Class representing the different crops a player can hold in their inventory

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        num_item: an int representing the number of items of that instance
            (ex. holding ten parsnips)
        crop_type: a string representing the name of the crop
        price: an int representing how much the crop sells for
    """

    def __init__(self, crop_type, price):
        """
        Initialize image of respective crop, price, and _num_item to be 1.
        """
        super().__init__()
        self.update_image("crops", f"{crop_type}.png")
        self.price = price
        self._num_item = 1


class ParsnipCrop(Crop):
    """
    Class representing sellable parsnip inventory item
    Has the same attributes as the parent Crop class
    """

    def __init__(self):
        """
        Initialize Parsnip Crop
        """
        super().__init__("parsnip", 35)


class CauliflowerCrop(Crop):
    """
    Class representing sellable cauliflower inventory item
    Has the same attributes as the parent Crop class
    """

    def __init__(self):
        """
        Initialize cauliflower crop
        """
        super().__init__("cauliflower", 175)


class PotatoCrop(Crop):
    """
    Class representing sellable potato inventory item
    Has the same attributes as the parent Crop class
    """

    def __init__(self):
        super().__init__("potato", 80)
