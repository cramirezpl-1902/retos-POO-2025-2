def es_palindromo(palabra):
    palabra = palabra.lower()
    izquierda = 0
    derecha = len(palabra) - 1
    while izquierda < derecha:
        if palabra[izquierda] != palabra[derecha]:
            return False
        izquierda = izquierda + 1
        derecha = derecha - 1
    return True

if __name__ == "__main__":
    print(" Verificador de palíndromos B)")
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print("Sí es un palíndromo")
    else:
        print("No es un palíndromo")
