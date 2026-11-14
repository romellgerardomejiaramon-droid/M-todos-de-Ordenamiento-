METODOS DE ORDENAMIENTO EN PYTHON
=================================

Colección de 9 programas que aplican tres métodos de ordenamiento: burbuja, inserción y selección, con tres ejercicios por método. Cada programa es independiente, se ejecuta desde la terminal y funciona con un menú interactivo.


1. REQUISITOS Y COMO EJECUTAR
-----------------------------

- Python 3.6 o superior (se usan f-strings).
- No requiere instalar librerías externas. Solo usa unicodedata y math, que vienen incluidas con Python.

Para ejecutar un programa, desde la carpeta donde están los archivos:

    python burbuja_ejercicio1.py

En algunos sistemas el comando es python3 en lugar de python.


2. ARCHIVOS
-----------

Burbuja:
- burbuja_ejercicio1.py: ranking de calificaciones
- burbuja_ejercicio2.py: inventario de una tienda
- burbuja_ejercicio3.py: ordenar nombres (A-Z / Z-A)

Inserción:
- insercion_ejercicio1.py: resultados de una carrera
- insercion_ejercicio2.py: catálogo de una biblioteca
- insercion_ejercicio3.py: ordenar números paso a paso

Selección:
- seleccion_ejercicio1.py: puntajes de un videojuego
- seleccion_ejercicio2.py: nómina de empleados
- seleccion_ejercicio3.py: temperaturas de ciudades


3. ESTRUCTURA INTERNA COMUN A TODOS LOS PROGRAMAS
-------------------------------------------------

3.1 Orden en que Python ejecuta un archivo

Python lee el archivo de arriba hacia abajo, una sola vez:

1. Importa los módulos (import unicodedata, y import math en los que lo necesitan).
2. Define todas las funciones (def ...). En este paso no se ejecuta nada de lo que hay dentro de ellas: solo se guardan en memoria.
3. Llega a la línea main() y ahí empieza el programa de verdad. main() contiene el ciclo del menú.
4. Cuando main() termina (el usuario eligió "Salir"), Python ejecuta la última línea, que imprime "Fin del programa."

3.2 La función leer()

Envuelve a input(). Hace tres cosas:

1. Lee lo que escribe el usuario con input(mensaje).
2. Lo limpia: unicodedata.normalize("NFKC", texto) convierte caracteres raros a su forma normal (por ejemplo, un 3 de ancho completo se vuelve un 3 normal), y la línea que usa isprintable() elimina caracteres invisibles que algunos editores o terminales agregan. Después strip() quita los espacios al inicio y al final.
3. Si el entorno no puede entregar más datos (EOFError), imprime "Fin del programa." y cierra con raise SystemExit, en lugar de mostrar un error.

Todo input() de los programas pasa por leer(). Por eso los menús y la captura de datos aceptan entradas como "3 " (con un espacio de más) sin problema.

3.3 Validación: pedir_entero() y pedir_decimal()

Piden un dato dentro de un ciclo while True que solo termina con return cuando el valor es válido:

1. Llaman a leer() para obtener el texto.
2. Intentan convertirlo con float(texto.replace(",", ".")). El replace permite escribir 9,5 además de 9.5.
3. Si falla (ValueError), muestran qué texto se recibió, por ejemplo: 'abc' no es un número... y continue vuelve a pedir el dato.
4. Validan el valor:
   - pedir_entero rechaza decimales (is_integer), valores infinitos (math.isfinite) y valores menores que minimo. Devuelve int(numero).
   - pedir_decimal rechaza valores fuera del rango entre minimo y maximo. Devuelve un float.

Los mínimos y máximos cambian según el dato: calificación de 0 a 10, precio mayor o igual a 0.01, existencia mayor o igual a 0, temperatura entre -80 y 60, etcétera.

3.4 Datos de ejemplo y datos manuales

Cada programa tiene dos funciones que devuelven la lista de datos con la que trabajará mostrar_resultados:

- Las funciones de ejemplo (alumnos_ejemplo, inventario_ejemplo, etc.) devuelven una lista ya escrita en el código. Crean una lista nueva en cada llamada, así que ordenar el ejemplo no lo daña para la siguiente vez que se elija la opción 1.
- Las funciones manuales (alumnos_manual, inventario_manual, etc.) preguntan cuántos elementos se van a registrar, repiten un ciclo for pidiendo cada dato con pedir_entero, pedir_decimal o leer, y devuelven la lista armada. Los elementos son diccionarios (por ejemplo {"nombre": "Ana", "calificacion": 9.5}), que permiten guardar varios datos por elemento.

3.5 mostrar_resultados()

Recibe la lista ya capturada, la ordena con el método del programa y muestra tablas y estadísticas (promedio, máximo, mínimo, totales, etcétera). Separa "qué se calcula" de "cómo se pide el dato", y es lo que se llama tanto desde la opción 1 como desde la opción 2.

3.6 main() y cómo funciona el menú

El menú de todos los programas tiene esta forma:

    def main():
        while True:
            print("\n===== MENÚ =====")
            print("1. Usar ejemplo")
            print("2. Crear mis propios datos")
            print("3. Salir")
            opcion = leer("Elige una opción: ")

            if opcion == "1":
                mostrar_resultados(datos_ejemplo())
            elif opcion == "2":
                datos = datos_manual()
                if datos:
                    mostrar_resultados(datos)
            elif opcion == "3":
                break
            else:
                print("Opción no válida.")

Cómo trabaja:

- while True repite el menú indefinidamente. Por eso, después de mostrar un resultado, el programa regresa solo al menú: simplemente termina la vuelta del ciclo y empieza otra.
- Opción 1: llama a mostrar_resultados con los datos de ejemplo.
- Opción 2: primero captura los datos con la función manual y luego los manda a mostrar_resultados.
- if datos: en burbuja 3 e inserción 3 la captura manual devuelve None si el usuario escribe menos de 2 elementos (no tiene sentido ordenar uno solo). Esta condición evita intentar ordenar None y el programa vuelve al menú.
- Opción 3: ejecuta break, que rompe el while True. main() termina y se imprime "Fin del programa."
- Cualquier otra cosa (9, una letra, vacío): cae en el else, imprime "Opción no válida." y el ciclo vuelve a mostrar el menú.

3.7 Submenús (burbuja 3 e inserción 3)

Estos dos programas tienen un segundo ciclo while True dentro de mostrar_resultados para elegir el orden:

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z          (o "De menor a mayor")
    2. De la Z a la A          (o "De mayor a menor")
    3. Volver al menú principal

Con 1 o 2 se ordena una copia de la lista y se muestra el resultado, y el submenú se repite: se puede ordenar la misma lista varias veces sin volver a capturarla. Con 3 se ejecuta break y se regresa al menú principal.

3.8 copy() y ordenar "en el lugar"

Los métodos de estos programas modifican la lista que reciben (ordenan "en el lugar"). Cuando el programa necesita ordenar varias veces la misma lista (por precio, por existencia, etcétera), usa lista.copy() para trabajar con una copia y no perder el orden original.


4. LOS METODOS DE ORDENAMIENTO
------------------------------

Los tres usan listas de Python y tienen complejidad O(n²) en el peor caso, así que sirven bien para listas pequeñas como las de estos ejercicios. Para miles de elementos se usan algoritmos más rápidos (en Python, la función sorted()).

