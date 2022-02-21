"""
This module is used to place orders
"""
import random
from location import Location
from item import Item
from typing import List
from vehicle import Vehicle


class Order:
    def __init__(self, user_name: str, city: str, postoffice: int, items: List[Item]):
        """
        This function saves info about order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items) #doctest: +ELLIPSIS
        Your order number is...
        """
        self.orderId = random.randint(1000000, 9999999)
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.items = items
        self.vehicle = None
        print(f"Your order number is {self.orderId}.")

    def __str__(self):
        """
        Prints out the order number
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items) #doctest: +ELLIPSIS
        Your order number is...
        >>> print(my_order) #doctest: +ELLIPSIS
        Your order number is...
        """
        return f"Your order number is {self.orderId}"

    def calulateAmount(self):
        """
        Calculates the total price of an order
        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items) #doctest: +ELLIPSIS
        Your order number is...
        >>> my_order.calulateAmount()
        154
        """
        total = 0
        for item in self.items:
            total += item.price
        return total

    def assignVehicle(self, vehicle: Vehicle):
        """
        Assigns a vehicle for the order
                >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items) #doctest: +ELLIPSIS
        Your order number is...
        >>> my_order.assignVehicle(Vehicle(1))
        >>> my_order.vehicle
        Vehicle(1, True)
        """
        self.vehicle = vehicle


import doctest
print(doctest.testmod())