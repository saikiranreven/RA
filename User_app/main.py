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
def order(product_id):
    if request.method == 'POST':
        user_id = request.form['user_id']
        quantity = int(request.form['quantity'])
        create_order(user_id=user_id, product_id=product_id, quantity=quantity)
        return redirect(url_for('confirmation'))
    return render_template('place_order.html', product_id=product_id)

@app.route('/confirmation')
def confirmation():
    return render_template('order_confirmation.html')

@app.route('/my_orders/<user_id>')
def my_orders(user_id):
    orders = get_user_orders(user_id)
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
