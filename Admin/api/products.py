from flask import Blueprint, jsonify

products_api = Blueprint('products_api', __name__)

@products_api.route('/api/products', methods=['GET'])
def get_products():
    products = [
        {"id": "P001", "name": "Wireless Mouse", "price": 25.99},
        {"id": "P002", "name": "Mechanical Keyboard", "price": 89.99}
    ]
    return jsonify(products)