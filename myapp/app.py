from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config
from models import db, Users

from admin.routes import admin
from tienda.routes import tienda
from usuario.routes import usuario

app = Flask(__name__)
login_manager = LoginManager(app)
app.config.from_object(config['development'])

#----------------------RUTAS-------------------------------------------------------------------------------------------------------------------------------------#

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('tienda.index'))

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

app.register_blueprint(admin)
app.register_blueprint(tienda)
app.register_blueprint(usuario)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------#

if __name__ =='__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager.login_view = 'usuario.login'
    app.run()