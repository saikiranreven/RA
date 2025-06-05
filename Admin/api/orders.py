from flask import Blueprint, jsonify

orders_api = Blueprint('orders_api', __name__)

@orders_api.route('/api/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": "ORD001", "customer": "Alice", "status": "Shipped", "total": 115.98},
        {"id": "ORD002", "customer": "Bob", "status": "Processing", "total": 89.99}
    ]
    return jsonify(orders)