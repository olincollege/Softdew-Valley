"""
A class that represents the stand items you can buy
"""
from equipmentclass import ParsnipSeeds, CauliflowerSeeds, PotatoSeeds


class Stand:
    """
    Represents a stand where you can buy items in game

    Attributes:
        par_seeds: a StandItem instance that represents parsnip seeds being sold
        par_seeds: a StandItem instance that represents cauliflower seeds being
        sold
        par_seeds: a StandItem instance that represents potato seeds being sold
        stock_list: a list of items being sold by the store
    """

    def __init__(self):
        """
        Initializes store items and stock list
        """
        self.par_seeds = SellingParsnipSeeds()
        self.caul_seeds = SellingCauliflowerSeeds()
        self.pot_seeds = SellingPotatoSeeds()
        self.stock_list = [self.par_seeds, self.caul_seeds, self.pot_seeds]


class StandItem:
    """
    Represents the items that can be sold at a store

    Attributes:
        price: an int that represents the price of an item
        inventory_item: an instance of the Equipment Class that represents
        the inventory item that corresponds to a buyable item
    """

    def __init__(self, price, inventory_item):
        """
        Initializes the price and inventory item of a buyable item
        """
        self._price = price
        self._inventory_item = inventory_item

    @property
    def price(self):
        """Returns the value of the price instance attribute"""
        return self._price

    @property
    def inventory_item(self):
        """Returns the value of the inventory_item attribute"""
        return self._inventory_item


class SellingParsnipSeeds(StandItem):
    """
    Represents parsnip seeds that can be sold at a store

    Attributes:
        price: an int that represents the price of an item
        inventory_item: an instance of the Equipment Class that represents
        the inventory item that corresponds to a buyable item
    """

    def __init__(self):
        """
        Initializes the price and inventory item of parsnip seeds
        """
        super().__init__(20, ParsnipSeeds())


class SellingCauliflowerSeeds(StandItem):
    """
    Represents the cauliflower seeds that can be sold at a store

    Attributes:
        price: an int that represents the price of an item
        inventory_item: an instance of the Equipment Class that represents
        the inventory item that corresponds to a buyable item
    """

    def __init__(self):
        """
        Initializes the price and inventory item of a cauliflower seeds
        """
        super().__init__(80, CauliflowerSeeds())


class SellingPotatoSeeds(StandItem):
    """
    Represents the potato seeds that can be sold at a store

    Attributes:
        price: an int that represents the price of an item
        inventory_item: an instance of the Equipment Class that represents
        the inventory item that corresponds to a buyable item
    """

    def __init__(self):
        """
        Initializes the price and inventory item of a potato seeds
        """
        super().__init__(50, PotatoSeeds())
