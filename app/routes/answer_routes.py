from flask import Blueprint
from app.controllers.answer_controller import *

bp = Blueprint("answers", __name__)

# Rutas generales
bp.route("/api/answers/", methods=["GET"])(get_answers)
bp.route("/api/answers/<int:id>/", methods=["GET"])(get_answer)
bp.route("/api/answers/<int:id>/", methods=["PUT"])(update_answer)
bp.route("/api/answers/<int:id>/", methods=["DELETE"])(delete_answer)

# Rutas para las respuestas de las questions
bp.route("/api/questions/<int:question_id>/answers/", methods=["GET"])(get_answers_by_question)
bp.route("/api/questions/<int:question_id>/answers/", methods=["POST"])(create_answer)
