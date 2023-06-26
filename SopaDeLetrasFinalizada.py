import random   # Importar el módulo random para generar números aleatorios
import string   # Importar el módulo string para trabajar con caracteres

def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [" "] * columnas  # Crear una lista de espacios vacíos del tamaño de las columnas
        matriz.append(fila)  # Agregar la fila a la matriz
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(fila))  # Unir los elementos de cada fila con un espacio y mostrarlos

def colocar_palabra(matriz, palabra, fila, columna, direccion): # Verificar si la palabra cabe en la matriz en la dirección dada
    if direccion == "horizontal" and columna + len(palabra) > len(matriz[0]):
        return False
    elif direccion == "vertical" and fila + len(palabra) > len(matriz):
        return False
    elif direccion == "diagonal" and (fila + len(palabra) > len(matriz) or columna + len(palabra) > len(matriz[0])):
        return False

    for i, letra in enumerate(palabra): # Verificar si la posición está vacía o coincide con la letra de la palabra
        if direccion == "horizontal":
            if matriz[fila][columna + i] != " " and matriz[fila][columna + i] != letra:
                return False
        elif direccion == "vertical":
            if matriz[fila + i][columna] != " " and matriz[fila + i][columna] != letra:
                return False
        elif direccion == "diagonal":
            if matriz[fila + i][columna + i] != " " and matriz[fila + i][columna + i] != letra:
                return False

    for i, letra in enumerate(palabra): # Colocar la palabra en la matriz
        if direccion == "horizontal":
            matriz[fila][columna + i] = letra
        elif direccion == "vertical":
            matriz[fila + i][columna] = letra
        elif direccion == "diagonal":
            matriz[fila + i][columna + i] = letra

    return True

def llenar_espacios_vacios(matriz):
    letras = string.ascii_uppercase  # Todas las letras mayúsculas del alfabeto
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == " ": # Verificar si el espacio está vacío
                matriz[i][j] = random.choice(letras)  # Asignar una letra aleatoria a ese espacio

def buscar_palabra(matriz, palabra):    #Verifica si la palabra esta en ese posicion
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == palabra[0]:
                if buscar_palabra_direccion(matriz, palabra, fila, columna):
                    return True
    return False

def buscar_palabra_direccion(matriz, palabra, fila, columna):   #Verifica la direccion en la que va la palabra
    for direccion in ["horizontal", "vertical", "diagonal"]:
        if colocar_palabra(matriz, palabra, fila, columna, direccion):
            return True
    return False

def main():
    min_tamano = 10  # Tamaño mínimo de la matriz
    max_tamano = 30  # Tamaño máximo de la matriz

    # Solicitar el tamaño de la matriz al usuario
    while True:
        try:
            filas = int(input("Ingrese el número de filas (entre {} y {}): ".format(min_tamano, max_tamano)))
            columnas = int(input("Ingrese el número de columnas (entre {} y {}): ".format(min_tamano, max_tamano)))

            if min_tamano <= filas <= max_tamano and min_tamano <= columnas <= max_tamano:
                break
            else:
                print("Error: el tamaño de la matriz debe estar entre {} y {}.".format(min_tamano, max_tamano))
        except ValueError:
            print("Error: por favor ingrese un número válido.")
    # Crear y mostrar la matriz
    matriz = crear_matriz(filas, columnas)
   
    palabras = []
    while True:
        palabra = input("Ingrese una palabra en mayúsculas (o presione Enter para finalizar): ")
        if not palabra:
            break
        palabras.append(palabra)

    # Colocar palabras aleatoriamente en la matriz
    for palabra in palabras:
        colocada = False
        while not colocada:
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
            direccion = random.choice(["horizontal", "vertical", "diagonal"])
            colocada = colocar_palabra(matriz, palabra, fila, columna, direccion)
    
    # Llenar los espacios vacíos con letras aleatorias
    llenar_espacios_vacios(matriz)

    print("\nMatriz final:")
    mostrar_matriz(matriz)
    print("\n¡Ahora es tu turno de resolver la sopa de letras!")
    palabras_encontradas = []
    while palabras:
        coordenadas = input("Ingrese las coordenadas (fila, columna) de una letra: ")
        fila, columna = map(int, coordenadas.split(","))
        if 0 <= fila < filas and 0 <= columna < columnas:
            letra = matriz[fila][columna]
            for palabra in palabras:
                if letra in palabra:
                    if buscar_palabra(matriz, palabra):
                        palabras_encontradas.append(palabra)
                        palabras.remove(palabra)
                        print("¡Encontraste la palabra '{}'!".format(palabra))
                        break
            else:
                print("No hay ninguna palabra en esas coordenadas.")
        else:
            print("Coordenadas inválidas. Por favor, ingrese coordenadas dentro del rango.")

    print("¡Has encontrado todas las palabras!")
    print("Palabras encontradas: {}".format(", ".join(palabras_encontradas)))

if __name__ == "__main__":
    main()  #Ejecuta la funcion principal