4.1 Burbuja

Idea: comparar pares de elementos vecinos e intercambiarlos si están en el orden equivocado. Después de cada pasada, el elemento más grande (o más pequeño, según el orden) "sube como burbuja" hasta su posición final.

    def burbuja(lista):
        n = len(lista)
        for i in range(n - 1):               # i = número de pasada
            hubo_cambio = False
            for j in range(n - 1 - i):       # compara vecinos
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    hubo_cambio = True
            if not hubo_cambio:              # si no cambió nada, ya está ordenada
                break

- El ciclo de afuera (i) cuenta las pasadas.
- El de adentro (j) compara lista[j] con lista[j + 1].
- El límite n - 1 - i evita revisar el final de la lista, donde ya están los elementos que quedaron en su lugar en pasadas anteriores.
- hubo_cambio detiene el algoritmo antes si una pasada completa no intercambió nada.

Ejemplo con la lista [5, 3, 8, 1]:

- Pasada 1: 5 > 3 intercambia; 5 < 8 no; 8 > 1 intercambia. Queda [3, 5, 1, 8].
- Pasada 2: 3 < 5 no; 5 > 1 intercambia. Queda [3, 1, 5, 8].
- Pasada 3: 3 > 1 intercambia. Queda [1, 3, 5, 8].

Para qué sirve: es el método más simple de entender y de explicar. Es útil para aprender y para listas muy pequeñas o casi ordenadas (gracias a hubo_cambio).

4.2 Inserción

Idea: igual que al ordenar cartas en la mano. Se toma un elemento a la vez y se coloca en el lugar correcto dentro de la parte que ya está ordenada.

    def insercion(lista):
        for i in range(1, len(lista)):
            actual = lista[i]                # elemento que se va a colocar
            j = i - 1
            while j >= 0 and lista[j] > actual:
                lista[j + 1] = lista[j]      # corre el mayor un lugar a la derecha
                j -= 1
            lista[j + 1] = actual            # coloca el elemento en el hueco

- La parte izquierda (desde la posición 0 hasta i-1) siempre está ordenada.
- actual guarda el elemento que se está colocando, porque su posición puede ser sobrescrita al correr los demás.
- El while desplaza (no intercambia) los elementos mayores hacia la derecha hasta encontrar el hueco.

Ejemplo con la lista [5, 3, 8, 1]:

- Paso 1 (actual = 3): corre el 5 y coloca el 3. Queda [3, 5, 8, 1].
- Paso 2 (actual = 8): 5 < 8, ya está en su lugar. Queda [3, 5, 8, 1].
- Paso 3 (actual = 1): corre 8, 5 y 3, y coloca el 1 al inicio. Queda [1, 3, 5, 8].

Para qué sirve: es muy rápido cuando la lista ya está casi ordenada y funciona bien con pocos datos o con datos que llegan de uno en uno.

4.3 Selección

Idea: en cada vuelta se busca el menor elemento (o el mayor, en orden descendente) de la parte que falta por ordenar y se coloca en la siguiente posición.

    def seleccion(lista):
        n = len(lista)
        for i in range(n - 1):
            minimo = i                          # posición del menor encontrado
            for j in range(i + 1, n):
                if lista[j] < lista[minimo]:
                    minimo = j
            lista[i], lista[minimo] = lista[minimo], lista[i]   # un solo intercambio

- El ciclo interno solo busca la posición del menor, no mueve nada.
- Al terminar de buscar se hace un solo intercambio. Por eso hace pocos intercambios (máximo n-1).
- Siempre hace las mismas comparaciones, esté la lista ordenada o no.

Ejemplo con la lista [5, 3, 8, 1]:

- Vuelta 1: el menor es 1 (posición 3) y se intercambia con la posición 0. Queda [1, 3, 8, 5].
- Vuelta 2: el menor de lo que falta es 3, que ya está en su lugar. Queda [1, 3, 8, 5].
- Vuelta 3: el menor de lo que falta es 5 (posición 3) y se intercambia con la posición 2. Queda [1, 3, 5, 8].

Para qué sirve: es útil cuando mover datos es costoso, porque hace muy pocos intercambios.

4.4 Comparación de los tres métodos

- Mejor caso: burbuja O(n) gracias a hubo_cambio; inserción O(n) si la lista está casi ordenada; selección O(n²) siempre.
- Peor caso: los tres O(n²).
- Cómo mueven los datos: burbuja hace muchos intercambios; inserción desplaza elementos; selección hace máximo n-1 intercambios.
- Ideal para: burbuja, aprender y listas pequeñas; inserción, listas pequeñas o casi ordenadas; selección, cuando mover datos es costoso.

4.5 Ordenar de mayor a menor

Los tres métodos pueden ordenar al revés cambiando solo el sentido de la comparación: el signo mayor que pasa a menor que (y viceversa). Los programas que ordenan por distintos criterios lo hacen con un parámetro llamado descendente, que decide qué comparación usar.


5. BURBUJA: LOS TRES PROGRAMAS
------------------------------

5.1 burbuja_ejercicio1.py: ranking de calificaciones

Qué hace: ordena alumnos de mayor a menor calificación y muestra estadísticas del grupo.

Funcionamiento interno:

- burbuja(alumnos) ordena la lista de diccionarios comparando alumnos[j]["calificacion"]. Como quiere el mejor primero, intercambia cuando el de la izquierda tiene menos calificación. Cuenta las comparaciones (cada vez que compara) y los intercambios (cada vez que intercambia) y los devuelve.
- alumnos_ejemplo() devuelve 6 alumnos. alumnos_manual() pregunta cuántos son y, por cada uno, pide el nombre y la calificación con pedir_decimal limitada de 0 a 10.
- mostrar_resultados(alumnos) guarda cantidad = len(alumnos), llama a burbuja (que ordena la lista en el lugar) y luego imprime el ranking con enumerate para numerar las posiciones; calcula el promedio con sum dividido entre la cantidad; toma la nota más alta de alumnos[0] y la más baja de alumnos[-1], porque la lista ya está ordenada; e imprime las comparaciones y los intercambios.

