class ProductoMenu:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_total(self):
        return self.precio


class Gaseosa(ProductoMenu):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño


class Adicion(ProductoMenu):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)


class Burguer(ProductoMenu):
    def __init__(self, nombre, precio, veggie, doble):
        super().__init__(nombre, precio)
        self.veggie = veggie
        self.doble = doble


class Pedido:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total_pedido(self):
        total = sum(p.precio_total() for p in self.productos)
        total = self.descuento(total)
        return total

    def descuento(self, total):
        burguers = [p for p in self.productos if isinstance(p, Burguer)]
        if len(burguers) > 2:
            return total * 0.9
        return total

    def mostrar_pedido(self):
        print("Bienvenido a Vete a la Burguer")
        print("Tu pedido:")
        for p in self.productos:
            print(f"- {p.nombre}: ${p.precio:.2f}")
        print(f"Total a pagar: ${self.total_pedido():.2f}")


if __name__ == "__main__":
    menu = [
        Burguer("La Incomible", 85, False, False),
        Burguer("La Tóxica", 95, False, False),
        Burguer("La Ex", 90, True, False),
        Burguer("La Infiel", 110, False, True),
        Burguer("La Chismosa", 88, False, False),
        Burguer("La Intensita", 92, False, False),
        Burguer("La Drama Queen", 100, False, False),
        Burguer("La Amiga Date Cuenta", 97, False, False),
        Burguer("La Celosa", 105, False, False),
        Burguer("La Tóxica Veggie", 93, True, False),
        Gaseosa("Coca-Cola", 20, "mediana"),
        Gaseosa("Pepsi", 20, "mediana"),
        Gaseosa("Sprite", 20, "mediana"),
        Gaseosa("Fanta", 20, "mediana"),
        Gaseosa("Manzana", 22, "grande"),
        Gaseosa("Colombiana", 22, "grande"),
        Gaseosa("7Up", 20, "mediana"),
        Gaseosa("Postobón Uva", 22, "grande"),
        Adicion("Papas Tóxicas", 40),
        Adicion("Aros Incomibles", 45),
        Adicion("Nuggets Intensos", 50),
        Adicion("Mazorca Chismosa", 35),
        Adicion("Queso Infiel", 10),
        Adicion("Tocineta Celosa", 12),
        Adicion("Salsa Drama", 8),
        Adicion("Guacamole Ex", 15),
    ]

    pedido = Pedido()
    pedido.agregar_producto(menu[0])   # La
    pedido.agregar_producto(menu[1])   # La Tóxica
    pedido.agregar_producto(menu[3])   # La Infiel
    pedido.agregar_producto(menu[10])  # Coca-Cola
    pedido.agregar_producto(menu[18])  # Papas Tóxicas
    pedido.agregar_producto(menu[22])  # Queso Infiel
    pedido.agregar_producto(menu[23])  # Tocineta Celosa

    pedido.mostrar_pedido()