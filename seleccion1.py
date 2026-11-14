
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


def seleccion(jugadores):
    """Ordena de mayor a menor puntaje. Devuelve comparaciones e intercambios."""
    n = len(jugadores)
    comparaciones = 0
    intercambios = 0
    for i in range(n - 1):
        mayor = i
        for j in range(i + 1, n):
            comparaciones += 1
            if jugadores[j]["puntos"] > jugadores[mayor]["puntos"]:
                mayor = j
        if mayor != i:
            jugadores[i], jugadores[mayor] = jugadores[mayor], jugadores[i]
            intercambios += 1
    return comparaciones, intercambios


def jugadores_ejemplo():
    return [
        {"nombre": "Shadow",  "puntos": 1520},
        {"nombre": "Luna",    "puntos": 2780},
        {"nombre": "Pixel",   "puntos": 940},
        {"nombre": "Dragón",  "puntos": 3105},
        {"nombre": "Nova",    "puntos": 1890},
        {"nombre": "Blaze",   "puntos": 2210},
    ]


def jugadores_manual():
    cantidad = pedir_entero("¿Cuántos jugadores desea registrar? ")
    jugadores = []
    for i in range(cantidad):
        nombre = leer(f"Nombre del jugador {i + 1}: ").strip()
        puntos = pedir_entero(f"Puntos de {nombre}: ", 0)
        jugadores.append({"nombre": nombre, "puntos": puntos})
    return jugadores


def mostrar_resultados(jugadores):
    cantidad = len(jugadores)
    comparaciones, intercambios = seleccion(jugadores)

    print("\n--- TABLA DE PUNTAJES ---")
    for posicion, j in enumerate(jugadores, start=1):
        print(f"{posicion}. {j['nombre']:<15} {j['puntos']:>6} pts")

    total = sum(j["puntos"] for j in jugadores)
    print(f"\nCampeón: {jugadores[0]['nombre']} con {jugadores[0]['puntos']} puntos")
    print(f"Puntos totales : {total}")
    print(f"Promedio       : {total / cantidad:.1f}")
    print(f"Comparaciones: {comparaciones} | Intercambios: {intercambios}")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar jugadores de ejemplo")
        print("2. Registrar mis propios jugadores")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(jugadores_ejemplo())
        elif opcion == "2":
            datos = jugadores_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
