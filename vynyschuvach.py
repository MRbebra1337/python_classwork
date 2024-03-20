from megatachka9000 import TransportVehicle

class Plane(TransportVehicle):
    def __init__(self, name, max_speed, flight_range):
        super().__init__(name, max_speed)
        self.flight_range = flight_range

    def display_info(self):
        super().display_info()
        print("Дальність польоту:", self.flight_range, "км")