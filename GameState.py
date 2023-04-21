import pygame
from GroundClass import Ground
from FarmerClass import Farmer


class GameState:
    def __init__(self, Farmer, Ground):
        self.farmer = Farmer
        self.ground = Ground

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

    def till_ground(self):
        action_pos = self.get_action_position()
        self.ground.til_square(action_pos[0], action_pos[1])

    def water_ground(self):
        action_pos = self.get_action_position()
        if self.ground.is_tilled(
            self.ground.get_square(action_pos[0], action_pos[1])
        ):
            self.ground.water_square(action_pos[0], action_pos[1])
