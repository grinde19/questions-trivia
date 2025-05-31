from flask import Blueprint
from app.controllers import user_controller

bp = Blueprint('user', __name__, url_prefix='/api/users')

bp.route('/', methods=['GET'])(user_controller.list_users)
bp.route('/<int:id>/', methods=['GET'])(user_controller.get_user)
bp.route('/', methods=['POST'])(user_controller.create_user)
bp.route('/<int:id>/', methods=['PUT'])(user_controller.update_user)
bp.route('/<int:id>/', methods=['DELETE'])(user_controller.delete_user)
bp.route('/<int:id>/roles/', methods=['PUT'])(user_controller.assign_roles)
