from flask import Blueprint, jsonify, request
from src.auth_utils import token_required

items_blueprint = Blueprint("items", __name__)

# In-memory store
ITEMS = {}

@items_blueprint.route("/items", methods=["GET"])
@token_required
def list_items(user_id):
    # GET all items
    return jsonify({"items": ITEMS}), 200

@items_blueprint.route("/items", methods=["POST"])
@token_required
def create_item(user_id):
    # Create a new item
    data = request.json
    item_id = str(len(ITEMS) + 1)  # naive id
    ITEMS[item_id] = data
    return jsonify({"message": "Item created", "item_id": item_id}), 201

@items_blueprint.route("/items/<item_id>", methods=["GET"])
@token_required
def get_item(user_id, item_id):
    # Get a specific item
    item = ITEMS.get(item_id)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    return jsonify({"item": item}), 200

@items_blueprint.route("/items/<item_id>", methods=["PUT"])
@token_required
def update_item(user_id, item_id):
    # Update item
    if item_id not in ITEMS:
        return jsonify({"message": "Item not found"}), 404
    data = request.json
    ITEMS[item_id] = data
    return jsonify({"message": "Item updated"}), 200

@items_blueprint.route("/items/<item_id>", methods=["DELETE"])
@token_required
def delete_item(user_id, item_id):
    # Delete item
    if item_id not in ITEMS:
        return jsonify({"message": "Item not found"}), 404
    del ITEMS[item_id]
    return jsonify({"message": "Item deleted"}), 200
