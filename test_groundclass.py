import pytest
from groundclass import Ground
from plants import Plants

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
test_unwatered_plant = Plants(1, 2, False, "parsnip")
ground_test.land[1][2] = test_unwatered_plant
test_watered_plant = Plants(5, 6, True, "parsnip")
ground_test.land[5][6] = test_watered_plant
second_watered_plant = Plants(5, 5, True, "parsnip")
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
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_watered(square) == bool_val


@pytest.mark.parametrize("position,bool_val", is_tilled_cases)
def test_is_tilled(position, bool_val):
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.is_tilled(square) == bool_val


@pytest.mark.parametrize("position,bool_val", has_crop_cases)
def test_has_crop(position, bool_val):
    square = ground_test.get_square(position[0], position[1])
    assert ground_test.has_crop(square) == bool_val


# TEST UPDATE METHODS
# Can use check methods here because previous tests have established they work
@pytest.mark.parametrize("position,bool_val", till_square_cases)
def test_till_square(position, bool_val):
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
    ground_test.unwater_squares()
    square = ground_test.get_square(position[0], position[1])
    print(square)
    assert ground_test.is_watered(square) == bool_val
