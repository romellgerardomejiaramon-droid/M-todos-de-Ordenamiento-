
import unicodedata


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


def burbuja(lista, descendente=False):
    """Ordena nombres alfabéticamente y muestra cada pasada."""
    n = len(lista)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            a, b = lista[j].lower(), lista[j + 1].lower()
            fuera_de_orden = a < b if descendente else a > b
            if fuera_de_orden:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        print(f"Pasada {i + 1}: {lista}")
        if not hubo_cambio:
            break
    return lista


def nombres_ejemplo():
    return ["Mariana", "Carlos", "Zoe", "Alberto", "Luis", "Fernanda"]


def nombres_manual():
    nombres = []
    print("Escribe nombres (deja vacío y presiona Enter para terminar):")
    while True:
        nombre = leer("> ").strip()
        if nombre == "":
            break
        nombres.append(nombre)

    if len(nombres) < 2:
        print("Se necesitan al menos 2 nombres.")
        return None
    return nombres


def mostrar_resultados(nombres):
    print(f"\nLista original: {nombres}")
    while True:
        print("\n--- ¿CÓMO DESEA ORDENAR? ---")
        print("1. De la A a la Z")
        print("2. De la Z a la A")
        print("3. Volver al menú principal")
        opcion = leer("Elige una opción: ").strip()

        if opcion in ("1", "2"):
            copia = nombres.copy()
            print(f"\nOriginal: {copia}")
            resultado = burbuja(copia, descendente=(opcion == "2"))
            print(f"Resultado final: {resultado}")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar nombres de ejemplo")
        print("2. Escribir mis propios nombres")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(nombres_ejemplo())
        elif opcion == "2":
            datos = nombres_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
