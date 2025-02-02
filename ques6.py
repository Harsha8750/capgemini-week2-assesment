#6. Implement a multi-level inheritance example where `Vehicle` is a base class, 
# `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.

class Vehicle:
    def __init__(self):
        pass
    def manual(self):
        print("Most of the vehicles are manual only some are automated")
    def fuel(self):
        print("Some vehicles run on petrol")
        print("Some vehicles run on Diesel")
        print("Some run on elctricity")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
    def horse_power(self):
        print("Depending on the model the horse power varies")
    def mailage(self):
        print("Mailage varies from car to car")

class Bike(Vehicle):
    def __init__(self):
        super().__init__()
    def colour(self):
        print("Bikes are available in various colours")
    def tyres(self):
        print("Bikes contain only two tyres")

class Electriccar(Car):
    def __init__(self):
        super().__init__()
    def time(self):
        print("The car battery requires more amount of time to charge")
    def capacity(self):
        print("The performance mainly depends on the capacity of the battery")

ec=Electriccar()
ec.time()
ec.capacity()
ec.horse_power()
ec.mailage()