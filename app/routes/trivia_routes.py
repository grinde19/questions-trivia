from flask import Blueprint
from app.controllers.trivia_controller import (
    get_all_trivias, get_trivia, create_trivia,
    update_trivia, delete_trivia
)

bp = Blueprint('trivia', __name__, url_prefix='/api/trivias')

# Rutas generales
bp.route('/', methods=['GET'])(get_all_trivias)
bp.route('/<int:id>', methods=['GET'])(get_trivia)
bp.route('/', methods=['POST'])(create_trivia)
bp.route('/<int:id>', methods=['PUT'])(update_trivia)
bp.route('/<int:id>', methods=['DELETE'])(delete_trivia)
