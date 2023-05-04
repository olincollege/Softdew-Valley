import pygame
from farmerclass import Farmer
from groundclass import Ground
from equipmentclass import (
    WateringCan,
    Hoe,
    Seed,
    ParsnipSeeds,
    CauliflowerSeeds,
)
from inventoryclass import Inventory
from plants import Plants
from houseclass import House
import constants
from audio import play_sound


class Model:
    """ """

    def __init__(self):
        self.farmer = Farmer()
        self.ground = Ground()
        self.watering_can = WateringCan()
        self.hoe = Hoe()
        self.parsnipseeds = ParsnipSeeds()
        self.cauliflowerseeds = CauliflowerSeeds()
        self.inventory = Inventory(
            self.watering_can,
            self.hoe,
            self.parsnipseeds,
            self.cauliflowerseeds,
        )
        self.house = House()
        self._is_till = False
        self._is_water = False

    def day_passes(self):
        """
        Grows any watered plants and sets them back to unwatered when called
        """
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                if isinstance(self.ground.land[i][j], Plants):
                    self.ground.land[i][j].grow()
        self.ground.unwater_squares()
        self.farmer.respawn_farmer()
        self.farmer.set_direction("down")

    def get_action_position(self):
        """
        Finds the x and y positions of the square the action is directed
        towards when called

        Returns:
            A tuple with the x and y positions of the square
        """
        pos = self.farmer.position
        action_pos_x = pos[0]
        action_pos_y = pos[1]
        farmer_direction = self.farmer.direction
        if farmer_direction == "up":
            action_pos_y -= 1
        elif farmer_direction == "down":
            action_pos_y += 1
        elif farmer_direction == "left":
            action_pos_x -= 1
        elif farmer_direction == "right":
            action_pos_x += 1
        return (action_pos_x, action_pos_y)

    def action_on_map(self):
        """
        Returns true if the action can be performed on the map, false if not
        """
        return (
            (
                self.farmer.farmer_rect.x
                + self.farmer.farmer_rect.width
                + constants.GROUND_SIZE // 2
            )
            < constants.WIDTH
            and (
                self.farmer.farmer_rect.y
                + self.farmer.farmer_rect.height
                + constants.GROUND_SIZE // 2
            )
            < constants.HEIGHT
            and not (self.farmer.farmer_rect.x < constants.GROUND_SIZE)
        )

    def action(self):
        equipped_item = self.inventory.get_equipped_item()
        if isinstance(equipped_item, WateringCan):
            self.water_ground()
        if isinstance(equipped_item, Hoe):
            self.till_ground()
        if isinstance(equipped_item, Seed):
            self.plant_seed(equipped_item.seed_type)

    def till_ground(self):
        """
        Call the till_square function on the action square and play the hoeing
        sound
        """
        if self.action_on_map():
            play_sound("hoeing")
            action_pos = self.get_action_position()
            self.ground.till_square(action_pos[0], action_pos[1])
            self._is_till = True

    def plant_seed(self, species):
        """
        Call the plant_crop function if the action square is tilled or watered

        species: a string representing the type of crop seed being planted
        """
        if self.action_on_map():
            action_pos = self.get_action_position()
            square = self.ground.get_square(action_pos[0], action_pos[1])
            if (
                self.ground.is_watered(square) or self.ground.is_tilled(square)
            ) and not isinstance(square, Plants):
                ground_watered = self.ground.is_watered(square)
                plant = Plants(ground_watered, species)
                print("Woo! You planted a seed <3")
                play_sound("planting", 1)
                self.ground.plant_crop(action_pos[0], action_pos[1], plant)

    def harvest_crop(self):
        """
        Calls the harvest function for the square in the action position if
        the square is harvestable and is a plant; adds the crop to the
        inventory either by increasing the quantity of that crop or adding it
        to a new slot depending on whether the crop is already in the inventory

        Args:
            inventory: An instance of the inventory class, stores harvested
                crops

        """
        action_pos = self.get_action_position()
        square = self.ground.get_square(action_pos[0], action_pos[1])
        if isinstance(square, Plants):
            if square.harvestable:
                self.ground.harvest(action_pos[0], action_pos[1])

                # check if it is already in the inventory
                found_item = False
                for idx, item in enumerate(self.inventory.inventory):
                    if type(item) is type(square.crop):
                        self.inventory.get_item(idx).add_crop()
                        found_item = True
                if not found_item:
                    slot = self.inventory.first_empty_slot()
                    self.inventory.add_item(slot, square.crop)

    def water_ground(self):
        """
        Call the water_square function if the ground is tilled or set the water
        attribute to True if there is a plant on the action square; plays a
        watering sound
        """
        if self.action_on_map():
            action_pos = self.get_action_position()
            square = self.ground.get_square(action_pos[0], action_pos[1])
            if self.ground.is_tilled(square):
                self.ground.water_square(action_pos[0], action_pos[1])
                play_sound("watering", 2)
                self._is_water = True

            if isinstance(square, Plants):
                play_sound("watering", 2)
                square.plant_water()
                self._is_water = True

    # These are for display purposes, it tells the view class to pause while
    # the action is occurring
    def stop_watering(self):
        """Sets _is_water to False"""
        self._is_water = False

    def stop_tilling(self):
        """Sets _is_till to False"""
        self._is_till = False

    @property
    def is_water(self):
        """Returns the value of the boolean _is_water"""
        return self._is_water

    @property
    def is_till(self):
        """Returns the value of the boolean _is_till"""
        return self._is_till
