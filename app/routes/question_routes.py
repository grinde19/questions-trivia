from flask import Blueprint
from app.controllers.question_controller import *

bp = Blueprint("questions", __name__)

# Rutas generales
bp.route("/api/questions/", methods=["GET"])(get_questions)
bp.route("/api/questions/", methods=["POST"])(create_question)
bp.route("/api/questions/<int:id>/", methods=["GET"])(get_question)
bp.route("/api/questions/<int:id>/", methods=["PUT"])(update_question)
bp.route("/api/questions/<int:id>/", methods=["DELETE"])(delete_question)


#Rutas para los los niveles y Trivias de las questions
bp.route("/api/levels/<int:level_id>/questions/", methods=["GET"])(get_questions_by_level)
bp.route("/api/trivias/<int:trivia_id>/questions/", methods=["GET"])(get_questions_by_trivia)