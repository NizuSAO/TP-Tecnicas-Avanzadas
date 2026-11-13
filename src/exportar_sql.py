
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent

# Abrimos nuestra base de datos
conexion = sqlite3.connect(BASE / "inventario.db")

sentencias = ["PRAGMA foreign_keys = ON;"]

# Exportamos la estructura de las tablas
for tabla in ["categorias", "productos"]:
    resultado = conexion.execute("""
        SELECT sql FROM sqlite_master
        WHERE type = 'table' AND name = ?
    """, (tabla,)).fetchone()

    if resultado is None:
        raise RuntimeError(f"No existe la tabla {tabla}")

    sentencias.append(resultado[0].rstrip(";") + ";")

conexion.close()

# Generamos el archivo SQL
carpeta = BASE / "dbf"
carpeta.mkdir(exist_ok=True)

archivo = carpeta / "inventario.sql"
archivo.write_text(
    "\n\n".join(sentencias) + "\n",
    encoding="utf-8"
)

print("Archivo SQL exportado correctamente.")
