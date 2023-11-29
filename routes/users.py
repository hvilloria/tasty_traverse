from models import db
from models.user import User
from flask import Blueprint, jsonify

bp = Blueprint('users', __name__, url_prefix='/users')

# Ruta para agregar un usuario
@bp.post('/<username>')
def add_user(username):

    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return f'Usuario {username} agregado correctamente'

# Ruta para mostrar todos los usuarios
@bp.get('/')
def show_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])