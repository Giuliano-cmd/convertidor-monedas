import tkinter as tk
from tkinter import *
from tkinter import ttk



class vistaMenu():
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Menu")

        self.boton_CotizacionActual = ttk.Button(root, width=40, text="Ver cotizacion actual", command=lambda:self.iniciarCotizacionActual(root))
        self.boton_convertirARSUSD = ttk.Button(root, width=40, text="Convertir ARS a USD", command=lambda:self.iniciarARSUSD(root))
        self.boton_convertirUSDARS = ttk.Button(root, width=40, text="Convertir USD a ARS", command=lambda:self.iniciarUSDARS(root))
        self.boton_historial = ttk.Button(root, width=40, text="Ver historial de cotizaciones USD", command=lambda:self.iniciarHistorial(root))
        

        self.boton_CotizacionActual.pack(padx=10, pady=10)
        self.boton_convertirARSUSD.pack(padx=10, pady=10)
        self.boton_convertirUSDARS.pack(padx=10, pady=10)
        self.boton_historial.pack(padx=10, pady=10)
    
    def iniciarHistorial(self, root):
        vistaHistorial(root)

    def iniciarCotizacionActual(self, root):
        vistaCotizacionActual(root)

    def iniciarARSUSD(self, root):
        vistaARSUSD(root)

    def iniciarUSDARS(self, root):
        vistaUSDARS(root)


class vistaCotizacionActual():
    def __init__(self, parent) -> None:
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Cotizacion actual del dolar")

        #Etiquetas
        self.etiqueta_fecha = ttk.Label(self.ventana, text="Fecha hoy")
        self.etiqueta_cotizacion = ttk.Label(self.ventana, text="Precio actual del dolar")


        self.etiqueta_fecha.pack(padx=10, pady=10)
        self.etiqueta_cotizacion.pack(padx=10, pady=10)


class vistaHistorial():
    def __init__(self, parent) -> None:
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Historial de cotizaciones USD")

        #Tabla
        columnas = ("id", "monto", "fecha")
        self.tabla = ttk.Treeview(self.ventana, columns=columnas, show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("monto", text="Monto")
        self.tabla.heading("fecha", text="Fecha")
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("monto", width=300)
        self.tabla.column("fecha", width=300)
        self.tabla.pack(padx=10, pady=10, fill="both", expand=True)

        self.botonBorrar = ttk.Button(self.ventana, text="Borrar cotizacion")
        self.botonBorrar.pack(padx=10, pady=10)

class vistaARSUSD():
    def __init__(self, parent) -> None:
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Convertidor de ARS a USD")


        self.etiqueta_cotizacion = ttk.Label(self.ventana, text="Precio actual del dolar")
        self.entrada_ARS = ttk.Entry(self.ventana)

        self.etiqueta_cotizacion.pack(padx=10, pady=10)
        self.entrada_ARS.pack(padx=10, pady=10)

class vistaUSDARS():
    def __init__(self, parent) -> None:
        self.ventana = tk.Toplevel(parent)
        self.ventana.title("Convertidor de USD a ARS")


        self.etiqueta_cotizacion = ttk.Label(self.ventana, text="Precio actual del dolar")
        self.entrada_ARS = ttk.Entry(self.ventana)

        self.etiqueta_cotizacion.pack(padx=10, pady=10)
        self.entrada_ARS.pack(padx=10, pady=10)




#vistaMenu(root)
