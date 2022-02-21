"""
This module saves information about items
"""


class Item:
    def __init__(self, name: str, price: float):
        """
        This function saves info about the item
        >>> water = Item('Water', 10)
        >>> water.price
        10
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Prints out the info about the item
        >>> water = Item('Water', 10)
        >>> print(water)
        Item name: Water;
        Item price: 10.
        """
        return f"Item name: {self.name};\n" \
               f"Item price: {self.price}."

    def __repr__(self):
        """
        Prints out the info about the item in a reusable way
        >>> water = Item('Water', 10)
        >>> print(repr(water))
        Item('Water', 10)
        """
        return f"Item('{self.name}', {self.price})"
