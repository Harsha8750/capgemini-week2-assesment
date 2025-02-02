#9. Simulate multiple inheritance where `FlyingCar` inherits from both 
# `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.

class Car:
    def __init__(self):
        pass
    def move(self):
        print("The car moves only on the land")
    def horse_power(self):
        print("Depending on the model of the car horse power varies")

class Airplane:
    def __init__(self):
        pass
    def move(self):
        print("The alirplane fly in the air")
    def power(self):
        print("Airplanes mainly uses fuel for running")

class FlyingCar(Car,Airplane):
    def __init__(self):
        super().__init__()
    def move(self):
        print("The flying car moves in the air")
    def display_info(self):
        Car.move(self)
        Airplane.move(self)

fly=FlyingCar()
fly.move()
fly.display_info()

