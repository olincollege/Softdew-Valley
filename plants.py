import pygame

# Cauliflower growth cycle
cauliflower = [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5]
parsnip = [0, 1, 2, 3, 4]



class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """

    def __init__(self, row, col, water):
        self._growth_stage = 0
        self._growth_days = 0
        self._species = "parsnip"
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
        if self.water:
            if self._species == "parsnip":
                self._growth_stage += 1 # Increase growth stage
            if self._species == "cauliflower":
                self._growth_days += 1
                try: self._growth_stage = cauliflower[self._growth_days]
                except IndexError:
                    self._growth_stage = cauliflower[-1]


    @property
    def growth_stage(self):
        """
        Returns the plant's growth stage
        """
        return self._growth_stage

    # def print_growth_stage(self):
    #     print(self._growth_stage)

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
            
        
        


    