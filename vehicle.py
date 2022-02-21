"""
This module is used to store information about vehicle
"""


class Vehicle:
    def __init__(self, vehicleNo: int, isAvailable=True):
        """
        This function saves info about vehicle
        >>> vehicle = Vehicle(1)

        >>> vehicle.isAvailable
        True
        """
        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable

    def __str__(self):
        """
        Prints out the info about the vehicle
        >>> vehicle = Vehicle(1)
        >>> print(vehicle)
        Vehicle number 1 is available.
        """
        if not self.isAvailable:
            return f"Vehicle number {self.vehicleNo} is not available."
        return f"Vehicle number {self.vehicleNo} is available."

    def __repr__(self):
        """
        Print out the info about the vehicle in a reusable way
        >>> vehicle = Vehicle(1)
        >>> print(repr(vehicle))
        Vehicle(1, True)
        """
        return f"Vehicle({self.vehicleNo}, {self.isAvailable})"
