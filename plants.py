from farmer.py import is_watered
import pygame

PARNSIP_IMAGES = {"seed": "parsnipseed.png", "sprout": "parsnipsprout.png", "ready": "parsnipready.png"}

class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """

    def __init__(self, _growth_stage):
        self._growth_stage = 0
        self._species = None

    def grow(self, row, col):
        """
        If the plant at row, col is watered when sleep is triggered, grow
        """

        if player_sleeping and is_watered(row, col):
            self._growth_stage += 1

        pass

    def get_growth_stage(self):
        """
        Determines the growth stage of any given plant
        """
        pass

    def get_plant_type(self, row, col):
        """
        Determines what plant type is in a square

        returns
            species: a string representing a type of plant
        """
        pass
        return species


    def display_plant(self, CROP_IMAGES):
        """
        Displays the appropriate image depending on growth stage
        and crop type
        """
        if self._growth_stage == 1:
            pygame.display(CROP_IMAGES["seed"])
        if self._growth_stage == 4:
            pygame.display(CROP_IMAGES["sprout"])
        if self._growth_stage == 6:
            pygame.display(CROP_IMAGES["ready"])

    def harvestable(self):
        """
        Introduces status "Harvestable" once the plant is ready
        """
        pass
            
        
        


    