from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_login import current_user
from models import Categories, Products, Users, Role, user_roles, db
import forms

admin = Blueprint('admin', __name__)

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

#Productos
@admin.route('/admin/index', methods=['GET'])
def get_products():
    products_Form = forms.ProductForm(request.form)
    productos = Products.query.all()
    categorias = Categories.query.all()
    products_Form.category.choices = [(categoria.name, categoria.name) for categoria in categorias]
    return render_template('admin_index.html', name = 'Admin', user = current_user, productos = productos, categorias = categorias, form = products_Form)

@admin.route('/admin/register/producto', methods=['POST'])
def register_products():
    products_Form = forms.ProductForm(request.form)
    producto = Products(
        name = products_Form.name.data,
        short_desc = products_Form.short_desc.data,
        long_desc = products_Form.long_desc.data,
        category = products_Form.category.data,
        photo_url = products_Form.photo_url.data,
        price = products_Form.price.data,
    )
    db.session.add(producto)
    db.session.commit()
    return redirect(url_for('admin.get_products'))

@admin.route('/admin/update/producto', methods=['POST'])
def update_products():
    products_Form = forms.ProductForm(request.form)
    producto = db.session.query(Products).filter(Products.id == products_Form.id.data).first()
    producto.name = products_Form.name.data
    producto.short_desc = products_Form.short_desc.data
    producto.long_desc = products_Form.long_desc.data
    producto.category = products_Form.category.data
    producto.photo_url = products_Form.photo_url.data
    producto.price = products_Form.price.data
    db.session.add(producto)
    db.session.commit()
    return redirect(url_for('admin.get_products'))

@admin.route('/admin/delete/producto', methods=['POST'])
def delete_products():
    products_Form = forms.ProductForm(request.form)
    producto = db.session.query(Products).filter(Products.id == products_Form.id.data).first()
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('admin.get_products'))

#Categorías
@admin.route('/admin/categorias', methods=['GET'])
def get_category():
    categories_form = forms.CategoryForm(request.form)
    categorias = Categories.query.all()
    return render_template('admin_category.html', name = 'Admin', user = current_user, categorias = categorias, form = categories_form)

@admin.route('/admin/register/categoria', methods=['POST'])
def register_category():
    categories_form = forms.CategoryForm(request.form)
    catego = Categories(
        name = categories_form.name.data
    )
    db.session.add(catego)
    db.session.commit()
    return redirect(url_for('admin.get_category'))

@admin.route('/admin/update/categoria', methods=['POST'])
def update_category():
    categories_form = forms.CategoryForm(request.form)
    categoria = db.session.query(Categories).filter(Categories.id == request.form.get('id')).first()
    categoria.name = categories_form.name.data
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for('admin.get_category'))

@admin.route('/admin/delete/categoria', methods=['POST'])
def delete_category():
    categories_form = forms.CategoryForm(request.form)
    categoria = db.session.query(Categories).filter(Categories.id == request.form.get('id')).first()
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('admin.get_category'))

#Usuarios
@admin.route('/admin/users', methods=['GET'])
def get_users():
    usersForm = forms.RoleForm(request.form)
    usuarios = Users.query.all()
    roles = Role.query.all()
    usersForm.roleId.choices = [(role.id, role.name) for role in roles]
    return render_template('admin_user_index.html', name = 'Admin', user = current_user, usuarios = usuarios, form = usersForm)

@admin.route('/admin/update/user', methods=['POST'])
def update_users():
    usersForm = forms.RoleForm(request.form)
    user = user_roles(
        userId = usersForm.userId.data,
        roleId = usersForm.roleId.data
    )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('admin.get_users'))