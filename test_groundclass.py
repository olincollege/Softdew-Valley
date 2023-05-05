"""
Test cases and implementation for the Ground class
"""
import pytest
import pygame

# Needs these two lines to not return a pygame error about display modes
# Need to be above import statements because that is where error is occurring
pygame.init()  # pylint: disable=no-member
pygame.display.set_mode((800, 600))

from groundclass import Ground  # pylint: disable=wrong-import-position
from plants import Plants  # pylint: disable=wrong-import-position

# Set up ground class
ground_test = Ground()
# till arbitrary squares
ground_test.land[3][4] = "T"
ground_test.land[4][5] = "T"
ground_test.land[2][3] = "T"
# water arbitrary squares
ground_test.land[6][2] = "TW"
ground_test.land[6][3] = "TW"
ground_test.land[6][4] = "TW"
# create plant instances and plant in arbitrary squares
test_unwatered_plant = Plants(False, "parsnip")
ground_test.land[1][2] = test_unwatered_plant
test_watered_plant = Plants(True, "parsnip")
ground_test.land[5][6] = test_watered_plant
second_watered_plant = Plants(True, "parsnip")
ground_test.land[5][5] = second_watered_plant

is_watered_cases = [
    # Check that a free square is not watered
    ([2, 8], False),
    # Make sure tilled and watered ground isn't getting confused
    ([3, 4], False),
    # Check that a watered square is watered
    ([6, 2], True),
    # The state of being watered is stored separately in plants, so we should
    # check that too
    # Check that an unwatered plant isn't returning watered
    ([1, 2], False),
    # Check that a watered plant returns as water
    ([5, 6], True),
]

# TEST CHECK METHODS
is_tilled_cases = [
    # Check that a free square is not tilled
    ([2, 8], False),
    # Make sure a tilled square returns tilled
    ([3, 4], True),
    # Make sure a tilled and watered square returns tilled
    ([6, 2], True),
    # All plants should return tilled
    ([1, 2], True),
    ([5, 6], True),
]

has_crop_cases = [
    # Check that a free square does not return having a crop
    ([2, 8], False),
    # Check that a tilled square does not return having a crop
    ([3, 4], False),
    # Check that a watered square does not return having a crop
    ([6, 2], False),
    # Plants should return as having a crop regardless of water status
    ([1, 2], True),
    ([5, 6], True),
]

# TEST UPDATE METHODS
till_square_cases = [
    # Check till_square works on a free square
    ([5, 8], True),
    # Check till_square works on a plant square
    # Tilling should destroy the plant
    ([5, 6], True),
]

water_square_cases = [
    # Check that a free square does not get watered
    ([10, 11], False),
    # Check that a tilled square does get watered
    ([3, 4], True),
    # Check that an unwatered plant gets watered
    ([1, 2], True),
]

unwater_squares_cases = [
    # watered ground remains watered
    ([6, 3], True),
    ([6, 4], True),
    # watered plants become unwatered
    ([5, 5], False),
]

# TEST CHECK METHODS
@pytest.mark.parametrize("position,bool_val", is_watered_cases)
def test_is_watered(position, bool_val):
    """
    Check that the is_watered function returns correctly
    Should return True for watered ground squares and watered plants

    Args:
        position: a tuple of two ints representing the x, y square position
        bool_val: a boolean that is True if the square should be watered, False
        otherwise
    """
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_watered(square) == bool_val


@pytest.mark.parametrize("position,bool_val", is_tilled_cases)
def test_is_tilled(position, bool_val):
    """
    Check that the is_tilled function returns correctly
    Should return True for tilled ground squares and plants

    Args:
        position: a tuple of two ints representing the x, y square position
        bool_val: a boolean that is True if the square should be tilled, False
        otherwise
    """
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_tilled(square) == bool_val


@pytest.mark.parametrize("position,bool_val", has_crop_cases)
def test_has_crop(position, bool_val):
    """
    Check that the has_crop function returns correctly
    Should return True if there is a plant on the square

    Args:
        position: a tuple of two ints representing the x, y square position
        bool_val: a boolean that is True if the square should have a crop,
        False otherwise
    """
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.has_crop(square) == bool_val


# TEST UPDATE METHODS
# Can use check methods here because previous tests have established they work
@pytest.mark.parametrize("position,bool_val", till_square_cases)
def test_till_square(position, bool_val):
    """
    Checks that till_square method is being performed accurately
    Nothing should prevent ground from being tilled
    If the ground is tilled, it should destroy a plant

    Args:
        position: a tuple of two ints representing the x, y square
        bool_val: a boolean that is True if the ground should be watered, False
        otherwise
    """
    ground_test.till_square(position[0], position[1])
    # Check truth through hard code
    assert (ground_test.land[position[0]][position[1]] == "T") == bool_val
    # Check truth with check methods
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_tilled(square) == bool_val
    # Ground that just had till_square called on it should not have a plant
    assert (
        not isinstance(ground_test.land[position[0]][position[1]], Plants)
    ) == bool_val


@pytest.mark.parametrize("position,bool_val", water_square_cases)
def test_water_square(position, bool_val):
    """
    Checks that water_ground method is being performed accurately
    The ground should not be watered if it is not tilled

    Args:
        position: a tuple of two ints representing the x, y square position
        bool_val: a boolean that is True if the ground should be watered, False
        otherwise
    """
    ground_test.water_square(position[0], position[1])
    # Check plant with hard code
    if isinstance(ground_test.land[position[0]][position[1]], Plants):
        assert ground_test.land[position[0]][position[1]].water == bool_val
    # Check no-plant ground through hard code
    else:
        assert ("W" in ground_test.land[position[0]][position[1]]) == bool_val
    # Check with check methods
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_watered(square) == bool_val


@pytest.mark.parametrize("position,bool_val", unwater_squares_cases)
def test_unwater_squares(position, bool_val):
    """
    Checks that the unwater_squares method makes the water attribute of all
    Plant instances on the map False

    Args:
        position: a tuple of two ints representing the x, y square position
        bool_val: a boolean that is True if the ground should remain watered
        False otherwise
    """
    ground_test.unwater_squares()
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_watered(square) == bool_val
