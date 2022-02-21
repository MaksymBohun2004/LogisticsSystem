"""
This is the main module of the logistic system
"""
from typing import List
from vehicle import Vehicle
from order import Order


class LogisticSystem:
    def __init__(self, vehicles: List[Vehicle]):
        """
        This function saves info about logistic system
        >>> my_order = LogisticSystem([Vehicle(1)])
        >>> my_order.vehicles
        [Vehicle(1, True)]
        """
        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order):
        """
        Places the order if possible
        """
        self.orders.append(order)
        for vehicle in self.vehicles:
            if vehicle.isAvailable:
                vehicle.isAvailable = False
                order.assignVehicle(vehicle)
                return
        print("There is no available vehicle to deliver an order.")

    def trackOrder(self, orderId: int):
        """
        Tracks the order if it exists
        """
        for order in self.orders:
            if order.orderId == orderId:
                if order.vehicle:
                    return f"Your order #{order.orderId} is sent to" \
                           f" {order.location.city}. Total price: {order.calulateAmount()} UAH."
        return "No such order."
