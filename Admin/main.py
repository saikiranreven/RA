from flask import Flask, render_template
from api.products import products_api
from api.inventory import inventory_api
from api.orders import orders_api

app = Flask(__name__)

# Admin dashboard route
@app.route('/')
def dashboard():
    return render_template('dashboard.html')

# Register API routes
app.register_blueprint(products_api)
app.register_blueprint(inventory_api)
app.register_blueprint(orders_api)

if __name__ == '__main__':
    app.run(debug=True)