Ejecución en la terminal (lo que aparece después de los dos puntos de cada pregunta es lo que escribe el usuario):

    ===== MENÚ =====
    1. Usar grupo de ejemplo
    2. Registrar mis propios alumnos
    3. Salir
    Elige una opción: 1

    --- RANKING DEL GRUPO ---
    1. María           10.0
    2. Ana             9.5
    3. Sofía           8.2
    4. Luis            7.0
    5. Pedro           6.5
    6. Carlos          5.8

    Promedio del grupo : 7.83
    Calificación más alta: María (10.0)
    Calificación más baja: Carlos (5.8)
    Comparaciones: 12 | Intercambios: 4

    ===== MENÚ =====
    1. Usar grupo de ejemplo
    2. Registrar mis propios alumnos
    3. Salir
    Elige una opción: 2
    ¿Cuántos alumnos desea registrar? 3
    Nombre del alumno 1: Ana
    Calificación de Ana (0 a 10): 9,5
    Nombre del alumno 2: Luis
    Calificación de Luis (0 a 10): abc
    'abc' no es un número. Escribe por ejemplo: 8.5
    Calificación de Luis (0 a 10): 7
    Nombre del alumno 3: Sofía
    Calificación de Sofía (0 a 10): 11
    El valor debe estar entre 0 y 10.
    Calificación de Sofía (0 a 10): 8.5

    --- RANKING DEL GRUPO ---
    1. Ana             9.5
    2. Sofía           8.5
    3. Luis            7.0

    Promedio del grupo : 8.33
    Calificación más alta: Ana (9.5)
    Calificación más baja: Luis (7.0)
    Comparaciones: 3 | Intercambios: 1

    ===== MENÚ =====
    1. Usar grupo de ejemplo
    2. Registrar mis propios alumnos
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar grupo de ejemplo
    2. Registrar mis propios alumnos
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- La opción 1 muestra el resultado y vuelve al menú, sin cerrar el programa.
- En la opción 2 se escribió 9,5 (con coma) y se aceptó; abc se rechazó mostrando lo que se escribió; 11 se rechazó por estar fuera del rango de 0 a 10. En ambos casos el programa vuelve a pedir el mismo dato.
- El 9 en el menú muestra "Opción no válida." y el menú reaparece.
- El 3 rompe el ciclo e imprime "Fin del programa."

5.2 burbuja_ejercicio2.py: inventario de una tienda

Qué hace: ordena un inventario por precio (de menor a mayor y de mayor a menor) y por existencia, y señala los productos por reabastecer.

Funcionamiento interno:

- burbuja(lista, clave, descendente=False) recibe qué campo comparar ("precio" o "stock") y en qué sentido. Dentro del ciclo toma los dos valores a comparar y decide si están fuera de orden según descendente. Como la clave es un parámetro, la misma función sirve para todas las tablas.
- mostrar(titulo, productos) imprime una tabla con columnas alineadas usando f-strings.
- inventario_manual() pide nombre, precio (pedir_decimal, mínimo 0.01) y existencia (pedir_entero, mínimo 0).
- mostrar_resultados(inventario) imprime el inventario original y luego tres versiones ordenadas, cada una sobre inventario.copy() para que las demás partan del orden original. Al final toma los dos primeros productos de la lista ordenada por existencia: los dos con menos piezas, que muestra como "por reabastecer".

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar inventario de ejemplo
    2. Crear mi propio inventario
    3. Salir
    Elige una opción: 1

    --- INVENTARIO ORIGINAL ---
    Producto          Precio  Existencia
    Laptop          12500.00           5
    Mouse             250.00          40
    Teclado           480.50          22
    Monitor          3200.00           9
    USB 32GB          150.00          75
    Bocinas           650.00          14

    --- PRECIO: de menor a mayor ---
    Producto          Precio  Existencia
    USB 32GB          150.00          75
    Mouse             250.00          40
    Teclado           480.50          22
    Bocinas           650.00          14
    Monitor          3200.00           9
    Laptop          12500.00           5

    --- PRECIO: de mayor a menor ---
    Producto          Precio  Existencia
    Laptop          12500.00           5
    Monitor          3200.00           9
    Bocinas           650.00          14
    Teclado           480.50          22
    Mouse             250.00          40
    USB 32GB          150.00          75

    --- EXISTENCIA: de menor a mayor ---
    Producto          Precio  Existencia
    Laptop          12500.00           5
    Monitor          3200.00           9
    Bocinas           650.00          14
    Teclado           480.50          22
    Mouse             250.00          40
    USB 32GB          150.00          75

    Productos por reabastecer: Laptop, Monitor

    ===== MENÚ =====
    1. Usar inventario de ejemplo
    2. Crear mi propio inventario
    3. Salir
    Elige una opción: 2
    ¿Cuántos productos desea registrar? 2

    Producto 1
    Nombre: Lápiz
    Precio: 5,5
    Existencia (piezas): 12

    Producto 2
    Nombre: Pluma
    Precio: x
    'x' no es un número. Escribe por ejemplo: 8.5
    Precio: 3
    Existencia (piezas): 10

    --- INVENTARIO ORIGINAL ---
    Producto          Precio  Existencia
    Lápiz               5.50          12
    Pluma               3.00          10

    --- PRECIO: de menor a mayor ---
    Producto          Precio  Existencia
    Pluma               3.00          10
    Lápiz               5.50          12

    --- PRECIO: de mayor a menor ---
    Producto          Precio  Existencia
    Lápiz               5.50          12
    Pluma               3.00          10

    --- EXISTENCIA: de menor a mayor ---
    Producto          Precio  Existencia
    Pluma               3.00          10
    Lápiz               5.50          12

    Productos por reabastecer: Pluma, Lápiz

    ===== MENÚ =====
    1. Usar inventario de ejemplo
    2. Crear mi propio inventario
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar inventario de ejemplo
    2. Crear mi propio inventario
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- Con el ejemplo, el orden por existencia coincide con el de precio de mayor a menor: es casualidad de los datos, los productos más caros tienen menos piezas.
- En la captura manual, el precio x se rechazó y se volvió a pedir solo ese dato; 5,5 con coma se aceptó como 5.50.
- Las tres tablas ordenadas parten del mismo inventario original porque se ordenan copias.

5.3 burbuja_ejercicio3.py: nombres, con submenú A-Z / Z-A

Qué hace: ordena una lista de nombres alfabéticamente (A-Z o Z-A) y muestra cada pasada del método.

Funcionamiento interno:

