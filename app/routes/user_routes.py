from flask import Blueprint
from app.controllers import *

bp = Blueprint('user', __name__)

bp.route('/api/users/', methods=['GET'])(list_users)
bp.route('/api/users/', methods=['POST'])(create_user)
bp.route('/api/users/<int:id>/', methods=['GET'])(get_user)
bp.route('/api/users/<int:id>/', methods=['PUT'])(update_user)
bp.route('/api/users/<int:id>/', methods=['DELETE'])(delete_user)
bp.route('/api/users/<int:id>/roles/', methods=['PUT'])(assign_roles)
