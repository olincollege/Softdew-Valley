"""
A class that represents the stand items you can buy
"""
from equipmentclass import Seed, ParsnipSeeds, CauliflowerSeeds, PotatoSeeds


class Stand:
    def __init__(self):
        self.par_seeds = SellingParsnipSeeds()
        self.caul_seeds = SellingCauliflowerSeeds()
        self.pot_seeds = SellingPotatoSeeds()
        self.stock_list = [self.par_seeds, self.caul_seeds, self.pot_seeds]


class StandItem:
    def __init__(self, price, inventory_item):
        self._price = price
        self._inventory_item = inventory_item

    @property
    def price(self):
        return self._price

    @property
    def inventory_item(self):
        return self._inventory_item


class SellingParsnipSeeds(StandItem):
    def __init__(self):
        super().__init__(20, ParsnipSeeds())


class SellingCauliflowerSeeds(StandItem):
    def __init__(self):
        super().__init__(80, CauliflowerSeeds())


class SellingPotatoSeeds(StandItem):
    def __init__(self):
        super().__init__(50, PotatoSeeds())


# Go to vendor position
# Press e
# Set enter_shop to True
# Shop screen pops up
# Can click in different places to buy things (enter_shop must be true)
#   Decrease funds
#   Add item to inventory
# Escape to leave shop
# Set enter shop to false
