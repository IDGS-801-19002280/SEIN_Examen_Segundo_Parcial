from flask import Blueprint, render_template, request
from flask_login import current_user
from models import Products, db

tienda = Blueprint('tienda', __name__)

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

@tienda.route('/tienda/index', methods=['GET'])
def index():
    productos = Products.query.all()
    return render_template('index.html', name = 'Inicio', user=current_user, productos = productos, want_footer = True)

@tienda.route('/tienda/productos', methods=['GET'])
def products():
    productos = Products.query.all()
    return render_template('all_products.html', name = 'Productos', productos = productos, user = current_user, want_footer = True)

@tienda.route('/tienda/contacto', methods=['GET'])
def contact():
    return render_template('contact.html', name = 'Contacto', user = current_user)