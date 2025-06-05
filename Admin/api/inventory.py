from flask import Blueprint, jsonify

inventory_api = Blueprint('inventory_api', __name__)

@inventory_api.route('/api/inventory', methods=['GET'])
def get_inventory():
    inventory = [
        {"id": "P001", "stock": 100},
        {"id": "P002", "stock": 55}
    ]
    return jsonify(inventory)