- burbuja(lista, descendente=False) compara los nombres con lower() para que mayúsculas y minúsculas no afecten el orden ("ana" y "Ana" se tratan igual). Después de cada pasada imprime "Pasada n" con la lista, y si no hubo cambios se detiene.
- nombres_manual() lee nombres en un ciclo while True y termina cuando el usuario presiona Enter sin escribir nada. Si hay menos de 2 nombres devuelve None y el menú principal no intenta ordenar.
- mostrar_resultados(nombres) tiene el submenú de orden (sección 3.7). Cada vez que se elige 1 o 2, ordena nombres.copy(), así que la lista original permanece intacta y se puede ordenar en el otro sentido.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar nombres de ejemplo
    2. Escribir mis propios nombres
    3. Salir
    Elige una opción: 1

    Lista original: ['Mariana', 'Carlos', 'Zoe', 'Alberto', 'Luis', 'Fernanda']

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 1

    Original: ['Mariana', 'Carlos', 'Zoe', 'Alberto', 'Luis', 'Fernanda']
    Pasada 1: ['Carlos', 'Mariana', 'Alberto', 'Luis', 'Fernanda', 'Zoe']
    Pasada 2: ['Carlos', 'Alberto', 'Luis', 'Fernanda', 'Mariana', 'Zoe']
    Pasada 3: ['Alberto', 'Carlos', 'Fernanda', 'Luis', 'Mariana', 'Zoe']
    Pasada 4: ['Alberto', 'Carlos', 'Fernanda', 'Luis', 'Mariana', 'Zoe']
    Resultado final: ['Alberto', 'Carlos', 'Fernanda', 'Luis', 'Mariana', 'Zoe']

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 2

    Original: ['Mariana', 'Carlos', 'Zoe', 'Alberto', 'Luis', 'Fernanda']
    Pasada 1: ['Mariana', 'Zoe', 'Carlos', 'Luis', 'Fernanda', 'Alberto']
    Pasada 2: ['Zoe', 'Mariana', 'Luis', 'Fernanda', 'Carlos', 'Alberto']
    Pasada 3: ['Zoe', 'Mariana', 'Luis', 'Fernanda', 'Carlos', 'Alberto']
    Resultado final: ['Zoe', 'Mariana', 'Luis', 'Fernanda', 'Carlos', 'Alberto']

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 9
    Opción no válida.

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 3

    ===== MENÚ =====
    1. Usar nombres de ejemplo
    2. Escribir mis propios nombres
    3. Salir
    Elige una opción: 2
    Escribe nombres (deja vacío y presiona Enter para terminar):
    > Zoe
    > Ana
    > Luis
    > 

    Lista original: ['Zoe', 'Ana', 'Luis']

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 1

    Original: ['Zoe', 'Ana', 'Luis']
    Pasada 1: ['Ana', 'Luis', 'Zoe']
    Pasada 2: ['Ana', 'Luis', 'Zoe']
    Resultado final: ['Ana', 'Luis', 'Zoe']

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De la A a la Z
    2. De la Z a la A
    3. Volver al menú principal
    Elige una opción: 3

    ===== MENÚ =====
    1. Usar nombres de ejemplo
    2. Escribir mis propios nombres
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- Hay dos niveles de menú: el principal (ejemplo / propios / salir) y el de orden (A-Z / Z-A / volver). La opción 3 del submenú regresa al principal, y la 3 del principal termina el programa.
- Las líneas "Pasada n" permiten ver el método trabajando: en cada pasada el nombre más grande (o más chico en Z-A) se va al final.
- En la última pasada del A-Z la lista no cambió, así que hubo_cambio quedó en False y el algoritmo se detuvo antes de recorrer todas las pasadas posibles.
- En el submenú, la lista original no cambia entre un orden y otro (ambas muestran la línea "Original" igual).


6. INSERCION: LOS TRES PROGRAMAS
--------------------------------

6.1 insercion_ejercicio1.py: resultados de una carrera

Qué hace: ordena corredores por tiempo (de menor a mayor), muestra el podio y estadísticas.

Funcionamiento interno:

- insercion(corredores) aplica el método comparando el tiempo de cada corredor con el del elemento actual. Cuenta las comparaciones (cada vez que compara en el while) y los desplazamientos (cada vez que corre un elemento a la derecha). El while usa un break cuando el de la izquierda ya no es mayor.
- corredores_manual() pide nombre y tiempo (pedir_decimal, mínimo 0.01).
- mostrar_resultados(corredores) guarda la cantidad de corredores, ordena y después imprime los resultados con enumerate; arma el podio con zip, que empareja las medallas Oro, Plata y Bronce con los primeros lugares (y se detiene si hay menos de 3 corredores); y calcula el promedio y la diferencia entre el último y el primero.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar carrera de ejemplo
    2. Registrar mis propios corredores
    3. Salir
    Elige una opción: 1

    --- RESULTADOS DE LA CARRERA ---
    1. Luis            11.20 s
    2. Pedro           11.90 s
    3. Sofía           12.10 s
    4. Ana             12.50 s
    5. María           13.80 s
    6. Carlos          14.30 s

    --- PODIO ---
    Oro    : Luis
    Plata  : Pedro
    Bronce : Sofía

    Tiempo promedio: 12.63 s
    Diferencia entre el primero y el último: 3.10 s
    Comparaciones: 9 | Desplazamientos: 5

    ===== MENÚ =====
    1. Usar carrera de ejemplo
    2. Registrar mis propios corredores
    3. Salir
    Elige una opción: 2
    ¿Cuántos corredores participaron? 3
    Nombre del corredor 1: Ana
    Tiempo de Ana (segundos): 12,5
    Nombre del corredor 2: Luis
    Tiempo de Luis (segundos): abc
    'abc' no es un número. Escribe por ejemplo: 8.5
    Tiempo de Luis (segundos): 11.2
    Nombre del corredor 3: María
    Tiempo de María (segundos): 13.8

    --- RESULTADOS DE LA CARRERA ---
    1. Luis            11.20 s
    2. Ana             12.50 s
    3. María           13.80 s

    --- PODIO ---
    Oro    : Luis
    Plata  : Ana
    Bronce : María

    Tiempo promedio: 12.50 s
    Diferencia entre el primero y el último: 2.60 s
    Comparaciones: 2 | Desplazamientos: 1

    ===== MENÚ =====
    1. Usar carrera de ejemplo
    2. Registrar mis propios corredores
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar carrera de ejemplo
    2. Registrar mis propios corredores
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- Los desplazamientos (5 en el ejemplo) son cuántas veces un corredor tuvo que "correrse" a la derecha para dejar espacio a otro que iba mejor.
- Con 3 corredores el podio se llena justo; con menos de 3, zip solo muestra las medallas que alcanzan.

6.2 insercion_ejercicio2.py: catálogo de una biblioteca

Qué hace: ordena un catálogo de libros por año, por número de páginas y por título.

Funcionamiento interno:

- insercion(lista, clave, descendente=False) es el método de inserción con clave configurable: dentro del while compara el valor de esa clave en el elemento de la izquierda contra el del elemento actual, en el sentido que indique descendente. Si no está fuera de orden, hace break.
- mostrar(titulo, libros) imprime la tabla con columnas alineadas.
- catalogo_manual() pide el título (leer), el año y las páginas (pedir_entero).
- mostrar_resultados(catalogo) imprime el original y tres versiones ordenadas (año ascendente, páginas descendente, título de la A a la Z), cada una sobre una copia. Para el libro más corto y el más largo ordena por páginas de menor a mayor y toma la primera y la última posición.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar catálogo de ejemplo
    2. Crear mi propio catálogo
    3. Salir
    Elige una opción: 1

    --- CATÁLOGO ORIGINAL ---
    Título                         Año   Páginas
    Cien años de soledad          1967       471
    El principito                 1943        96
    Don Quijote                   1605       863
    Pedro Páramo                  1955       128
    La sombra del viento          2001       487
    El laberinto de la soledad    1950       191

    --- AÑO: del más antiguo al más reciente ---
    Título                         Año   Páginas
    Don Quijote                   1605       863
    El principito                 1943        96
    El laberinto de la soledad    1950       191
    Pedro Páramo                  1955       128
    Cien años de soledad          1967       471
    La sombra del viento          2001       487

    --- PÁGINAS: de mayor a menor ---
    Título                         Año   Páginas
    Don Quijote                   1605       863
    La sombra del viento          2001       487
    Cien años de soledad          1967       471
    El laberinto de la soledad    1950       191
    Pedro Páramo                  1955       128
    El principito                 1943        96

    --- TÍTULO: de la A a la Z ---
    Título                         Año   Páginas
    Cien años de soledad          1967       471
    Don Quijote                   1605       863
    El laberinto de la soledad    1950       191
    El principito                 1943        96
    La sombra del viento          2001       487
    Pedro Páramo                  1955       128

    Libro más corto: El principito (96 páginas)
    Libro más largo: Don Quijote (863 páginas)

    ===== MENÚ =====
    1. Usar catálogo de ejemplo
    2. Crear mi propio catálogo
    3. Salir
    Elige una opción: 2
    ¿Cuántos libros desea registrar? 2

    Libro 1
    Título: Rayuela
    Año de publicación: 1963
    Número de páginas: 600

    Libro 2
    Título: Dune
    Año de publicación: abc
    'abc' no es un número. Escribe solo dígitos, por ejemplo: 5
    Año de publicación: 1965
    Número de páginas: 412

    --- CATÁLOGO ORIGINAL ---
    Título                         Año   Páginas
    Rayuela                       1963       600
    Dune                          1965       412

    --- AÑO: del más antiguo al más reciente ---
    Título                         Año   Páginas
    Rayuela                       1963       600
    Dune                          1965       412

    --- PÁGINAS: de mayor a menor ---
    Título                         Año   Páginas
    Rayuela                       1963       600
    Dune                          1965       412

    --- TÍTULO: de la A a la Z ---
    Título                         Año   Páginas
    Dune                          1965       412
    Rayuela                       1963       600

    Libro más corto: Dune (412 páginas)
    Libro más largo: Rayuela (600 páginas)

    ===== MENÚ =====
    1. Usar catálogo de ejemplo
    2. Crear mi propio catálogo
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar catálogo de ejemplo
    2. Crear mi propio catálogo
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- La misma función ordena números (año, páginas) y texto (título), porque Python compara ambos con los signos mayor que y menor que.
- Los títulos se ordenan en el orden alfabético que usa Python para texto: distingue mayúsculas de minúsculas (una letra minúscula queda después de todas las mayúsculas).
- Con abc en el año, el mensaje dice "solo dígitos" porque el año es un entero.

