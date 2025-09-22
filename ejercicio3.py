def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i = i + 1
    return True

if __name__ == "__main__":
    print("¿Es primo o no es primo? ")
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(numero, "es primo")
    else:
        print(numero, "no es primo")

