from Shape.shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectángulo")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
