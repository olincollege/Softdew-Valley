from FarmerClass import Farmer
from GroundClass import Ground
import pygame

class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """

    def __init__(self, row, col):
        self._growth_days = 1
        self._species = "PARSNIP"
        self.row = row
        self.col = col

    def grow(self):
        """
        If the plant at row, col is watered when sleep is triggered, grow.
        This is only intended to be called by the Day class when sleep is 
        triggered, and will unwater a square where a plant has grown
        """
        if Farmer.is_watered(self.row, self.col):
            if self._growth_days < self.harvestable(self._species):
                self._growth_days += 1 # Increase growth stage
            Ground.land[self.row][self.col].replace("W","") # Square is no longer watered

    @property
    def growth_days(self):
        """
        Returns the number of days a plant has been growing
        """
        return self._growth_days

    def print_growth_days(self):
        print(self._growth_days)

    @property
    def get_species(self):
        """
        Returns the species of a crop
        """
        return self._species
    # def get_plant_type(self, row, col):
    #     """
    #     Determines what plant type is in a square

    #     returns
    #         species: a string representing a type of plant
    #     """
    #     pass
    #     return species


    def display_plant(self, CROP_IMAGES, row, col):
        """
        Displays the appropriate image depending on growth stage
        and crop type
        """
        pygame.blit(CROP_IMAGES[f"growthstage{self._growth_days}"], (row, col))

    def harvestable(self):
        """
        Introduces status "Harvestable" once the plant is ready

        Returns the int number of growth days necessary for a certain plant to
        be ready
        """
        if self._species == "PARSNIP":
            return 5
        return None
            
        
        


    