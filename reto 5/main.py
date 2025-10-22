
from Shape import Circle, Rectangle

def main():
    circle = Circle(7)
    rectangle = Rectangle(5, 3)

    print(circle.describe())
    print(f"Área del círculo: {circle.area():.2f}")
    print(f"Perímetro del círculo: {circle.perimeter():.2f}\n")

    print(rectangle.describe())
    print(f"Área del rectángulo: {rectangle.area()}")
    print(f"Perímetro del rectángulo: {rectangle.perimeter()}")

if __name__ == "__main__":
    main()
