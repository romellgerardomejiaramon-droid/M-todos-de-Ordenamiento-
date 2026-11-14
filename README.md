# Métodos-de-Ordenamiento-

# Métodos de ordenamiento en Python

Colección de 9 programas en Python que aplican tres métodos de ordenamiento: **burbuja**, **inserción** y **selección**. Hay tres ejercicios por método, y cada programa funciona de forma independiente desde la terminal.

## Requisitos

- Python 3.6 o superior (se usan f-strings).
- No necesita instalar librerías externas.

## Cómo ejecutar

bash
python burbuja_ejercicio1.py


En algunos sistemas el comando es python3 en lugar de python.

## Archivos

| Método | Archivo | Ejercicio |
|---|---|---|
| Burbuja | burbuja_ejercicio1.py | Ranking de calificaciones |
| Burbuja | burbuja_ejercicio2.py | Inventario de una tienda |
| Burbuja | burbuja_ejercicio3.py | Ordenar nombres (A-Z / Z-A) |
| Inserción | insercion_ejercicio1.py | Resultados de una carrera |
| Inserción | insercion_ejercicio2.py | Catálogo de una biblioteca |
| Inserción | insercion_ejercicio3.py | Ordenar números paso a paso |
| Selección | seleccion_ejercicio1.py | Puntajes de un videojuego |
| Selección | seleccion_ejercicio2.py | Nómina de empleados |
| Selección | seleccion_ejercicio3.py | Temperaturas de ciudades |

## Menú principal

Todos los programas muestran el mismo menú:

===== MENÚ =====
1. Usar ejemplo
2. Crear mis propios datos
3. Salir

- **Opción 1:** carga datos de ejemplo ya escritos en el código, muestra el resultado y regresa al menú.
- **Opción 2:** pide los datos al usuario (validándolos), muestra el resultado y regresa al menú.
- **Opción 3:** termina el programa e imprime Fin del programa.
- Una opción inválida muestra Opción no válida. y vuelve a mostrar el menú.

burbuja_ejercicio3.py e insercion_ejercicio3.py tienen además un submenú para elegir el orden (A-Z / Z-A o menor a mayor / mayor a menor) y volver al menú principal.

## Funcionamiento interno

Al ejecutar un programa, Python define todas las funciones y después llama a main(), que contiene el ciclo del menú:


while True:
    mostrar opciones
    leer opción
    si es 1 → mostrar_resultados(datos de ejemplo)
    si es 2 → capturar datos y mostrar_resultados(datos)
    si es 3 → break
    si no   → "Opción no válida."


Al terminar main(), se imprime Fin del programa.

### Funciones comunes

| Función | Para qué sirve |
|---|---|
| leer() | Envuelve a input(): limpia espacios y caracteres invisibles, y termina sin error si no llegan datos. |
| pedir_entero() / pedir_decimal() | Piden un número en un ciclo hasta que sea válido. Aceptan coma decimal (9,5) y validan rangos. |
| ..._ejemplo() | Devuelve datos de ejemplo (una lista nueva cada vez). |
| ..._manual() | Captura los datos que escribe el usuario. |
| mostrar_resultados() | Ordena los datos y muestra la información. |

## Métodos de ordenamiento

| | Burbuja | Inserción | Selección |
|---|---|---|---|
| **Idea** | Compara elementos vecinos y los intercambia si están al revés | Toma cada elemento y lo coloca en su lugar entre los ya ordenados | Busca el menor (o mayor) de los que faltan y lo coloca en su posición |
| **Mejor caso** | Rápido si ya está ordenada | Rápido si está casi ordenada | Siempre hace las mismas comparaciones |
| **Peor caso** | O(n²) | O(n²) | O(n²) |
| **Intercambios** | Muchos | Desplaza elementos | Pocos (máximo n-1) |
| **Útil para** | Aprender, listas pequeñas | Listas pequeñas o casi ordenadas | Cuando mover datos es costoso |

- **Burbuja:** el ciclo externo cuenta las pasadas y el interno compara lista[j] con lista[j + 1]. Si una pasada no hace cambios, se detiene antes.
- **Inserción:** actual guarda el elemento a colocar. Se recorren hacia la derecha los elementos mayores, y actual se coloca en el hueco.
- **Selección:** en cada vuelta se guarda la posición del mejor elemento restante y se intercambia una sola vez con la posición actual.

## Descripción de los programas

### Burbuja
- **Ejercicio 1:** ordena a los alumnos de mayor a menor calificación. Muestra el ranking, el promedio, la nota más alta y la más baja, y las comparaciones e intercambios realizados.
- **Ejercicio 2:** ordena el inventario de una tienda por precio (ascendente y descendente) y por existencia. Muestra los productos por reabastecer.
- **Ejercicio 3:** ordena nombres de la A a la Z o de la Z a la A, mostrando cada pasada.

### Inserción
- **Ejercicio 1:** ordena corredores por tiempo. Muestra el podio, el tiempo promedio, la diferencia entre el primero y el último, y los desplazamientos realizados.
- **Ejercicio 2:** ordena un catálogo de libros por año, páginas y título. Muestra el libro más corto y el más largo.
- **Ejercicio 3:** ordena números mostrando cómo se inserta cada elemento.

### Selección
- **Ejercicio 1:** ordena jugadores por puntaje. Muestra la tabla, el campeón, el total y el promedio.
- **Ejercicio 2:** ordena empleados por sueldo, antigüedad y nombre. Muestra la nómina total y el sueldo más alto.
- **Ejercicio 3:** ordena ciudades por temperatura mostrando cada paso. Muestra la ciudad más fría, la más cálida y la diferencia.

## Herramientas de Python utilizadas

- Listas de diccionarios para guardar varios datos por elemento.
- .copy() para ordenar sin alterar la lista original.
- Intercambio de variables con a, b = b, a.
- f-strings con formato (:<15, :>10, :.2f) para alinear columnas.
- enumerate, zip, sum y len.
- try/except ValueError para validar la captura de datos.
