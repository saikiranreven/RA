from flask import Flask, render_template, request, redirect, url_for
from api.products import get_all_products
from api.orders import create_order, get_user_orders

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', products=get_all_products())

@app.route('/place_order/<product_id>', methods=['GET', 'POST'])
def place_order(product_id):
    if request.method == 'POST':
        create_order(request.form['user_id'], product_id, int(request.form['quantity']))
        return redirect(url_for('order_success'))
    return render_template('place_order.html', product_id=product_id)

@app.route('/order_success')
def order_success():
    return render_template('order_success.html')

@app.route('/my_orders', methods=['GET', 'POST'])
def my_orders():
    orders = None
    if request.method == 'POST':
        orders = get_user_orders(request.form['user_id'])
    return render_template('my_orders.html', orders=orders)