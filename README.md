# TP Final

**Materia:** Técnicas Avanzadas de Programación  
**Alumno:** Nicolás Paz  
**Proyecto:** Sistema de Gestión de Inventario

## Descripción del proyecto

Sistema de gestión de inventario desarrollado en Python, utilizando Flask para implementar una API REST y SQLite como base de datos.

El sistema permite administrar productos y categorías mediante las cuatro operaciones CRUD: crear, consultar, actualizar y eliminar registros.

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- Postman
- GitHub

## Arquitectura MVC

El proyecto implementa el patrón Modelo-Vista-Controlador para separar las responsabilidades del código.

- **Modelo:** administra las operaciones sobre la base de datos SQLite.
- **Vista:** representa las respuestas de la API en formato JSON.
- **Controlador:** recibe las solicitudes HTTP, valida los datos y coordina las operaciones.

## Base de datos

El sistema utiliza dos tablas relacionadas:

- **categorias:** id, nombre y descripcion.
- **productos:** id, nombre, precio, stock y categoria_id.

La relación es de uno a muchos (1:N), donde una categoría puede contener varios productos.

La estructura SQL se encuentra en `dbf/inventario.sql`.

## Operaciones disponibles

| Método | Endpoint | Descripción |
|---|---|---|
| GET | /categorias | Consultar categorías |
| POST | /categorias | Registrar categoría |
| PUT | /categorias/{id} | Actualizar categoría |
| DELETE | /categorias/{id} | Eliminar categoría |
| GET | /productos | Consultar productos |
| POST | /productos | Registrar producto |
| PUT | /productos/{id} | Actualizar producto |
| DELETE | /productos/{id} | Eliminar producto |

## Instalación y ejecución

1. Tener Python instalado.
2. Instalar las dependencias mediante `python -m pip install -r requirements.txt`.
3. Preparar la base de datos SQLite utilizando el archivo SQL incluido si todavía no existe `src/inventario.db`.
4. Ejecutar el servidor mediante `python src/app.py`.
5. Abrir Postman y enviar las solicitudes a `http://127.0.0.1:5000`.

## Pruebas

Las operaciones CRUD se probaron utilizando Postman, verificando respuestas HTTP y la persistencia de los registros en SQLite.