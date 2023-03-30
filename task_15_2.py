class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Autobus(Transport):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.capacity = None

    def seating_capacity(self, capacity=50):
        self.capacity = capacity
        print(f"Вместимость одного автобуса {self.name} {self.capacity} пассажиров")


bus: Autobus = Autobus("Renaul Logan", 180, 12)
bus.seating_capacity()

