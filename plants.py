import pygame

class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """

    def __init__(self, row, col, water):
        self._growth_days = 0
        self._species = "PARSNIP"
        self.row = row
        self.col = col
        self.water = water
    
    def plant_water(self):
        self.water = True

    def grow(self):
        """
        If the plant is watered when sleep is triggered, grow.
        This is only intended to be called by the Day class when sleep is 
        triggered.
        """
        if self._growth_days < self.harvestable() and self.water:
            self._growth_days += 1 # Increase growth stage

    @property
    def growth_days(self):
        """
        Returns the number of days a plant has been growing
        """
        return self._growth_days

    def print_growth_days(self):
        print(self._growth_days)

    @property
    def species(self):
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

    def harvestable(self):
        """
        Introduces status "Harvestable" once the plant is ready

        Returns the int number of growth days necessary for a certain plant to
        be ready
        """
        if self._species == "PARSNIP":
            return 5
        return None
            
        
        


    