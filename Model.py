import pygame
from FarmerClass import Farmer
from GroundClass import Ground
from GameState import GameState
from EquipmentClass import (
    WateringCan,
    Hoe,
    ParsnipSeeds,
    CauliflowerSeeds,
)
from Inventory_Class import Inventory
from plants import Plants
from House_Class import House
from ViewClass import View


class Model:
    def __init__(self):
        self.farmer = Farmer()
        self.ground = Ground()
        self.gamestate = GameState(self.farmer, self.ground)
        self.watering_can = WateringCan(self.gamestate)
        self.hoe = Hoe(self.gamestate)
        self.parsnipseeds = ParsnipSeeds(self.gamestate)
        self.cauliflowerseeds = CauliflowerSeeds(self.gamestate)
        self.inventory = Inventory(
            self.watering_can,
            self.hoe,
            self.parsnipseeds,
            self.cauliflowerseeds,
        )
        self.house = House()

    def day_passes(self):
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                if isinstance(self.ground.land[i][j], Plants):
                    self.ground.land[i][j].grow()
        self.ground.unwater_squares()
        self.farmer.redraw_farmer()
        # print("change to black")
