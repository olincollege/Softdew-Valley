"""
Holds all the different classes of items that can go in the inventory
"""
import os
import pygame
import viewclass

mixer_works = pygame.init()
INVENTORY_ITEM_SIZE = viewclass.INVENTORY_ITEM_SIZE


class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Instance Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
        num_item: an int representing the number of items of that instance
            (ex. holding ten parsnips)
    """

    def __init__(self, gamestate=None):
        self._equipped = False
        self._pg_image = None
        self._gamestate = gamestate
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
                os.path.join(f"Assets/{subfolder}", f"{image_name}")
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

    def action(self):
        """
        Perform the action of an item
        """

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
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
    """

    def __init__(self, gamestate):
        """Initialize watering can"""
        super().__init__(gamestate)
        self.update_image("equipment", "watering_can.png")

    def action(self):
        """
        Water the ground

        Calls the gamestate function water_ground, which updates the ground
        and/or plant class, updates the action occurring in the view class
        """
        self._gamestate.water_ground()


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
    """

    def __init__(self, gamestate):
        """Initialize hoe"""
        super().__init__(gamestate)
        self.update_image("equipment", "hoe.png")

    def action(self):
        """
        Till the ground

        Calls the gamestate function till_ground, which updates the ground
        class, updates the action occurring in the view class
        """
        self._gamestate.till_ground()


class Seed(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
        seed_type: a string representing what kind of plant is being planted
            by the seed
    """

    def __init__(self, gamestate, seed_type):
        """Initialize seed"""
        super().__init__(gamestate)
        self.seed_type = seed_type
        self.update_image("seeds", f"{seed_type}_seeds.png")

    def action(self):
        """
        Plant a seed

        Calls the gamestate function plant, which updates the ground class and
        initializes a plant class. The plant depends on the seed_type
        """
        self._gamestate.plant_seed(self.seed_type)


class ParsnipSeeds(Seed):
    """
    A subclass of the Seeds class which represents parsnip seeds

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
        seed_type: a string representing what kind of plant is being planted
            by the seed
    """

    def __init__(self, gamestate):
        super().__init__(gamestate, "parsnip")


class CauliflowerSeeds(Seed):
    """
    A subclass of the Seeds class which represents cauliflower seeds

    Attributes:
        equipped: a boolean that shows whether the item is equipped or not
        pg_image: the pygame image that represents the image displayed for
            an item in the inventory
        gamestate: an instance of the gamestate class, allows the class
            to interact with the gamestate when displaying equipment actions
        seed_type: a string representing what kind of plant is being planted
            by the seed
    """

    def __init__(self, gamestate):
        super().__init__(gamestate, "cauliflower")


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
        super().__init__()
        self.update_image("crops", f"{crop_type}.png")
        self.price = price
        self._num_item = 1

    def add_crop(self):
        """
        Adds one crop to num_item
        """
        self._num_item += 1


class ParsnipCrop(Crop):
    """
    Class representing sellable parsnip inventory item
    Has the same attributes as the parent Crop class
    """

    def __init__(self):
        super().__init__("parsnip", 35)


class CauliflowerCrop(Crop):
    """
    Class representing sellable parsnip inventory item
    Has the same attributes as the parent Crop class
    """

    def __init__(self):
        super().__init__("cauliflower", 175)
