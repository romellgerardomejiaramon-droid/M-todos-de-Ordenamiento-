
import tkinter as tk
from tkinter import ttk, messagebox


class AplicacionOrdenamiento:
    def __init__(self, ventana):
        self.raiz = ventana
        self.raiz.title("Sistema de Metodos de Ordenamiento")

        ancho_pantalla = self.raiz.winfo_screenwidth()
        alto_pantalla = self.raiz.winfo_screenheight()

        ancho = min(1100, ancho_pantalla - 40)
        alto = min(850, alto_pantalla - 80)

        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2

        self.raiz.geometry(f"{ancho}x{alto}+{x}+{y}")
        self.raiz.minsize(
            min(600, ancho_pantalla),
            min(450, alto_pantalla)
        )

        try:
            self.raiz.state("zoomed")
        except tk.TclError:
            pass

        self.canvas = tk.Canvas(
            self.raiz,
            highlightthickness=0
        )

        self.barra = ttk.Scrollbar(
            self.raiz,
            orient="vertical",
            command=self.canvas.yview
        )

        self.canvas.configure(
            yscrollcommand=self.barra.set
        )

        self.barra.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.contenido = ttk.Frame(
            self.canvas,
            padding=15
        )

        self.id_contenido = self.canvas.create_window(
            (0, 0),
            window=self.contenido,
            anchor="nw"
        )

        self.contenido.bind(
            "<Configure>",
            lambda evento: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind(
            "<Configure>",
            lambda evento: self.canvas.itemconfigure(
                self.id_contenido,
                width=evento.width
            )
        )

        self.canvas.bind_all(
            "<MouseWheel>",
            self.desplazar
        )

        self.ventana = self.contenido

        self.metodos = {
            "Burbuja": {
                "descripcion": "Compara elementos vecinos e intercambia sus posiciones cuando estan desordenados.",
                "funcionamiento": "Recorre la lista varias veces. En cada recorrido compara dos numeros consecutivos. Si estan en el orden incorrecto, intercambia sus posiciones.",
                "ejemplo": [8, 3, 6, 1, 5]
            },
            "Insercion": {
                "descripcion": "Toma un elemento y lo coloca en la posicion correcta dentro de la parte que ya esta ordenada.",
                "funcionamiento": "Comienza desde el segundo elemento. Guarda su valor, compara con los anteriores y desplaza los mayores para dejar espacio al elemento que se esta insertando.",
                "ejemplo": [7, 4, 9, 2, 5]
            },
            "Seleccion": {
                "descripcion": "Busca el elemento menor de la parte desordenada y lo coloca en la posicion correspondiente.",
                "funcionamiento": "Busca el numero menor de la parte que falta ordenar. Despues lo intercambia con el primer elemento de esa parte. Repite el proceso hasta terminar.",
                "ejemplo": [9, 3, 7, 1, 5]
            }
        }

        self.metodo_actual = ""

        self.mostrar_menu()

    def desplazar(self, evento):
        self.canvas.yview_scroll(
            int(-1 * (evento.delta / 120)),
            "units"
        )

    def limpiar(self):
        for elemento in self.ventana.winfo_children():
            elemento.destroy()

        self.canvas.yview_moveto(0)

    def crear_titulo(self, texto):
        ttk.Label(
            self.ventana,
            text=texto,
            font=("Arial", 21, "bold")
        ).pack(pady=15)

    def mostrar_menu(self):
        self.limpiar()

        self.crear_titulo("METODOS DE ORDENAMIENTO")

        ttk.Label(
            self.ventana,
            text="Selecciona el metodo que deseas utilizar.",
            font=("Arial", 12)
        ).pack(pady=15)

        opciones = [
            ("1. Metodo Burbuja", lambda: self.mostrar_metodo("Burbuja")),
            ("2. Metodo Insercion", lambda: self.mostrar_metodo("Insercion")),
            ("3. Metodo Seleccion", lambda: self.mostrar_metodo("Seleccion")),
            ("4. Comparar los tres metodos", self.mostrar_comparacion),
            ("5. Salir", self.raiz.destroy)
        ]

        for texto, funcion in opciones:
            ttk.Button(
                self.ventana,
                text=texto,
                command=funcion,
                width=40
            ).pack(pady=9, ipady=7)

        ttk.Label(
            self.ventana,
            text="El programa resuelve los ejercicios y muestra todo el procedimiento.",
            font=("Arial", 10, "italic"),
            wraplength=850
        ).pack(pady=25)

    def mostrar_metodo(self, metodo):
        self.limpiar()

        self.metodo_actual = metodo
        datos = self.metodos[metodo]

        self.crear_titulo("METODO " + metodo.upper())

        ttk.Label(
            self.ventana,
            text="¿QUE ES?",
            font=("Arial", 13, "bold")
        ).pack(anchor="w", padx=25, pady=(5, 2))

        ttk.Label(
            self.ventana,
            text=datos["descripcion"],
            wraplength=850,
            justify="left"
        ).pack(anchor="w", padx=25)

        ttk.Label(
            self.ventana,
            text="¿COMO FUNCIONA?",
            font=("Arial", 13, "bold")
        ).pack(anchor="w", padx=25, pady=(15, 2))

        ttk.Label(
            self.ventana,
            text=datos["funcionamiento"],
            wraplength=850,
            justify="left"
        ).pack(anchor="w", padx=25)

        ttk.Separator(
            self.ventana
        ).pack(fill="x", padx=25, pady=20)

        ttk.Label(
            self.ventana,
            text="¿QUE EJERCICIO DESEAS RESOLVER?",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        ttk.Button(
            self.ventana,
            text="Utilizar un ejemplo",
            command=lambda: self.seleccionar_ejemplo(metodo),
            width=40
        ).pack(pady=10, ipady=7)

        ttk.Button(
            self.ventana,
            text="Crear mi propio ejercicio",
            command=lambda: self.crear_ejercicio(metodo),
            width=40
        ).pack(pady=10, ipady=7)

        ttk.Button(
            self.ventana,
            text="Volver al menu principal",
            command=self.mostrar_menu
        ).pack(pady=20)

    def seleccionar_ejemplo(self, metodo):
        self.limpiar()

        self.crear_titulo("EJEMPLO DEL METODO " + metodo.upper())

        lista = self.metodos[metodo]["ejemplo"]

        ttk.Label(
            self.ventana,
            text="Este es el ejercicio predeterminado:",
            font=("Arial", 12)
        ).pack(pady=10)

        ttk.Label(
            self.ventana,
            text=str(lista),
            font=("Arial", 20, "bold")
        ).pack(pady=15)

        self.seleccionar_direccion(metodo, lista)

    def crear_ejercicio(self, metodo):
        self.limpiar()

        self.crear_titulo("CREAR MI PROPIO EJERCICIO")

        ttk.Label(
            self.ventana,
            text="Introduce los numeros que deseas ordenar.",
            font=("Arial", 12)
        ).pack(pady=15)

        ttk.Label(
            self.ventana,
            text="Escribe los numeros separados por comas:"
        ).pack(pady=5)

        entrada = ttk.Entry(
            self.ventana,
            width=50,
            font=("Arial", 12)
        )
        entrada.pack(pady=10)

        entrada.insert(0, "8, 3, 6, 1, 5")

        def continuar():
            try:
                texto = entrada.get().strip()

                if not texto:
                    messagebox.showwarning(
                        "Dato faltante",
                        "Introduce una lista de numeros."
                    )
                    return

                lista = [
                    int(numero.strip())
                    for numero in texto.split(",")
                ]

                if len(lista) < 2:
                    messagebox.showwarning(
                        "Lista incompleta",
                        "Introduce al menos dos numeros."
                    )
                    return

                if len(lista) > 30:
                    messagebox.showwarning(
                        "Lista demasiado grande",
                        "Introduce un maximo de 30 numeros."
                    )
                    return

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Escribe numeros enteros separados por comas."
                )
                return

            self.seleccionar_direccion(metodo, lista)

        ttk.Button(
            self.ventana,
            text="Continuar",
            command=continuar
        ).pack(pady=15, ipadx=20, ipady=5)

        ttk.Button(
            self.ventana,
            text="Volver",
            command=lambda: self.mostrar_metodo(metodo)
        ).pack(pady=10)

    def seleccionar_direccion(self, metodo, lista):
        self.limpiar()

        self.crear_titulo("CONFIGURAR ORDENAMIENTO")

        ttk.Label(
            self.ventana,
            text="Metodo seleccionado: " + metodo,
            font=("Arial", 13, "bold")
        ).pack(pady=10)

        ttk.Label(
            self.ventana,
            text="Lista que se va a resolver: " + str(lista),
            font=("Arial", 13)
        ).pack(pady=10)

        direccion = tk.StringVar(value="Ascendente")

        ttk.Label(
            self.ventana,
            text="Selecciona el tipo de ordenamiento:"
        ).pack(pady=10)

        ttk.Radiobutton(
            self.ventana,
            text="Ascendente (menor a mayor)",
            variable=direccion,
            value="Ascendente"
        ).pack(pady=5)

        ttk.Radiobutton(
            self.ventana,
            text="Descendente (mayor a menor)",
            variable=direccion,
            value="Descendente"
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Resolver ejercicio",
            command=lambda: self.mostrar_resultado(
                metodo,
                lista,
                direccion.get()
            )
        ).pack(pady=20, ipadx=25, ipady=7)

        ttk.Button(
            self.ventana,
            text="Volver",
            command=lambda: self.mostrar_metodo(metodo)
        ).pack(pady=10)

    def ordenar_con_pasos(self, lista, metodo, direccion):
        valores = lista.copy()
        pasos = []
        comparaciones = 0
        movimientos = 0

        def esta_desordenado(a, b):
            if direccion == "Ascendente":
                return a > b
            return a < b

        pasos.append((
            "Estado inicial",
            "La lista original es " + str(valores),
            valores.copy()
        ))

        if metodo == "Burbuja":

            for i in range(len(valores) - 1):
                hubo_cambio = False

                for j in range(len(valores) - 1 - i):
                    a = valores[j]
                    b = valores[j + 1]

                    comparaciones += 1

                    if esta_desordenado(a, b):
                        valores[j], valores[j + 1] = b, a
                        movimientos += 1
                        hubo_cambio = True

                        pasos.append((
                            "Intercambio",
                            "Se compararon " + str(a) + " y " + str(b) +
                            ". Como estaban desordenados, se intercambiaron.",
                            valores.copy()
                        ))

                    else:
                        pasos.append((
                            "Comparacion",
                            "Se compararon " + str(a) + " y " + str(b) +
                            ". Ya estaban en el orden correcto.",
                            valores.copy()
                        ))

                if not hubo_cambio:
                    pasos.append((
                        "Finalizacion",
                        "La lista ya esta ordenada. El algoritmo termina.",
                        valores.copy()
                    ))
                    break

                pasos.append((
                    "Recorrido terminado",
                    "Se completo el recorrido numero " + str(i + 1) + ".",
                    valores.copy()
                ))

        elif metodo == "Insercion":

            for i in range(1, len(valores)):
                actual = valores[i]
                j = i - 1

                pasos.append((
                    "Seleccion del elemento",
                    "Se toma el numero " + str(actual) +
                    " para encontrar su posicion correcta.",
                    valores.copy()
                ))

                while j >= 0:
                    comparaciones += 1

                    if esta_desordenado(valores[j], actual):
                        desplazado = valores[j]
                        valores[j + 1] = valores[j]
                        movimientos += 1

                        pasos.append((
                            "Desplazamiento",
                            "El numero " + str(desplazado) +
                            " se desplaza una posicion hacia la derecha.",
                            valores.copy()
                        ))

                        j -= 1

                    else:
                        pasos.append((
                            "Comparacion",
                            "El numero " + str(valores[j]) +
                            " ya esta en el orden correcto respecto a " +
                            str(actual) + ".",
                            valores.copy()
                        ))
                        break

                valores[j + 1] = actual

                pasos.append((
                    "Insercion",
                    "El numero " + str(actual) +
                    " se coloca en su posicion correcta.",
                    valores.copy()
                ))

        elif metodo == "Seleccion":

            for i in range(len(valores) - 1):
                posicion = i

                pasos.append((
                    "Busqueda",
                    "Se busca el elemento que debe ocupar la posicion " +
                    str(i + 1) + ".",
                    valores.copy()
                ))

                for j in range(i + 1, len(valores)):
                    comparaciones += 1

                    pasos.append((
                        "Comparacion",
                        "Se compara " + str(valores[posicion]) +
                        " con " + str(valores[j]) + ".",
                        valores.copy()
                    ))

                    if esta_desordenado(valores[posicion], valores[j]):
                        posicion = j

                if posicion != i:
                    primero = valores[i]
                    segundo = valores[posicion]

                    valores[i], valores[posicion] = valores[posicion], valores[i]
                    movimientos += 1

                    pasos.append((
                        "Intercambio",
                        "Se intercambia " + str(primero) +
                        " con " + str(segundo) +
                        " para colocarlo en su posicion.",
                        valores.copy()
                    ))

                else:
                    pasos.append((
                        "Posicion correcta",
                        "El elemento ya se encuentra en su posicion.",
                        valores.copy()
                    ))

        pasos.append((
            "Resultado final",
            "El ordenamiento ha terminado correctamente.",
            valores.copy()
        ))

        return valores, pasos, comparaciones, movimientos

    def mostrar_resultado(self, metodo, lista, direccion):
        self.limpiar()

        self.crear_titulo("RESOLUCION DEL EJERCICIO")

        resultado, pasos, comparaciones, movimientos = self.ordenar_con_pasos(
            lista,
            metodo,
            direccion
        )

        ttk.Label(
            self.ventana,
            text="Metodo: " + metodo +
            "     Orden: " + direccion,
            font=("Arial", 12, "bold")
        ).pack(pady=5)

        ttk.Label(
            self.ventana,
            text="Lista inicial: " + str(lista),
            font=("Arial", 12)
        ).pack(pady=5)

        ttk.Label(
            self.ventana,
            text="PROCEDIMIENTO PASO A PASO",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        marco_tabla = ttk.Frame(self.ventana)
        marco_tabla.pack(fill="both", expand=True, padx=10, pady=8)

        tabla = ttk.Treeview(
            marco_tabla,
            columns=("paso", "tipo", "explicacion", "lista"),
            show="headings",
            height=10
        )

        barra_tabla_vertical = ttk.Scrollbar(
            marco_tabla,
            orient="vertical",
            command=tabla.yview
        )

        barra_tabla_horizontal = ttk.Scrollbar(
            marco_tabla,
            orient="horizontal",
            command=tabla.xview
        )

        tabla.configure(
            yscrollcommand=barra_tabla_vertical.set,
            xscrollcommand=barra_tabla_horizontal.set
        )

        tabla.heading("paso", text="Paso")
        tabla.heading("tipo", text="Accion")
        tabla.heading("explicacion", text="Explicacion")
        tabla.heading("lista", text="Estado de la lista")

        tabla.column("paso", width=60, minwidth=50, anchor="center", stretch=False)
        tabla.column("tipo", width=125, minwidth=100, anchor="center", stretch=False)
        tabla.column("explicacion", width=420, minwidth=220, stretch=True)
        tabla.column("lista", width=190, minwidth=140, stretch=False)

        tabla.grid(row=0, column=0, sticky="nsew")
        barra_tabla_vertical.grid(row=0, column=1, sticky="ns")
        barra_tabla_horizontal.grid(row=1, column=0, sticky="ew")

        marco_tabla.grid_rowconfigure(0, weight=1)
        marco_tabla.grid_columnconfigure(0, weight=1)

        for i, paso in enumerate(pasos):
            tabla.insert(
                "",
                "end",
                values=(
                    i + 1,
                    paso[0],
                    paso[1],
                    str(paso[2])
                )
            )

        ttk.Label(
            self.ventana,
            text="RESULTADOS DEL EJERCICIO",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        ttk.Label(
            self.ventana,
            text="Lista inicial: " + str(lista) +
            "\nResultado final: " + str(resultado) +
            "\nComparaciones realizadas: " + str(comparaciones) +
            "\nMovimientos realizados: " + str(movimientos),
            font=("Arial", 12),
            justify="center"
        ).pack(pady=10)

        ttk.Button(
            self.ventana,
            text="Resolver otro ejercicio",
            command=lambda: self.mostrar_metodo(metodo)
        ).pack(pady=8)

        ttk.Button(
            self.ventana,
            text="Volver al menu principal",
            command=self.mostrar_menu
        ).pack(pady=8)

    def mostrar_comparacion(self):
        self.limpiar()

        self.crear_titulo("COMPARACION DE LOS TRES METODOS")

        ttk.Label(
            self.ventana,
            text="Introduce una lista para ejecutar los tres algoritmos.",
            font=("Arial", 12)
        ).pack(pady=10)

        entrada = ttk.Entry(
            self.ventana,
            width=45,
            font=("Arial", 12)
        )

        entrada.insert(0, "8, 3, 6, 1, 5")
        entrada.pack(pady=8)

        direccion = tk.StringVar(value="Ascendente")

        ttk.Radiobutton(
            self.ventana,
            text="Ascendente",
            variable=direccion,
            value="Ascendente"
        ).pack(pady=3)

        ttk.Radiobutton(
            self.ventana,
            text="Descendente",
            variable=direccion,
            value="Descendente"
        ).pack(pady=3)

        marco_comparacion = ttk.Frame(self.ventana)
        marco_comparacion.pack(fill="x", padx=10, pady=8)

        tabla = ttk.Treeview(
            marco_comparacion,
            columns=("metodo", "resultado", "comparaciones", "movimientos"),
            show="headings",
            height=4
        )

        barra_comparacion = ttk.Scrollbar(
            marco_comparacion,
            orient="horizontal",
            command=tabla.xview
        )

        tabla.configure(xscrollcommand=barra_comparacion.set)

        tabla.heading("metodo", text="Metodo")
        tabla.heading("resultado", text="Resultado")
        tabla.heading("comparaciones", text="Comparaciones")
        tabla.heading("movimientos", text="Movimientos")

        tabla.column("metodo", width=120, minwidth=100, anchor="center", stretch=False)
        tabla.column("resultado", width=250, minwidth=180, anchor="center", stretch=True)
        tabla.column("comparaciones", width=140, minwidth=120, anchor="center", stretch=False)
        tabla.column("movimientos", width=140, minwidth=120, anchor="center", stretch=False)

        tabla.pack(fill="x")
        barra_comparacion.pack(fill="x")

        marco_detalle = ttk.Frame(self.ventana)
        marco_detalle.pack(fill="both", expand=True, padx=10, pady=8)

        detalle = tk.Text(
            marco_detalle,
            height=12,
            wrap="word",
            font=("Arial", 10)
        )

        barra_detalle = ttk.Scrollbar(
            marco_detalle,
            orient="vertical",
            command=detalle.yview
        )

        detalle.configure(yscrollcommand=barra_detalle.set)

        detalle.pack(side="left", fill="both", expand=True)
        barra_detalle.pack(side="right", fill="y")
        detalle.config(state="disabled")

        def comparar():
            try:
                texto = entrada.get().strip()

                if not texto:
                    messagebox.showwarning(
                        "Dato faltante",
                        "Introduce una lista de numeros."
                    )
                    return

                lista = [
                    int(x.strip())
                    for x in texto.split(",")
                ]

                if len(lista) < 2:
                    messagebox.showwarning(
                        "Lista incompleta",
                        "Introduce al menos dos numeros."
                    )
                    return

                if len(lista) > 30:
                    messagebox.showwarning(
                        "Lista demasiado grande",
                        "Introduce un maximo de 30 numeros."
                    )
                    return

            except ValueError:
                messagebox.showerror(
                    "Error",
                    "Escribe numeros enteros separados por comas."
                )
                return

            for elemento in tabla.get_children():
                tabla.delete(elemento)

            detalle.config(state="normal")
            detalle.delete("1.0", "end")

            for metodo in ["Burbuja", "Insercion", "Seleccion"]:

                resultado, pasos, comparaciones, movimientos = self.ordenar_con_pasos(
                    lista,
                    metodo,
                    direccion.get()
                )

                tabla.insert(
                    "",
                    "end",
                    values=(
                        metodo,
                        str(resultado),
                        comparaciones,
                        movimientos
                    )
                )

                detalle.insert(
                    "end",
                    "METODO " + metodo.upper() + "\n"
                )

                detalle.insert(
                    "end",
                    "Lista inicial: " + str(lista) + "\n"
                )

                for i, paso in enumerate(pasos):
                    detalle.insert(
                        "end",
                        "\nPaso " + str(i + 1) + ": " +
                        paso[0] + "\n"
                        + paso[1] + "\n"
                        "Lista: " + str(paso[2]) + "\n"
                    )

                detalle.insert(
                    "end",
                    "\nResultado final: " + str(resultado) +
                    "\nComparaciones: " + str(comparaciones) +
                    "\nMovimientos: " + str(movimientos) +
                    "\n\n" + "-" * 55 + "\n\n"
                )

            detalle.config(state="disabled")

        ttk.Button(
            self.ventana,
            text="Ejecutar comparacion",
            command=comparar
        ).pack(pady=10, ipadx=20, ipady=5)

        ttk.Button(
            self.ventana,
            text="Volver al menu principal",
            command=self.mostrar_menu
        ).pack(pady=15)


ventana = tk.Tk()
aplicacion = AplicacionOrdenamiento(ventana)
ventana.mainloop()