6.3 insercion_ejercicio3.py: números paso a paso, con submenú

Qué hace: ordena números mostrando cómo se inserta cada elemento en su lugar.

Funcionamiento interno:

- insercion(lista, descendente=False) aplica el método y, al terminar de colocar cada elemento, imprime "Paso n: se inserta" con el elemento y la lista resultante. Esa línea es la que permite "ver" el algoritmo trabajando.
- numeros_manual() lee números en un ciclo hasta que se presiona Enter sin escribir nada. Cada dato pasa por float(dato.replace(",", ".")), de modo que acepta 2,5; se rechazan texto e inf; y el número se guarda como entero si no tiene decimales (5 en vez de 5.0). Con menos de 2 números devuelve None.
- mostrar_resultados(numeros) tiene el submenú (menor a mayor / mayor a menor / volver) y ordena siempre una copia.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar números de ejemplo
    2. Escribir mis propios números
    3. Salir
    Elige una opción: 1

    Lista original: [38, 12, 27, 5, 44, 19]

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 1

    Original: [38, 12, 27, 5, 44, 19]
    Paso 1: se inserta 12     -> [12, 38, 27, 5, 44, 19]
    Paso 2: se inserta 27     -> [12, 27, 38, 5, 44, 19]
    Paso 3: se inserta 5      -> [5, 12, 27, 38, 44, 19]
    Paso 4: se inserta 44     -> [5, 12, 27, 38, 44, 19]
    Paso 5: se inserta 19     -> [5, 12, 19, 27, 38, 44]
    Resultado final: [5, 12, 19, 27, 38, 44]

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 2

    Original: [38, 12, 27, 5, 44, 19]
    Paso 1: se inserta 12     -> [38, 12, 27, 5, 44, 19]
    Paso 2: se inserta 27     -> [38, 27, 12, 5, 44, 19]
    Paso 3: se inserta 5      -> [38, 27, 12, 5, 44, 19]
    Paso 4: se inserta 44     -> [44, 38, 27, 12, 5, 19]
    Paso 5: se inserta 19     -> [44, 38, 27, 19, 12, 5]
    Resultado final: [44, 38, 27, 19, 12, 5]

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 9
    Opción no válida.

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 3

    ===== MENÚ =====
    1. Usar números de ejemplo
    2. Escribir mis propios números
    3. Salir
    Elige una opción: 2
    Escribe números (deja vacío y presiona Enter para terminar):
    > 5
    > abc
    'abc' no es un número. Escribe por ejemplo: 5 o 2.5
    > 2,5
    > 9
    > 

    Lista original: [5, 2.5, 9]

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 2

    Original: [5, 2.5, 9]
    Paso 1: se inserta 2.5    -> [5, 2.5, 9]
    Paso 2: se inserta 9      -> [9, 5, 2.5]
    Resultado final: [9, 5, 2.5]

    --- ¿CÓMO DESEA ORDENAR? ---
    1. De menor a mayor
    2. De mayor a menor
    3. Volver al menú principal
    Elige una opción: 3

    ===== MENÚ =====
    1. Usar números de ejemplo
    2. Escribir mis propios números
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- En "Paso 3: se inserta 5" de menor a mayor, el 5 viaja hasta el inicio de la lista: el método corrió 38, 27 y 12 a la derecha para hacerle espacio.
- En el "Paso 4: se inserta 44" la lista no cambia: 44 ya era mayor que todos los de su izquierda.
- El número escrito como 2,5 se guardó como 2.5 y el 5 se guardó como entero.


7. SELECCION: LOS TRES PROGRAMAS
--------------------------------

7.1 seleccion_ejercicio1.py: puntajes de un videojuego

Qué hace: ordena jugadores de mayor a menor puntaje y muestra al campeón y estadísticas.

Funcionamiento interno:

- seleccion(jugadores) busca en cada vuelta el jugador con más puntos de los que faltan y lo intercambia con la posición i. Solo intercambia si el mayor no está ya en esa posición, así evita movimientos innecesarios. Cuenta las comparaciones y los intercambios.
- jugadores_manual() pide nombre y puntos (pedir_entero, mínimo 0).
- mostrar_resultados(jugadores) imprime la tabla con enumerate, el campeón (la primera posición de la lista ordenada), el total con sum, el promedio dividido entre la cantidad de jugadores y los contadores.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar jugadores de ejemplo
    2. Registrar mis propios jugadores
    3. Salir
    Elige una opción: 1

    --- TABLA DE PUNTAJES ---
    1. Dragón            3105 pts
    2. Luna              2780 pts
    3. Blaze             2210 pts
    4. Nova              1890 pts
    5. Shadow            1520 pts
    6. Pixel              940 pts

    Campeón: Dragón con 3105 puntos
    Puntos totales : 12445
    Promedio       : 2074.2
    Comparaciones: 15 | Intercambios: 3

    ===== MENÚ =====
    1. Usar jugadores de ejemplo
    2. Registrar mis propios jugadores
    3. Salir
    Elige una opción: 2
    ¿Cuántos jugadores desea registrar? 3
    Nombre del jugador 1: Ana
    Puntos de Ana: 1500
    Nombre del jugador 2: Luis
    Puntos de Luis: -4
    Debe ser mayor o igual a 0.
    Puntos de Luis: 2200
    Nombre del jugador 3: Sofía
    Puntos de Sofía: 3000

    --- TABLA DE PUNTAJES ---
    1. Sofía             3000 pts
    2. Luis              2200 pts
    3. Ana               1500 pts

    Campeón: Sofía con 3000 puntos
    Puntos totales : 6700
    Promedio       : 2233.3
    Comparaciones: 3 | Intercambios: 1

    ===== MENÚ =====
    1. Usar jugadores de ejemplo
    2. Registrar mis propios jugadores
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar jugadores de ejemplo
    2. Registrar mis propios jugadores
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- Las comparaciones siempre son las mismas para una lista del mismo tamaño (15 para 6 jugadores, 3 para 3 jugadores): es una característica de selección.
- Los intercambios son pocos (3 en el ejemplo con 6 jugadores), mucho menos que las comparaciones.
- Los puntos negativos (-4) se rechazan con el mensaje del mínimo permitido.

