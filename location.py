"""
This module is used to store information about location
"""


class Location:
    def __init__(self, city: str, postoffice: int):
        """
        This function saves info about location
        >>> ternopil = Location('Ternopil', 46000)
        >>> ternopil.postoffice
        46000
        """
        self.city = city
        self.postoffice = postoffice

    def __str__(self):
        """
        Prints out the info about the location
        >>> ternopil = Location('Ternopil', 46000)
        >>> print(ternopil)
        Location: Ternopil, post office number 46000.
        """
        return f"Location: {self.city}, " \
               f"post office number {self.postoffice}."

    def __repr__(self):
        """
        Prints out the info about the location in a reusable way
        >>> ternopil = Location('Ternopil', 46000)
        >>> print(repr(ternopil))
        Location('Ternopil', 46000)
        """
        return f"Location('{self.city}', {self.postoffice})"
