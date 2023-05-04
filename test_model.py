"""
Test cases and implementation for the Model class
"""

import pytest
import pygame

# Needs these two lines to not return a pygame error about display modes
# Need to be above import statements because that is where error is occurring
pygame.init()
pygame.display.set_mode((800, 600))
from Model import Model
from plants import Plants
from equipmentclass import Crop

test_model = Model()
test_ground = test_model.ground
test_farmer = test_model.farmer
# till arbitrary squares
test_ground.land[3][4] = "T"
test_ground.land[4][5] = "T"
test_ground.land[2][3] = "T"
# water arbitrary squares
test_ground.land[6][2] = "TW"
test_ground.land[6][3] = "TW"
test_ground.land[6][4] = "TW"
# create plant instances and plant in arbitrary squares
test_unwatered_plant = Plants(False, "parsnip")
test_ground.land[1][2] = test_unwatered_plant
test_watered_plant = Plants(True, "parsnip")
test_ground.land[5][6] = test_watered_plant
second_watered_plant = Plants(True, "parsnip")
test_ground.land[5][5] = second_watered_plant

test_inventory = test_model.inventory

# create plants at different growth stages
stage_one_plant = Plants(True, "parsnip")
stage_one_plant._growth_days = 0  # pylint: disable=protected-access
stage_one_plant.grow()
stage_three_plant = Plants(True, "parsnip")
stage_three_plant._growth_days = 2  # pylint: disable=protected-access
stage_three_plant.grow()
harvestable_parsnip = Plants(True, "parsnip")
harvestable_parsnip._growth_days = 3  # pylint: disable=protected-access
harvestable_parsnip.grow()
harvestable_cauliflower = Plants(True, "cauliflower")
harvestable_cauliflower._growth_days = 11  # pylint: disable=protected-access
harvestable_cauliflower.grow()
test_ground.land[7][7] = stage_one_plant
test_ground.land[8][8] = stage_three_plant
test_ground.land[9][9] = harvestable_parsnip
test_ground.land[10][10] = harvestable_cauliflower

get_action_position_cases = [
    # returns correct action square when farmer is facing down
    ([4, 5], "down", (4, 6)),
    # returns correct action square when farmer is facing right
    ([6, 7], "right", (6, 8)),
    # returns correct action square when farmer is facing up
    ([5, 7], "up", (5, 5)),
    # returns correct action square when farmer is facing left
    ([2, 5], "left", (2, 4)),
]

till_ground_cases = [
    # tills free ground
    # Check till_square works on a free square
    ([5, 8], True),
    # tills watered ground
    ([6, 4], True),
    # Check till_square works on a plant square
    # Tilling should destroy the plant
    ([5, 6], True),
]

water_ground_cases = [
    # Check that a free square does not get watered
    ([10, 11], False),
    # Check that a tilled square does get watered
    ([3, 4], True),
    # Check that an unwatered plant gets watered
    ([1, 2], True),
]

plant_seed_cases = [
    # Check that you can't plant on free ground
    ([3, 3], False),
    # Check that you can plant on tilled ground
    ([4, 5], True),
    # Check that you can plant on watered ground
    ([6, 2], True),
    # Check you can't plant a new plant on top of a plant
    ([5, 5], True),  # checks if it's a new plant in function
]

harvest_crop_cases = [
    # Check that a stage one crop isn't harvestable
    ([7, 7], False),
    # Check that a stage three crop isn't harvestable
    ([8, 8], False),
    # Check that a parsnip is harvestable once fully grown
    ([9, 9], True),
    # Check that a cauliflower is harvestable once fully grown
    ([10, 10], True),
]


@pytest.mark.parametrize(
    "farmer_pos,farmer_dir,action_pos", get_action_position_cases
)
def test_get_action_position(farmer_pos, farmer_dir, action_pos):
    """
    This function checks whether the square an action is being performed on
    is accurate

    Args:
        farmer_pos: a tuple of two ints representing the x, y square position
        of the farmer
        farmer_dir: a string representing the position the farmer is facing
        action_pos: a tuple of two ints representing the x, y square position
        of the expected action
    """
    test_farmer.set_position(farmer_pos[0], farmer_pos[1])
    test_farmer.set_direction(farmer_dir)
    return test_model.get_action_position() == action_pos


@pytest.mark.parametrize("position,bool_val", till_ground_cases)
def test_till_ground(position, bool_val):
    """
    Checks that till_ground method is being performed accurately
    Nothing should prevent ground from being tilled
    If the ground is tilled, it should destroy a plant

    Args:
        position: a tuple of two ints representing the x, y square position
        of the action
        bool_val: a boolean that is True if the action should happen, False
        otherwise
    """
    test_farmer.set_direction("down")
    test_farmer.set_position(position[0], position[1] - 1)
    test_model.till_ground()
    # Check truth with check methods
    square = test_ground.get_square(position[0], position[1])
    assert test_ground.is_tilled(square) == bool_val
    # Ground that just had till_square called on it should not have a plant
    assert (
        not isinstance(test_ground.land[position[0]][position[1]], Plants)
    ) == bool_val


@pytest.mark.parametrize("position,bool_val", water_ground_cases)
def test_water_ground(position, bool_val):
    """
    Checks that water_ground method is being performed accurately
    The ground should not be watered if it is not tilled

    Args:
        position: a tuple of two ints representing the x, y square position
        of the action
        bool_val: a boolean that is True if the action should happen, False
        otherwise
    """
    test_farmer.set_direction("down")
    test_farmer.set_position(position[0], position[1] - 1)
    test_model.water_ground()
    # Check with check methods
    square = test_ground.get_square(position[0], position[1])
    assert test_ground.is_watered(square) == bool_val


@pytest.mark.parametrize("position,bool_val", plant_seed_cases)
def test_plant_seed(position, bool_val):
    """
    Checks that plant_seed method is being performed accurately
    A seed should not be planted on free ground
    A new plant should not be planted on top of an already existing plant

    Args:
        position: a tuple of two ints representing the x, y square position
        of the action
        bool_val: a boolean that is True if the action should happen, False
        otherwise
    """
    has_plant = test_ground.has_crop(
        test_ground.get_square(position[0], position[1])
    )
    test_farmer.set_direction("down")
    test_farmer.set_position(position[0], position[1] - 1)
    test_model.plant_seed("cauliflower")
    # Check with check methods
    square = test_ground.get_square(position[0], position[1])
    assert test_ground.has_crop(square) == bool_val
    # Checks that if there was already a plant on the square, the same plant is
    # still there
    if has_plant:
        assert (
            test_ground.get_square(position[0], position[1]).species
            == "parsnip"
        )


@pytest.mark.parametrize("position,bool_val", harvest_crop_cases)
def test_harvest_crop(position, bool_val):
    """
    Checks that harvest_crop method is being performed accurately
    A plant must be fully grown to be harvested
    If a plant is harvested it should be removed from the ground
    If a plant is harvested it should be added to the next open inventory slot
    (slot 4)

    Args:
        position: a tuple of two ints representing the x, y square position
        of the action
        bool_val: a boolean that is True if the action should happen, False
        otherwise
    """
    test_farmer.set_direction("down")
    test_farmer.set_position(position[0], position[1] - 1)
    test_model.harvest_crop()
    # Check with check methods
    square = test_ground.get_square(position[0], position[1])
    # if harvested, ground square should be a string
    assert isinstance(square, str) == bool_val
    # if harvested slot four in inventory should be a crop instance
    assert isinstance(test_inventory.inventory[4], Crop) == bool_val
