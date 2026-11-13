
import sqlite3
from pathlib import Path

# Ubicamos el archivo SQL
BASE = Path(__file__).resolve().parent
archivo = BASE / "dbf" / "inventario.sql"

# Leemos las instrucciones SQL
sql = archivo.read_text(encoding="utf-8")

# Creamos una base de datos temporal en memoria
conexion = sqlite3.connect(":memory:")
conexion.execute("PRAGMA foreign_keys = ON")

# Ejecutamos las instrucciones SQL
conexion.executescript(sql)

# Verificamos las tablas y sus columnas
for tabla in ["categorias", "productos"]:
    columnas = conexion.execute(
        f"PRAGMA table_info({tabla})"
    ).fetchall()

    print(f"\nTabla: {tabla}")

    for columna in columnas:
        print("-", columna[1])

# Verificamos la relación entre tablas
relaciones = conexion.execute(
    "PRAGMA foreign_key_list(productos)"
).fetchall()

if any(
    r[2] == "categorias" and r[3] == "categoria_id"
    for r in relaciones
):
    print("\nRelación entre tablas: CORRECTA")
else:
    print("\nATENCIÓN: falta la clave foránea")

conexion.close()

print("\nVerificación terminada.")
