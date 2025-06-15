from flask import Blueprint, jsonify
from server.models.pizza import Pizza

pizza_bp = Blueprint('pizza_bp', __name__, url_prefix='/pizzas')

@pizza_bp.route('', methods=['GET'])
def get_all_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        {"id": p.id, "name": p.name, "ingredients": p.ingredients}
        for p in pizzas
    ]), 200
