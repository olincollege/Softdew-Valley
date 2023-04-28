import pygame

# Crop growth cycle dictionary
plant_dictionary = {"cauliflower": [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5], "parsnip" : [0, 1, 2, 3, 4]}



class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """

    def __init__(self, row, col, water, species):
        self._growth_stage = 0
        self._growth_days = 0
        self._species = species
        self.row = row
        self.col = col
        self.water = water
        self._harvestable = False
    
    def plant_water(self):
        """
        Sets the water attribute of a specific plant instance to true
        """
        self.water = True


    def grow(self):
        """
        If the plant is watered when sleep is triggered, grow.
        This is only intended to be called by the Day class when sleep is 
        triggered.
        """
        if self.water:
            self._growth_days += 1
            # min of growth and list
            try: self._growth_stage = plant_dictionary[self._species][self._growth_days]
            except IndexError:
                self._growth_stage = plant_dictionary[self._species][-1]
        if self._growth_stage == plant_dictionary[self._species][-1]:
            print("grow has set harvestable to true")
            self._harvestable = True

    @property
    def harvestable(self):
        """
        Returns whether a plant can be harvested
        """
        return self._harvestable
    
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
            
        
        


    