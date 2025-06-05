from flask import Flask, render_template, request, redirect, url_for
from api.products import get_all_products
from api.orders import create_order

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', products=get_all_products())

@app.route('/order', methods=['POST'])
def order():
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])
    user_id = request.form['user_id']
    
    create_order(user_id=user_id, product_id=product_id, quantity=quantity)
    return render_template('order_success.html', product_id=product_id, quantity=quantity)