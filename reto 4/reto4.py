import math

class Punto:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def obtener_x(self):
        return self._x

    def obtener_y(self):
        return self._y

    def cambiar_x(self, nuevo_x):
        self._x = nuevo_x

    def cambiar_y(self, nuevo_y):
        self._y = nuevo_y

    def calcular_distancia(self, otro_punto):
        return math.sqrt((self._x - otro_punto._x) ** 2 + (self._y - otro_punto._y) ** 2)

class Linea:
    def __init__(self, punto_inicio, punto_fin):
        self._punto_inicio = punto_inicio
        self._punto_fin = punto_fin

    def obtener_punto_inicio(self):
        return self._punto_inicio

    def obtener_punto_fin(self):
        return self._punto_fin

    def cambiar_punto_inicio(self, nuevo_inicio):
        self._punto_inicio = nuevo_inicio

    def cambiar_punto_fin(self, nuevo_fin):
        self._punto_fin = nuevo_fin

    def longitud(self):
        return self._punto_inicio.calcular_distancia(self._punto_fin)

class Figura:
    def __init__(self, vertices):
        self._vertices = vertices
        self._lados = self._calcular_lados()
        self._es_regular = False

    def obtener_vertices(self):
        return self._vertices

    def cambiar_vertices(self, nuevos_vertices):
        self._vertices = nuevos_vertices
        self._lados = self._calcular_lados()

    def obtener_lados(self):
        return self._lados

    def es_regular(self):
        return self._es_regular

    def cambiar_regularidad(self, valor):
        self._es_regular = valor

    def _calcular_lados(self):
        lados = []
        n = len(self._vertices)
        for i in range(n):
            lados.append(Linea(self._vertices[i], self._vertices[(i+1)%n]))
        return lados

    def calcular_perimetro(self):
        total = 0
        for lado in self._lados:
            total += lado.longitud()
        return total

    def calcular_area(self):
        print("Este método debe ser implementado por las subclases.")
        return None

class Rectangulo(Figura):
    def __init__(self, esquina_inferior_izq, ancho, alto):
        vertices = [
            esquina_inferior_izq,
            Punto(esquina_inferior_izq.obtener_x() + ancho, esquina_inferior_izq.obtener_y()),
            Punto(esquina_inferior_izq.obtener_x() + ancho, esquina_inferior_izq.obtener_y() + alto),
            Punto(esquina_inferior_izq.obtener_x(), esquina_inferior_izq.obtener_y() + alto)
        ]
        super().__init__(vertices)
        self._ancho = ancho
        self._alto = alto

    def obtener_ancho(self):
        return self._ancho

    def cambiar_ancho(self, nuevo_ancho):
        self._ancho = nuevo_ancho
        self.cambiar_vertices([
            self._vertices[0],
            Punto(self._vertices[0].obtener_x() + nuevo_ancho, self._vertices[0].obtener_y()),
            Punto(self._vertices[0].obtener_x() + nuevo_ancho, self._vertices[0].obtener_y() + self._alto),
            Punto(self._vertices[0].obtener_x(), self._vertices[0].obtener_y() + self._alto)
        ])

    def obtener_alto(self):
        return self._alto

    def cambiar_alto(self, nuevo_alto):
        self._alto = nuevo_alto
        self.cambiar_vertices([
            self._vertices[0],
            Punto(self._vertices[0].obtener_x() + self._ancho, self._vertices[0].obtener_y()),
            Punto(self._vertices[0].obtener_x() + self._ancho, self._vertices[0].obtener_y() + nuevo_alto),
            Punto(self._vertices[0].obtener_x(), self._vertices[0].obtener_y() + nuevo_alto)
        ])

    def calcular_area(self):
        return self._ancho * self._alto

    def calcular_perimetro(self):
        return 2 * (self._ancho + self._alto)

class Cuadrado(Rectangulo):
    def __init__(self, esquina_inferior_izq, lado):
        super().__init__(esquina_inferior_izq, lado, lado)
        self._lado = lado
        self.cambiar_regularidad(True)

    def obtener_lado(self):
        return self._lado

    def cambiar_lado(self, nuevo_lado):
        self._lado = nuevo_lado
        self.cambiar_ancho(nuevo_lado)
        self.cambiar_alto(nuevo_lado)

    def calcular_area(self):
        return self._lado ** 2

    def calcular_perimetro(self):
        return 4 * self._lado

