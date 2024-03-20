class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print("Назва транспортного засобу:", self.name)
        print("Максимальна швидкість:", self.max_speed, "км/год")

vehicle = TransportVehicle("МЕГА ТАЧКА 9000", 200)
vehicle.display_info()
#zadacha 2
class Plane(TransportVehicle):
    def __init__(self, name, max_speed, flight_range):
        super().__init__(name, max_speed)
        self.flight_range = flight_range
    def display_info(self):
        super().display_info()
        print("Дальність польоту:", self.flight_range, "км")
plane = Plane("Винищувач", 1200, 14870)
plane.display_info()

#zadacha3

from megatachka9000 import TransportVehicle
from vynyschuvach import Plane

vehicle = TransportVehicle("Автомобіль", 200)
vehicle.display_info()

plane = Plane("Літак", 900, 5000)
plane.display_info()
