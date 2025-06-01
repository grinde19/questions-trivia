from flask import Blueprint
from app.controllers.user_answer_controller import *


bp = Blueprint('user-answer', __name__)

# Rutas generales

bp.route('/api/user-answer/trivias/<int:trivia_id>/stats', methods=['GET'])(get_users_trivia_stats)
bp.route('/api/user-answer/', methods=['POST'])(create_all_answer)
