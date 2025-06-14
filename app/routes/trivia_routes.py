from flask import Blueprint
from app.controllers.trivia_controller import *

bp = Blueprint('trivia', __name__)

# Rutas generales
bp.route('/api/trivias/', methods=['GET'])(get_all_trivias)
bp.route('/api/trivias/', methods=['POST'])(create_trivia)
bp.route('/api/trivias/<int:id>', methods=['GET'])(get_trivia)
bp.route('/api/trivias/<int:id>', methods=['PUT'])(update_trivia)
bp.route('/api/trivias/<int:id>', methods=['DELETE'])(delete_trivia)

bp.route('/api/trivias/<int:trivia_id>/users', methods=['GET'])(get_users_trivia)
bp.route('/api/trivias/<int:trivia_id>/users', methods=['POST'])(add_users_trivia)