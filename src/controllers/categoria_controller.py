
from flask import Blueprint, request, jsonify
from models import categoria_model as modelo

# Agrupamos las rutas de categorías
categorias_bp = Blueprint("categorias", __name__)


# GET - Consultar categorías
@categorias_bp.route("/categorias", methods=["GET"])
def obtener_categorias():
    categorias = modelo.obtener_categorias()
    return jsonify(categorias), 200


# POST - Crear categoría
@categorias_bp.route("/categorias", methods=["POST"])
def crear_categoria():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "JSON inválido"}), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion", "")

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({"error": "Nombre obligatorio"}), 400

    if not isinstance(descripcion, str):
        return jsonify({"error": "Descripción inválida"}), 400

    id_categoria = modelo.crear_categoria(
        nombre.strip(), descripcion
    )

    return jsonify({
        "mensaje": "Categoría creada correctamente",
        "id": id_categoria
    }), 201


# PUT - Actualizar categoría
@categorias_bp.route("/categorias/<int:id>", methods=["PUT"])
def actualizar_categoria(id):
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict):
        return jsonify({"error": "JSON inválido"}), 400

    nombre = datos.get("nombre")
    descripcion = datos.get("descripcion", "")

    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({"error": "Nombre obligatorio"}), 400

    if not isinstance(descripcion, str):
        return jsonify({"error": "Descripción inválida"}), 400

    actualizado = modelo.actualizar_categoria(
        id, nombre.strip(), descripcion
    )

    if not actualizado:
        return jsonify({"error": "Categoría no encontrada"}), 404

    return jsonify({
        "mensaje": "Categoría actualizada correctamente"
    }), 200


# DELETE - Eliminar categoría
@categorias_bp.route("/categorias/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):
    resultado = modelo.eliminar_categoria(id)

    if resultado == "no_existe":
        return jsonify({"error": "Categoría no encontrada"}), 404

    if resultado == "en_uso":
        return jsonify({
            "error": "La categoría tiene productos asociados"
        }), 409

    return jsonify({
        "mensaje": "Categoría eliminada correctamente"
    }), 200
