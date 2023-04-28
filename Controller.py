import pygame


class Controller:
    def __init__(self, farmer):
        self.farmer = farmer
        self.VEL = 5

    def move_left(self):
        if self.farmer.farmer_rect.x - self.VEL > 0:
            self.farmer.farmer_rect.x -= self.VEL
            self.farmer.update_direction("left")
        self.update_position()

    def move_right(self):
        if (
            self.farmer.farmer_rect.x
            - self.VEL
            + self.farmer.farmer_rect.width
            + 10
            < self.farmer.WIDTH
        ):
            self.farmer.farmer_rect.x += self.VEL
            self.farmer.update_direction("right")
        self.update_position()

    def move_up(self):
        if self.farmer.farmer_rect.y - self.VEL > 0:  # UP
            self.farmer.farmer_rect.y -= self.VEL
            self.farmer.update_direction("up")
        self.update_position()

    def move_down(self):
        if (
            self.farmer.farmer_rect.y
            + self.VEL
            + self.farmer.farmer_rect.height
            < self.farmer.HEIGHT
        ):  # DOWN
            self.farmer.farmer_rect.y += self.VEL
            self.farmer.update_direction("down")
        self.update_position()

    def update_position(self):
        x = (
            self.farmer.farmer_rect.x + self.farmer.FARMER_WIDTH // 2
        ) // self.farmer.SQUARE_SIZE

        y = (
            self.farmer.farmer_rect.y + self.farmer.FARMER_HEIGHT // 2
        ) // self.farmer.SQUARE_SIZE

        self.farmer.update_position(x, y)

    def move_farmer(self, keys):
        if (
            keys[pygame.K_a] and self.farmer.farmer_rect.x - self.VEL > 0
        ):  # LEFT
            self.farmer.farmer_rect.x -= self.VEL
            self.farmer.update_direction("left")
        if (
            keys[pygame.K_d]
            and self.farmer.farmer_rect.x
            - self.VEL
            + self.farmer.farmer_rect.width
            + 10
            < self.farmer.WIDTH
        ):  # RIGHT
            self.farmer.farmer_rect.x += self.VEL
            self.farmer.update_direction("right")
        if keys[pygame.K_w] and self.farmer.farmer_rect.y - self.VEL > 0:  # UP
            self.farmer.farmer_rect.y -= self.VEL
            self.farmer.update_direction("up")
        if (
            keys[pygame.K_s]
            and self.farmer.farmer_rect.y
            + self.VEL
            + self.farmer.farmer_rect.height
            < self.farmer.HEIGHT
        ):  # DOWN
            self.farmer.farmer_rect.y += self.VEL
            self.farmer.update_direction("down")
        self.update_position()
