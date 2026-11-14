
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


def insercion(corredores):
    """Ordena de menor a mayor tiempo. Devuelve comparaciones y desplazamientos."""
    comparaciones = 0
    desplazamientos = 0
    for i in range(1, len(corredores)):
        actual = corredores[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if corredores[j]["tiempo"] > actual["tiempo"]:
                corredores[j + 1] = corredores[j]
                desplazamientos += 1
                j -= 1
            else:
                break
        corredores[j + 1] = actual
    return comparaciones, desplazamientos


def corredores_ejemplo():
    return [
        {"nombre": "Ana",    "tiempo": 12.50},
        {"nombre": "Luis",   "tiempo": 11.20},
        {"nombre": "María",  "tiempo": 13.80},
        {"nombre": "Pedro",  "tiempo": 11.90},
        {"nombre": "Sofía",  "tiempo": 12.10},
        {"nombre": "Carlos", "tiempo": 14.30},
    ]


def corredores_manual():
    cantidad = pedir_entero("¿Cuántos corredores participaron? ")
    corredores = []
    for i in range(cantidad):
        nombre = leer(f"Nombre del corredor {i + 1}: ").strip()
        tiempo = pedir_decimal(f"Tiempo de {nombre} (segundos): ", 0.01)
        corredores.append({"nombre": nombre, "tiempo": tiempo})
    return corredores


def mostrar_resultados(corredores):
    cantidad = len(corredores)
    comparaciones, desplazamientos = insercion(corredores)

    print("\n--- RESULTADOS DE LA CARRERA ---")
    for lugar, c in enumerate(corredores, start=1):
        print(f"{lugar}. {c['nombre']:<15} {c['tiempo']:.2f} s")

    print("\n--- PODIO ---")
    medallas = ["Oro", "Plata", "Bronce"]
    for medalla, c in zip(medallas, corredores):
        print(f"{medalla:<7}: {c['nombre']}")

    promedio = sum(c["tiempo"] for c in corredores) / cantidad
    diferencia = corredores[-1]["tiempo"] - corredores[0]["tiempo"]
    print(f"\nTiempo promedio: {promedio:.2f} s")
    print(f"Diferencia entre el primero y el último: {diferencia:.2f} s")
    print(f"Comparaciones: {comparaciones} | Desplazamientos: {desplazamientos}")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar carrera de ejemplo")
        print("2. Registrar mis propios corredores")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(corredores_ejemplo())
        elif opcion == "2":
            datos = corredores_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
