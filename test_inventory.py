"""
Test cases and implementation for the Inventory class
"""
import pytest
import pygame

# Needs these two lines to not return a pygame error about display modes
# Need to be above import statements because that is where error is occurring
pygame.init()  # pylint: disable=wrong-import-position
pygame.display.set_mode((800, 600))  # pylint: disable=wrong-import-position
from inventoryclass import Inventory
from equipmentclass import (
    WateringCan,
    Hoe,
    ParsnipSeeds,
    CauliflowerSeeds,
    ParsnipCrop,
)
from farmerclass import Farmer
from groundclass import Ground

test_farmer = Farmer()
test_ground = Ground()
test_watering_can = WateringCan()
test_hoe = Hoe()
test_par_seeds = ParsnipSeeds()
test_caul_seeds = CauliflowerSeeds()
test_inventory = Inventory(
    test_watering_can, test_hoe, test_par_seeds, test_caul_seeds
)

equip_item_cases = [
    # Check each slot works
    (0, test_watering_can, True),
    (1, test_hoe, True),
    (2, test_par_seeds, True),
    (3, test_caul_seeds, True),
    # Check that other items aren't equipped when another slot should be
    (3, test_watering_can, False),
    # Check that other items aren't equipped when nothing should be equipped
    (5, test_watering_can, False),
    (5, test_hoe, False),
    (5, test_par_seeds, False),
    (5, test_caul_seeds, False),
]

get_equipped_item_cases = [
    # Equip a slot and check if it is equipped
    (0, test_watering_can, True),
    # Equip a slot and check if a different item is equipped
    (0, test_hoe, False),
    # The above but in the opposite direction to check if indexing matters
    (1, test_watering_can, False),
    # Having no item equipped returns None
    (5, None, True),
]

get_equipped_item_slot_cases = [
    # Equip a slot and check if it is equipped
    (0, 0, True),
    # Equip a slot and check if a different slot is equipped
    (0, 1, False),
    # The above but in the opposite direction to check if indexing matters
    (1, 0, False),
    # Having no item equipped returns None
    (5, None, True),
]

add_item_cases = [
    # add new item in open slot
    (4, ParsnipCrop()),
    # We don't need to handle adding items on top of other items
]

first_empty_slot_cases = [
    # no additional items
    (0, 4, True),
    (0, 0, False),
    # several additional items
    (2, 6, True),
    (2, 0, False),
    # full inventory returns None
    (4, None, True),
]


@pytest.mark.parametrize("slot,item,bool_val", equip_item_cases)
def test_equip_item(slot, item, bool_val):
    """
    Check that the equip_item method works accurately
    Equips an item and then checks if that item is equipped using item
    properties

    Args:
        slot: an int representing the inventory slot being equipped
        item: an Equipment instance representing an item that might be equipped
        bool_val: a boolean representing whether item should be equipped
    """
    test_inventory.equip_item(slot)
    assert item.equipped == bool_val
    # Unequip all items to reset for next test
    test_watering_can.unequip()
    test_hoe.unequip()
    test_par_seeds.unequip()
    test_caul_seeds.unequip()


@pytest.mark.parametrize("equipped_slot,item,bool_val", get_equipped_item_cases)
def test_get_equipped_item(equipped_slot, item, bool_val):
    """
    Check the get_equipped_item method works as expected
    Checks if the returned item that is correct

    Args:
        slot: an int representing the inventory slot that should be equipped
        item: the Equipment instance we are checking is equipped
        bool_val: a boolean representing whether item should be equipped
    """
    test_inventory.equip_item(equipped_slot)
    equipped_item = test_inventory.get_equipped_item()
    assert (equipped_item is item) == bool_val
    # reset for next test
    if equipped_item is not None:
        equipped_item.unequip()


@pytest.mark.parametrize(
    "equipped_slot,check_slot,bool_val", get_equipped_item_slot_cases
)
def test_get_equipped_slot_item(equipped_slot, check_slot, bool_val):
    """
    Check the get_equipped_item method works as expected
    Checks if the returned item that is correct

    Args:
        slot: an int representing the inventory slot that should be equipped
        check_slot: the slot being checked to see if it is equipped
        bool_val: a boolean representing whether item should be equipped
    """
    test_inventory.equip_item(equipped_slot)
    equipped_slot = test_inventory.get_equipped_item_slot()
    assert (equipped_slot == check_slot) == bool_val
    # reset for next test
    test_watering_can.unequip()
    test_hoe.unequip()
    test_par_seeds.unequip()
    test_caul_seeds.unequip()


@pytest.mark.parametrize("slot,item", add_item_cases)
def test_add_items(slot, item):
    """
    Check that add_item adds an item to the specified slot

    Args:
        slot: An int representing the slot an item is being added to
        item: The item being added to the inventory
    """
    test_inventory.add_item(slot, item)
    assert test_inventory.get_item(slot) is item


@pytest.mark.parametrize("iterations,slot,bool_val", first_empty_slot_cases)
def test_first_empty_slot(iterations, slot, bool_val):
    """
    Check that first_empty_slot returns the first empty slot of the inventory

    Args:
        iterations: How many times to add a new item to the inventory
        slot: The slot we are checking to see is the first empty inventory slot
        bool_val: A boolean representing whether or not slot should be what is
        returns
    """
    watering_can = WateringCan()
    hoe = Hoe()
    par_seeds = ParsnipSeeds()
    caul_seeds = CauliflowerSeeds()
    inventory = Inventory(watering_can, hoe, par_seeds, caul_seeds)
    for i in range(iterations):
        inventory.add_item(i + 4, ParsnipCrop())
    if slot is not None:
        assert (inventory.first_empty_slot() == slot) == bool_val
    else:
        assert (inventory.first_empty_slot() is slot) == bool_val


def test_remove_item():
    """
    Check that remove_item makes the specified inventory slot empty
    """
    watering_can = WateringCan()
    hoe = Hoe()
    par_seeds = ParsnipSeeds()
    caul_seeds = CauliflowerSeeds()
    inventory = Inventory(watering_can, hoe, par_seeds, caul_seeds)
    inventory.remove_item(0)
    assert inventory.inventory[0] == " "
    inventory.remove_item(1)
    assert inventory.inventory[1] == " "
    inventory.remove_item(2)
    assert inventory.inventory[2] == " "
    inventory.remove_item(3)
    assert inventory.inventory[3] == " "
