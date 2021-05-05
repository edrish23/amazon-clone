
from flask import Blueprint, render_template
from .models import Product

blueprint = Blueprint('products', __name__, template_folder='templates') 

@blueprint.route('/')
def products():
    
    product1 = Product('prod1', 200)
    product2 = Product('prod2', 300)
    product3 = Product('prod2', 400)
    product4 = Product('prod2', 500)
    product5 = Product('prod2', 600)
    product6 = Product('prod2', 300)
    products = [product1, product2, product3, product4, product5]
    #print(products),product1, product2, product3, product4, product5, product6, product4, product5, product6
    return render_template('products.html', prods=products)