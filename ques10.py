#Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn 
# inherits from `Electronics`. Demonstrate method overriding and attribute reuse.

class Electronics:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class MobileDevice(Electronics):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} mAh")

class SmartPhone(MobileDevice):
    def __init__(self, brand, model, battery_capacity, os):
        super().__init__(brand, model, battery_capacity)
        self.os = os

    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.os}")


smartphone = SmartPhone("Apple", "iPhone 13", 3095, "iOS")
smartphone.display_info()


