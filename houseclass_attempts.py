# HIT_WALL = pygame.USEREVENT + 4
# # HOUSE WALLS
# left_wall = pygame.Rect(
#     house_start_x, house_start_y, HOUSE_SIZE // 16, HOUSE_SIZE
# )
# right_wall = pygame.Rect(
#     house_start_x + 15 * HOUSE_SIZE // 16, house_start_y,
#     HOUSE_SIZE // 16, HOUSE_SIZE
# )
# top_wall = pygame.Rect(
#     house_start_x, house_start_y, HOUSE_SIZE, HOUSE_SIZE // 16
# )
# # bottom_wall_left = pygame.Rect(
# #     house_start_x, house_start_y - HOUSE_SIZE // 16,
# #     # FILL IN, HOUSE_SIZE // 16
# # )
# # bottom_wall_right = pygame.Rect(
# #     # FILL IN, house_start_y - HOUSE_SIZE // 16,
# #     # FILL IN, HOUSE_SIZE // 16
# # )
# # door = pygame.Rect(
# #     # FILL IN, house_start_y - HOUSE_SIZE // 16,
# #     # FILL IN, HOUSE_SIZE // 16
# # )
# house_walls = [left_wall, right_wall, top_wall]
# # inner_collision_dict = {(left_wall), "left", (right_wall): "right", (top_wall): "top"} ARGHH UNHASHABLE
# # outer_collision_dict = {left_wall: "right", right_wall: "left", top_wall: "bottom"}

# # def hit_wall(self, farmer):
# #     """
# #     Disallow player movement through walls
# #     """
# #     for rect in self.house_walls:
# #         collide = pygame.Rect.colliderect(rect, farmer.farmer_rect)
# #         if collide:
# #             pygame.event.post(pygame.event.Event(HIT_WALL))
# #             print("You can't walk through walls")

# # def collide_wall(self, farmer_movement_rect):
# #     """
# #     Detects if a player has hit a wall and returns a string representing
# #     what direction of movement should be disallowed
# #     """
# #     for rect in self.house_walls:
# #         collide = pygame.Rect.colliderect(rect, farmer_movement_rect)
# #         if collide:
# #             if self.enter_house(self, farmer_movement_rect):
# #                 return self.inner_collision_dict[rect]
# #             else:
# #                 return self.outer_collision_dict[rect]


# #THIS PART WAS IN MAIN
# # if event.type == houseclass.HIT_WALL:
# #             print("that was a wall")
# #             # prevent farmer position from increasing towards wall?
# # model.house.hit_wall(model.farmer)
