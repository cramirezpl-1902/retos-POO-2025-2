def mayor_suma_consecutiva(lista):
    if len(lista) < 2:
        return "La lista debe tener al menos dos números"
    mayor = lista[0] + lista[1]
    i = 1
    while i < len(lista) - 1:
        suma = lista[i] + lista[i + 1]
        if suma > mayor:
            mayor = suma
        i = i + 1
    return mayor

if __name__ == "__main__":
    print("Mayor suma entre dos números consecutivos")
    numeros = input("Ingrese una lista de números separados por espacios: ")
    lista = [int(x) for x in numeros.split()]
    print("La mayor suma consecutiva es:", mayor_suma_consecutiva(lista))
