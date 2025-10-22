def operar(a, b, op):
    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        if b == 0:
            resultado = "Error: división entre cero"
        else:
            resultado = a / b
    else:
        resultado = "Operación no válida"
    return resultado

if __name__ == "__main__":
    print(" Calculadora de operaciones básicas :) ")
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    op = input("Ingrese la operación (+, -, *, /): ")
    print("Resultado:", operar(a, b, op))
