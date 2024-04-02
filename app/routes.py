from flask import request, jsonify
from . import app, db
from .models import Articulo


# Rutas de la API
@app.route("/api/articulos", methods=["GET"])
def get_articulos():
    articulos = Articulo.query.all()
    return jsonify(
        [
            {
                "id": articulo.id,
                "descripcion": articulo.descripcion,
                "precio": articulo.precio,
                "stock": articulo.stock,
            }
            for articulo in articulos
        ]
    )


@app.route("/api/articulos", methods=["POST"])
def create_articulo():
    data = request.get_json()
    if "descripcion" not in data or "precio" not in data or "stock" not in data:
        return (
            jsonify(
                {"error": "Los campos 'descripcion', 'precio' y 'stock' son requeridos"}
            ),
            400,
        )
    try:
        precio = float(data["precio"])
        stock = int(data["stock"])
    except ValueError:
        return (
            jsonify(
                {
                    "error": "El precio debe ser un número decimal y el stock debe ser un número entero"
                }
            ),
            400,
        )

    articulo = Articulo(descripcion=data["descripcion"], precio=precio, stock=stock)
    db.session.add(articulo)
    db.session.commit()
    return jsonify({"message": "Articulo creado correctamente"}), 201


@app.route("/api/articulos/<int:id>", methods=["PUT"])
def update_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    data = request.get_json()
    if "descripcion" not in data or "precio" not in data or "stock" not in data:
        return (
            jsonify(
                {"error": "Los campos 'descripcion', 'precio' y 'stock' son requeridos"}
            ),
            400,
        )
    try:
        precio = float(data["precio"])
        stock = int(data["stock"])
    except ValueError:
        return (
            jsonify(
                {
                    "error": "El precio debe ser un número decimal y el stock debe ser un número entero"
                }
            ),
            400,
        )

    articulo.descripcion = data["descripcion"]
    articulo.precio = precio
    articulo.stock = stock
    db.session.commit()
    return jsonify({"message": "Articulo actualizado correctamente"})


@app.route("/api/articulos/<int:id>", methods=["DELETE"])
@app.route("/api/articulos/<int:id>", methods=["DELETE"])
def delete_articulo(id):
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()
    return jsonify({"message": "Articulo eliminado correctamente"})
