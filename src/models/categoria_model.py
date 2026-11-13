import sqlite3
from pathlib import Path

# Ubicación de la base de datos
DB = Path(__file__).resolve().parent.parent / "inventario.db"


# Función para conectar con SQLite
def conectar():
    conexion = sqlite3.connect(DB)
    conexion.row_factory = sqlite3.Row
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


# GET - Consultar categorías
def obtener_categorias():
    conexion = conectar()

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()

        return [dict(c) for c in categorias]
    finally:
        conexion.close()


# POST - Crear categoría
def crear_categoria(nombre, descripcion):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO categorias (nombre, descripcion)
            VALUES (?, ?)
        """, (nombre, descripcion))

        conexion.commit()
        return cursor.lastrowid
    finally:
        conexion.close()


# PUT - Actualizar categoría
def actualizar_categoria(id, nombre, descripcion):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE categorias
            SET nombre = ?, descripcion = ?
            WHERE id = ?
        """, (nombre, descripcion, id))

        conexion.commit()
        return cursor.rowcount > 0
    finally:
        conexion.close()


# DELETE - Eliminar categoría
def eliminar_categoria(id):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        cursor.execute(
            "DELETE FROM categorias WHERE id = ?",
            (id,)
        )

        if cursor.rowcount == 0:
            return "no_existe"

        conexion.commit()
        return "eliminada"

    except sqlite3.IntegrityError:
        conexion.rollback()
        return "en_uso"

    finally:
        conexion.close()
