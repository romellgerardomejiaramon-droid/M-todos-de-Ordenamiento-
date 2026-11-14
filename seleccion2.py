
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


def valor_de(elemento, clave):
    valor = elemento[clave]
    return valor.lower() if isinstance(valor, str) else valor


def seleccion(lista, clave, descendente=False):
    """Ordena una lista de diccionarios según la clave indicada."""
    n = len(lista)
    for i in range(n - 1):
        elegido = i
        for j in range(i + 1, n):
            if descendente:
                es_mejor = valor_de(lista[j], clave) > valor_de(lista[elegido], clave)
            else:
                es_mejor = valor_de(lista[j], clave) < valor_de(lista[elegido], clave)
            if es_mejor:
                elegido = j
        lista[i], lista[elegido] = lista[elegido], lista[i]
    return lista


def mostrar(titulo, empleados):
    print(f"\n--- {titulo} ---")
    print(f"{'Empleado':<14}{'Sueldo':>12}{'Antigüedad':>13}")
    for e in empleados:
        unidad = "año" if e["anios"] == 1 else "años"
        antiguedad = f"{e['anios']} {unidad}"
        print(f"{e['nombre']:<14}{e['sueldo']:>12,.2f}{antiguedad:>13}")


def empleados_ejemplo():
    return [
        {"nombre": "Roberto",  "sueldo": 18500.00, "anios": 6},
        {"nombre": "Daniela",  "sueldo": 24000.00, "anios": 9},
        {"nombre": "Javier",   "sueldo": 12800.00, "anios": 2},
        {"nombre": "Patricia", "sueldo": 31500.00, "anios": 12},
        {"nombre": "Miguel",   "sueldo": 15200.00, "anios": 4},
        {"nombre": "Alejandra","sueldo": 21000.00, "anios": 7},
    ]


def empleados_manual():
    cantidad = pedir_entero("¿Cuántos empleados desea registrar? ")
    empleados = []
    for i in range(cantidad):
        print(f"\nEmpleado {i + 1}")
        nombre = leer("Nombre: ").strip()
        sueldo = pedir_decimal("Sueldo: ", 0.01)
        anios = pedir_entero("Años de antigüedad: ", 0)
        empleados.append({"nombre": nombre, "sueldo": sueldo, "anios": anios})
    return empleados


def mostrar_resultados(empleados):
    mostrar("NÓMINA ORIGINAL", empleados)
    mostrar("SUELDO: de mayor a menor", seleccion(empleados.copy(), "sueldo", True))
    mostrar("ANTIGÜEDAD: de mayor a menor", seleccion(empleados.copy(), "anios", True))
    mostrar("NOMBRE: de la A a la Z", seleccion(empleados.copy(), "nombre"))

    total = sum(e["sueldo"] for e in empleados)
    mejor = seleccion(empleados.copy(), "sueldo", True)[0]
    print(f"\nNómina total: {total:,.2f}")
    print(f"Sueldo más alto: {mejor['nombre']} ({mejor['sueldo']:,.2f})")


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar nómina de ejemplo")
        print("2. Crear mi propia nómina")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(empleados_ejemplo())
        elif opcion == "2":
            datos = empleados_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