7.2 seleccion_ejercicio2.py: nómina de empleados

Qué hace: ordena empleados por sueldo, por antigüedad y por nombre, y calcula la nómina total.

Funcionamiento interno:

- valor_de(elemento, clave) devuelve el valor de un campo, pasándolo a minúsculas si es texto. Así, al ordenar por nombre, "ana" y "Ana" se comparan igual.
- seleccion(lista, clave, descendente=False) busca en cada vuelta el elemento "mejor" según la clave: con descendente busca el mayor y sin él, el menor. Como la clave es un parámetro, ordena por sueldo, por antigüedad o por nombre con la misma función.
- mostrar(titulo, empleados) imprime la tabla. El sueldo se muestra con separador de miles y la antigüedad dice "año" si es 1 y "años" en los demás casos.
- mostrar_resultados(empleados) imprime la nómina original y tres versiones ordenadas (por sueldo, por antigüedad y por nombre de la A a la Z, sobre copias), la nómina total (suma de sueldos) y quién tiene el sueldo más alto.

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar nómina de ejemplo
    2. Crear mi propia nómina
    3. Salir
    Elige una opción: 1

    --- NÓMINA ORIGINAL ---
    Empleado            Sueldo   Antigüedad
    Roberto          18,500.00       6 años
    Daniela          24,000.00       9 años
    Javier           12,800.00       2 años
    Patricia         31,500.00      12 años
    Miguel           15,200.00       4 años
    Alejandra        21,000.00       7 años

    --- SUELDO: de mayor a menor ---
    Empleado            Sueldo   Antigüedad
    Patricia         31,500.00      12 años
    Daniela          24,000.00       9 años
    Alejandra        21,000.00       7 años
    Roberto          18,500.00       6 años
    Miguel           15,200.00       4 años
    Javier           12,800.00       2 años

    --- ANTIGÜEDAD: de mayor a menor ---
    Empleado            Sueldo   Antigüedad
    Patricia         31,500.00      12 años
    Daniela          24,000.00       9 años
    Alejandra        21,000.00       7 años
    Roberto          18,500.00       6 años
    Miguel           15,200.00       4 años
    Javier           12,800.00       2 años

    --- NOMBRE: de la A a la Z ---
    Empleado            Sueldo   Antigüedad
    Alejandra        21,000.00       7 años
    Daniela          24,000.00       9 años
    Javier           12,800.00       2 años
    Miguel           15,200.00       4 años
    Patricia         31,500.00      12 años
    Roberto          18,500.00       6 años

    Nómina total: 123,000.00
    Sueldo más alto: Patricia (31,500.00)

    ===== MENÚ =====
    1. Usar nómina de ejemplo
    2. Crear mi propia nómina
    3. Salir
    Elige una opción: 2
    ¿Cuántos empleados desea registrar? 2

    Empleado 1
    Nombre: Zed
    Sueldo: 1000,50
    Años de antigüedad: 3

    Empleado 2
    Nombre: Ana
    Sueldo: 2000
    Años de antigüedad: 1

    --- NÓMINA ORIGINAL ---
    Empleado            Sueldo   Antigüedad
    Zed               1,000.50       3 años
    Ana               2,000.00        1 año

    --- SUELDO: de mayor a menor ---
    Empleado            Sueldo   Antigüedad
    Ana               2,000.00        1 año
    Zed               1,000.50       3 años

    --- ANTIGÜEDAD: de mayor a menor ---
    Empleado            Sueldo   Antigüedad
    Zed               1,000.50       3 años
    Ana               2,000.00        1 año

    --- NOMBRE: de la A a la Z ---
    Empleado            Sueldo   Antigüedad
    Ana               2,000.00        1 año
    Zed               1,000.50       3 años

    Nómina total: 3,000.50
    Sueldo más alto: Ana (2,000.00)

    ===== MENÚ =====
    1. Usar nómina de ejemplo
    2. Crear mi propia nómina
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar nómina de ejemplo
    2. Crear mi propia nómina
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- En el ejemplo, el orden por sueldo y por antigüedad salen iguales: es casualidad de los datos (los empleados con más antigüedad ganan más). En la captura manual sí difieren: Zed tiene más antigüedad pero Ana tiene más sueldo.
- El mismo código ordena números y texto: la clave cambia, el algoritmo no.
- 1000,50 (con coma) se interpretó como 1000.50.

7.3 seleccion_ejercicio3.py: temperaturas de ciudades, paso a paso

Qué hace: ordena ciudades de la más fría a la más cálida mostrando qué elemento elige el método en cada paso.

Funcionamiento interno:

- seleccion(ciudades) busca en cada vuelta la ciudad con la temperatura más baja de las que faltan. Antes de intercambiar, imprime "Paso n: la menor restante es" y el nombre de la ciudad, y después imprime cómo quedó la lista.
- describir(ciudades) convierte la lista en un texto de una línea, por ejemplo "Oslo -5.5°, Mérida 35.5°", para poder imprimirla.
- ciudades_manual() pide nombre y temperatura con pedir_decimal limitada de -80 a 60, así que acepta temperaturas negativas pero rechaza valores imposibles.
- mostrar_resultados(ciudades) imprime la lista original, llama a seleccion, imprime la tabla final y calcula la diferencia entre la más cálida (última posición) y la más fría (primera posición).

