class ProductoMenu:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    def precio_total(self):
        return self._precio


class Gaseosa(ProductoMenu):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self._tamaño = tamaño

    def get_tamaño(self):
        return self._tamaño

    def set_tamaño(self, tamaño):
        self._tamaño = tamaño

    def precio_total(self):
        return self._precio


class Adicion(ProductoMenu):
    def __init__(self, nombre, precio):
        super().__init__(nombre, precio)


class Burguer(ProductoMenu):
    def __init__(self, nombre, precio, veggie, doble):
        super().__init__(nombre, precio)
        self._veggie = veggie
        self._doble = doble

    def get_veggie(self):
        return self._veggie

    def set_veggie(self, veggie):
        self._veggie = veggie

    def get_doble(self):
        return self._doble

    def set_doble(self, doble):
        self._doble = doble

    def precio_total(self):
        precio_final = self._precio
        if self._doble:
            precio_final *= 1.2
        return precio_final


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
        gaseosas = [p for p in self.productos if isinstance(p, Gaseosa)]
        if len(burguers) > 2:
            total *= 0.9
        if burguers and gaseosas:
            descuento_gaseosas = sum(p.precio_total() * 0.2 for p in gaseosas)
            total -= descuento_gaseosas
        return total

    def mostrar_pedido(self):
        print(" Bienvenido a Vete a la Burguer ")
        print("Tu pedido:")
        for p in self.productos:
            print(f"- {p.get_nombre()}: ${p.precio_total():.2f}")
        print(f"\nTotal a pagar: ${self.total_pedido():.2f}")


class Pago:
    def __init__(self):
        pass

    def pagar(self, monto):
        raise NotImplementedError("Las subclases deben implementar el método pagar().")


class Tarjeta(Pago):
    def __init__(self, numero, cvv):
        super().__init__()
        self.numero = numero
        self.cvv = cvv

    def pagar(self, monto):
        print(f"Pagando ${monto:.2f} con tarjeta terminada en {self.numero[-4:]}")


class Efectivo(Pago):
    def __init__(self, monto_entregado):
        super().__init__()
        self.monto_entregado = monto_entregado

    def pagar(self, monto):
        if self.monto_entregado >= monto:
            cambio = self.monto_entregado - monto
            print(f"Pago en efectivo realizado. Cambio: ${cambio:.2f}")
        else:
            faltante = monto - self.monto_entregado
            print(f"Fondos insuficientes. Faltan ${faltante:.2f} para completar el pago.")


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
    pedido.agregar_producto(menu[0])
    pedido.agregar_producto(menu[1])
    pedido.agregar_producto(menu[3])
    pedido.agregar_producto(menu[10])
    pedido.agregar_producto(menu[18])
    pedido.agregar_producto(menu[22])
    pedido.agregar_producto(menu[23])

    pedido.mostrar_pedido()

    print("\n--- Método de Pago ---")
    total = pedido.total_pedido()

    pago = Tarjeta("1234567890123456", 123)
    # pago = Efectivo(300)

    pago.pagar(total)

