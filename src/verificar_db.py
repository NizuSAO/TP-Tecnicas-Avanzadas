
import sqlite3
from pathlib import Path

DB = Path(__file__).with_name("inventario.db")

conexion = sqlite3.connect(DB)
conexion.execute("PRAGMA foreign_keys = ON")

cursor = conexion.cursor()

# Consultamos las columnas existentes
cursor.execute("PRAGMA table_info(productos)")
columnas = [columna[1] for columna in cursor.fetchall()]

# Agregamos la columna si todavía no existe
if "categoria_id" not in columnas:
    cursor.execute("""
        ALTER TABLE productos
        ADD COLUMN categoria_id INTEGER
        REFERENCES categorias(id)
    """)

    conexion.commit()
    print("Columna categoria_id agregada correctamente")
else:
    print("La columna categoria_id ya existe")

conexion.close()
