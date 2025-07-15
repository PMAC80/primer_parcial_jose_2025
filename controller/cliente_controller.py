from model.cliente import Cliente

import sqlite3

class ClienteController:
    def __init__(self):
        self._conexion = sqlite3.connect("clientes.db")
        self._cursor = self._conexion.cursor()
        self._crear_tabla()

    def _crear_tabla(self):
        self._cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT NOT NULL
            )
        """)
        self._cursor.execute("""
            INSERT INTO sqlite_sequence (name, seq)
            SELECT 'clientes', 99
            WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'clientes')
        """)
        self._conexion.commit()

    def alta_cliente(self, cliente):
        self._cursor.execute("""
            INSERT INTO clientes (nombre, apellido, direccion)
            VALUES (?, ?, ?)
        """, (cliente.nombre, cliente.apellido, cliente.direccion))
        self._conexion.commit()
        print("[LOG] Cliente agregado correctamente.")

    def baja_cliente(self, id):
        self._cursor.execute("DELETE FROM clientes WHERE id=?", (id,))
        self._conexion.commit()
        print("[LOG] Cliente eliminado correctamente.")

    def modificar_cliente(self, cliente):
        self._cursor.execute("""
            UPDATE clientes
            SET nombre=?, apellido=?, direccion=?
            WHERE id=?
        """, (cliente.nombre, cliente.apellido, cliente.direccion, cliente.id))
        self._conexion.commit()
        print("[LOG] Cliente actualizado correctamente.")

    def obtener_cliente(self, id):
        self._cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
        datos = self._cursor.fetchone()
        if datos:
            return Cliente(*datos)
        else:
            print("[LOG] Cliente no encontrado.")
            return None

    def listar_clientes(self):
        self._cursor.execute("SELECT * FROM clientes")
        datos = self._cursor.fetchall()
        return [Cliente(*fila) for fila in datos]

    def cerrar_conexion(self):
        self._conexion.close()