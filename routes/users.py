from models import db
from models.user import User
from flask import Blueprint, jsonify, request

bp = Blueprint('users', __name__, url_prefix='/users')

# Ruta para agregar un usuario
@bp.post('/')
def add_user():
    params = request.get_json()
    user = User(username=params['user'], password=params['password'])
    db.session.add(user)
    db.session.commit()
    return (user.as_dict(), 201)

# Ruta para mostrar todos los usuarios
@bp.get('/')
def show_users():
    users = User.query.all()
    return jsonify([user.as_dict() for user in users])