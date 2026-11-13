
import sqlite3

# Conectamos con nuestra base de datos
conexion = sqlite3.connect("inventario.db")

# Activamos las claves foráneas
conexion.execute("PRAGMA foreign_keys = ON")

# Creamos la tabla categorias
conexion.execute("""
    CREATE TABLE IF NOT EXISTS categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
    )
""")

# Creamos la tabla productos
conexion.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL CHECK(precio >= 0),
        stock INTEGER NOT NULL CHECK(stock >= 0),
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
""")

# Guardamos los cambios
conexion.commit()

# Cerramos la conexión
conexion.close()

print("Base de datos y tablas creadas correctamente.")

# Conectamos con la base de datos
conexion = sqlite3.connect("inventario.db")

# Agregamos la columna stock a productos
conexion.execute("""
    ALTER TABLE productos
    ADD COLUMN stock INTEGER NOT NULL DEFAULT 0
""")

conexion.commit()
conexion.close()

print("Columna stock agregada correctamente")