Ejecución en la terminal:

    ===== MENÚ =====
    1. Usar ciudades de ejemplo
    2. Registrar mis propias ciudades
    3. Salir
    Elige una opción: 1

    Original: Mérida 35.5°, Monterrey 31.0°, CDMX 22.0°, Guadalajara 27.0°, Tijuana 24.0°, Chihuahua 18.0°

    Paso 1: la menor restante es Chihuahua (18.0°C)
            -> Chihuahua 18.0°, Monterrey 31.0°, CDMX 22.0°, Guadalajara 27.0°, Tijuana 24.0°, Mérida 35.5°
    Paso 2: la menor restante es CDMX (22.0°C)
            -> Chihuahua 18.0°, CDMX 22.0°, Monterrey 31.0°, Guadalajara 27.0°, Tijuana 24.0°, Mérida 35.5°
    Paso 3: la menor restante es Tijuana (24.0°C)
            -> Chihuahua 18.0°, CDMX 22.0°, Tijuana 24.0°, Guadalajara 27.0°, Monterrey 31.0°, Mérida 35.5°
    Paso 4: la menor restante es Guadalajara (27.0°C)
            -> Chihuahua 18.0°, CDMX 22.0°, Tijuana 24.0°, Guadalajara 27.0°, Monterrey 31.0°, Mérida 35.5°
    Paso 5: la menor restante es Monterrey (31.0°C)
            -> Chihuahua 18.0°, CDMX 22.0°, Tijuana 24.0°, Guadalajara 27.0°, Monterrey 31.0°, Mérida 35.5°

    --- DE LA MÁS FRÍA A LA MÁS CÁLIDA ---
    1. Chihuahua         18.0 °C
    2. CDMX              22.0 °C
    3. Tijuana           24.0 °C
    4. Guadalajara       27.0 °C
    5. Monterrey         31.0 °C
    6. Mérida            35.5 °C

    Más fría : Chihuahua (18.0°C)
    Más cálida: Mérida (35.5°C)
    Diferencia entre ambas: 17.5°C

    ===== MENÚ =====
    1. Usar ciudades de ejemplo
    2. Registrar mis propias ciudades
    3. Salir
    Elige una opción: 2
    ¿Cuántas ciudades desea registrar? 3
    Nombre de la ciudad 1: Mérida
    Temperatura de Mérida (°C): 35,5
    Nombre de la ciudad 2: Oslo
    Temperatura de Oslo (°C): -5,5
    Nombre de la ciudad 3: Lima
    Temperatura de Lima (°C): 200
    El valor debe estar entre -80 y 60.
    Temperatura de Lima (°C): 20

    Original: Mérida 35.5°, Oslo -5.5°, Lima 20.0°

    Paso 1: la menor restante es Oslo (-5.5°C)
            -> Oslo -5.5°, Mérida 35.5°, Lima 20.0°
    Paso 2: la menor restante es Lima (20.0°C)
            -> Oslo -5.5°, Lima 20.0°, Mérida 35.5°

    --- DE LA MÁS FRÍA A LA MÁS CÁLIDA ---
    1. Oslo              -5.5 °C
    2. Lima              20.0 °C
    3. Mérida            35.5 °C

    Más fría : Oslo (-5.5°C)
    Más cálida: Mérida (35.5°C)
    Diferencia entre ambas: 41.0°C

    ===== MENÚ =====
    1. Usar ciudades de ejemplo
    2. Registrar mis propias ciudades
    3. Salir
    Elige una opción: 9
    Opción no válida.

    ===== MENÚ =====
    1. Usar ciudades de ejemplo
    2. Registrar mis propias ciudades
    3. Salir
    Elige una opción: 3

    Fin del programa.

Qué se observa:

- En cada paso, la ciudad elegida pasa a ocupar la siguiente posición ordenada. Por ejemplo, en el paso 1 Chihuahua (la más fría) se intercambia con Mérida (que estaba en la posición 0).
- En los pasos 4 y 5 la lista no cambia: la ciudad elegida ya estaba en su lugar, así que no hubo cambio.
- Con n ciudades hay n-1 pasos (5 pasos para 6 ciudades, 2 pasos para 3 ciudades): la última ciudad queda en su lugar automáticamente.
- 200 se rechazó por estar fuera del rango, y -5,5 (negativo, con coma) se aceptó.


8. HERRAMIENTAS DE PYTHON UTILIZADAS
------------------------------------

- Listas de diccionarios: guardar varios datos por elemento y ordenar por cualquier campo.
- lista.copy(): ordenar sin perder la lista original.
- a, b = b, a: intercambiar dos valores sin variable auxiliar.
- f-strings con formato: alinear columnas, fijar decimales y separar miles.
- enumerate(lista, start=1): numerar posiciones al imprimir rankings.
- zip(a, b): emparejar dos listas (medallas con corredores).
- sum() y len(): totales, promedios y conteos.
- try / except ValueError: atrapar texto donde debía ir un número.
- while True con break o return: menús y validaciones que se repiten hasta que haya una respuesta válida.
- isinstance(valor, str): distinguir texto de números al comparar (nómina).
- unicodedata y math.isfinite: limpiar la entrada del teclado y rechazar valores como inf.
- raise SystemExit: terminar el programa limpiamente si no llegan más datos.


9. RESUMEN DE LO QUE HACE CADA MENU AL EJECUTAR
-----------------------------------------------

- Escribes 1: muestra el resultado con los datos de ejemplo y regresa al menú.
- Escribes 2: te pide tus propios datos (validándolos), muestra el resultado y regresa al menú.
- Escribes 3: termina el programa e imprime "Fin del programa."
- Escribes cualquier otra cosa: imprime "Opción no válida." y muestra el menú otra vez.
- En un submenú, 1 o 2: ordena la misma lista en el sentido elegido y vuelve a mostrar el submenú.
- En un submenú, 3: regresa al menú principal.


10. FUNCIONAMIENTO INTERNO Y RECORRIDO COMPLETO AL EJECUTAR
-----------------------------------------------------------

En esta sección se explica el recorrido que sigue el programa desde que se escribe el comando para ejecutarlo hasta que termina. También se describe cómo se conectan las funciones entre sí y qué sucede con los datos durante el proceso.

10.1 ¿Qué sucede desde que se ejecuta el archivo?

Por ejemplo, al escribir en la terminal:

    python burbuja_ejercicio1.py

ocurre lo siguiente:

1. La terminal inicia Python y le indica qué archivo debe ejecutar.
2. Python lee el archivo de arriba hacia abajo. Primero encuentra los import, que cargan las herramientas necesarias, como unicodedata y math.
3. Después encuentra las funciones def. Python registra sus nombres y el código que contienen. Todavía no ordena datos ni muestra los menús, porque las instrucciones de cada función se ejecutan hasta que esa función es llamada.
4. Al llegar a main(), comienza la ejecución principal. La función muestra el menú y espera que el usuario escriba una opción.
5. La opción seleccionada determina qué función se ejecuta: usar los datos de ejemplo, capturar datos propios o terminar.
6. Cuando ya existe una lista de datos válida, se llama a mostrar_resultados() o a la función equivalente del ejercicio. Esta función prepara la información, llama al algoritmo de ordenamiento y presenta los resultados.
7. Cuando termina de mostrar los resultados, el control vuelve al ciclo del menú. El programa no se cierra después de ordenar; espera una nueva elección.
8. Cuando el usuario selecciona Salir, break termina el ciclo del menú. La función main() finaliza y se muestra el mensaje final del archivo.

10.2 Cómo se conectan las funciones durante una ejecución

El recorrido general de los programas es el siguiente:

    Inicio del archivo
          |
          v
    Carga de módulos y definición de funciones
          |
          v
    main(): muestra el menú
          |
          v
    El usuario selecciona una opción
          |
          +-------------------------------+
          |               |               |
          v               v               v
       Ejemplo       Datos propios       Salir
          |               |               |
          v               v               v
    Función de       Función manual     Termina el
    datos ejemplo    y validaciones     ciclo del menú
          |               |
          +-------+-------+
                  |
                  v
          mostrar_resultados()
                  |
                  v
          Algoritmo de ordenamiento
                  |
                  v
          Resultados y estadísticas
                  |
                  v
          Regresa al menú principal

La función de captura no realiza el ordenamiento. Su responsabilidad es reunir los datos y comprobar que sean válidos. La función del algoritmo tampoco se encarga de mostrar todo el menú: recibe la lista, la ordena y, cuando corresponde, devuelve contadores o imprime los pasos. Finalmente, mostrar_resultados() organiza la salida que verá el usuario.

10.3 Qué ocurre cuando el usuario captura sus propios datos

