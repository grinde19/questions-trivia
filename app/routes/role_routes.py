from flask import Blueprint
from app.controllers.role_controller import *

bp = Blueprint('role', __name__)

# Rutas generales
bp.route('/api/roles/', methods=['GET'])(get_all_roles)
bp.route('/api/roles/', methods=['POST'])(create_role)
bp.route('/api/roles/<int:id>', methods=['GET'])(get_role)
bp.route('/api/roles/<int:id>', methods=['PUT'])(update_role)
bp.route('/api/roles/<int:id>', methods=['DELETE'])(delete_role)
