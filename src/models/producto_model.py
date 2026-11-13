
import sqlite3
from models.categoria_model import conectar


# GET - Consultar todos los productos
def obtener_productos():

    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT
                p.id,
                p.nombre,
                p.precio,
                p.stock,
                p.categoria_id,
                c.nombre AS categoria
            FROM productos p
            INNER JOIN categorias c
                ON p.categoria_id = c.id
        """)

        productos = cursor.fetchall()

        return [dict(p) for p in productos]

    finally:
        conexion.close()


# POST - Crear un producto
def crear_producto(nombre, precio, stock, categoria_id):

    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO productos
            (nombre, precio, stock, categoria_id)
            VALUES (?, ?, ?, ?)
        """, (nombre, precio, stock, categoria_id))

        conexion.commit()

        return cursor.lastrowid

    except sqlite3.IntegrityError:
        conexion.rollback()
        return None

    finally:
        conexion.close()


# PUT - Actualizar un producto
def actualizar_producto(id, nombre, precio, stock, categoria_id):

    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE productos
            SET nombre = ?,
                precio = ?,
                stock = ?,
                categoria_id = ?
            WHERE id = ?
        """, (nombre, precio, stock, categoria_id, id))

        if cursor.rowcount == 0:
            return "no_existe"

        conexion.commit()

        return "actualizado"

    except sqlite3.IntegrityError:
        conexion.rollback()
        return "categoria_invalida"

    finally:
        conexion.close()


# DELETE - Eliminar un producto
def eliminar_producto(id):

    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM productos WHERE id = ?",
            (id,)
        )

        if cursor.rowcount == 0:
            return False

        conexion.commit()

        return True

    finally:
        conexion.close()
