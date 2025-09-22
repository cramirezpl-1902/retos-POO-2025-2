def son_anagramas(palabra1, palabra2):
    return sorted(palabra1) == sorted(palabra2)

def filtrar_anagramas(lista):
    resultado = []
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if son_anagramas(lista[i], lista[j]):
                if lista[i] not in resultado:
                    resultado.append(lista[i])
                if lista[j] not in resultado:
                    resultado.append(lista[j])
            j = j + 1
        i = i + 1
    return resultado

if __name__ == "__main__":
    print(" Detector de anagramas exactos :0")
    palabras = input("Ingrese palabras separadas por espacios: ")
    lista = palabras.split()
    print("Palabras que son anagramas:", filtrar_anagramas(lista))

