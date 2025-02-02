class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


square = Square(4)
triangle = Triangle(3, 6)

print(f"Area of square: {square.area()}")
print(f"Area of triangle: {triangle.area()}")
