from flask import Blueprint
from app.controllers import role_controller

bp = Blueprint('role', __name__, url_prefix='/api/roles')

bp.route('/', methods=['GET'])(role_controller.list_roles)
bp.route('/', methods=['POST'])(role_controller.create_role)
