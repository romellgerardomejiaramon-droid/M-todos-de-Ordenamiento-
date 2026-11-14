
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


def insercion(lista, descendente=False):
    """Ordena la lista y muestra el paso a paso de cada inserción."""
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i - 1
        while j >= 0:
            if descendente:
                fuera_de_orden = lista[j] < actual
            else:
                fuera_de_orden = lista[j] > actual
            if not fuera_de_orden:
                break
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual
        print(f"Paso {i}: se inserta {actual:<6} -> {lista}")
    return lista


def numeros_ejemplo():
    return [38, 12, 27, 5, 44, 19]


def numeros_manual():
    numeros = []
    print("Escribe números (deja vacío y presiona Enter para terminar):")
    while True:
        dato = leer("> ").strip()
        if dato == "":
            break
        try:
            valor = float(dato.replace(",", "."))
            if not math.isfinite(valor):
                raise ValueError
            numeros.append(int(valor) if valor.is_integer() else valor)
        except ValueError:
            print(f"'{dato}' no es un número. Escribe por ejemplo: 5 o 2.5")

    if len(numeros) < 2:
        print("Se necesitan al menos 2 números.")
        return None
    return numeros


def mostrar_resultados(numeros):
    print(f"\nLista original: {numeros}")
    while True:
        print("\n--- ¿CÓMO DESEA ORDENAR? ---")
        print("1. De menor a mayor")
        print("2. De mayor a menor")
        print("3. Volver al menú principal")
        opcion = leer("Elige una opción: ").strip()

        if opcion in ("1", "2"):
            copia = numeros.copy()
            print(f"\nOriginal: {copia}")
            resultado = insercion(copia, descendente=(opcion == "2"))
            print(f"Resultado final: {resultado}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar números de ejemplo")
        print("2. Escribir mis propios números")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(numeros_ejemplo())
        elif opcion == "2":
            datos = numeros_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
