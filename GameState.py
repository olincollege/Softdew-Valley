from GroundClass import Ground
from FarmerClass import Farmer
from plants import Plants
from EquipmentClass import Crop
import pygame
import random

mixer_works = pygame.mixer.get_init()  # None if the mixer doesn't work


class GameState:
    def __init__(self, Farmer, Ground):
        self.farmer = Farmer
        self.ground = Ground
        self._is_water = False
        self._is_till = False

    def get_action_position(self):
        pos = self.farmer.position
        action_pos_x = pos[0]  # - self.farmer.farmer_rect.width // 2
        action_pos_y = pos[1]  # - self.farmer.farmer_rect.height // 2
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

    def till_ground(self):
        action_pos = self.get_action_position()
        self.ground.till_square(action_pos[0], action_pos[1])
        self._is_till = True

    def plant_seed(self, species):
        action_pos = self.get_action_position()
        square = self.ground.get_square(action_pos[0], action_pos[1])
        if (
            self.ground.is_watered(square) or self.ground.is_tilled(square)
        ) and not isinstance(square, Plants):
            ground_watered = self.ground.is_watered(square)
            plant = Plants(
                action_pos[0], action_pos[1], ground_watered, species
            )
            print("Woo! You planted a seed <3")
            if mixer_works is not None:
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound(
                        f"Assets/sound_bites/planting_sound{random.randint(0,1)}.wav"
                    )
                )
            self.ground.plant_crop(action_pos[0], action_pos[1], plant)

    def harvest_crop(self, inventory):
        print("you called harvest_crop in gamestate")
        action_pos = self.get_action_position()
        square = self.ground.get_square(action_pos[0], action_pos[1])
        if isinstance(square, Plants):
            print("i am successfully seeing a plant in a square")
            print(f"square.harvestable is {square.harvestable}")
            print(square.growth_stage)
            if square.harvestable:
                print("it's a harvestable plant")
                self.ground.harvest(action_pos[0], action_pos[1])
            # add the crop to inventory here
            # check if it is already in the inventory
            found_item = False
            for idx, item in enumerate(inventory.inventory):
                if type(item) is type(square.crop):
                    inventory.get_item(idx).add_crop()
                    found_item = True
            if not found_item:
                slot = inventory.first_empty_slot()
                inventory.add_item(slot, square.crop)

            # for checking purposes I know it's kinda stupid
            # Checks if the object stored in the inventory is keeping track of
            # how many crops there should be
            for idx, item in enumerate(inventory.inventory):
                if type(item) is type(square.crop):
                    num = inventory.get_item(idx).num_crops
            print(f"You have {num} of {square.crop}")

    def water_ground(self):
        action_pos = self.get_action_position()
        square = self.ground.get_square(action_pos[0], action_pos[1])
        if self.ground.is_tilled(square):
            self.ground.water_square(action_pos[0], action_pos[1])
            self._is_water = True
            if mixer_works is not None:
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound(
                        f"Assets/sound_bites/watering_sound{random.randint(0, 2)}.wav"
                    )
                )
        if isinstance(square, Plants):
            if mixer_works is not None:
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound(
                        f"Assets/sound_bites/watering_sound{random.randint(0, 2)}.wav"
                    )
                )
            square.plant_water()

    def stop_watering(self):
        self._is_water = False

    def stop_tilling(self):
        self._is_till = False

    # These are for display purposes, it tells the view class to pause while
    # the action is occuring
    @property
    def is_water(self):
        return self._is_water

    @property
    def is_till(self):
        return self._is_till
