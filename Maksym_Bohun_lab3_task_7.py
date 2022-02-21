"""
This module is used to work with logistics system
"""
import random
import sys

from order import Order
from vehicle import Vehicle
from logistic_system import LogisticSystem
from item import Item


def main():
    """
    This is a test function that shows how this module
    can theoretically be used.
    >>> vehicles = [Vehicle(1), Vehicle(2)]

    >>> logSystem = LogisticSystem(vehicles)

    >>> my_items = [Item('book',110), Item('chupachups',44)]

    >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items) #doctest: +ELLIPSIS
    Your order number is...
    >>> logSystem.placeOrder(my_order)

    'Your order #...
    >>> my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]

    >>> my_order2 = Order('Andrii', 'Odessa', 3, my_items2) #doctest: +ELLIPSIS
    Your order number is...
    >>> logSystem.placeOrder(my_order2)

    >>> logSystem.trackOrder(my_order2.orderId) #doctest: +ELLIPSIS
    'Your order #...
    >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]

    >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3) #doctest: +ELLIPSIS
    Your order number is...
    >>> logSystem.placeOrder(my_order3)
    There is no available vehicle to deliver an order.
    >>> logSystem.trackOrder(my_order3.orderId)
    'No such order.'
    """
    available_vehicles = [Vehicle(1), Vehicle(2)]
    logistic_system = LogisticSystem(available_vehicles)
    ordered_items = list()
    while True:
        item = str(input("Enter item you'd like to order:\n>>> "))
        if item != '-1':
            price = random.randint(1, 200)
            print(f'The item you chose ({item}) costs {price} UAH.')
            print('If you want ot order more, just enter the item')
            print('ELse, enter -1')
            ordered_items.append(Item(item, price))
        else:
            break
    while True:
        name = input('Please, enter your name:\n>>> ')
        if name.isalpha():
            break
        else:
            print('Name should only consist of letters. Try again.')
    while True:
        city = input('Please, enter your city:\n>>> ')
        if city.isalpha():
            break
        else:
            print('City should only consist of letters. Try again.')
    while True:
        try:
            postoffice = int(input('Please, enter the number of the Post office:\n>>> '))
            break
        except ValueError:
            print('Wrong Post office. Try again.')
    order = Order(user_name=name, city=city, postoffice=postoffice, items=ordered_items)
    logistic_system.placeOrder(order)
    print(logistic_system.trackOrder(order.orderId))
    print(f'Good luck, dear {name}, and thanks for you order!')
    sys.exit()


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
    main()