Cuando se selecciona la opción para registrar información, el programa solicita los datos necesarios para el ejercicio. Dependiendo del archivo, puede pedir nombres, calificaciones, precios, existencias, tiempos, títulos, páginas, puntos, sueldos, antigüedad, ciudades o temperaturas.

Cada dato se procesa antes de guardarse:

- Los textos se reciben mediante leer(), que limpia espacios sobrantes y caracteres no imprimibles.
- Los números pasan por pedir_entero() o pedir_decimal(), según corresponda.
- Si el usuario escribe letras donde se espera un número, la conversión falla y el programa muestra un mensaje para volver a capturar ese mismo dato.
- Si el número está fuera del rango permitido, también se rechaza y se vuelve a solicitar.
- Cuando el dato cumple las condiciones, se incorpora a la lista que utilizará el programa.

En los ejercicios que reciben números o nombres hasta presionar Enter con la entrada vacía, ese Enter indica que terminó la captura. Si no se reúnen al menos dos elementos, los ejercicios que lo requieren no intentan ordenar una lista insuficiente y regresan al menú.

10.4 Qué hace internamente cada algoritmo durante el ordenamiento

Burbuja:

- Recibe la lista que debe ordenar y obtiene su cantidad de elementos con len().
- El ciclo for externo controla las pasadas y el ciclo interno recorre los pares vecinos.
- En cada comparación revisa si los dos elementos están en el orden solicitado.
- Cuando están al revés, intercambia sus posiciones y registra el cambio si el ejercicio lleva contador.
- En las versiones que utilizan hubo_cambio, si una pasada termina sin intercambios, el algoritmo sabe que la lista ya está ordenada y puede detenerse.
- En los ejercicios que muestran el procedimiento, se imprime el estado de la lista después de cada pasada.

Inserción:

- Comienza desde el segundo elemento, porque una lista con un solo elemento ya está ordenada.
- Guarda el elemento actual en una variable para no perderlo mientras mueve otros valores.
- Compara ese elemento con los que están a su izquierda.
- Mientras encuentra elementos que deben ir después, los desplaza una posición a la derecha.
- Cuando encuentra el espacio correcto, coloca ahí el elemento guardado.
- En los ejercicios que muestran pasos, imprime cómo quedó la lista después de insertar cada elemento.

Selección:

- Recorre la lista desde la primera posición hasta la penúltima.
- En cada vuelta guarda en una variable la posición del mejor elemento encontrado hasta ese momento (por ejemplo, el menor o el mayor, según el ejercicio).
- El ciclo interno revisa el resto de los elementos y actualiza esa posición cuando encuentra uno que debe ocupar el lugar actual.
- Al terminar la búsqueda, intercambia el elemento elegido con el que estaba en la posición que se está ordenando, si es necesario.
- En los ejercicios que muestran pasos, informa qué elemento seleccionó y cómo quedó la lista después del intercambio.

10.5 Recorrido de ejecución de los nueve ejercicios

Los nueve archivos comparten la idea de recibir datos, ordenarlos y presentar resultados, pero cada uno utiliza el método en una situación diferente.

Burbuja:

- burbuja_ejercicio1.py: al iniciar muestra el menú del ranking. Si se elige el ejemplo, carga los alumnos; si se registran alumnos propios, valida nombres y calificaciones. Después ordena por calificación de mayor a menor, muestra las posiciones, calcula el promedio y presenta la calificación más alta y la más baja. También informa las comparaciones y los intercambios realizados.
- burbuja_ejercicio2.py: solicita o carga los productos del inventario. Después prepara copias de la lista para ordenarlas por precio ascendente, precio descendente y existencia ascendente. Muestra las tres tablas y señala los productos con menor existencia. La lista original se conserva para que cada ordenamiento comience con los mismos datos.
- burbuja_ejercicio3.py: carga o captura los nombres y muestra el submenú de orden alfabético. Al elegir A-Z o Z-A, ordena una copia y muestra las pasadas del algoritmo. El submenú permanece disponible para probar el otro sentido con los mismos nombres. Al elegir volver, regresa al menú principal.

Inserción:

- insercion_ejercicio1.py: carga o captura corredores y sus tiempos. Ordena los tiempos de menor a mayor, porque un tiempo menor representa un mejor resultado. Después presenta la clasificación, asigna las medallas a los primeros lugares y calcula el promedio y la diferencia entre el primer y el último tiempo. También muestra comparaciones y desplazamientos.
- insercion_ejercicio2.py: carga o captura libros. Utiliza la misma función de inserción con distintas claves para ordenar por año, por páginas y por título. Presenta cada tabla y determina cuál libro tiene menos páginas y cuál tiene más. Las copias permiten conservar el catálogo original.
- insercion_ejercicio3.py: carga los números de ejemplo o permite escribir números hasta presionar Enter. Después muestra el submenú para elegir ascendente o descendente. Al ordenar, imprime cada paso de inserción y el resultado final. La lista original se mantiene para poder repetir el proceso en el otro sentido.

Selección:

- seleccion_ejercicio1.py: carga o captura jugadores y puntos. Busca el jugador con mayor puntuación para colocarlo en la siguiente posición. Al finalizar muestra la tabla, identifica al campeón y calcula los puntos totales y el promedio. También presenta las comparaciones y los intercambios.
- seleccion_ejercicio2.py: carga o captura los empleados. La función de selección recibe una clave para saber si debe comparar sueldo, antigüedad o nombre. Por eso puede utilizarse el mismo algoritmo para generar tres ordenamientos diferentes. Al final muestra las tablas, suma la nómina y señala el sueldo más alto.
- seleccion_ejercicio3.py: carga o captura ciudades y temperaturas. En cada vuelta busca la ciudad con la temperatura menor entre las que todavía faltan por ordenar. Muestra el elemento seleccionado y el estado de la lista. Finalmente presenta las ciudades de la más fría a la más cálida y calcula la diferencia de temperatura.

10.6 Qué ve el usuario después de que termina el ordenamiento

El resultado depende del ejercicio, pero normalmente se presenta en este orden:

1. Una tabla o lista con los elementos ya ordenados.
2. Información adicional del ejercicio, como promedio, total, podio, campeón, productos por reabastecer, libro más corto, libro más largo o diferencia de temperaturas.
3. Los contadores del algoritmo, cuando el ejercicio los incluye: comparaciones, intercambios o desplazamientos.
4. El menú principal otra vez, para que el usuario pueda ejecutar otra opción sin iniciar nuevamente el archivo.

En los ejercicios que muestran el procedimiento, antes del resultado final también aparecen las pasadas o pasos intermedios. Esto permite observar cómo cambia la lista mientras trabaja el algoritmo, en lugar de ver únicamente la respuesta terminada.

10.7 Cómo termina el programa

El programa permanece activo mientras el ciclo del menú siga funcionando. Si se escribe una opción incorrecta, muestra "Opción no válida." y vuelve a solicitar una opción. Si se utiliza un submenú, la opción para volver termina únicamente ese submenú, no todo el archivo.

Cuando se selecciona la opción Salir del menú principal, se ejecuta break. Esto rompe el ciclo while, permite que main() termine y el programa alcanza la instrucción final que muestra "Fin del programa.". En ese momento concluye la ejecución.
