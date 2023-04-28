from FarmerClass import Farmer

# from ViewClass import View
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

    def perform_action(self):
        equipped_item = self.inventory.get_equipped_item()
        if equipped_item is not None:
            # the action function is different for each item
            equipped_item.action()

    # def update_equipped_inventory(self, mouse_pos):
    #     if (
    #         mouse_pos[0] > View.INVENTORY_START_WIDTH
    #         and mouse_pos[0] < View.INVENTORY_START_WIDTH + 7 * 50
    #     ):
    #         if (
    #             mouse_pos[1] > View.INVENTORY_START_HEIGHT
    #             and mouse_pos[1]
    #             < View.INVENTORY_START_HEIGHT + View.GROUND_SIZE
    #         ):
    #             self.inventory.control_inventory(mouse_pos)

    def day_passes(self):
        rows = self.ground.num_rows
        cols = self.ground.num_cols
        for j in range(cols):
            for i in range(rows):
                if isinstance(self.ground.land[i][j], Plants):
                    self.ground.land[i][j].grow()
        self.ground.unwater_squares()
