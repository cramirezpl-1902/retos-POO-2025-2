import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("El método area() debe ser implementado por la subclase")

    def perimeter(self):
        raise NotImplementedError("El método perimeter() debe ser implementado por la subclase")

    def describe(self):
        return f"Soy una figura geométrica llamada {self.name}"
