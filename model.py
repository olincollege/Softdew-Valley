from farmerclass import Farmer
from groundclass import Ground
from gamestate import GameState
from houseclass import House
from plants import Plants
from equipmentclass import (
    WateringCan,
    Hoe,
    ParsnipSeeds,
    CauliflowerSeeds,
)
from inventoryclass import Inventory
import pygame

farmer = Farmer()
ground = Ground()
gamestate = GameState(farmer, ground)
watering_can = WateringCan(gamestate)
hoe = Hoe(gamestate)
parsnipseeds = ParsnipSeeds(gamestate)
cauliflowerseeds = CauliflowerSeeds(gamestate)
house = House()
inventory = Inventory(
    watering_can,
    hoe,
    parsnipseeds,
    cauliflowerseeds,
)

# I don't know where to put this rn:
walls_dict = {}


def day_passes():
    """
    Grows any watered plants and sets them back to unwatered when called
    """
    rows = ground.num_rows
    cols = ground.num_cols
    for j in range(cols):
        for i in range(rows):
            if isinstance(ground.land[i][j], Plants):
                ground.land[i][j].grow()
    ground.unwater_squares()
    farmer.respawn_farmer()
    farmer.set_direction("down")


# class Model:
#     """
#     Initializes a farmer, ground, gamestate, and inventory instance and passes
#     the day

#     Attributes:
#         farmer: an instance of the Farmer class
#         ground: an instance of the Ground class
#         gamestate: an instance of the GameState class
#         watering_can: an instance of the WateringCan class
#         hoe: an instance of the Hoe class
#         parsnipseeds: an instance of the ParsnipSeeds class
#         cauliflowerseeds: an instance of the CauliflowerSeeds class
#         inventory: an instance of the Inventory class containing the instances
#         of watering_can, hoe, parsnipseeds and cauliflowerseeds
#     """

#     farmer = Farmer()
#     ground = Ground()
#     gamestate = GameState(farmer, ground)
#     watering_can = WateringCan(gamestate)
#     hoe = Hoe(gamestate)
#     parsnipseeds = ParsnipSeeds(gamestate)
#     cauliflowerseeds = CauliflowerSeeds(gamestate)
#     inventory = Inventory(
#         watering_can,
#         hoe,
#         parsnipseeds,
#         cauliflowerseeds,
#     )

#     def __init__(self):
#         pass
