# Selección - Ejercicio 3: temperaturas de ciudades, paso a paso

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


def seleccion(ciudades):
    """Ordena de la más fría a la más cálida y muestra cada paso."""
    n = len(ciudades)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if ciudades[j]["temp"] < ciudades[minimo]["temp"]:
                minimo = j
        c = ciudades[minimo]
        print(f"Paso {i + 1}: la menor restante es {c['ciudad']} ({c['temp']}°C)")
        if minimo != i:
            ciudades[i], ciudades[minimo] = ciudades[minimo], ciudades[i]
        print("        ->", describir(ciudades))
    return ciudades


def describir(ciudades):
    return ", ".join(f"{c['ciudad']} {c['temp']}°" for c in ciudades)


def ciudades_ejemplo():
    return [
        {"ciudad": "Mérida",      "temp": 35.5},
        {"ciudad": "Monterrey",   "temp": 31.0},
        {"ciudad": "CDMX",        "temp": 22.0},
        {"ciudad": "Guadalajara", "temp": 27.0},
        {"ciudad": "Tijuana",     "temp": 24.0},
        {"ciudad": "Chihuahua",   "temp": 18.0},
    ]


def ciudades_manual():
    cantidad = pedir_entero("¿Cuántas ciudades desea registrar? ")
    ciudades = []
    for i in range(cantidad):
        ciudad = leer(f"Nombre de la ciudad {i + 1}: ").strip()
        temp = pedir_decimal(f"Temperatura de {ciudad} (°C): ", -80, 60)
        ciudades.append({"ciudad": ciudad, "temp": temp})
    return ciudades


def mostrar_resultados(ciudades):
    print(f"\nOriginal: {describir(ciudades)}\n")
    ordenadas = seleccion(ciudades)

    print("\n--- DE LA MÁS FRÍA A LA MÁS CÁLIDA ---")
    for posicion, c in enumerate(ordenadas, start=1):
        print(f"{posicion}. {c['ciudad']:<15} {c['temp']:>6.1f} °C")

    rango = ordenadas[-1]["temp"] - ordenadas[0]["temp"]
    print(f"\nMás fría : {ordenadas[0]['ciudad']} ({ordenadas[0]['temp']}°C)")
    print(f"Más cálida: {ordenadas[-1]['ciudad']} ({ordenadas[-1]['temp']}°C)")
    print(f"Diferencia entre ambas: {rango:.1f}°C")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar ciudades de ejemplo")
        print("2. Registrar mis propias ciudades")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(ciudades_ejemplo())
        elif opcion == "2":
            datos = ciudades_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
