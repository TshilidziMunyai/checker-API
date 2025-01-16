from flask import Blueprint, request, jsonify
from .database import get_db_connection

main = Blueprint('main', __name__)

@main.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?', (id,)).fetchone()
    conn.close()
    if product is None:
        return jsonify({'error': 'Product not found'}), 404
    return jsonify(dict(product))

@main.route('/products', methods=['GET'])
def get_products_in_range():
    min_price = request.args.get('min_price', type=float, default=0)
    max_price = request.args.get('max_price', type=float, default=float('inf'))

    conn = get_db_connection()
    products = conn.execute(
        'SELECT * FROM products WHERE price BETWEEN ? AND ?',
        (min_price, max_price)
    ).fetchall()
    conn.close()
    return jsonify([dict(product) for product in products])

@main.route('/', methods=['GET'])
def home():
    return "API is working!"
