from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(IShape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14159 * self.radius * self.radius


rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Area of rectangle: {rectangle.calculate_area()}")
print(f"Area of circle: {circle.calculate_area()}")
