PRAGMA foreign_keys = ON;

CREATE TABLE categorias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
    );

CREATE TABLE productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    , stock INTEGER NOT NULL DEFAULT 0, categoria_id INTEGER
        REFERENCES categorias(id));
