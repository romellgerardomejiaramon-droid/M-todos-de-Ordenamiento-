
import unicodedata
import math


def leer(mensaje=""):
    """Lee texto del teclado y limpia espacios y caracteres invisibles."""
    try:
        texto = input(mensaje)
    except EOFError:
        print("\nNo se recibieron más datos.")
        print("\nFin del programa.")
        raise SystemExit
    texto = unicodedata.normalize("NFKC", texto)
    return "".join(c for c in texto if c.isprintable()).strip()


def pedir_entero(mensaje, minimo=1):
    while True:
        texto = leer(mensaje)
        try:
            numero = float(texto.replace(",", "."))
        except ValueError:
            print(f"'{texto}' no es un número. Escribe solo dígitos, por ejemplo: 5")
            continue
        if not math.isfinite(numero) or not numero.is_integer():
            print("Debe ser un número entero, sin decimales.")
        elif numero < minimo:
            print(f"Debe ser mayor o igual a {minimo}.")
        else:
            return int(numero)


def pedir_decimal(mensaje, minimo=0.0, maximo=None):
    while True:
        texto = leer(mensaje)
        try:
            numero = float(texto.replace(",", "."))
        except ValueError:
            print(f"'{texto}' no es un número. Escribe por ejemplo: 8.5")
            continue
        if not math.isfinite(numero):
            print("Escribe un número válido.")
        elif numero < minimo or (maximo is not None and numero > maximo):
            if maximo is not None:
                print(f"El valor debe estar entre {minimo} y {maximo}.")
            else:
                print(f"El valor debe ser mayor o igual a {minimo}.")
        else:
            return numero


def insercion(lista, clave, descendente=False):
    """Ordena una lista de diccionarios según la clave indicada."""
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0:
            if descendente:
                fuera_de_orden = lista[j][clave] < actual[clave]
            else:
                fuera_de_orden = lista[j][clave] > actual[clave]
            if not fuera_de_orden:
                break
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
    return lista


def mostrar(titulo, libros):
    print(f"\n--- {titulo} ---")
    print(f"{'Título':<28}{'Año':>6}{'Páginas':>10}")
    for l in libros:
        print(f"{l['titulo']:<28}{l['anio']:>6}{l['paginas']:>10}")


def catalogo_ejemplo():
    return [
        {"titulo": "Cien años de soledad",       "anio": 1967, "paginas": 471},
        {"titulo": "El principito",              "anio": 1943, "paginas": 96},
        {"titulo": "Don Quijote",                "anio": 1605, "paginas": 863},
        {"titulo": "Pedro Páramo",               "anio": 1955, "paginas": 128},
        {"titulo": "La sombra del viento",       "anio": 2001, "paginas": 487},
        {"titulo": "El laberinto de la soledad", "anio": 1950, "paginas": 191},
    ]


def catalogo_manual():
    cantidad = pedir_entero("¿Cuántos libros desea registrar? ")
    libros = []
    for i in range(cantidad):
        print(f"\nLibro {i + 1}")
        titulo = leer("Título: ").strip()
        anio = pedir_entero("Año de publicación: ")
        paginas = pedir_entero("Número de páginas: ")
        libros.append({"titulo": titulo, "anio": anio, "paginas": paginas})
    return libros


def mostrar_resultados(catalogo):
    mostrar("CATÁLOGO ORIGINAL", catalogo)
    mostrar("AÑO: del más antiguo al más reciente", insercion(catalogo.copy(), "anio"))
    mostrar("PÁGINAS: de mayor a menor", insercion(catalogo.copy(), "paginas", True))
    mostrar("TÍTULO: de la A a la Z", insercion(catalogo.copy(), "titulo"))

    por_paginas = insercion(catalogo.copy(), "paginas")
    print(f"\nLibro más corto: {por_paginas[0]['titulo']} ({por_paginas[0]['paginas']} páginas)")
    print(f"Libro más largo: {por_paginas[-1]['titulo']} ({por_paginas[-1]['paginas']} páginas)")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar catálogo de ejemplo")
        print("2. Crear mi propio catálogo")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(catalogo_ejemplo())
        elif opcion == "2":
            datos = catalogo_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
