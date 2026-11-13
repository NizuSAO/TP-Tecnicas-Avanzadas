
from flask import Blueprint, request, jsonify
from models import producto_model as modelo

# Creamos el Blueprint de productos
productos_bp = Blueprint("productos", __name__)


# Función para validar productos
def validar_producto(datos):

    if not isinstance(datos, dict):
        return "JSON inválido"

    nombre = datos.get("nombre")
    precio = datos.get("precio")
    stock = datos.get("stock")
    categoria_id = datos.get("categoria_id")

    if not isinstance(nombre, str) or not nombre.strip():
        return "Nombre obligatorio"

    if (type(precio) not in (int, float)
            or not 0 <= precio < float("inf")):
        return "Precio inválido"

    if type(stock) is not int or stock < 0:
        return "Stock inválido"

    if type(categoria_id) is not int or categoria_id <= 0:
        return "Categoría inválida"

    return None


# GET - Consultar productos
@productos_bp.route("/productos", methods=["GET"])
def obtener_productos():

    productos = modelo.obtener_productos()

    return jsonify(productos), 200


# POST - Crear producto
@productos_bp.route("/productos", methods=["POST"])
def crear_producto():

    datos = request.get_json(silent=True)

    error = validar_producto(datos)

    if error:
        return jsonify({"error": error}), 400

    producto_id = modelo.crear_producto(
        datos["nombre"].strip(),
        datos["precio"],
        datos["stock"],
        datos["categoria_id"]
    )

    if producto_id is None:
        return jsonify({
            "error": "La categoría indicada no existe"
        }), 400

    return jsonify({
        "mensaje": "Producto creado correctamente",
        "id": producto_id
    }), 201


# PUT - Actualizar producto
@productos_bp.route("/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):

    datos = request.get_json(silent=True)

    error = validar_producto(datos)

    if error:
        return jsonify({"error": error}), 400

    resultado = modelo.actualizar_producto(
        id,
        datos["nombre"].strip(),
        datos["precio"],
        datos["stock"],
        datos["categoria_id"]
    )

    if resultado == "no_existe":
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    if resultado == "categoria_invalida":
        return jsonify({
            "error": "La categoría indicada no existe"
        }), 400

    return jsonify({
        "mensaje": "Producto actualizado correctamente"
    }), 200


# DELETE - Eliminar producto
@productos_bp.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):

    eliminado = modelo.eliminar_producto(id)

    if not eliminado:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    return jsonify({
        "mensaje": "Producto eliminado correctamente"
    }), 200
