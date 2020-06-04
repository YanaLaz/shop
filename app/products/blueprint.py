from flask import Blueprint
from flask import render_template

from app.models import Product

products = Blueprint('products', __name__, template_folder='templates')

@products.route('/')
def index():
    products = Product.query.all()
    return render_template('products/index.html', products = products)

@products.route('/<slug>')
def product_detail(slug):
    product = Product.query.filter(Product.slug==slug).first()
    return render_template('products/prod_detail.html', product=product)