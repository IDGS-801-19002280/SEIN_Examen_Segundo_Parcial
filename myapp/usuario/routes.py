from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import forms
from models import Users, db, Role
from decorator import logout_required

usuario = Blueprint('usuario', __name__)

UserDataStore = SQLAlchemyUserDatastore(db, Users, Role)

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

# LOGIN
@usuario.route('/usuario/login', methods = ['GET'])
@logout_required
def show_Login():
    login_Form = forms.LoginForm(request.form)
    return render_template('login.html', name = 'Login', form = login_Form, user=current_user)

@usuario.route('/usuario/login', methods=['POST'])
@logout_required
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = Users.query.filter_by(username=username).first()
    
    if not user or not check_password_hash(user.password, password):
        flash('El usuario o contraseña son incorrectos')
        return redirect(url_for('usuario.show_Login'))
    
    login_user(user, remember = remember)
    return redirect(url_for('tienda.index'))
    
#REGISTER
@usuario.route('/usuario/register', methods=['GET'])
@logout_required
def show_Register():
    login_Form = forms.LoginForm(request.form)
    return render_template('register.html', name = 'Register', form = login_Form, user=current_user)

@usuario.route('/usuario/register', methods = ['POST'])
@logout_required
def register():
    email = request.form.get('email')
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    
    us_Email = Users.query.filter_by(email=email).first()
    us_Username = Users.query.filter_by(username=username).first()
    
    if us_Email or us_Username:
        flash('El usuario ya existe')
        return redirect(url_for('usuario.show_Register'))
    
    UserDataStore.create_user(
        name = name,
        username = username,
        email = email,
        password = generate_password_hash(password, method="sha256")
    )
    db.session.commit()
    return redirect(url_for('usuario.show_Login'))

#LOGOUT
@usuario.route('/usuario/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.show_Login'))