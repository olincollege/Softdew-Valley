"""
Crop_Class
"""


class Crop:
    """
    Class that defines the crops

    Attributes:
        parsnip: A string that represents the parsnip crop
    """

    def __init__(self):
        """
        Initializes parsnip attribute.
        """
        pass

    def price(self):
        """
        Sets selling price of crop
        """
        pass

    def sell(self):
        """
        Creates action to sell a crop.

        Returns: Integer representing the money earned from selling the crop.
        Money earned is equivalent to the set price.
        """
        pass

    def harvested(self, num_days):
        """
        Determines if crop is ready to be harvested. Takes in the num_days
        since a crop has been harvested and if the number is more than the set
        days that the crop needs to grow then it is ready to be harvested.

        Args:
            num_days: integer representing the number of days since a crop has
            been harvested.
        """
        pass
