
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


def burbuja(lista, clave, descendente=False):
    """Ordena una lista de diccionarios según la clave indicada."""
    n = len(lista)
    for i in range(n - 1):
        hubo_cambio = False
        for j in range(n - 1 - i):
            a, b = lista[j][clave], lista[j + 1][clave]
            fuera_de_orden = a < b if descendente else a > b
            if fuera_de_orden:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return lista


def mostrar(titulo, productos):
    print(f"\n--- {titulo} ---")
    print(f"{'Producto':<14}{'Precio':>10}{'Existencia':>12}")
    for p in productos:
        print(f"{p['nombre']:<14}{p['precio']:>10.2f}{p['stock']:>12}")


def inventario_ejemplo():
    return [
        {"nombre": "Laptop",   "precio": 12500.00, "stock": 5},
        {"nombre": "Mouse",    "precio": 250.00,   "stock": 40},
        {"nombre": "Teclado",  "precio": 480.50,   "stock": 22},
        {"nombre": "Monitor",  "precio": 3200.00,  "stock": 9},
        {"nombre": "USB 32GB", "precio": 150.00,   "stock": 75},
        {"nombre": "Bocinas",  "precio": 650.00,   "stock": 14},
    ]


def inventario_manual():
    cantidad = pedir_entero("¿Cuántos productos desea registrar? ")
    productos = []
    for i in range(cantidad):
        print(f"\nProducto {i + 1}")
        nombre = leer("Nombre: ").strip()
        precio = pedir_decimal("Precio: ", 0.01)
        stock = pedir_entero("Existencia (piezas): ", 0)
        productos.append({"nombre": nombre, "precio": precio, "stock": stock})
    return productos


def mostrar_resultados(inventario):
    mostrar("INVENTARIO ORIGINAL", inventario)
    mostrar("PRECIO: de menor a mayor", burbuja(inventario.copy(), "precio"))
    mostrar("PRECIO: de mayor a menor", burbuja(inventario.copy(), "precio", True))
    mostrar("EXISTENCIA: de menor a mayor", burbuja(inventario.copy(), "stock"))

    agotandose = [p["nombre"] for p in burbuja(inventario.copy(), "stock")[:2]]
    print("\nProductos por reabastecer:", ", ".join(agotandose))


def main():
    while True:
        print("\n===== MENÚ =====")
        print("1. Usar inventario de ejemplo")
        print("2. Crear mi propio inventario")
        print("3. Salir")
        opcion = leer("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_resultados(inventario_ejemplo())
        elif opcion == "2":
            datos = inventario_manual()
            if datos:
                mostrar_resultados(datos)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


main()
print("\nFin del programa.")
