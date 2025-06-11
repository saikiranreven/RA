from flask import Flask, render_template, request, redirect, url_for
from api.products import get_all_products
from api.orders   import create_order, get_user_orders

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html', products=get_all_products())

# NEW: handle the POST from products.html
@app.route('/order', methods=['POST'])
def order():
    order_id = create_order(
        user_id    = request.form['user_id'],
        product_id = request.form['product_id'],
        quantity   = int(request.form['quantity'])
    )
    # pass order_id to success page
    return redirect(url_for('order_success', order_id=order_id))

@app.route('/order_success')
def order_success():
    oid = request.args.get('order_id')
    return render_template('order_success.html', order_id=oid)

@app.route('/my_orders', methods=['GET', 'POST'])
def my_orders():
    orders = None
    uid = None
    if request.method == 'POST':
        uid = request.form['user_id']
        orders = get_user_orders(uid)
    return render_template('my_orders.html', orders=orders, uid=uid)

if __name__ == '__main__':
    app.run(port=8080, debug=True)