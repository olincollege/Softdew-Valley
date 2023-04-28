import pygame
from ViewClass import View


class Controller:
    def __init__(self, farmer, inventory):
        self.farmer = farmer
        self.VEL = 5
        self.inventory = inventory

    def update_position(self):
        x = (
            self.farmer.farmer_rect.x + View.FARMER_WIDTH // 2
        ) // View.GROUND_SIZE

        y = (
            self.farmer.farmer_rect.y + View.FARMER_HEIGHT // 2
        ) // View.GROUND_SIZE

        self.farmer.set_position(x, y)

    def move_farmer(self, keys):
        if (
            keys[pygame.K_a] and self.farmer.farmer_rect.x - self.VEL > 0
        ):  # LEFT
            self.farmer.farmer_rect.x -= self.VEL
            self.farmer.set_direction("left")
        if (
            keys[pygame.K_d]
            and self.farmer.farmer_rect.x
            - self.VEL
            + self.farmer.farmer_rect.width
            + 10
            < View.WIDTH
        ):  # RIGHT
            self.farmer.farmer_rect.x += self.VEL
            self.farmer.set_direction("right")
        if keys[pygame.K_w] and self.farmer.farmer_rect.y - self.VEL > 0:  # UP
            self.farmer.farmer_rect.y -= self.VEL
            self.farmer.set_direction("up")
        if (
            keys[pygame.K_s]
            and self.farmer.farmer_rect.y
            + self.VEL
            + self.farmer.farmer_rect.height
            < View.HEIGHT
        ):  # DOWN
            self.farmer.farmer_rect.y += self.VEL
            self.farmer.set_direction("down")
        self.update_position()

    def select_inventory(self, mouse_pos=None, num=None):
        """click the thing and do the thing"""
        current_item = self.inventory.get_equipped_item()
        if current_item is not None:
            current_item.unequip()
        slot = num
        if mouse_pos is not None:
            mouse_posx = mouse_pos[0]
            for i in range(8):
                if mouse_posx > View.INVENTORY_START_WIDTH + (
                    i * View.GROUND_SIZE
                ) and mouse_posx < View.INVENTORY_START_WIDTH + (
                    (i + 1) * View.GROUND_SIZE
                ):
                    slot = i

        self.inventory.equip_item(slot)

    def click_inventory(self, mouse_pos):
        if (
            mouse_pos[0] > View.INVENTORY_START_WIDTH
            and mouse_pos[0] < View.INVENTORY_START_WIDTH + 7 * 50
        ):
            if (
                mouse_pos[1] > View.INVENTORY_START_HEIGHT
                and mouse_pos[1]
                < View.INVENTORY_START_HEIGHT + View.GROUND_SIZE
            ):
                self.select_inventory(mouse_pos)
