from plants import Plants
import ViewClass
from audio import play_sound


class GameState:
    def __init__(self, Farmer, Ground):
        self.farmer = Farmer
        self.ground = Ground
        self._is_water = False
        self._is_till = False

    def get_action_position(self):
        pos = self.farmer.position
        action_pos_x = pos[0]
        action_pos_y = pos[1]
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

    def action_on_map(self):
        """
        Returns true if the action can be performed on the map, false if not
        """
        return (
            (
                self.farmer.farmer_rect.x
                + self.farmer.farmer_rect.width
                + ViewClass.GROUND_SIZE // 2
            )
            < ViewClass.WIDTH
            and (
                self.farmer.farmer_rect.y
                + self.farmer.farmer_rect.height
                + ViewClass.GROUND_SIZE // 2
            )
            < ViewClass.HEIGHT
            and not (self.farmer.farmer_rect.x < ViewClass.GROUND_SIZE)
        )

    def till_ground(self):
        if self.action_on_map():
            play_sound("hoeing")
            action_pos = self.get_action_position()
            self.ground.till_square(action_pos[0], action_pos[1])
            self._is_till = True

    def plant_seed(self, species):
        if self.action_on_map():
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
                play_sound("planting", 1)
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

                # check if it is already in the inventory
                found_item = False
                for idx, item in enumerate(inventory.inventory):
                    if type(item) is type(square.crop):
                        inventory.get_item(idx).add_crop()
                        found_item = True
                if not found_item:
                    slot = inventory.first_empty_slot()
                    inventory.add_item(slot, square.crop)

    def water_ground(self):
        if self.action_on_map():
            action_pos = self.get_action_position()
            square = self.ground.get_square(action_pos[0], action_pos[1])
            if self.ground.is_tilled(square):
                self.ground.water_square(action_pos[0], action_pos[1])
                self._is_water = True
                play_sound("watering", 2)

            if isinstance(square, Plants):
                play_sound("watering", 2)
                square.plant_water()

    def stop_watering(self):
        self._is_water = False

    def stop_tilling(self):
        self._is_till = False

    # These are for display purposes, it tells the view class to pause while
    # the action is occurring
    @property
    def is_water(self):
        return self._is_water

    @property
    def is_till(self):
        return self._is_till
