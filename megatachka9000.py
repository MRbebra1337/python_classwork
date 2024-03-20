class TransportVehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def display_info(self):
        print("Назва транспортного засобу:", self.name)
        print("Максимальна швидкість:", self.max_speed, "км/год")