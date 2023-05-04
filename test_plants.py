"""
Test cases and implementation for the Plants class
"""

import pytest
from plants import Plants

watered_plant = Plants(1, 1, True, "parsnip")
unwatered_plant = Plants(2, 2, False, "parsnip")
stage_one_to_two = Plants(3, 3, True, "parsnip")
stage_one_to_two._growth_days = 1  # pylint: disable=protected-access
stage_three_to_harvest = Plants(4, 4, True, "parsnip")
stage_three_to_harvest._growth_days = 3  # pylint: disable=protected-access
stage_two_to_three = Plants(5, 5, True, "cauliflower")
stage_two_to_three._growth_days = 6  # pylint: disable=protected-access
no_growth_stage_change = Plants(6, 6, True, "cauliflower")
no_growth_stage_change._growth_days = 5  # pylint: disable=protected-access

grow_water_cases = [
    # growth_days adds one when watered, update growth stage
    (watered_plant, 1),
    (stage_one_to_two, 2),
    (stage_three_to_harvest, 4),
    (stage_two_to_three, 7),
    (no_growth_stage_change, 6),
    # growth_days doesn't update when not watered
    (unwatered_plant, 0),
]

grow_growth_stage_cases = [
    # growth stage should update when watered
    (watered_plant, 1),
    (stage_one_to_two, 2),
    # going to harvest updates growth stage
    (stage_three_to_harvest, 4),
    # checks cauliflower, which is on a slower grow cycle
    (stage_two_to_three, 3),
    # growth stage should not update when watered
    # unwatered plant doesn't update
    (unwatered_plant, 0),
    # slower grow cycle means stage doesn't update every time grow is called
    (no_growth_stage_change, 2),
]

grow_harvestable_cases = [
    # should update to be ready to harvest
    (stage_three_to_harvest, True),
    # should not be ready to harvest
    (watered_plant, False),
    (unwatered_plant, False),
    (stage_one_to_two, False),
    (stage_two_to_three, False),
    (no_growth_stage_change, False),
]


@pytest.mark.parametrize("plant,growth_days", grow_water_cases)
def test_grow_water(plant, growth_days):
    """
    Checks that growth_days updates correctly

    Args:
        plant: An instance of the Plant class being tested
        growth_days: An int representing the number of days growth_days should
        be

    """
    plant.grow()
    assert plant._growth_days == growth_days  # pylint: disable=protected-access


@pytest.mark.parametrize("plant,growth_stage", grow_growth_stage_cases)
def test_grow_growth_stage(plant, growth_stage):
    """
    Checks that growth_days updates correctly

    Args:
        plant: An instance of the Plant class being tested
        growth_stage: An int representing the growth stage of the plant
    """
    assert plant.growth_stage == growth_stage


@pytest.mark.parametrize("plant,harvestable", grow_harvestable_cases)
def test_grow_harvest(plant, harvestable):
    """
    Checks that growth_days updates correctly

    Args:
        plant: An instance of the Plant class being tested
        harvestable: A boolean representing if the plant is ready to be
        harvested
    """
    assert plant.harvestable == harvestable
