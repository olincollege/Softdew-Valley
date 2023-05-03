"""
Contains the controller class and all related methods for user interaction
"""
import pygame
import viewclass

VEL = 5  # farmer movement speed


class Controller:
    """
    A class that handles all user interaction elements of the game

    Attributes:
        farmer: An instance of the farmer class that represents the player
        character
        inventory: An instance of the Inventory class that represents the
        player's inventory
    """

    def __init__(self, farmer, inventory):
        self.farmer = farmer
        self.inventory = inventory

    def update_position(self):
        """
        Update the position of the farmer in the farmer class based off of the
        position of the farmer rectangle
        """
        x_val = (
            self.farmer.farmer_rect.x + self.farmer.farmer_rect.width // 2
        ) // viewclass.GROUND_SIZE
        y_val = (
            self.farmer.farmer_rect.y
            + int(self.farmer.farmer_rect.height * 0.75)
        ) // viewclass.GROUND_SIZE
        self.farmer.set_position(x_val, y_val)

    def move_farmer(self, keys):
        """
        Move the farmer rectangle and update farmer direction and position
        based off of key input

        Args:
            keys: The keys pressed by the user, created using pygame.key.
            get_pressed()
        """
        if keys[pygame.K_a] and self.farmer.farmer_rect.x - VEL > 0:  # LEFT
            self.farmer.farmer_rect.x -= VEL
            self.farmer.set_direction("left")
        if (
            keys[pygame.K_d]
            and self.farmer.farmer_rect.x
            - VEL
            + self.farmer.farmer_rect.width
            + 10
            < viewclass.WIDTH
        ):  # RIGHT
            self.farmer.farmer_rect.x += VEL
            self.farmer.set_direction("right")
        if keys[pygame.K_w] and self.farmer.farmer_rect.y - VEL > 0:  # UP
            self.farmer.farmer_rect.y -= VEL
            self.farmer.set_direction("up")
        if (
            keys[pygame.K_s]
            and self.farmer.farmer_rect.y + VEL + self.farmer.farmer_rect.height
            < viewclass.HEIGHT
        ):  # DOWN
            self.farmer.farmer_rect.y += VEL
            self.farmer.set_direction("down")
        self.update_position()

    def select_inventory(self, mouse_pos=None, num=None):
        """
        Equip an item based on a slot number

        Given mouse input, find the slot that is clicked by the mouse and equip
        the item in that slot
        Given keyboard input, equip the item in the correlated number slot

        Args:
            num: An int representing the slot of the item being equipped
            mouse_pos: A tuple that is the  (x, y) position in pixels of the
            mouse cursor on the window
        """
        current_item = self.inventory.get_equipped_item()
        if current_item is not None:
            current_item.unequip()
        slot = num
        if mouse_pos is not None:
            mouse_posx = mouse_pos[0]
            for i in range(8):
                if mouse_posx > viewclass.INVENTORY_START_WIDTH + (
                    i * viewclass.GROUND_SIZE
                ):
                    if mouse_posx < viewclass.INVENTORY_START_WIDTH + (
                        (i + 1) * viewclass.GROUND_SIZE
                    ):
                        slot = i

        self.inventory.equip_item(slot)

    def click_inventory(self, mouse_pos):
        """
        Checks that a user has clicked in the inventory area of the window
        If the user has clicked in the inventory area, call the
        select_inventory method

        Args:
            mouse_pos: A tuple that is the  (x, y) position in pixels of the
            mouse cursor on the window
        """
        if (
            mouse_pos[0] > viewclass.INVENTORY_START_WIDTH
            and mouse_pos[0]
            < viewclass.INVENTORY_START_WIDTH + 7 * viewclass.GROUND_SIZE
        ):
            if (
                mouse_pos[1] > viewclass.INVENTORY_START_HEIGHT
                and mouse_pos[1]
                < viewclass.INVENTORY_START_HEIGHT + viewclass.GROUND_SIZE
            ):
                self.select_inventory(mouse_pos)

    def perform_action(self):
        """
        Perform the action of an equipped item

        Check that an item is actually equipped before calling the action
        method for an Equipment instance
        """
        equipped_item = self.inventory.get_equipped_item()
        if equipped_item is not None:
            # the action function is different for each item
            equipped_item.action()
