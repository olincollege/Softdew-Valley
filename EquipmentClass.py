class Equipment:
    """
    Class that represents an item that can be equipped from the inventory

    Attributes:
        inventory_slot: an int that represents the inventory location
        equipped: a boolean that shows whether the item is equipped or not
    """

    def __init__(self, slot):
        self._equipped = False
        self._inventory_slot = slot

    def update_inventory_slot(self, new_slot):
        """
        Update the inventory_slot attribute if the item is moved
        """
        self._inventory_slot = new_slot

    @property
    def equipped(self):
        return self._equipped


class WateringCan(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__(slot)


class Hoe(Equipment):
    """
    Class that represents the watering can item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__(slot)


class Seeds(Equipment):
    """
    Class that represents the seeds item

    Attributes:
        inventory_slot: an int that represents the inventory location
    """

    def __init__(self, slot):
        super(Equipment, self).__init__(slot)
