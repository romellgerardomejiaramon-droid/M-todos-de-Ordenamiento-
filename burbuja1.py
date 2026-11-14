
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


def burbuja(alumnos):
    """Ordena de mayor a menor calificación. Devuelve comparaciones e intercambios."""
    n = len(alumnos)
    comparaciones = 0
    intercambios = 0
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            comparaciones += 1
            if alumnos[j]["calificacion"] < alumnos[j + 1]["calificacion"]:
                alumnos[j], alumnos[j + 1] = alumnos[j + 1], alumnos[j]
                intercambios += 1
                hubo_cambio = True
        if not hubo_cambio:
            break
    return comparaciones, intercambios


def alumnos_ejemplo():
    return [
        {"nombre": "Ana",    "calificacion": 9.5},
        {"nombre": "Luis",   "calificacion": 7.0},
        {"nombre": "María",  "calificacion": 10.0},
        {"nombre": "Pedro",  "calificacion": 6.5},
        {"nombre": "Sofía",  "calificacion": 8.2},
        {"nombre": "Carlos", "calificacion": 5.8},
    ]


def alumnos_manual():
    cantidad = pedir_entero("¿Cuántos alumnos desea registrar? ")
    alumnos = []
    for i in range(cantidad):
        nombre = leer(f"Nombre del alumno {i + 1}: ").strip()
        calificacion = pedir_decimal(f"Calificación de {nombre} (0 a 10): ", 0, 10)
        alumnos.append({"nombre": nombre, "calificacion": calificacion})
    return alumnos


def mostrar_resultados(alumnos):
    cantidad = len(alumnos)
    comparaciones, intercambios = burbuja(alumnos)

    print("\n--- RANKING DEL GRUPO ---")
    for posicion, alumno in enumerate(alumnos, start=1):
        print(f"{posicion}. {alumno['nombre']:<15} {alumno['calificacion']:.1f}")

    promedio = sum(a["calificacion"] for a in alumnos) / cantidad
    print(f"\nPromedio del grupo : {promedio:.2f}")
    print(f"Calificación más alta: {alumnos[0]['nombre']} ({alumnos[0]['calificacion']:.1f})")
    print(f"Calificación más baja: {alumnos[-1]['nombre']} ({alumnos[-1]['calificacion']:.1f})")
    print(f"Comparaciones: {comparaciones} | Intercambios: {intercambios}")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar grupo de ejemplo")
        print("2. Registrar mis propios alumnos")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(alumnos_ejemplo())
        elif opcion == "2":
            datos = alumnos_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
