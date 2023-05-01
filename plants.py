import pygame
from EquipmentClass import Parsnip_Crop, Cauliflower_Crop



class Plants:
    """
    This parent class is responsible for keeping track of the state of any
    given crop from a seed.
    """
    # Crop growth cycle dictionary
    plant_dictionary = {
        "cauliflower": ([0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5], Cauliflower_Crop()),
        "parsnip" : ([0, 1, 2, 3, 4], Parsnip_Crop())
    }


    def __init__(self, row, col, water, species):
        """
        Initializes instance attributes and creates a plant instance

        Args:
            row: An int row value of a given square plot
            col: An int column value of a given square plot
            water: A bool representing whether a crop is watered or not 
            (watered is True)
            species: A string representing the species of crop (i.e. "parsnip")
        """
        self._growth_stage = 0
        self._growth_days = 0
        self._species = species
        self.row = row
        self.col = col
        self.water = water
        self._harvestable = False
        self._crop = self.plant_dictionary[species][1] #random slot, reassigned later

    
    def plant_water(self):
        """
        Sets the water attribute of a specific plant instance to true
        """
        self.water = True


    def grow(self):
        """
        If the crop is watered when sleep is triggered, grow. If a crop is 
        fully grown, set self._harvestable to True. grow() is only intended to
        be called by the Day class when sleep is triggered.
        
        Returns:
            None
        Raises:
            IndexError: number of growth days has become longer than the 
            associated crop's growth cycle list
        """
        if self.water:
            self._growth_days += 1
            try: self._growth_stage = (
                self.plant_dictionary[self._species][0][self._growth_days])
            except IndexError:
                self._growth_stage = self.plant_dictionary[self._species][0][-1]
        if self._growth_stage == self.plant_dictionary[self._species][0][-1]:
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

    @property
    def species(self):
        """
        Returns the species of a crop
        """
        return self._species
    
    @property
    def crop(self):
        """"""
        return self._crop
            
        
        


    