class Triangulo(Figura):
    def __init__(self, p1, p2, p3):
        vertices = [p1, p2, p3]
        super().__init__(vertices)

    def calcular_area(self):
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def calcular_angulos_internos(self):
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        try:
            angulo_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
            angulo_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
            angulo_C = 180 - angulo_A - angulo_B
            return [angulo_A, angulo_B, angulo_C]
        except:
            return [None, None, None]

class Isosceles(Triangulo):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        if not ((a == b and b != c) or (a == c and a != b) or (b == c and b != a)):
            print("Advertencia: No es un triángulo isósceles.")

class Equilatero(Triangulo):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        if not (abs(a - b) < 1e-6 and abs(a - c) < 1e-6):
            print("Advertencia: No es un triángulo equilátero.")
        else:
            self.cambiar_regularidad(True)

class Escaleno(Triangulo):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        if a == b or a == c or b == c:
            print("Advertencia: No es un triángulo escaleno.")

class TriRectangulo(Triangulo):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)
        a = self._lados[0].longitud()
        b = self._lados[1].longitud()
        c = self._lados[2].longitud()
        lados = sorted([a, b, c])
        if not math.isclose(lados[0]**2 + lados[1]**2, lados[2]**2, rel_tol=1e-6):
            print("Advertencia: No es un triángulo rectángulo.")

if __name__ == "__main__":
    print("Rectángulo 1:")
    rect1 = Rectangulo(Punto(0, 0), 5, 2)
    print("Area:", rect1.calcular_area())
    print("Perimetro:", rect1.calcular_perimetro())

    print("\nRectángulo 2:")
    rect2 = Rectangulo(Punto(-3, 4), 7, 3)
    print("Area:", rect2.calcular_area())
    print("Perimetro:", rect2.calcular_perimetro())

    print("\nCuadrado 1:")
    cuad1 = Cuadrado(Punto(1, 1), 4)
    print("Area:", cuad1.calcular_area())
    print("Perimetro:", cuad1.calcular_perimetro())

    print("\nCuadrado 2:")
    cuad2 = Cuadrado(Punto(-2, -2), 10)
    print("Area:", cuad2.calcular_area())
    print("Perimetro:", cuad2.calcular_perimetro())

    print("\nTriángulo genérico:")
    t1 = Triangulo(Punto(0, 0), Punto(4, 0), Punto(0, 3))
    print("Area:", t1.calcular_area())
    print("Perimetro:", t1.calcular_perimetro())
    print("Angulos internos:", t1.calcular_angulos_internos())

    print("\nTriángulo isósceles:")
    t2 = Isosceles(Punto(0, 0), Punto(2, 0), Punto(1, 2))
    print("Area:", t2.calcular_area())
    print("Perimetro:", t2.calcular_perimetro())
    print("Angulos internos:", t2.calcular_angulos_internos())

    print("\nTriángulo equilátero:")
    t3 = Equilatero(Punto(0, 0), Punto(1, math.sqrt(3)), Punto(2, 0))
    print("Area:", t3.calcular_area())
    print("Perimetro:", t3.calcular_perimetro())
    print("Angulos internos:", t3.calcular_angulos_internos())

    print("\nTriángulo escaleno:")
    t4 = Escaleno(Punto(0, 0), Punto(4, 0), Punto(1, 3))
    print("Area:", t4.calcular_area())
    print("Perimetro:", t4.calcular_perimetro())
    print("Angulos internos:", t4.calcular_angulos_internos())

    print("\nTriángulo rectangulo:")
    t5 = TriRectangulo(Punto(0, 0), Punto(3, 0), Punto(0, 4))
    print("Area:", t5.calcular_area())
    print("Perimetro:", t5.calcular_perimetro())
    print("Angulos internos:", t5.calcular_angulos_internos())
    print()
    print()
#Ejemplos donde no se cumple con las caracteristicas de los triangulos
    print("cuando las condiciones de los triangulos no se cumplen :(")
    t = Equilatero(Punto(0, 0), Punto(2, 0), Punto(1, 1))
    t = Isosceles(Punto(0, 0), Punto(2, 0), Punto(1, 3))
    t = Escaleno(Punto(0, 0), Punto(2, 0), Punto(1, 0))
    t = TriRectangulo(Punto(0, 0), Punto(1, 1), Punto(2, 2))
    print()
    print()
    print()
    print("Gracias por usar :)")  
    