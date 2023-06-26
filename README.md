# Sopa de Letras en Python ByteBuilders
![image](https://user-images.githubusercontent.com/124606636/225486236-e4618eec-16f2-465f-b317-142d70c5942e.png)

Creamos un  programa en Python que genera una sopa de letras y permite al usuario buscar palabras en ella. A continuación, se explica el código y la función de cada parte.

## Funciones

### `crear_matriz(filas, columnas)`

Esta función recibe el número de filas y columnas y devuelve una matriz vacía con el tamaño especificado. La matriz se representa como una lista de listas, donde cada elemento representa una celda en la sopa de letras.

### `mostrar_matriz(matriz)`

Esta función recibe una matriz y la imprime en la consola, mostrando la sopa de letras.

### `colocar_palabra(matriz, palabra, fila, columna, direccion)`

Esta función recibe una matriz, una palabra, una posición inicial (fila y columna) y una dirección (horizontal, vertical o diagonal). Intenta colocar la palabra en la matriz siguiendo la dirección especificada. Devuelve `True` si la palabra se pudo colocar correctamente y `False` en caso contrario.

### `llenar_espacios_vacios(matriz)`

Esta función recibe una matriz parcialmente llena y la completa con letras aleatorias en las celdas vacías. Utiliza el módulo `string` para obtener el alfabeto en mayúsculas y selecciona una letra al azar para cada celda vacía.

### `buscar_palabra(matriz, palabra)`

Esta función recorre la matriz en busca de la primera letra de la palabra especificada. Luego, llama a `buscar_palabra_direccion` para intentar encontrar la palabra en todas las direcciones posibles (horizontal, vertical y diagonal). Devuelve `True` si encuentra la palabra y `False` en caso contrario.

### `buscar_palabra_direccion(matriz, palabra, fila, columna)`

Esta función recibe una matriz, una palabra y una posición inicial (fila y columna). Intenta colocar la palabra en la matriz en todas las direcciones posibles y devuelve `True` si la encuentra en alguna dirección y `False` en caso contrario.

### `main()`

Esta es la función principal del programa. Solicita al usuario el tamaño de la sopa de letras, la lista de palabras a buscar y muestra la sopa de letras resultante. Luego, permite al usuario ingresar coordenadas para buscar las palabras en la sopa.

## Uso del código

El código se ejecuta desde la función `main()`, que se llama al final del script utilizando la construcción `if __name__ == "__main__":`.

Para utilizar el programa, se debe ejecutar el archivo `sopa_de_letras.py` en la línea de comandos o terminal. A continuación, se solicitará al usuario ingresar el tamaño de la sopa de letras, las palabras a buscar y las coordenadas para buscar las palabras. Se mostrará la sopa de letras final y las palabras encontradas.

Es necesario importar las librerias de Random y String para poder ejecutar el codigo. 

## Colaboradores

- Alejandro Ortega(https://github.com/dortegasa)
- Julian Lopez(https://github.com/julopezpa)
- Carlos Villamil Bejarano(https://github.com/crlos-16)
  


