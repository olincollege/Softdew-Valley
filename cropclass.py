"""
Crop_Class
"""
import inventoryclass


class Crop:
    """
    Class that defines the crops

    Attributes:
        parsnip: A string that represents the parsnip crop
    """

    # SUB CLASSES OF DIFFERENT CROPS - PARSNIPS
    _parsnip_symbol = "Parsnip"
    crop_price = 5

    def __init__(self):
        """
        Initializes parsnip attribute.
        """
        self._parsnip = self._parsnip_symbol

    @property
    def crop_price(self):
        return self.crop_price
