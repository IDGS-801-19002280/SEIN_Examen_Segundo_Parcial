from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import datetime

db = SQLAlchemy()

user_roles = db.Table('user_roles',
  db.Column('userId', db.Integer, db.ForeignKey('user.id')),
  db.Column('roleId', db.Integer, db.ForeignKey('role.id')),
)

class Users(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(15))
    email = db.Column(db.String(50))
    password = db.Column(db.String(150))
    active = db.Column(db.Boolean)
    roles = db.relationship('Role',
        secondary=user_roles,
        backref = db.backref('users', lazy='dynamic')
    )
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

class Products(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    short_desc = db.Column(db.String(150))
    long_desc = db.Column(db.Text)
    category = db.Column(db.String(20))
    photo_url = db.Column(db.String(250))
    price = db.Column(db.Float())
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

class Categories(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

class Role(RoleMixin, db.Model):
  __tablename__ = 'role'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255))