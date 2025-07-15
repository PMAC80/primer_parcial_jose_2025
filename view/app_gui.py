from model.cliente import Cliente

import tkinter as tk
from tkinter import ttk

class AppGUI(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Gestión de Clientes - NicBread")
        self.geometry("800x300")
        self.controller = controller
        self.crear_menu()
        self.crear_interfaz()
        self.protocol("WM_DELETE_WINDOW", self.on_cerrar)

    def crear_menu(self):
        menu_bar = tk.Menu(self)
        cliente_menu = tk.Menu(menu_bar, tearoff=0)
        cliente_menu.add_command(label="Dar de alta", command=self.ventana_alta)
        cliente_menu.add_command(label="Modificar", command=self.ventana_modificar)
        cliente_menu.add_command(label="Eliminar", command=self.ventana_baja)
        cliente_menu.add_command(label="Listar uno", command=self.ventana_listar_cliente)
        cliente_menu.add_command(label="Listar todos", command=self.listar_clientes)
        menu_bar.add_cascade(label="Clientes", menu=cliente_menu)
        self.config(menu=menu_bar)
        
    def ventana_listar_cliente(self):
        ventana = tk.Toplevel(self)
        ventana.title("Listar Cliente")

        tk.Label(ventana, text="Código").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()

        resultado_label = tk.Label(ventana, text="")
        resultado_label.pack(pady=10)

        def buscar():
            try:
                id_cliente = int(id_entry.get())
            except ValueError:
                resultado_label.config(text="Ingrese un código válido.")
                return
            cliente = self.controller.obtener_cliente(id_cliente)
            if cliente:
                resultado = f"Código: {cliente.id}\nNombre: {cliente.nombre}\nApellido: {cliente.apellido}\nDirección: {cliente.direccion}"
            else:
                resultado = "Cliente no encontrado."
            resultado_label.config(text=resultado)

        tk.Button(ventana, text="Buscar", command=buscar).pack()

    def crear_interfaz(self):
        self.tabla_frame = tk.Frame(self)
        self.tabla_frame.pack(padx=10, pady=10)
        self.tabla = ttk.Treeview(self.tabla_frame, columns=("id", "nombre", "apellido", "direccion"), show='headings')
        self.tabla.heading("id", text="Código")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("apellido", text="Apellido")
        self.tabla.heading("direccion", text="Dirección")
        self.tabla.pack()

    def refresh_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        clientes = self.controller.listar_clientes()
        if clientes:
            for c in clientes:
                self.tabla.insert("", tk.END, values=(c.id, c.nombre, c.apellido, c.direccion))
        else:
            self.tabla.insert("", tk.END, values=("No hay clientes.", "", "", ""))

    def ventana_alta(self):
        ventana = tk.Toplevel(self)
        ventana.title("Alta de Cliente")

        tk.Label(ventana, text="Nombre").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()

        tk.Label(ventana, text="Apellido").pack()
        apellido_entry = tk.Entry(ventana)
        apellido_entry.pack()

        tk.Label(ventana, text="Dirección").pack()
        direccion_entry = tk.Entry(ventana)
        direccion_entry.pack()

        def guardar():
            cliente = Cliente(None, nombre_entry.get(), apellido_entry.get(), direccion_entry.get())
            self.controller.alta_cliente(cliente)
            ventana.destroy()
            self.refresh_tabla()

        tk.Button(ventana, text="Guardar", command=guardar).pack()

    def ventana_baja(self):
        ventana = tk.Toplevel(self)
        ventana.title("Baja de Cliente")

        tk.Label(ventana, text="Código").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()

        def eliminar():
            id_cliente = int(id_entry.get())
            self.controller.baja_cliente(id_cliente)
            ventana.destroy()
            self.refresh_tabla()

        tk.Button(ventana, text="Eliminar", command=eliminar).pack()

    def ventana_modificar(self):
        ventana = tk.Toplevel(self)
        ventana.title("Modificar Cliente")

        tk.Label(ventana, text="Código").pack()
        id_entry = tk.Entry(ventana)
        id_entry.pack()

        tk.Label(ventana, text="Nombre").pack()
        nombre_entry = tk.Entry(ventana)
        nombre_entry.pack()

        tk.Label(ventana, text="Apellido").pack()
        apellido_entry = tk.Entry(ventana)
        apellido_entry.pack()

        tk.Label(ventana, text="Dirección").pack()
        direccion_entry = tk.Entry(ventana)
        direccion_entry.pack()

        def actualizar():
            id_cliente = int(id_entry.get())
            cliente = self.controller.obtener_cliente(id_cliente)
            if cliente:
                cliente.nombre = nombre_entry.get()
                cliente.apellido = apellido_entry.get()
                cliente.direccion = direccion_entry.get()
                self.controller.modificar_cliente(cliente)
                ventana.destroy()
                self.refresh_tabla()

        tk.Button(ventana, text="Actualizar", command=actualizar).pack()
    
    
    def listar_clientes(self):
        self.refresh_tabla()
        clientes = self.controller.listar_clientes()
        print("\n[LOG] Listado de clientes:")
        for c in clientes:
            print(f"Código: {c.id}, Nombre: {c.nombre}, Apellido: {c.apellido}, Dirección: {c.direccion}")

    def on_cerrar(self):
        self.controller.cerrar_conexion()
        self.destroy()